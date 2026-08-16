# Workflow — Notion Export Ingestion and CRUD Authority

Status: Draft v1.0
Owner: Ed (Steward)
Applies To: Executive Council, OpenClaw operators, governance workflows
Last Updated: 2026-02-23

## Purpose

Define a governed workflow for manually exporting Notion content and ingesting it through OpenClaw, with explicit CRUD authority boundaries and human approval gates.

Notion serves as a human-facing UI for business operations. OpenClaw does not directly treat Notion content as executable authority. Instead, a user manually exports a Notion snapshot, which OpenClaw ingests as a bounded source package. OpenClaw then produces reviewable interpretations, proposed CRUD actions, and governance-aware recommendations. Human approval is required for restricted actions and any canonical changes.

## Core Design

- **Notion = UI / interaction surface for operations**
- **Export = user-authorized state snapshot**
- **OpenClaw = ingestion + interpretation + proposal engine**
- **Import/CRUD actions = governed outputs, not automatic truth**

## Design Principles

1. OpenClaw should not treat Notion exports as self-executing instructions
2. Exports are state snapshots and user intent signals, not commands
3. Candidate actions must be classified and proposed, not auto-executed
4. Human approval gates are required for restricted operations
5. Local-first preprocessing; premium models only for high-stakes synthesis

## Operating Model

### 1) User Works in Notion (Business UI)

Users interact with Notion as the primary business interface:
- View project kanban boards (moving cards represents decisions)
- OpenClaw performs work based on those decisions
- Shared calendar for scheduling meetings
- Task management and prioritization

### 2) User Manually Exports Notion

This is the explicit "handoff" to OpenClaw.

Requirements:
- Intentional and bounded
- Reviewable
- No silent API automation drift
- Limited to executive council members
- Changes tracked in git as journal entries (minus private data)
- Annotations point to what in Notion was changed
- Export coordination happens via Mattermost (accessible from mobile)

### 3) OpenClaw Ingests the Export

OpenClaw parses the exported files and builds:
- Normalized records
- Entity map
- Change candidates
- User request interpretations
- Proposed CRUD operations

### 4) OpenClaw Classifies Requested Actions

For each proposed action, classify by operation type:
- **Create**
- **Read / summarize / query**
- **Update**
- **Delete** (usually restricted)

And by authority/risk:
- **Allowed** — autonomous assistive
- **Propose-only** — human review required
- **Restricted** — explicit human approval required each time

### 5) Human Reviews Proposed CRUD Plan

OpenClaw outputs a reviewable plan, not immediate execution.

### 6) Approved Actions Are Executed/Imported

Only after human approval are changes applied to target systems.

## CRUD + Authority Matrix

| Operation | Default Authority | Notes |
|---|---|---|
| Read (summarize/query/organize) | Usually allowed | Low risk |
| Create (draft records/tasks) | Propose-only or allowed in draft zones | No canonical creation without review |
| Update (status/owner/date) | Propose-only unless explicitly scoped | Must be reviewable |
| Delete | Restricted — explicit human approval every time | Treat deletes as radioactive |

## Three-Layer Architecture

### A) Source Snapshot Layer (immutable)

The raw Notion export zip and extracted contents.
- Preserve original zip
- Timestamp it
- Assign batch ID

### B) Interpretation Layer (AI-generated, reviewable)

OpenClaw produces:
- Normalized entities
- Inferred intents
- Proposed CRUD actions
- Ambiguity flags

### C) Execution Layer (governed)

Only approved actions become actual imports/updates.

This separation is the difference between a safe ops system and a chaos machine.

## Folder Structure

Inside the local knowledge staging / ingestion area:

- `notion-exports/incoming/` — landing zone for new exports
- `notion-exports/source-zips/` — preserved original exports
- `notion-exports/extracted/` — extracted export contents
- `notion-exports/normalized/` — normalized records
- `notion-exports/proposed-crud/` — proposed CRUD operation plans
- `notion-exports/reviewed/` — approved and reviewed plans
- `notion-exports/logs/` — processing logs and audit trail

Each batch gets a batch ID:
- `2026-02-23_notion-export_ops_v1`

## Batch Import Plan (Required Output)

Each export batch must produce a batch import plan containing:
- Batch ID
- Export timestamp
- Source scope (which Notion spaces/pages/databases)
- Parsed entities summary
- Detected user requests
- Proposed CRUD operations
- Ambiguities / conflicts
- Restricted actions requiring approval
- Recommended next steps

This artifact is the review surface for human approval.

## AI Resource Constraints

- Do not send the full export to a premium model first
- Use local preprocessing, chunking, extraction, and classification
- Reserve premium models for unresolved conflicts and high-stakes synthesis
- Follow the AI Resource Stewardship and Model Routing policy

## Intent Preservation

OpenClaw must distinguish between:
- **User request** — what the user actually asked/changed
- **AI interpretation** — what OpenClaw infers from the export
- **Proposed operation** — what OpenClaw recommends doing
- **Approved action** — what a human has explicitly authorized

## Conflict Handling

If Notion state changed after export:
- Flag as potential conflict
- Do not auto-resolve
- Present both states for human review

## Security and Access

- Export access limited to executive council members
- Journal entries exclude private data
- Exports containing sensitive information follow the restricted data handling rules
- No credentials or secrets should appear in exports or processing artifacts

## Failure Modes to Avoid

- Treating Notion exports as self-executing instructions
- Auto-executing deletes without human approval
- Over-inferring intent from ambiguous state changes
- Silent API automation replacing the manual export checkpoint
- Mixing source snapshots with interpreted outputs
- No batch ID or audit trail for processed exports

## Review Cadence

Review this workflow after:
- First successful export-to-import cycle
- First conflict or ambiguity in processing
- Changes to Notion workspace structure
- Onboarding additional executive council members to the export process
