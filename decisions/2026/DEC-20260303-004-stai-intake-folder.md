# DEC-20260303-004 — STAI Intake Folder Established in iCloud

**Decision ID:** DEC-20260303-004
**Title:** STAI Intake Folder Established in iCloud
**Status:** Approved
**Date:** 2026-03-03
**Owner / Approver:** Ed (Steward)

---

## Context

The iCloud Drive folder previously named "Intake Directory" was renamed to "STAI Intake" to establish a clearly named, purpose-specific intake channel for documents and files originating from iPhone and iPad. This formalizes the mobile intake path as a distinct, labeled location within iCloud Drive.

## Decision

`iCloud Drive/STAI Intake/` is the official mobile intake path for Smoking Tigers. EA monitors this folder alongside `~/Desktop/intake/` as a parallel intake source. Files placed in STAI Intake from mobile devices enter the EA intake pipeline on the next processing cycle.

## Rationale

- Clear, unambiguous naming prevents confusion with generic folders
- Establishes a defined mobile intake channel alongside the existing desktop intake path
- EA can monitor both locations within a single intake pipeline pass
- Aligns with the intake taxonomy defined in Phase 2 (see DEC-20260303-005)

## Tradeoffs / Risks

- iCloud sync latency means files may not be immediately available on Mac Mini — EA must tolerate sync delays
- No automatic differentiation between mobile-originated and desktop-originated files once in pipeline (acceptable at this stage)
- Folder rename may require brief user habit adjustment

## Impacts

- EA: monitors `iCloud Drive/STAI Intake/` in addition to `~/Desktop/intake/`
- Ed / STM users: STAI Intake is the designated drop folder for mobile-originating documents
- Intake taxonomy docs should reference this path

## Dependencies

- iCloud Drive sync active on Mac Mini
- EA intake pipeline configured to watch this path
- Related: DEC-20260303-005 (EA pipeline definition)

## References / Sources

- Phase 2 EA pipeline work: 2026-03-03
- Intake taxonomy: see docs/ea-pipeline.md (referenced in DEC-20260303-005)

## Change History

| Date | Change | Author |
|------|--------|--------|
| 2026-03-03 | Initial draft | Governance Ops |
| 2026-03-04 | Approved by Ed (Steward) | Ed |
