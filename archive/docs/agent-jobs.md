---
last-updated: 2026-07-16
purpose: Scheduled agent jobs running on Mac Mini (OpenClaw cron). All jobs are autonomous — no manual input required.
---

# Scheduled Agent Jobs

All jobs run on the Mac Mini via OpenClaw's cron system (`~/.openclaw/cron/jobs.json`).
All jobs use local models only (hard local block). Failures post to MM `#agent-logs`.

---

## Job 1: OpenRouter Cost Tracker

**Schedule:** Every 6 hours (`0 */6 * * *`)
**Model:** `lmstudio/qwen/qwen3.5-9b`
**Owner:** Ed Hwang

### What it does
1. Calls `GET https://openrouter.ai/api/v1/auth/key` with `Authorization: Bearer $OPENROUTER_API_KEY`
2. Reads: `usage_daily`, `usage_weekly`, `usage_monthly`, `total_credits`, `usage`
3. Calculates remaining balance: `(total_credits - usage) × (initial_top_up_dollars / initial_total_credits)`
   - Calibration values (set manually when topping up): store in `~/.openclaw/workspace/ste-ops/openrouter-calibration.json`
4. Creates a LedgerSMB journal entry via the LedgerSMB API (see Job 1b below)
5. Creates an OpenProjects work package in project 3 (STE Ops) if daily spend > $5.00 threshold
6. Posts to MM `#agent-logs`: `💰 OpenRouter daily: $X.XX | weekly: $X.XX | balance: $X.XX`

### Calibration file format
```json
{
  "top_up_date": "2026-07-16",
  "top_up_dollars": 50.00,
  "credits_at_top_up": 2850,
  "usage_at_top_up": 2805.00
}
```
(Update this file whenever Ed tops up the OpenRouter account)

### API reference
```
GET https://openrouter.ai/api/v1/auth/key
Authorization: Bearer {OPENROUTER_API_KEY}

Returns:
{
  "data": {
    "usage": <lifetime credits used>,
    "usage_daily": <credits used today>,
    "usage_weekly": <credits used this week>,
    "usage_monthly": <credits used this month>,
    "total_credits": <total credits ever purchased>
  }
}
```

---

## Job 1b: LedgerSMB Cost Journal Entry

**Triggered by:** Job 1 (daily, when usage_daily > 0)
**Model:** `lmstudio/qwen/qwen3.5-9b`

### What it does
1. Takes the daily usage in dollars (calculated by Job 1)
2. Creates a journal entry in LedgerSMB via its API or web interface
3. Account: AI Infrastructure / OpenRouter
4. Description: `OpenRouter API usage — {date} — {model_breakdown_if_available}`

### LedgerSMB
- URL: `https://ste-business-server.tailebe6d3.ts.net:5762/`
- Auth: Ed's credentials (stored separately — do NOT use service account)
- **Note:** LedgerSMB REST API capabilities need to be verified; may require XML-RPC or scraping

### Fallback (until LedgerSMB API is verified)
Create an OpenProjects work package in project 3:
```
Subject: COST LOG: OpenRouter {date} daily=${X.XX} weekly=${X.XX}
Description: Raw data from /auth/key endpoint. Manual LedgerSMB entry pending.
```

---

## Job 2: Google Calendar Monitor

**Schedule:** Every 30 minutes (`*/30 * * * *`)
**Model:** `lmstudio/qwen/qwen3.5-9b`
**Owner:** Ed Hwang

### What it does
1. Reads Google Calendar for Ed's account (`ed.hwang@quorum.one`)
2. Looks for meetings in the next 48 hours
3. For each meeting that has Fathom recording enabled OR is a known recurring team meeting:
   - Creates an OpenProjects work package: `"Record + post transcript: [meeting title] [date]"`
   - Routes to the correct project based on meeting title keywords
   - Posts reminder to MM `#agent-logs` 1 hour before the meeting
4. After a meeting ends: posts to MM `#transcripts`:
   `"📅 [Meeting title] just ended. Post the transcript here when ready: @ed"`

### Google Calendar Setup Required
The service account `stai-eva-agent@smoking-tigers-agents.iam.gserviceaccount.com`
needs read access to Ed's calendar. Two options:

**Option A — Calendar sharing (recommended, simpler):**
1. Open Google Calendar → Settings → `ed.hwang@quorum.one` calendar → Share with specific people
2. Add: `stai-eva-agent@smoking-tigers-agents.iam.gserviceaccount.com`
3. Permission: "See all event details"
4. No admin access needed

**Option B — Domain-wide delegation (blocked):**
Requires Workspace admin on quorum.one. Not available currently.

### Calendar API
```
GET https://www.googleapis.com/calendar/v3/calendars/{calendarId}/events
Authorization: Bearer {service_account_access_token}
params: timeMin=now, timeMax=now+48h, orderBy=startTime, singleEvents=true
```
Calendar ID: `ed.hwang@quorum.one` (primary calendar)

### Meeting → Project routing (keyword map)
| Keywords in title | OP Project | ID |
|---|---|---|
| RMA, Sage, Nikki | RMA — New Meeting Flow | 13 |
| Camp Audax, Victor, Brad, Gathering | Camp Audax | 11 |
| STE, website, Christine, community | STE Website | 6 |
| AI, Mac Mini, Scout, infra, OpenClaw | STE AI Buildout | 12 |
| Default / no match | STE Operations | 3 |

---

## Job 3: OpenRouter ↔ LedgerSMB Audit

**Schedule:** Weekly, Sunday 9am (`0 9 * * 0`)
**Model:** `lmstudio/qwen/qwen3.5-9b`

### What it does
1. Pulls weekly spend from OpenRouter (`usage_weekly` from `/auth/key`)
2. Pulls LedgerSMB AI Infrastructure cost entries for the past 7 days
3. Compares the two: flag any discrepancy > $1.00
4. Posts audit report to MM `#agent-logs`:
   ```
   📊 Weekly AI Cost Audit
   OpenRouter reported: $X.XX
   LedgerSMB recorded: $X.XX
   Discrepancy: $X.XX [OK / ⚠️ REVIEW]
   ```
5. If discrepancy > $1.00: creates an OpenProjects work package in project 3:
   `AUDIT ALERT: OpenRouter/LedgerSMB discrepancy $X.XX — week of {date}`

---

## Implementation Status

| Job | Status | Blocker |
|---|---|---|
| Job 1: OpenRouter Cost Tracker | ✅ Live — runs every 6h via `ai.ste.cost-tracker` launchd | First run 2026-07-16 16:58 — WP #240 created in OP; posted to MM #agent-logs |
| Job 1b: LedgerSMB Journal Entry | ⬜ Deferred | LedgerSMB REST API format needs verification; fallback = OP work package (already doing) |
| Job 2: Google Calendar Monitor | ✅ Live — runs every 30min via `ai.ste.gcal-monitor` launchd | First run 2026-07-16 17:42 — found 3 events, created WP #241-242 for Ed+Sage Production Planning in OP project 13 |
| Job 3: OpenRouter ↔ LedgerSMB Audit | ⬜ Spec written | Depends on LedgerSMB API (Job 1b) |

---

## Next Steps

1. ~~Share calendar with service account~~ — **DONE**. Calendar `ed.hwang@quorum.one` is shared. Job 2 is live.

2. **Ed: Create the calibration file** with today's top-up data:
   ```bash
   cat > ~/.openclaw/workspace/ste-ops/openrouter-calibration.json << 'EOF'
   {
     "top_up_date": "2026-07-16",
     "top_up_dollars": 50.00,
     "credits_at_top_up": 2850,
     "usage_at_top_up": 2805.0,
     "note": "Balance at end of session was $32.31 with usage=2827.49"
   }
   EOF
   ```
   → Unlocks Job 1 accurate dollar calculations.

3. **Verify LedgerSMB API** — open `https://ste-business-server.tailebe6d3.ts.net:5762/` and check if there's a REST or XML-RPC interface for creating journal entries.
   → Unlocks Job 1b.

4. **Add cron jobs to Mac Mini** — update `~/.openclaw/cron/jobs.json` with Jobs 1, 2, 3.
   → The Mac Mini already has cron running (6 jobs active as of today).
