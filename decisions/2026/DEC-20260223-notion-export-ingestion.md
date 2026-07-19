# DEC-20260223-notion-export-ingestion

**Decision ID:** DEC-20260223-016
**Title:** Adopt Notion Export Ingestion and CRUD Authority Workflow
**Status:** Approved
**Date:** 2026-02-23
**Owner / Approver:** Ed (Steward)

## Context
Notion serves as the human-facing UI for business operations. A governed workflow is needed to ingest manual Notion exports into OpenClaw with explicit CRUD authority boundaries.

## Decision
Adopt a Notion export ingestion workflow with manual export handoff, three-layer architecture (source/interpretation/execution), CRUD authority matrix, and human approval gates.

## Rationale
- Preserves human checkpoint at export step
- Prevents OpenClaw from treating exports as self-executing instructions
- Supports auditability and reproducible snapshots

## Tradeoffs / Risks
- Manual export step adds friction vs live sync
- Export-to-processing lag may cause stale state conflicts

## Impacts
- Notion exports processed through standardized batch pipeline
- Delete operations always require explicit human approval
- Executive council coordinates exports via Mattermost

## Dependencies
- Mattermost access policy
- Agent authority matrix
- Knowledge staging pipeline

## References / Sources
- Workflow: `workflows/notion-export-ingestion.md`
- Discussion: Mattermost #executive, 2026-02-23
