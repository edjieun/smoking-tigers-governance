# Policy — Google Drive Knowledge Organization (Working Knowledge and Intake)

Status: Draft v1.0
Owner: Ed (Steward)
Applies To: Executive Council, Project Leads, Contributors, OpenClaw-assisted knowledge workflows
Last Updated: 2026-02-23

## Purpose

Establish best practices for organizing Google Drive knowledge so that:
- raw inputs are preserved
- working documents stay findable
- canonical decisions/policies are promotable to governance systems
- OpenClaw can ingest and process files more reliably

## Core Principle

**Drive is a working knowledge environment, not the final source of truth for approved governance decisions.**

Drive holds raw and working materials. Canonical governance records live in the governance repo (GitHub) and/or designated systems of record.

## Folder Layer Model (Recommended)

Use a layered structure to separate maturity of information.

### 1) `Intake/`

Raw capture from humans and tools. High noise, low structure.

Examples:
- voice memo transcripts
- stream-of-consciousness notes
- AI rough analyses
- imported chat exports
- screenshots
- meeting dumps

### 2) `Workspace/`

Active working docs being shaped into usable outputs.

Examples:
- draft policies
- draft meeting summaries
- project planning docs
- synthesis notes

### 3) `Reference/`

Stable reference materials used repeatedly but not necessarily canonical governance.

Examples:
- templates
- style guides
- vendor docs
- research summaries

### 4) `Publish/` or `Promoted/` (optional)

Clean outputs ready for promotion or distribution.

Examples:
- reviewed policies
- approved one-pagers
- presentation-ready docs

### 5) `Archive/`

Inactive, superseded, or historical material retained for traceability.

## Naming Conventions (Required)

Use names that support sorting and machine processing.

### General File Naming

`YYYY-MM-DD_topic_short-description_v#.<ext>`

Examples:
- `2026-02-22_exec-meeting_capture-summary_v1.md`
- `2026-02-22_calendar-policy_draft_v2.md`

### Avoid

- `notes final final REALLY FINAL.docx`
- `Untitled document`
- `New Text Document (4)`

## File Format Standards (OpenClaw-Friendly)

Preferred formats for knowledge processing:
- `.md`
- `.txt`
- `.csv`
- `.json`

Allowed with caution:
- `.docx`
- `.pdf`
- image files (if OCR/transcription pipeline exists)

Avoid as primary working format when possible:
- `.rtf` (can introduce formatting noise)
- proprietary exports with inconsistent parsing

## Metadata Header Standard (Recommended for `.md`)

At top of markdown docs, include:
- Title
- Status (draft/review/approved)
- Owner
- Date
- Source(s)
- Tags

This improves human review and AI parsing consistency.

## Source Integrity Rules

- Preserve original raw files in `Intake/`
- Do not overwrite raw source content after ingest
- If transformed, create a new file in `Workspace/` and reference the original

Example:
- `Intake/2026-02-22_voice-memo-transcript_raw.txt`
- `Workspace/2026-02-22_voice-memo-synthesis_v1.md`

## Promotion Rules (Drive → Canonical)

Documents may be promoted from Drive working docs to canonical records only when:
- reviewed by appropriate human owner
- status is explicit
- source inputs are known
- version is identifiable

Promotions should be logged (manually or via OpenClaw) to preserve traceability.

## OpenClaw Interaction Rules

OpenClaw may:
- read/summarize intake files
- propose folder organization
- generate structured drafts from raw content
- produce promotion-ready outputs

OpenClaw should not:
- silently reorganize or rename large portions of Drive without approved policy/workflow
- delete source files without explicit human authorization
- mark drafts as approved

## Reorganization Policy (Important)

Because Drive often contains mixed historical content, reorganization should happen in phases.

### Phase-Based Reorganization

1. **Map** current structure
2. **Classify** by folder purpose (intake/workspace/reference/archive)
3. **Propose** moves/renames
4. **Human review/approval**
5. **Execute in batches**
6. **Log changes**

Avoid "big bang" reorganizations that break links and habits.

## Link Stability

Before moving files/folders:
- identify shared links in active use
- confirm impact on Notion/docs/workflows
- prioritize alias/index docs when possible instead of constant moves

## Access and Permissions

Apply least privilege:
- Executive / governance folders limited access
- Project folders role-based access
- Intake folders can be broad or narrow depending on sensitivity
- Sensitive legal/financial/security materials stored in restricted folders

## Drive-to-Repo Relationship

Use this decision rule:
- **Raw / in-progress / exploratory** → Google Drive
- **Approved governance / policy / decision logs** → GitHub repo
- **Task execution / databases / dashboards** → Notion (or equivalent operational systems)

This prevents overloading one system with every function.

## Minimum Folder Set (Practical Starter)

If starting small, use:
- `Intake/`
- `Workspace/`
- `Reference/`
- `Archive/`

Add project-specific subfolders once the pattern is stable.

## Audit and Cleanup Rhythm

Monthly (or biweekly for active teams):
- archive stale drafts
- standardize filenames
- remove duplicates (keep source + latest working draft)
- identify promotable docs
- log major reorg actions

## Failure Modes to Avoid

- giant dumping ground folders
- no separation between raw and approved materials
- rich text everywhere
- file names with no dates/versions
- silent AI rewrites replacing source files
- "final" files with no status/owner

## Review Cadence

Review after:
- first reorganization pass
- onboarding of new contributors
- major tooling change (OpenClaw ingestion, RAG pipeline, etc.)
