# DEC-20260223-google-drive-knowledge-organization

**Decision ID:** DEC-20260223-004
**Title:** Adopt Google Drive Knowledge Organization Policy
**Status:** Approved
**Date:** 2026-02-23
**Owner / Approver:** Ed (Steward)

## Context

Google Drive is used for raw and working knowledge capture across the organization. Without structure, it becomes a dumping ground where nothing is findable and nothing is clearly promotable to canonical governance systems.

## Decision

Adopt the Google Drive Knowledge Organization policy (Draft v1.0). Drive content will follow a layered folder model (Intake → Workspace → Reference → Publish → Archive) with naming conventions, format standards, and promotion rules for moving content to the GitHub governance repo.

## Rationale

- Separates raw capture from approved governance records
- Makes Drive content machine-processable for OpenClaw workflows
- Establishes clear promotion path from working docs to canonical systems

## Tradeoffs / Risks

- Requires discipline to maintain folder structure
- Existing Drive content may need phased reorganization

## Impacts

- All new Drive content should follow the layered folder model
- Naming conventions are required for machine processing
- OpenClaw may read/summarize but cannot reorganize without approval

## Dependencies

- GitHub Decision Tracking policy (defines where canonical records live)
- OpenClaw ingestion pipeline (benefits from consistent formats)

## References / Sources

- Policy: `/policies/operations/google-drive-knowledge-organization.md`
- Discussion: Mattermost #executive, 2026-02-23
