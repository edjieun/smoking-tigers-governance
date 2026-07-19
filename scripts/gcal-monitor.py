#!/usr/bin/env python3
"""
gcal-monitor.py

Monitors Ed's Google Calendar for meetings.
Every 30 minutes:
  - Fetches events in next 48 hours
  - Creates OP work packages for meetings that need transcripts
  - Posts reminders to MM #agent-logs 1 hour before meetings
  - After a meeting ends: prompts in MM #transcripts to post the recording

Calendar: ed.hwang@quorum.one (also ed@quorum.one)
Service account: stai-eva-agent@smoking-tigers-agents.iam.gserviceaccount.com
"""

import json, urllib.request, urllib.parse, time, base64, subprocess
import tempfile, os
from datetime import datetime, timezone, timedelta
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────
SECRETS_ENV  = Path.home() / ".ste-secrets/.env"
SA_KEY_FILE  = Path.home() / ".ste-secrets/google/google-service-account.json"
STATE_FILE   = Path.home() / ".openclaw/workspace/ste-ops/gcal-monitor-state.json"
LOG_FILE     = Path.home() / "Library/Logs/ste-agents/gcal-monitor.log"

CAL_ID       = "ed.hwang@quorum.one"
LOOK_AHEAD_H = 48
REMIND_BEFORE_H = 1

MM_BASE      = "https://ste-business-server.tailebe6d3.ts.net:8065"
MM_LOGS      = "hphi4p6noffbtntq7g6pyrzm7e"   # #agent-logs
MM_TRANS     = "uhyi1xfac7yd9esfytouokko4h"   # #transcripts
OP_BASE      = "https://ste-business-server.tailebe6d3.ts.net:8080"

# Meeting title → OP project ID routing
ROUTING = {
    "rma": 13, "sage": 13, "nikki": 13, "kurt": 13,
    "camp audax": 11, "audax": 11, "victor": 11, "brad": 11, "gathering": 11,
    "ste": 6, "website": 6, "christine": 6, "community": 6,
    "ai": 12, "mac mini": 12, "scout": 12, "openclaw": 12, "infra": 12,
}
DEFAULT_PROJECT = 3  # STE Operations

# Meeting keywords that indicate a recordable team meeting (warrant transcript prompt)
RECORDABLE_KEYWORDS = [
    "ed", "sage", "christine", "rma", "camp", "audax", "ste", "smoking tigers",
    "planning", "production", "recording", "meeting", "call", "sync"
]

# ── Helpers ───────────────────────────────────────────────────────────────────
def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")

def load_env():
    env = {}
    if SECRETS_ENV.exists():
        for line in SECRETS_ENV.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, _, v = line.partition("=")
                env[k.strip()] = v.strip()
    return env

def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"reminded": [], "prompted": [], "op_created": []}

def save_state(state):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2))

def get_gcal_token():
    sa = json.loads(SA_KEY_FILE.read_text())
    def b64u(d):
        if isinstance(d, str): d = d.encode()
        return base64.urlsafe_b64encode(d).rstrip(b'=').decode()
    header = b64u(json.dumps({"alg":"RS256","typ":"JWT"}))
    now = int(time.time())
    claim = b64u(json.dumps({
        "iss": sa["client_email"],
        "scope": "https://www.googleapis.com/auth/calendar.readonly",
        "aud": "https://oauth2.googleapis.com/token",
        "iat": now, "exp": now + 3600
    }))
    signing_input = f"{header}.{claim}"
    with tempfile.NamedTemporaryFile(mode='w', suffix='.pem', delete=False) as f:
        f.write(sa["private_key"]); kf = f.name
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write(signing_input); df = f.name
    try:
        sig = subprocess.check_output(["openssl","dgst","-sha256","-sign",kf,"-binary",df])
        jwt = f"{signing_input}.{b64u(sig)}"
        data = urllib.parse.urlencode({
            "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
            "assertion": jwt
        }).encode()
        req = urllib.request.Request(
            "https://oauth2.googleapis.com/token", data=data,
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        with urllib.request.urlopen(req, timeout=10) as r:
            return json.load(r)["access_token"]
    finally:
        os.unlink(kf); os.unlink(df)

def http_get(url, headers):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.load(r)

def http_post(url, headers, payload):
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.load(r)

def mm_post(channel_id, message, mm_token):
    try:
        http_post(
            f"{MM_BASE}/api/v4/posts",
            {"Authorization": f"Bearer {mm_token}", "Content-Type": "application/json"},
            {"channel_id": channel_id, "message": message}
        )
        log(f"MM: posted to {channel_id}")
    except Exception as e:
        log(f"WARNING: MM post failed: {e}")

def op_create_wp(project_id, subject, description, op_key):
    try:
        creds = base64.b64encode(f"apikey:{op_key}".encode()).decode()
        wp = http_post(
            f"{OP_BASE}/api/v3/projects/{project_id}/work_packages",
            {"Authorization": f"Basic {creds}", "Content-Type": "application/json"},
            {
                "subject": subject,
                "description": {"raw": description},
                "_links": {"type": {"href": f"{OP_BASE}/api/v3/types/1"}}
            }
        )
        log(f"OP: created WP #{wp.get('id')} in project {project_id}")
        return wp.get("id")
    except Exception as e:
        log(f"WARNING: OP WP creation failed: {e}")
        return None

def route_project(title: str) -> int:
    title_lower = title.lower()
    for kw, pid in ROUTING.items():
        if kw in title_lower:
            return pid
    return DEFAULT_PROJECT

def is_recordable(title: str) -> bool:
    title_lower = title.lower()
    return any(kw in title_lower for kw in RECORDABLE_KEYWORDS)

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    log("gcal-monitor: starting")
    env = load_env()
    mm_token = env.get("MATTERMOST_TOKEN", "")
    op_key   = env.get("OPENPROJECTS_API_KEY", "")

    try:
        gcal_token = get_gcal_token()
        log("gcal-monitor: got GCal token")
    except Exception as e:
        log(f"ERROR: GCal token failed: {e}")
        return

    now = datetime.now(timezone.utc)
    t_min = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    t_max = (now + timedelta(hours=LOOK_AHEAD_H)).strftime("%Y-%m-%dT%H:%M:%SZ")

    try:
        events_data = http_get(
            f"https://www.googleapis.com/calendar/v3/calendars/{urllib.parse.quote(CAL_ID)}/events"
            f"?timeMin={t_min}&timeMax={t_max}&singleEvents=true&orderBy=startTime&maxResults=20",
            {"Authorization": f"Bearer {gcal_token}"}
        )
        events = events_data.get("items", [])
        log(f"gcal-monitor: {len(events)} events in next {LOOK_AHEAD_H}h")
    except Exception as e:
        log(f"ERROR: GCal events fetch failed: {e}")
        return

    state = load_state()

    for event in events:
        eid     = event.get("id", "")
        title   = event.get("summary", "(no title)")
        start   = event.get("start", {}).get("dateTime", event.get("start", {}).get("date", ""))
        end     = event.get("end", {}).get("dateTime", event.get("end", {}).get("date", ""))
        project = route_project(title)

        # Parse start/end times
        try:
            if "T" in start:
                start_dt = datetime.fromisoformat(start.replace("Z", "+00:00"))
                end_dt   = datetime.fromisoformat(end.replace("Z", "+00:00"))
            else:
                continue  # all-day events — skip
        except Exception:
            continue

        minutes_until = (start_dt - now).total_seconds() / 60
        minutes_since_end = (now - end_dt).total_seconds() / 60

        # 1. Create OP work package for recordable meetings (once per event)
        if eid not in state["op_created"] and is_recordable(title) and minutes_until > 0:
            start_str = start_dt.strftime("%Y-%m-%d %H:%M")
            wp_id = op_create_wp(
                project,
                f"Record + post transcript: {title} ({start_dt.strftime('%Y-%m-%d')})",
                f"Meeting: {title}\nStart: {start_str}\nCalendar: {CAL_ID}\n"
                f"Action: Record the meeting, then post the raw transcript to MM #transcripts using @scout.",
                op_key
            )
            if wp_id:
                state["op_created"].append(eid)
                if mm_token:
                    mm_post(MM_LOGS,
                        f"📅 New meeting on calendar: **{title}** at {start_dt.strftime('%a %b %d %H:%M')}\n"
                        f"OP work package created: [WP #{wp_id}]({OP_BASE}/work_packages/{wp_id})",
                        mm_token
                    )

        # 2. Send 1-hour reminder
        if eid not in state["reminded"] and 0 < minutes_until <= 60 and is_recordable(title):
            if mm_token:
                mm_post(MM_LOGS,
                    f"⏰ **1-hour reminder:** {title} starts at {start_dt.strftime('%H:%M')}\n"
                    f"Remember to start recording (Fathom or built-in). Post transcript to #transcripts after.",
                    mm_token
                )
            state["reminded"].append(eid)
            log(f"Sent 1h reminder for: {title}")

        # 3. Post transcript prompt after meeting ends (within 30 min of end)
        if eid not in state["prompted"] and 0 <= minutes_since_end <= 30 and is_recordable(title):
            if mm_token:
                mm_post(MM_TRANS,
                    f"📅 **{title}** just ended.\n"
                    f"When you have the transcript or recording link, post it here and @scout will process it.\n"
                    f"— _gcal-monitor_",
                    mm_token
                )
            state["prompted"].append(eid)
            log(f"Sent post-meeting prompt for: {title}")

    # Prune old state entries (keep last 50)
    for key in ("reminded", "prompted", "op_created"):
        state[key] = state[key][-50:]

    save_state(state)
    log("gcal-monitor: done")

if __name__ == "__main__":
    main()
