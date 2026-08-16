# Rev Point Ledger Entry — Nick / Trade Like Nick

**Entry ID:** RPL-2026-001
**Status:** ✅ CONFIRMED — Steward clarified 2026-03-13
**Created:** 2026-03-02
**Created By:** EA (Eva) — delegated by Scout/Ed
**Updated:** 2026-03-13 — Steward correction applied

---

## Transaction Details

| Field | Value | Notes |
|---|---|---|
| Purchaser | Nick Pham | Trade Like Nick |
| RP Amount | 12,500 RP | ✅ Canonical — confirmed by Steward 2026-03-13 |
| Cash Paid | $2,500 USD | ✅ |
| Rate | $0.20/RP (20 cents on the dollar) | Standard TLN deal rate |
| Face Value | $1.00/RP | Standard Q1 face value |
| Agreement Type | Contribution Agreement + CCA | Nick is NOT signing an RTPA — see note below |
| Date | 2026-03-02 | ✅ |
| Project | Trade Like Nick | ✅ |
| Status | ACTIVE — pending Contribution Agreement execution |

---

## Steward Notes (2026-03-13)

**On the 50,000 RP entry:** A special discounted rate ($0.05/RP) was offered but NOT accepted by Nick. That offer is void. Canonical transaction is 12,500 RP for $2,500 at $0.20/RP.

**On the agreement instrument:** Nick is NOT purchasing RP via an RTPA. He is purchasing the **right to use Ed's rev points**. The correct instrument is a **Contribution Agreement** — stating Nick is launching Trade Like Nick — designed to work in synergy with the CCA (Creator Content Agreement). Governance-ops should draft accordingly.

---

## Governance Notes

- RTPA-DRAFT-2026-001 is VOID — wrong instrument. Draft Contribution Agreement instead.
- Contribution Agreement must be synced with CCA
- Entry is linked to: `/projects/trade-like-nick/` in governance repo

---

## Notion Entry Payload (when DB is live)

```json
{
  "parent": {"database_id": "<REV_POINT_LEDGER_DB_ID>"},
  "properties": {
    "Purchaser": {"title": [{"text": {"content": "Nick"}}]},
    "RP Amount": {"number": 50000},
    "Cash Paid": {"number": 2500},
    "Face Value per RP": {"number": 0.05},
    "RTPA Ref": {"rich_text": [{"text": {"content": "RTPA-DRAFT-2026-001 — PENDING EXECUTION"}}]},
    "Date": {"date": {"start": "2026-03-02"}},
    "Project": {"select": {"name": "Trade Like Nick"}},
    "Status": {"select": {"name": "PENDING RTPA"}}
  }
}
```
