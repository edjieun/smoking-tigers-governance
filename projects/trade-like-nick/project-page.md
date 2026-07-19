# Trade Like Nick — Project Page

**Status:** ⚠️ DRAFT — PENDING STEWARD REVIEW
**Notion Status:** NOT YET CREATED (Notion API not configured as of 2026-03-02)
**Created By:** EA (Eva) — delegated by Scout
**Created:** 2026-03-02

---

## Project Overview

| Field | Value | Confirmed |
|---|---|---|
| Project Name | Trade Like Nick | ✅ |
| Status | Active (Intake Phase) | ✅ |
| Partner | Nick | ⚠️ Full legal name TBD |
| Project Type | STM Client / Partner Project | ✅ |
| Initial RTPA | $2,500 / 50,000 RP | ✅ |
| RTPA Status | PENDING — formal doc not yet signed | ✅ |
| Date Initiated | 2026-03-02 | ⚠️ Confirm with Ed |
| Steward | Ed Hwang | ✅ |

---

## Financial Records

| Record | Location | Status |
|---|---|---|
| RPL-2026-001 — Initial RP Purchase | `finance/rev-point-ledger/entries/2026-03-02-nick-initial.md` | ✅ CONFIRMED |
| RPL-2026-002 — TLN Ops Workspace Charge | `finance/rev-point-ledger/entries/2026-03-13-nick-tln-ops-workspace.md` | ✅ APPROVED |
| RPL-2026-003 — Contributor Status | `finance/rev-point-ledger/entries/2026-04-24-nick-contributor-status.md` | ✅ CONFIRMED 2026-04-24 |
| Income Tracking | `finance/income-tracking/` (entry to be added) | PENDING NOTION SETUP |
| RP → Cash Conversions | `finance/rp-cash-conversions/` | No entries yet |

**Nick's Current RP Balance: 7,925 RP** (as of 2026-04-24, pre-earnings)
**Contributor Status: ✅ Active — earns RP for participation**

### Notion DB Links (once created)
- Rev Point Ledger: TBD
- Income Tracking: TBD
- Rev Point → Cash Conversions: TBD

---

## Open Items

- [ ] **CRITICAL:** Confirm Nick's full legal name (required for RTPA)
- [ ] **CRITICAL:** Confirm RP pricing rationale — standard face value is $1/RP; this transaction implies $0.05/RP. Is this a bulk rate? Discounted rate? Different RP class?
- [ ] Execute formal RTPA document (governance-ops is drafting)
- [ ] Configure Notion API key and create Finance DBs
- [ ] Create this page in Notion (ExecDB or Projects DB)
- [ ] Link Finance DBs to this project page in Notion
- [ ] Define project scope and deliverables
- [ ] Set RPM (Rev Point Multiplier) for this project
- [ ] Confirm transaction date (currently using 2026-03-02)

---

## Governance & Coordination

- **RTPA Draft:** governance-ops is working on this in parallel
- **RP Ledger Entry:** Created locally as DRAFT (Entry RPL-2026-001)
- **Decision Promotion Status:** DRAFT → awaiting Steward review
- **Related Governance File:** `/srv/q1/governance/smoking-tigers-governance/projects/trade-like-nick/`

---

## Notes

> All information in this file is DRAFT until Steward confirms.
> No RP has been formally issued, and no RTPA is binding, until the formal document is executed.
> Nick's participation is active-intent; governance documents are in progress.

---

## Notion Page Creation Payload (when API is available)

This page should be created in the **ExecDB** or **Projects** database in Notion.

```json
{
  "parent": {"database_id": "<EXECDB_OR_PROJECTS_DB_ID>"},
  "properties": {
    "Name": {"title": [{"text": {"content": "Trade Like Nick"}}]},
    "Status": {"select": {"name": "Active (Intake Phase)"}},
    "Partner": {"rich_text": [{"text": {"content": "Nick (full legal name TBD)"}}]},
    "Initial RTPA": {"rich_text": [{"text": {"content": "$2,500 / 50,000 RP — PENDING EXECUTION"}}]},
    "Type": {"select": {"name": "Client / Partner Project"}},
    "Date": {"date": {"start": "2026-03-02"}},
    "Steward": {"rich_text": [{"text": {"content": "Ed Hwang"}}]}
  }
}
```
