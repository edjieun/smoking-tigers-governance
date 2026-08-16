# Finance Directory — Smoking Tigers Media

Status: DRAFT v1.0
Owner: Ed (Steward)
Created: 2026-03-02
Coordinator: EA (Eva)

---

## Purpose

This directory contains local canonical representations of STE Finance databases.
These are the authoritative local schemas — intended to be mirrored in Notion once Notion API access is configured.

## Structure

- `rev-point-ledger/` — Rev Point issuance tracking (RP Ledger)
- `income-tracking/` — Cash received from all sources
- `rp-cash-conversions/` — Rev Point → USD conversion events

## Governance

- All entries marked DRAFT/PENDING until Steward review
- Finance data is Tier: Private (not shared externally)
- Canonical source: Notion (once set up); local files are working copies
- No RTPA or legal terms are binding unless formally executed

## Notion Setup Status

⚠️ **PENDING** — Notion API key not configured. Databases have not yet been created in Notion.

To create Notion Finance DBs:
1. Configure NOTION_API_KEY at `~/.config/notion/api_key`
2. Share the target Notion page with the OpenClaw integration
3. Run creation scripts from this directory

## Open Items (as of 2026-03-02)

- [ ] Configure Notion API key
- [ ] Create Rev Point Ledger database in Notion
- [ ] Create Income Tracking database in Notion
- [ ] Create Rev Point → Cash Conversions database in Notion
- [ ] Link all 3 databases to Trade Like Nick project page
- [ ] Confirm Nick's full legal name
- [ ] Confirm RP face value / pricing rationale ($0.05/RP vs. standard $1/RP)
- [ ] Execute formal RTPA document
