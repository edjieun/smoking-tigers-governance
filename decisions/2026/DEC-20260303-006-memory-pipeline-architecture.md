# DEC-20260303-006 — Memory Pipeline Architecture Adopted

**Decision ID:** DEC-20260303-006
**Title:** Memory Pipeline Architecture Adopted
**Status:** Approved
**Date:** 2026-03-03
**Owner / Approver:** Ed (Steward)

---

## Context

Knowledge-ops runs a nightly memory digest (11 PM Pacific) that reads Scout's session JSONL log, extracts a clean transcript via a pre-processing script (`extract-session-transcript.py`), and writes structured memory files to `memory/YYYY-MM-DD.md` and updates `MEMORY.md`. A fix was applied on 2026-03-03: the cron job delivery target was missing, preventing completion notifications from reaching the team. The target has been set to deliver to the `#executive` channel on completion.

## Decision

The memory pipeline — comprising `get-scout-session.sh`, `extract-session-transcript.py`, and the knowledge-ops HEARTBEAT cron job — is the official Scout memory architecture. Nightly execution at 11 PM Pacific produces structured daily memory files and updates the master `MEMORY.md`. Completion events are delivered to the `#executive` Mattermost channel.

## Rationale

- Persistent, structured memory enables Scout to maintain context across sessions without relying solely on in-context history
- Pipeline separates raw session data (JSONL) from clean, queryable memory artifacts — good separation of concerns
- Nightly cadence is appropriate for daily operational memory without excessive processing overhead
- `#executive` delivery ensures Ed and the executive team have visibility into memory pipeline health

## Memory Pruning Policy

Memory files accumulate indefinitely without management. The following pruning rules apply:

### Daily Memory Files (`memory/YYYY-MM-DD.md`)
- **Retention:** 90 days rolling window
- **After 90 days:** Daily files are archived to `memory/archive/YYYY/` (not deleted)
- **Archive format:** Unchanged — preserve original content
- **Trigger:** Knowledge-ops checks for eligible files during each nightly run and moves any that exceed the 90-day window

### Master Memory (`MEMORY.md`)
- **Retention:** Permanent — never pruned automatically
- **Policy:** MEMORY.md is a curated summary, not a raw log. Knowledge-ops may propose additions but may not delete or overwrite entries without explicit Ed (Steward) approval
- **Review cadence:** Ed reviews MEMORY.md for staleness monthly (or on-demand)

### Archive Pruning
- Archive files older than 1 year may be deleted by Scout with Ed's explicit approval
- No automatic deletion of archives without human sign-off

### Rationale
- 90-day rolling window balances context availability vs. storage growth
- Archive-before-delete prevents irreversible loss
- MEMORY.md as permanent curated record preserves institutional knowledge
- Human approval gate on archive deletion protects against accidental data loss

---

## Tradeoffs / Risks

- Pipeline depends on Scout session JSONL availability — if session logging fails, nightly digest produces no output
- `extract-session-transcript.py` quality directly affects memory accuracy — script errors can corrupt memory
- Single-agent pipeline (knowledge-ops) is a single point of failure; no fallback if knowledge-ops heartbeat fails
- Memory archive directory grows over time — annual deletion requires explicit Ed approval

## Impacts

- Scout: benefits from structured persistent memory updated nightly
- Knowledge-ops: responsible for nightly pipeline execution and health
- Ed / `#executive`: receives nightly completion notification confirming memory update
- Ops: `get-scout-session.sh` and `extract-session-transcript.py` must be maintained as infrastructure scripts

## Dependencies

- Scout session JSONL logging (must be active)
- `get-scout-session.sh` (retrieval script)
- `extract-session-transcript.py` (transcript extraction script)
- Knowledge-ops HEARTBEAT cron job (nightly, 11 PM Pacific)
- `#executive` Mattermost channel (delivery target)
- `memory/YYYY-MM-DD.md` write path
- `MEMORY.md` (master memory index)

## References / Sources

- Memory pipeline build and fix session: 2026-03-03
- Cron delivery fix: target set to `#executive` (2026-03-03)
- Related: knowledge-ops agent HEARTBEAT config

## Change History

| Date | Change | Author |
|------|--------|--------|
| 2026-03-03 | Initial draft | Governance Ops |
| 2026-03-04 | Approved by Ed (Steward) | Ed |
| 2026-03-05 | Memory Pruning Policy added — Approved by Ed (Steward) | Scout |
