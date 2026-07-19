#!/usr/bin/env python3
"""
openrouter-cost-tracker.py

Polls OpenRouter /api/v1/credits for current balance and usage.
Logs to:
  - Mattermost #agent-logs (balance + daily spend estimate)
  - OpenProjects project 3 (STE Ops) work package if daily spend > $5

Runs every 6 hours via launchd (ai.ste.cost-tracker.plist).
Hard local operation — no LLM needed, just API calls.
"""

import json
import os
import sys
import urllib.request
import urllib.error
import base64
from datetime import datetime
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────
SECRETS_ENV = Path.home() / ".ste-secrets" / ".env"
CALIB_FILE  = Path.home() / ".openclaw/workspace/ste-ops/openrouter-calibration.json"
LOG_FILE    = Path.home() / "Library/Logs/ste-agents/cost-tracker.log"

MM_BASE     = "https://ste-business-server.tailebe6d3.ts.net:8065"
MM_CHANNEL  = "hphi4p6noffbtntq7g6pyrzm7e"   # #agent-logs
OP_BASE     = "https://ste-business-server.tailebe6d3.ts.net:8080"
OP_PROJECT  = 3                                 # STE Operations
DAILY_ALERT_THRESHOLD = 5.00                    # $ — create OP work package if exceeded

# ── Helpers ───────────────────────────────────────────────────────────────────
def log(msg: str):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")

def load_env() -> dict:
    env = {}
    if SECRETS_ENV.exists():
        for line in SECRETS_ENV.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, _, v = line.partition("=")
                env[k.strip()] = v.strip()
    # Also check os.environ
    for k in ("OPENROUTER_API_KEY", "MATTERMOST_TOKEN", "OPENPROJECTS_API_KEY"):
        if k in os.environ:
            env[k] = os.environ[k]
    return env

def http_get(url: str, headers: dict) -> dict:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.load(resp)

def http_post(url: str, headers: dict, payload: dict) -> dict:
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.load(resp)

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    log("cost-tracker: starting")

    env = load_env()
    OR_KEY  = env.get("OPENROUTER_API_KEY", "")
    MM_TOK  = env.get("MATTERMOST_TOKEN", "")
    OP_KEY  = env.get("OPENPROJECTS_API_KEY", "")

    if not OR_KEY:
        log("ERROR: OPENROUTER_API_KEY not found")
        sys.exit(1)

    # 1. Fetch OpenRouter credits
    try:
        credits_data = http_get(
            "https://openrouter.ai/api/v1/credits",
            {"Authorization": f"Bearer {OR_KEY}"}
        )["data"]
        total_credits = float(credits_data["total_credits"])
        total_usage   = float(credits_data["total_usage"])
        remaining_credits = total_credits - total_usage
    except Exception as e:
        log(f"ERROR: OpenRouter /credits failed: {e}")
        sys.exit(1)

    # 2. Fetch daily usage from /auth/key
    try:
        key_data = http_get(
            "https://openrouter.ai/api/v1/auth/key",
            {"Authorization": f"Bearer {OR_KEY}"}
        )["data"]
        usage_daily   = float(key_data.get("usage_daily", 0))
        usage_weekly  = float(key_data.get("usage_weekly", 0))
        usage_monthly = float(key_data.get("usage_monthly", 0))
    except Exception as e:
        log(f"ERROR: OpenRouter /auth/key failed: {e}")
        usage_daily = usage_weekly = usage_monthly = 0.0

    # 3. Load calibration for known balance → dynamic rate
    calib = {}
    if CALIB_FILE.exists():
        calib = json.loads(CALIB_FILE.read_text())

    known_balance = calib.get("final_balance_dollars", None)

    if known_balance and remaining_credits > 0:
        # Dynamic rate: current known_balance / remaining_credits
        rate = known_balance / remaining_credits
    else:
        # Fallback: $50 / credits-per-$50 (approximate)
        rate = 1.4354  # last known rate from 2026-07-16

    balance_est    = remaining_credits * rate
    daily_dollars  = usage_daily  * rate
    weekly_dollars = usage_weekly * rate

    log(f"credits remaining: {remaining_credits:.2f} | rate: ${rate:.4f}/credit | balance: ~${balance_est:.2f}")
    log(f"daily: ${daily_dollars:.2f} | weekly: ${weekly_dollars:.2f}")

    # 4. Post to Mattermost #agent-logs
    if MM_TOK:
        ts_str = datetime.now().strftime("%Y-%m-%d %H:%M")
        msg = (
            f"💰 **OpenRouter cost update** ({ts_str})\n"
            f"Balance est: **${balance_est:.2f}** | "
            f"Daily: ${daily_dollars:.2f} | "
            f"Weekly: ${weekly_dollars:.2f}\n"
            f"Credits: {remaining_credits:.2f} remaining of {total_credits:.0f}"
        )
        try:
            http_post(
                f"{MM_BASE}/api/v4/posts",
                {"Authorization": f"Bearer {MM_TOK}", "Content-Type": "application/json"},
                {"channel_id": MM_CHANNEL, "message": msg}
            )
            log("Mattermost: posted to #agent-logs")
        except Exception as e:
            log(f"WARNING: Mattermost post failed: {e}")

    # 5. Create OpenProjects work package if daily > threshold
    if OP_KEY and daily_dollars > DAILY_ALERT_THRESHOLD:
        today = datetime.now().strftime("%Y-%m-%d")
        creds = base64.b64encode(f"apikey:{OP_KEY}".encode()).decode()
        try:
            wp = http_post(
                f"{OP_BASE}/api/v3/projects/{OP_PROJECT}/work_packages",
                {"Authorization": f"Basic {creds}", "Content-Type": "application/json"},
                {
                    "subject": f"COST LOG: OpenRouter {today} daily=${daily_dollars:.2f} weekly=${weekly_dollars:.2f}",
                    "description": {"raw": f"Auto-logged by cost-tracker agent.\nBalance est: ${balance_est:.2f}\nCredits remaining: {remaining_credits:.2f}\nRate: ${rate:.4f}/credit"},
                    "_links": {"type": {"href": f"{OP_BASE}/api/v3/types/1"}}
                }
            )
            log(f"OpenProjects: created WP #{wp.get('id')} in project {OP_PROJECT}")
        except Exception as e:
            log(f"WARNING: OpenProjects WP creation failed: {e}")

    log("cost-tracker: done")

if __name__ == "__main__":
    main()
