# Income Tracking — Database Schema

**Status:** DRAFT — PENDING NOTION SETUP
**Owner:** Ed (Steward)
**Coordinator:** EA (Eva)
**Created:** 2026-03-02
**Purpose:** Track all cash received by STE across all sources and projects.

---

## Notion Database Spec

**Database Name:** Income Tracking
**Parent:** Finance (Notion page — TBD)
**Type:** Full-page database

### Properties / Fields

| Field Name | Property Type | Notes |
|---|---|---|
| Name | Title | Brief description of the income event |
| Amount | Number | USD received (format: currency) |
| Source / Client | Rich Text | Who paid (person, entity, or platform) |
| Project | Select | Associated project |
| Date | Date | Date received |
| Category | Select | Type of income (see options below) |
| Notes | Rich Text | Additional context, invoice ref, memo, etc. |

### Category Options
- `RTPA Payment` — Rev Token Purchase Agreement cash
- `Service Revenue` — Direct services/consulting
- `Platform Revenue` — YouTube, Spotify, streaming, etc.
- `Licensing` — IP licensing revenue
- `Grant / Award` — Non-repayable funding
- `Other` — Catch-all; must include explanation in Notes

### Project Options (same as Rev Point Ledger)
- Trade Like Nick
- Smoking Tigers AI
- AXIOM
- RMA
- Studio Model
- STM General

---

## Notion API Creation Payload

```json
{
  "parent": {"page_id": "<FINANCE_PAGE_ID>"},
  "title": [{"text": {"content": "Income Tracking"}}],
  "is_inline": false,
  "properties": {
    "Name": {"title": {}},
    "Amount": {"number": {"format": "dollar"}},
    "Source / Client": {"rich_text": {}},
    "Project": {
      "select": {
        "options": [
          {"name": "Trade Like Nick", "color": "blue"},
          {"name": "Smoking Tigers AI", "color": "green"},
          {"name": "AXIOM", "color": "purple"},
          {"name": "RMA", "color": "orange"},
          {"name": "Studio Model", "color": "red"},
          {"name": "STM General", "color": "gray"}
        ]
      }
    },
    "Date": {"date": {}},
    "Category": {
      "select": {
        "options": [
          {"name": "RTPA Payment", "color": "blue"},
          {"name": "Service Revenue", "color": "green"},
          {"name": "Platform Revenue", "color": "purple"},
          {"name": "Licensing", "color": "orange"},
          {"name": "Grant / Award", "color": "yellow"},
          {"name": "Other", "color": "default"}
        ]
      }
    },
    "Notes": {"rich_text": {}}
  }
}
```

---

## First Entry — Nick / Trade Like Nick

```json
{
  "parent": {"database_id": "<INCOME_TRACKING_DB_ID>"},
  "properties": {
    "Name": {"title": [{"text": {"content": "Nick — RTPA Initial Payment"}}]},
    "Amount": {"number": 2500},
    "Source / Client": {"rich_text": [{"text": {"content": "Nick (full name TBD)"}}]},
    "Project": {"select": {"name": "Trade Like Nick"}},
    "Date": {"date": {"start": "2026-03-02"}},
    "Category": {"select": {"name": "RTPA Payment"}},
    "Notes": {"rich_text": [{"text": {"content": "DRAFT — $2,500 received in exchange for 50,000 RP. RTPA not yet formally executed. Confirm date and Nick's legal name before finalizing."}}]}
  }
}
```
