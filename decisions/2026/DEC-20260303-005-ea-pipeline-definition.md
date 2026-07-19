# DEC-20260303-005 — EA Pipeline Defined (Intake, Templates, Naming, Routing)

**Decision ID:** DEC-20260303-005
**Title:** EA Pipeline Defined (Intake, Templates, Naming, Routing)
**Status:** Approved
**Date:** 2026-03-03
**Owner / Approver:** Ed (Steward)

---

## Context

Phase 2 of EA operational build-out defined the full EA pipeline: intake taxonomy (local desktop + iCloud), output artifact templates (meeting note, task, project brief, daily summary), file naming conventions, and routing map for different input types. This work produced `docs/ea-pipeline.md` as the canonical pipeline reference document.

## Decision

The EA pipeline as defined in `docs/ea-pipeline.md` is the official operating standard for EA. This includes:

- **Intake taxonomy:** `~/Desktop/intake/` (local) and `iCloud Drive/STAI Intake/` (mobile)
- **Output artifact templates:** meeting note, task, project brief, daily summary
- **Naming convention:** `YYYY-MM-DD-[slug]-[descriptor]`
- **Routing map:**
  - Voice memos → transcription (Whisper) → Notion
  - Calendar inputs → Notion
  - Daily summaries → Mattermost DM to Ed
  - Google Drive → manual process (pending Drive API decision)

## Rationale

- Establishes a consistent, repeatable processing standard for EA
- Naming convention ensures chronological sorting and unambiguous identification
- Routing map makes explicit where each input type lands — prevents ad hoc routing decisions
- Daily summaries via Mattermost DM keeps Ed's daily digest in the primary internal comms channel
- Whisper for voice memo transcription keeps audio processing local and private

## Tradeoffs / Risks

- Google Drive left as manual until a Drive API decision is made — creates a gap in full automation
- Routing map is opinionated; any new input type not covered requires a pipeline amendment
- `docs/ea-pipeline.md` must be kept current as the pipeline evolves — stale docs are a governance risk

## Impacts

- EA: operates per `docs/ea-pipeline.md` as the binding standard
- Ed: receives daily summaries via Mattermost DM
- Governance: pipeline changes require an amendment to this decision or a superseding decision
- Ops: Whisper must be available on Mac Mini for voice memo processing

## Dependencies

- `docs/ea-pipeline.md` (must exist and be current)
- DEC-20260303-004 (STAI Intake folder)
- DEC-20260303-003 (Notion API integration — routing destination)
- Whisper installed on Mac Mini
- Google Drive API decision (deferred — manual process in interim)

## References / Sources

- Phase 2 EA pipeline build-out: 2026-03-03
- `docs/ea-pipeline.md` (canonical pipeline reference)
- Related: DEC-20260303-003, DEC-20260303-004

## Change History

| Date | Change | Author |
|------|--------|--------|
| 2026-03-03 | Initial draft | Governance Ops |
| 2026-03-04 | Approved by Ed (Steward) | Ed |
