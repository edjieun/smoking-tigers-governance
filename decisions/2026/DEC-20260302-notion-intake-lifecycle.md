# DEC-20260302-notion-intake-lifecycle

**Decision ID:** DEC-20260302-001
**Title:** Fix & Upgrade Notion Intake System — Adopt Intake Lifecycle Workflow
**Status:** Draft (pending Ed confirmation of truncated constraints)
**Date:** 2026-03-02
**Owner / Approver:** Ed (Steward)

## Context

The existing Notion export ingestion workflow (DEC-20260223-016) defined the broad architecture
but lacked operational specifics: trigger logic, database write targets, activation eligibility
criteria, and governance constraints around project activation.

Ed directed Scout to fix and upgrade the Notion intake system with the following requirements:
- Ed exports Notion teamspace as zip to Smoking Tigers Google Drive folder
- Google Drive is too large to store locally — stays in cloud
- OpenClaw must manage knowledge via memory artifacts (especially project knowledge bibles as RAG)
- Produce: intake lifecycle model, trigger logic, database write logic, activation eligibility criteria
- Governance constraint: no project activation without RP/cash structure (message truncated at this point)

## Decision

Adopt the Notion Intake Lifecycle workflow as defined in `workflows/notion-intake-lifecycle.md`.

Key elements:
- Ed-initiated intake via Mattermost signal
- knowledge-ops downloads only the specific export zip (Drive stays in cloud)
- Batch Import Plan required for every cycle, reviewed before any writes
- Database writes target governance repo (canonical), not Notion directly
- Project activation requires Tier 1–4 criteria including both RP AND cash structure
- knowledge-ops flags eligibility — Ed approves activation
- RP/financial data restricted to EA; knowledge-ops does not process it

## Status Note

Ed's message was truncated at "no project activation without RP/cash structure" —
additional constraints may follow. This decision is marked Draft until confirmed.

## Rationale

- Closes gap between architecture (existing workflow) and operations (trigger/write/eligibility)
- Enforces dual-currency requirement (RP + cash) as activation gate
- Keeps Drive in cloud, knowledge in memory — avoids local storage sprawl
- Maintains human approval gates throughout

## Impacts

- knowledge-ops SOURCES.md to be updated with Drive download path
- Drive intake folder path to be confirmed by Ed
- ste-index.md (Drive index) to be built
- EA Notion Finance DBs required before RP data can be properly classified

## Dependencies

- `workflows/notion-export-ingestion.md` (superseded for operational detail by this doc)
- `workflows/knowledge-staging-pipeline.md`
- `policies/operations/google-drive-knowledge-organization.md`
- EA agent for financial/RP data handling

## References

- Workflow: `workflows/notion-intake-lifecycle.md`
- Discussion: Mattermost #executive, 2026-03-02
- Prior decision: DEC-20260223-016 (notion-export-ingestion)
