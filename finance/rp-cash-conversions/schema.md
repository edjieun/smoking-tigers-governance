# Rev Point → Cash Conversions — Database Schema

**Status:** DRAFT — PENDING NOTION SETUP
**Owner:** Ed (Steward)
**Coordinator:** EA (Eva)
**Created:** 2026-03-02
**Purpose:** Track when Rev Points convert to USD payouts. This is the execution record of the RP redemption process.

---

## Notion Database Spec

**Database Name:** Rev Point → Cash Conversions
**Parent:** Finance (Notion page — TBD)
**Type:** Full-page database

### Properties / Fields

| Field Name | Property Type | Notes |
|---|---|---|
| Name | Title | Conversion event identifier (e.g., "Nick Q1-2026 Conversion #1") |
| Holder | Rich Text | RP holder receiving USD payout |
| RP Amount | Number | Number of Rev Points being converted |
| Conversion Rate | Number | USD per RP at time of conversion |
| USD Amount | Number | Total USD paid out (RP Amount × Conversion Rate) |
| Date | Date | Date of conversion/payout |
| Approval Ref | Rich Text | Reference to Steward approval decision ID |
| Notes | Rich Text | Context, source pool, constraints applied, etc. |

### Governance Notes
- Conversion events require explicit Steward approval
- Conversion rate is set at time of conversion, not at time of RP issuance
- Subject to Recovery Pool throttle (≤20% annual EBITDA for STM AI; project-specific for others)
- Recovery Cap must not be exceeded

---

## Notion API Creation Payload

```json
{
  "parent": {"page_id": "<FINANCE_PAGE_ID>"},
  "title": [{"text": {"content": "Rev Point → Cash Conversions"}}],
  "is_inline": false,
  "properties": {
    "Name": {"title": {}},
    "Holder": {"rich_text": {}},
    "RP Amount": {"number": {"format": "number"}},
    "Conversion Rate": {"number": {"format": "dollar"}},
    "USD Amount": {"number": {"format": "dollar"}},
    "Date": {"date": {}},
    "Approval Ref": {"rich_text": {}},
    "Notes": {"rich_text": {}}
  }
}
```

---

## Notes

- No entries exist yet as of 2026-03-02 (first RP issuance is PENDING RTPA)
- First conversion event for Trade Like Nick will require:
  - Executed RTPA
  - Steward approval decision
  - Recovery Pool allocation confirmed
  - Compliance check against Recovery Cap
