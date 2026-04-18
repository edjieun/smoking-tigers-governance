#!/usr/bin/env python3
"""
OpenRouter ↔ Notion Reconciliation Script
Nightly job: matches OpenRouter generation records to ST:AI Request Queue rows.

Strategy (management key enabled):
  1. Pull daily aggregate stats from /api/v1/activity for yesterday using mgmt key
  2. For each unreconciled Notion row on that date, match by model name (Agent field)
  3. If a generation ID is stored in the row text, use /api/v1/generation?id= for
     precise per-request data (tokens/cost).
  4. If no gen ID, stamp the row with the daily aggregate tokens/cost for that model.
     (Note: aggregate stats represent ALL requests for that model that day, not per-row.)
  5. Mark rows as reconciled. Leave rows with no OR match for manual review.

Activity endpoint response fields:
  date, model, model_permaslug, usage (cost in USD), requests,
  prompt_tokens, completion_tokens, reasoning_tokens, provider_name, endpoint_id

Run at: 11:30 PM Pacific nightly via cron
"""

import json
import logging
import os
import re
import sys
import traceback
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import urllib.request
import urllib.error

# ─── Config ────────────────────────────────────────────────────────────────────

WORKSPACE = Path("/Users/edlicious/.openclaw/workspace")
LOG_FILE = WORKSPACE / "logs" / "openrouter-reconciliation.log"
AUTH_FILE = WORKSPACE / "agents" / "ea" / "auth.json"
SYSOPS_AUTH = WORKSPACE / "agents" / "sysops" / "auth-profiles.json"

NOTION_DB_ID = "3266f6ac689e81099afbd6362fa943d6"
NOTION_BASE = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"

OPENROUTER_BASE = "https://openrouter.ai/api/v1"

# Mattermost config (sysops bot posting to #sysops)
MATTERMOST_BASE = "http://localhost:8065"
MATTERMOST_BOT_TOKEN = "ksk4hzh463gx9f13cdob4puyoh"   # sys-ops bot
MATTERMOST_CHANNEL = "7s5prot6jfdxjx7m9j75g55jjw"     # #sysops

PACIFIC = ZoneInfo("America/Los_Angeles")

# ─── Logging ───────────────────────────────────────────────────────────────────

LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(str(LOG_FILE), encoding="utf-8"),
    ],
)
log = logging.getLogger("openrouter-reconcile")


# ─── Helpers ───────────────────────────────────────────────────────────────────

def load_config():
    """Load API keys from config files."""
    config = {}

    # Notion token
    try:
        with open(AUTH_FILE) as f:
            auth = json.load(f)
        config["notion_token"] = auth["notion"]["api_token"]
    except Exception as e:
        raise RuntimeError(f"Cannot load Notion token from {AUTH_FILE}: {e}")

    # OpenRouter keys
    try:
        with open(SYSOPS_AUTH) as f:
            profiles = json.load(f)
        config["openrouter_key"] = profiles["profiles"]["openrouter:default"]["key"]
        config["openrouter_mgmt_key"] = profiles["profiles"]["openrouter:management"]["key"]
    except Exception as e:
        raise RuntimeError(f"Cannot load OpenRouter keys from {SYSOPS_AUTH}: {e}")

    return config


def http_request(url, method="GET", headers=None, body=None, timeout=30):
    """Simple HTTP helper using stdlib."""
    if body and isinstance(body, dict):
        body = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=body, headers=headers or {}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
            return resp.status, json.loads(data) if data else {}
    except urllib.error.HTTPError as e:
        data = e.read()
        try:
            return e.code, json.loads(data)
        except Exception:
            return e.code, {"error": data.decode("utf-8", errors="replace")}


def mattermost_alert(message: str, config: dict):
    """Post an alert to Mattermost #sysops channel."""
    try:
        url = f"{MATTERMOST_BASE}/api/v4/posts"
        headers = {
            "Authorization": f"Bearer {MATTERMOST_BOT_TOKEN}",
            "Content-Type": "application/json",
        }
        body = {
            "channel_id": MATTERMOST_CHANNEL,
            "message": f"🔴 **OpenRouter Reconciliation Alert**\n\n{message}",
        }
        status, resp = http_request(url, method="POST", headers=headers, body=body)
        if status not in (200, 201):
            log.error(f"Mattermost post failed: {status} {resp}")
        else:
            log.info("Alert posted to Mattermost #sysops")
    except Exception as e:
        log.error(f"Failed to post Mattermost alert: {e}")


# ─── OpenRouter ────────────────────────────────────────────────────────────────

def fetch_activity(mgmt_key: str, date_from: str, date_to: str) -> list[dict]:
    """
    Fetch daily aggregated activity using the management key.
    Returns list of activity records for the given date range.

    Each record has: date, model, model_permaslug, usage (USD), requests,
    prompt_tokens, completion_tokens, reasoning_tokens, provider_name, endpoint_id
    """
    headers = {"Authorization": f"Bearer {mgmt_key}"}
    url = f"{OPENROUTER_BASE}/activity?date_from={date_from}&date_to={date_to}"
    status, data = http_request(url, headers=headers)
    if status != 200:
        raise RuntimeError(f"OpenRouter /api/v1/activity failed: {status} {data}")
    return data.get("data", [])


def build_activity_index(activity_records: list[dict], target_date: str) -> dict:
    """
    Build an index: model_shortname → aggregated stats for the target date.
    Multiple providers for the same model on the same day are summed.

    Returns: { "claude-sonnet-4.6": { prompt_tokens, completion_tokens, usage, requests }, ... }
    """
    index = defaultdict(lambda: {
        "prompt_tokens": 0,
        "completion_tokens": 0,
        "reasoning_tokens": 0,
        "usage": 0.0,
        "requests": 0,
        "model_permaslug": "",
        "providers": [],
    })

    for record in activity_records:
        record_date = record.get("date", "")[:10]  # "2026-03-16 00:00:00" → "2026-03-16"
        if record_date != target_date:
            continue

        model = record.get("model", "")  # e.g. "anthropic/claude-sonnet-4.6"
        # Extract short name after last "/"
        short_name = model.split("/")[-1] if "/" in model else model

        index[short_name]["prompt_tokens"] += record.get("prompt_tokens", 0)
        index[short_name]["completion_tokens"] += record.get("completion_tokens", 0)
        index[short_name]["reasoning_tokens"] += record.get("reasoning_tokens", 0)
        index[short_name]["usage"] += record.get("usage", 0.0)
        index[short_name]["requests"] += record.get("requests", 0)
        index[short_name]["model_permaslug"] = record.get("model_permaslug", "")
        index[short_name]["providers"].append(record.get("provider_name", ""))
        # Also index by full model path
        index[model]["prompt_tokens"] += record.get("prompt_tokens", 0)
        index[model]["completion_tokens"] += record.get("completion_tokens", 0)
        index[model]["reasoning_tokens"] += record.get("reasoning_tokens", 0)
        index[model]["usage"] += record.get("usage", 0.0)
        index[model]["requests"] += record.get("requests", 0)
        index[model]["model_permaslug"] = record.get("model_permaslug", "")

    return dict(index)


def fetch_openrouter_generation(api_key: str, generation_id: str) -> dict | None:
    """
    Fetch a single generation record by ID.
    Returns None if not found.
    """
    headers = {"Authorization": f"Bearer {api_key}"}
    status, data = http_request(
        f"{OPENROUTER_BASE}/generation?id={generation_id}",
        headers=headers,
    )
    if status == 200 and data.get("data"):
        return data["data"]
    return None


# ─── Notion ────────────────────────────────────────────────────────────────────

def notion_headers(token: str) -> dict:
    return {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def get_unreconciled_rows(notion_token: str, target_date: str) -> list[dict]:
    """
    Query Notion for rows where:
    - OpenRouter Reconciled = false
    - Date Requested = target_date (YYYY-MM-DD)
    Returns list of page dicts.
    """
    url = f"{NOTION_BASE}/databases/{NOTION_DB_ID}/query"
    headers = notion_headers(notion_token)

    filter_body = {
        "filter": {
            "and": [
                {
                    "property": "OpenRouter Reconciled",
                    "checkbox": {"equals": False},
                },
                {
                    "property": "Date Requested",
                    "date": {"equals": target_date},
                },
            ]
        },
        "page_size": 100,
    }

    all_results = []
    has_more = True
    cursor = None

    while has_more:
        if cursor:
            filter_body["start_cursor"] = cursor
        status, data = http_request(url, method="POST", headers=headers, body=filter_body)
        if status != 200:
            raise RuntimeError(f"Notion query failed: {status} {data}")
        all_results.extend(data.get("results", []))
        has_more = data.get("has_more", False)
        cursor = data.get("next_cursor")

    return all_results


def get_prop(page: dict, prop_name: str):
    """Extract a property value from a Notion page."""
    props = page.get("properties", {})
    prop = props.get(prop_name, {})
    ptype = prop.get("type")

    if ptype == "title":
        items = prop.get("title", [])
        return items[0].get("plain_text", "") if items else ""
    elif ptype == "rich_text":
        items = prop.get("rich_text", [])
        return items[0].get("plain_text", "") if items else ""
    elif ptype == "date":
        d = prop.get("date")
        return d["start"] if d else None
    elif ptype == "checkbox":
        return prop.get("checkbox", False)
    elif ptype == "number":
        return prop.get("number")
    elif ptype == "select":
        s = prop.get("select")
        return s["name"] if s else None
    elif ptype == "url":
        return prop.get("url")
    return None


def update_notion_row(
    notion_token: str,
    page_id: str,
    tokens_in: int | None,
    tokens_out: int | None,
    cost_usd: float | None,
    reconciled: bool = True,
) -> bool:
    """Update a Notion row with token/cost data and mark reconciled."""
    url = f"{NOTION_BASE}/pages/{page_id}"
    headers = notion_headers(notion_token)

    properties = {
        "OpenRouter Reconciled": {"checkbox": reconciled},
    }
    if tokens_in is not None:
        properties["Tokens In"] = {"number": tokens_in}
    if tokens_out is not None:
        properties["Tokens Out"] = {"number": tokens_out}
    if cost_usd is not None:
        properties["Estimated Cost (USD)"] = {"number": round(cost_usd, 6)}

    body = {"properties": properties}
    status, data = http_request(url, method="PATCH", headers=headers, body=body)
    if status != 200:
        log.error(f"Failed to update page {page_id}: {status} {data}")
        return False
    return True


def mark_reconciled_no_data(notion_token: str, page_id: str) -> bool:
    """Mark a row as reconciled even if no OR data found (to prevent re-processing)."""
    url = f"{NOTION_BASE}/pages/{page_id}"
    headers = notion_headers(notion_token)
    body = {
        "properties": {
            "OpenRouter Reconciled": {"checkbox": True},
        }
    }
    status, data = http_request(url, method="PATCH", headers=headers, body=body)
    return status == 200


# ─── Matching Logic ────────────────────────────────────────────────────────────

def extract_generation_id(agent_notes: str, description: str, request_title: str) -> str | None:
    """
    Try to extract an OpenRouter generation ID from Notion text fields.
    Generation IDs look like: gen-xxxxxxxxxxxxxxxx
    """
    pattern = r"gen-[a-zA-Z0-9]+"
    for text in [agent_notes, description, request_title]:
        if text:
            match = re.search(pattern, text)
            if match:
                return match.group(0)
    return None


def extract_model_from_agent(agent_field: str) -> str | None:
    """
    Parse the Agent field like 'Eva / claude-sonnet-4.6' to get model name.
    Returns the model portion, e.g. 'claude-sonnet-4.6'
    Also handles bare model names or full paths like 'anthropic/claude-sonnet-4.6'.
    """
    if not agent_field:
        return None
    # Look for " / " separator (agent name / model)
    if " / " in agent_field:
        parts = agent_field.split(" / ")
        return parts[-1].strip()
    # Look for "/" (model path like anthropic/claude-sonnet-4.6)
    if "/" in agent_field:
        return agent_field.split("/")[-1].strip()
    return agent_field.strip()


def find_activity_match(model_name: str, activity_index: dict) -> dict | None:
    """
    Given a model name from the Notion Agent field, find the best match
    in the activity index. Returns the activity record or None.

    Tries exact match, then partial match (model short name in key).
    """
    if not model_name:
        return None

    # Direct key match
    if model_name in activity_index:
        return activity_index[model_name]

    # Try lowercased
    model_lower = model_name.lower()
    for key in activity_index:
        if key.lower() == model_lower:
            return activity_index[key]

    # Partial: key contains model_name or model_name contains key
    for key in activity_index:
        key_lower = key.lower()
        if model_lower in key_lower or key_lower in model_lower:
            return activity_index[key]

    return None


LOCAL_MODEL_PATTERNS = [
    "qwen", "ollama", "local", "llama", "mistral", "phi", "gemma",
    "deepseek", "yi-", "orca", "falcon", "vicuna",
]


def is_local_model(model_name: str) -> bool:
    """Return True if model appears to be a local/Ollama model (no billing)."""
    if not model_name:
        return False
    m = model_name.lower()
    return any(pat in m for pat in LOCAL_MODEL_PATTERNS)


# ─── Main Reconciliation ────────────────────────────────────────────────────────

def run_reconciliation(target_date: str | None = None):
    """
    Main reconciliation logic.
    target_date: YYYY-MM-DD, defaults to yesterday Pacific time.
    """
    now_pacific = datetime.now(PACIFIC)
    if target_date is None:
        target_date = (now_pacific - timedelta(days=1)).strftime("%Y-%m-%d")

    log.info("=" * 60)
    log.info(f"OpenRouter Reconciliation — target date: {target_date}")
    log.info(f"Run time: {now_pacific.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    log.info("=" * 60)

    # Load credentials
    config = load_config()
    notion_token = config["notion_token"]
    or_key = config["openrouter_key"]
    mgmt_key = config["openrouter_mgmt_key"]

    # ── Step 1: Pull bulk activity from management key ──────────────────────────
    log.info(f"Fetching OpenRouter activity for {target_date} via management key...")
    try:
        activity_records = fetch_activity(mgmt_key, target_date, target_date)
        log.info(f"Activity endpoint returned {len(activity_records)} record(s)")
        # Build lookup index for the target date
        activity_index = build_activity_index(activity_records, target_date)
        log.info(f"Activity index keys: {list(activity_index.keys())}")
        # Log a brief summary of what we found
        for model_key, stats in activity_index.items():
            if "/" not in model_key:  # Only log short names to avoid duplication
                log.info(
                    f"  {model_key}: {stats['requests']} req | "
                    f"in={stats['prompt_tokens']:,} out={stats['completion_tokens']:,} | "
                    f"cost=${stats['usage']:.4f}"
                )
    except Exception as e:
        log.error(f"Failed to fetch activity data: {e}")
        log.warning("Will fall back to per-ID lookup only.")
        activity_index = {}

    # ── Step 2: Query Notion for unreconciled rows ──────────────────────────────
    log.info(f"Querying Notion DB for unreconciled rows on {target_date}...")
    rows = get_unreconciled_rows(notion_token, target_date)
    log.info(f"Found {len(rows)} unreconciled row(s) for {target_date}")

    if not rows:
        log.info("Nothing to reconcile. Exiting cleanly.")
        return {
            "date": target_date,
            "rows_found": 0,
            "rows_updated": 0,
            "rows_no_data": 0,
            "rows_skipped_local": 0,
            "errors": 0,
        }

    stats = {
        "date": target_date,
        "rows_found": len(rows),
        "rows_updated": 0,
        "rows_no_data": 0,
        "rows_skipped_local": 0,
        "errors": 0,
    }

    # ── Step 3: Process each row ────────────────────────────────────────────────
    for row in rows:
        page_id = row["id"]
        title = get_prop(row, "Request") or "(no title)"
        agent_field = get_prop(row, "Agent") or ""
        agent_notes = get_prop(row, "Agent Notes") or ""
        description = get_prop(row, "Description") or ""
        date_requested = get_prop(row, "Date Requested")
        model_name = extract_model_from_agent(agent_field)

        log.info(f"  Row: {title[:60]!r}")
        log.info(f"    Agent: {agent_field!r} | Model: {model_name!r} | Date: {date_requested}")

        # ── Path A: Generation ID lookup (most precise) ──────────────────────
        gen_id = extract_generation_id(agent_notes, description, title)
        if gen_id:
            log.info(f"    Found generation ID: {gen_id} — attempting per-ID lookup")
            try:
                gen_data = fetch_openrouter_generation(or_key, gen_id)
                if gen_data:
                    tokens_in = gen_data.get("tokens_prompt")
                    tokens_out = gen_data.get("tokens_completion")
                    cost = gen_data.get("total_cost")
                    if cost is not None:
                        cost = float(cost)
                    log.info(
                        f"    OR gen data: tokens_in={tokens_in} "
                        f"tokens_out={tokens_out} cost=${cost}"
                    )
                    ok = update_notion_row(notion_token, page_id, tokens_in, tokens_out, cost)
                    if ok:
                        log.info(f"    ✅ Updated via generation ID — reconciled")
                        stats["rows_updated"] += 1
                    else:
                        log.error(f"    ❌ Notion update failed for {page_id}")
                        stats["errors"] += 1
                else:
                    log.warning(
                        f"    Generation {gen_id} not found in OpenRouter. "
                        "Falling through to activity index match."
                    )
                    gen_id = None  # fall through to activity path
            except Exception as e:
                log.error(f"    Error fetching generation {gen_id}: {e}")
                gen_id = None  # fall through

        # ── Path B: Activity index match by model name ───────────────────────
        if not gen_id:
            # Check for local/Ollama model first (free, no OR billing)
            if is_local_model(model_name or ""):
                log.info(
                    f"    Local/Ollama model detected — marking reconciled "
                    f"with $0 cost (no OR billing)"
                )
                ok = update_notion_row(
                    notion_token, page_id,
                    tokens_in=get_prop(row, "Tokens In"),
                    tokens_out=get_prop(row, "Tokens Out"),
                    cost_usd=0.0,
                )
                if ok:
                    stats["rows_skipped_local"] += 1
                    stats["rows_updated"] += 1
                continue

            # Look up in activity index
            activity = find_activity_match(model_name or "", activity_index)
            if activity:
                tokens_in = activity["prompt_tokens"]
                tokens_out = activity["completion_tokens"]
                cost_usd = activity["usage"]
                req_count = activity["requests"]
                log.info(
                    f"    Matched via activity index: "
                    f"tokens_in={tokens_in:,} tokens_out={tokens_out:,} "
                    f"cost=${cost_usd:.4f} ({req_count} total requests for model that day)"
                )
                log.info(
                    f"    ⚠️  Note: These are DAILY AGGREGATES for '{model_name}', "
                    f"not per-request values."
                )
                ok = update_notion_row(
                    notion_token, page_id, tokens_in, tokens_out, cost_usd
                )
                if ok:
                    log.info(
                        f"    ✅ Updated with aggregate activity data — reconciled "
                        f"(aggregate note: {req_count} requests total for model)"
                    )
                    stats["rows_updated"] += 1
                else:
                    log.error(f"    ❌ Notion update failed for {page_id}")
                    stats["errors"] += 1
            else:
                log.warning(
                    f"    ⚠️  No OR activity match for model {model_name!r} on {target_date}. "
                    f"Row left unreconciled for manual review."
                )
                stats["rows_no_data"] += 1

    log.info("─" * 60)
    log.info(
        f"Reconciliation complete: "
        f"{stats['rows_found']} found | "
        f"{stats['rows_updated']} updated | "
        f"{stats['rows_no_data']} no-data | "
        f"{stats['rows_skipped_local']} local-model | "
        f"{stats['errors']} errors"
    )
    return stats


# ─── Entry Point ───────────────────────────────────────────────────────────────

def main():
    import argparse
    parser = argparse.ArgumentParser(description="OpenRouter ↔ Notion Reconciliation")
    parser.add_argument(
        "--date",
        help="Target date to reconcile (YYYY-MM-DD). Defaults to yesterday.",
        default=None,
    )
    args = parser.parse_args()

    try:
        stats = run_reconciliation(target_date=args.date)

        # Alert if there were errors
        if stats.get("errors", 0) > 0:
            config = load_config()
            mattermost_alert(
                f"**Date:** {stats['date']}\n"
                f"**Rows found:** {stats['rows_found']}\n"
                f"**Updated:** {stats['rows_updated']}\n"
                f"**No data:** {stats['rows_no_data']}\n"
                f"**Errors:** {stats['errors']}\n\n"
                f"Check log: `{LOG_FILE}`",
                config,
            )

        # Alert if rows couldn't be reconciled (no-data rows > 0)
        if stats.get("rows_no_data", 0) > 0:
            config = load_config()
            mattermost_alert(
                f"⚠️ **Manual review needed for {stats['date']}**\n\n"
                f"{stats['rows_no_data']} row(s) could not be auto-reconciled "
                f"(no OpenRouter activity match found for model).\n\n"
                f"Log: `{LOG_FILE}`",
                config,
            )

        sys.exit(0)

    except Exception as e:
        error_msg = traceback.format_exc()
        log.error(f"FATAL: Reconciliation failed: {e}")
        log.error(error_msg)

        # Post alert to Mattermost
        try:
            config = load_config()
            mattermost_alert(
                f"**FATAL ERROR** in reconciliation script\n\n"
                f"```\n{str(e)}\n```\n\n"
                f"Log: `{LOG_FILE}`",
                config,
            )
        except Exception as alert_err:
            log.error(f"Could not send Mattermost alert: {alert_err}")

        sys.exit(1)


if __name__ == "__main__":
    main()
