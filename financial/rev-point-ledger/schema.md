# Rev Point Ledger — Database Schema

**Status:** DRAFT — PENDING NOTION SETUP
**Owner:** Ed (Steward)
**Coordinator:** EA (Eva)
**Created:** 2026-03-02
**Purpose:** Track all Rev Point issuance events, including purchaser details, amounts, and RTPA references.

---

## Notion Database Spec

**Database Name:** Rev Point Ledger
**Parent:** Finance (Notion page — TBD once API configured)
**Type:** Full-page database

### Properties / Fields

| Field Name | Property Type | Notes |
|---|---|---|
| Purchaser | Title | Name of the RP purchaser (person or entity) |
| RP Amount | Number | Total Rev Points issued in this transaction |
| Cash Paid | Number | USD amount received (format: currency) |
| Face Value per RP | Number | Calculated: Cash Paid ÷ RP Amount (USD per RP) |
| RTPA Ref | Rich Text | Reference to the Rev Token Purchase Agreement document ID |
| Date | Date | Date of issuance / transaction |
| Project | Select | Associated project (e.g., Trade Like Nick, STM AI, AXIOM) |
| Status | Select | PENDING RTPA / ACTIVE / CONVERTED / ARCHIVED / DRAFT |

### Status Options
- `PENDING RTPA` — Transaction recorded but formal RTPA not yet signed
- `ACTIVE` — RTPA executed, RP live and redeemable per agreement
- `PARTIALLY CONVERTED` — Some RP converted to USD
- `FULLY CONVERTED` — All RP converted to USD
- `ARCHIVED` — Closed / expired
- `DRAFT` — Entry in draft, not yet reviewed by Steward

---

## Notion API Creation Payload

```json
{
  "parent": {"page_id": "<FINANCE_PAGE_ID>"},
  "title": [{"text": {"content": "Rev Point Ledger"}}],
  "is_inline": false,
  "properties": {
    "Purchaser": {"title": {}},
    "RP Amount": {"number": {"format": "number"}},
    "Cash Paid": {"number": {"format": "dollar"}},
    "Face Value per RP": {"number": {"format": "dollar"}},
    "RTPA Ref": {"rich_text": {}},
    "Date": {"date": {}},
    "Project": {
      "select": {
        "options": [
          {"name": "Trade Like Nick", "color": "blue"},
          {"name": "Smoking Tigers AI", "color": "green"},
          {"name": "AXIOM", "color": "purple"},
          {"name": "RMA", "color": "orange"},
          {"name": "Studio Model", "color": "red"}
        ]
      }
    },
    "Status": {
      "select": {
        "options": [
          {"name": "PENDING RTPA", "color": "yellow"},
          {"name": "ACTIVE", "color": "green"},
          {"name": "PARTIALLY CONVERTED", "color": "blue"},
          {"name": "FULLY CONVERTED", "color": "gray"},
          {"name": "ARCHIVED", "color": "default"},
          {"name": "DRAFT", "color": "red"}
        ]
      }
    }
  }
}
```

---

## Notes

- Face Value per RP should be computed automatically if possible
- Standard Q1 face value is $1/RP. Transactions deviating from this require Steward explanation in RTPA Ref or Notes
- All entries remain DRAFT until Steward confirms
