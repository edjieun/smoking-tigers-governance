---
id: SOP-004
title: "SOP-004: Decision Extraction Pipeline"
type: SOP
status: draft
owner: Copilot Agent
authors:
  - Hobbes
---

## Purpose

Extract governance decisions from meeting transcripts and record them as DACI log entries and, where architectural, ADR stubs.

## Pipeline

1. **Transcript arrives** — via Fathom / Mattermost intake into `_incoming/` (or linked from the meeting Work Package).
2. **Agent extracts decision statements** — pull explicit decisions, not full discussion.
3. **Each decision → DACI log entry** with fields:
   - decision text
   - date
   - accountable person
   - consulted parties
   - informed parties
   - linked Work Package (if any)
4. **Commit DACI entries** to `decisions/daci/YYYY-MM-DD-<slug>.md`.
5. **If architectural** — also create an ADR stub in `decisions/adr/ADR-NNN-<slug>.md`.
6. **Wiki update (manual)** — OpenProject wiki write requires a human; create a wiki-creation Task when a page must change.

## Done when

- DACI entries committed with all fields
- ADR stub created for architectural decisions
- Wiki task raised if wiki content must reflect the new decision