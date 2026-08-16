# Workflow — Knowledge Staging Pipeline for OpenClaw (Local-First, Agent-Optimized Markdown)
Status: Draft v2.0
Owner: Ed (Steward)
Applies To: Intake processing, local agent workflows, OpenClaw knowledge prep, governance repo support
Last Updated: 2026-02-23

## Purpose
Define a practical **knowledge staging workflow** for turning messy raw inputs (voice memos, transcripts, copied notes, AI outputs, rough documents) into **clean, chunked, markdown knowledge documents** that are:

\- suitable for OpenClaw ingestion
\- optimized for local agents using small-parameter LLMs (via Ollama)
\- reviewable by humans before promotion
\- cost-efficient to process on local compute
\- consistent with governance and system-of-record rules

This workflow is not primarily about LM Studio. It is about building a **repeatable knowledge pipeline** that improves habits and preserves quality.

## Core Principle
**Local compute handles preprocessing and staging. Humans review. OpenClaw operationalizes.**

Use local agents for:
\- capture cleanup
\- sorting
\- splitting
\- metadata shaping
\- markdown standardization

Reserve premium models for:
\- high-stakes synthesis
\- conflict resolution
\- final strategic wording
(See AI Resource Stewardship and Model Routing policy.)

## What This Workflow Produces
The target output is not “files for LM Studio.”

The target output is a set of **OpenClaw-ready staged markdown files** that are:
\- one topic per file (or intentionally grouped)
\- clearly named
\- source-linked
\- chunk-friendly for small local models
\- easy for agents to summarize/extract/route
\- safe for intended processing tier

## Scope
This document covers:
\- intake staging folder design
\- local-agent-assisted preprocessing
\- markdown output standards
\- curation rules for OpenClaw knowledge staging
\- sensitive data separation and handling
\- automation/CLI/Automator opportunities
\- validation checks aligned to user/SOP needs

This document does **not** define:
\- final governance approval or decision authority
\- GitHub merge/approval policy
\- OpenClaw agent authority boundaries
\- model tuning parameters (temperature/context/etc.)

## Relationship to OpenClaw
This is a **knowledge staging pipeline**.

It sits *before* canonical governance workflows and *before* high-authority automation.

### Pipeline Goal
Convert raw, messy inputs into structured markdown knowledge artifacts.

### OpenClaw Goal
Use staged knowledge to assist operations, routing, synthesis, and governance workflows with human approval gates.

### Practical Framing
\- Local tools/agents \= preprocess and shape
\- OpenClaw \= orchestrate and operationalize
\- Human steward \= approve, prioritize, promote

## Why the Prior Version Was Wrong (Design Correction)
The prior version assumed:
\- files were being curated “for LM Studio projects”
\- manual capture/sort/split by the user
\- LM Studio was the primary destination

That is not the intended workflow.

### Corrected Design Intent
\- Curation is for **OpenClaw knowledge staging**
\- Capture/sort/split should be handled by **local agents on the server** (where possible)
\- LM Studio is a helpful tool in the toolchain, not the governing frame
\- The output should be optimized for **small local models and agents**, not just ad hoc retrieval

## Staging Pipeline Overview (Local-First)
Raw Inputs (human \+ machine)
→ Intake landing
→ Local agent preprocessing (capture/sort/normalize/split)
→ Markdown staging (chunked, structured, named)
→ Human review
→ OpenClaw ingestion (selective, by domain)
→ Promotion to working/canonical systems as appropriate

## Recommended Folder Structure (Knowledge Staging-Oriented)
Use a staging-first structure. Example:

Knowledge-Staging/
\- `00-inbox/`
\- `01-raw/`
\- `02-normalized/`
\- `03-chunked-md/`
\- `04-openclaw-staging/`
\- `05-reviewed/`
\- `06-promoted/`
\- `07-restricted/`
\- `08-archive/`
\- `automation/`
\- `logs/`

## Folder Purpose
### `00-inbox/`
Landing zone for new files and captures (human or automated).

Examples:
\- copied notes
\- transcript exports
\- voice memo transcriptions
\- AI rough outputs
\- documents dropped for processing

### `01-raw/`
Preserved source artifacts. Do not overwrite.

Examples:
\- `.rtf`, `.docx`, `.pdf`, images, transcript dumps, exports

### `02-normalized/`
Plain text and markdown conversions with obvious formatting cleanup.

### `03-chunked-md/`
Markdown files split and shaped into chunk-friendly units for local agents and OpenClaw staging.

### `04-openclaw-staging/`
Curated staged markdown files intended for OpenClaw processing by domain/workflow.

### `05-reviewed/`
Human-reviewed staged documents ready for deeper OpenClaw workflows.

### `06-promoted/`
Artifacts promoted onward (e.g., to Workspace/Governance flows) after review.

### `07-restricted/`
Sensitive or access-restricted materials separated from general AI staging.

### `08-archive/`
Historical batches, superseded staged outputs, or retired processing sets.

### `automation/`
Scripts, Automator workflows, helper tooling, templates, and processor configs.

### `logs/`
Processing logs, staging notes, review notes, error logs.

## Processing Ownership Model (Important)
### Local Agents on Server (Default for Mechanical Work)
Capture, sort, normalize, and split should be handled by local agents using small local models (via Ollama) plus deterministic scripts/tools where possible.

### Human Steward / Operator
Reviews outputs, confirms intent, catches policy/meaning drift, approves promotion.

### OpenClaw
Consumes curated staged markdown and uses it for operational workflows (summaries, synthesis, routing, policy support, decision support) within governance boundaries.

## Staging Workflow (Practical, OpenClaw-Oriented)

### Step 1 — Capture (Human or Automated Intake)
New content enters `00-inbox/`.

Sources may include:
\- voice memo transcripts
\- copied notes from LM Studio/ChatGPT
\- meeting exports
\- stream-of-consciousness text
\- rough policy drafts
\- screenshots/OCR output
\- imported documents

**Goal:** collect first, do not over-edit at intake.

### Step 2 — Preserve and Register Raw Inputs (Local Agent \+ Script)
Move originals into `01-raw/` by date/batch/topic using a deterministic naming convention.

Local agents may assist with:
\- file identification
\- suggested names
\- basic classification

Deterministic tools/scripts should handle actual file moves when possible.

**Goal:** preserve source integrity and establish traceability.

### Step 3 — Normalize to Plain Text / Markdown (Local Agent \+ Tools)
Convert files into `.txt` and/or `.md`, clean obvious formatting noise, and save to `02-normalized/`.

Examples:
\- `.rtf` → `.txt`
\- transcript dumps → cleaned `.txt`
\- rough notes → structured `.md`

**Rule:** Preserve the original in `01-raw/`. Never overwrite source artifacts.

### Step 4 — Split and Shape into Chunked Markdown (Local Agent)
Break large files into smaller markdown documents optimized for:
\- one topic / one purpose / one meeting component
\- local small-model processing
\- OpenClaw routing and extraction jobs

Store in `03-chunked-md/`.

Examples:
\- transcript raw (`.txt`) \+ summary (`.md`) \+ actions (`.md`)
\- one policy concept per file
\- one meeting package split into `SUMMARY`, `DECISIONS`, `ACTIONS`, `OPEN_QUESTIONS`

**Goal:** create agent-usable chunks, not giant mixed notes.

### Step 5 — Curate for OpenClaw Staging (Not LM Studio)
Select only relevant, clean, intended files and move/copy into `04-openclaw-staging/` by domain/workflow.

This is curation for **OpenClaw knowledge processing**, not a generic local AI project corpus.

### Step 6 — Human Review and Status Marking
Human reviews staged markdown files before broader OpenClaw processing.

Review focus:
\- intent preserved?
\- wording safe?
\- authority/approval language correct?
\- sensitive info separated?
\- file appropriately scoped/chunked?

Mark status (example):
\- `Draft`
\- `Reviewed`
\- `Ready for OpenClaw`
\- `Restricted`
\- `Needs Rework`

Store reviewed files (or copies) in `05-reviewed/` as needed.

### Step 7 — OpenClaw Processing (Selective, by Domain)
OpenClaw processes reviewed staged files by workflow/domain (not all-at-once ingestion).

Examples:
\- governance staging batch
\- sysops staging batch
\- meeting follow-up batch
\- policy draft support batch

### Step 8 — Promote Outputs (Human-Gated)
Polished outputs may be promoted to:
\- Workspace/Governance flows
\- GitHub governance repo (via decision/policy workflow)
\- Notion/task systems
\- archives/reference sets

Promotion must follow governance approval rules.

## Curation Rules for OpenClaw Staging (Updated)
Do **not** dump your entire Intake Directory into one staging set or one processing run.

Curate by operational domain and job-to-be-done.

### Recommended Staging Domains
\- `governance/`
\- `sysops/`
\- `creator-support/`
\- `meeting-summaries/`
\- `calendar-scheduling/`
\- `tooling-costs/`
\- `security-access/`
\- `intake-recovery/` (temporary recovery batches)

### Why
Smaller, domain-specific staged sets improve:
\- local agent accuracy
\- extraction quality
\- routing clarity
\- token efficiency
\- debugging when outputs go wrong

### Curation Rule
Each staged file set should answer:
\- What job is this for?
\- Which agent/workflow will use it?
\- What system might this be promoted to?
\- What sensitivity tier applies?

If those answers are unclear, it is not ready for staging.

## Quality Checks Before Adding to OpenClaw Staging (Updated)
Before placing a file in `04-openclaw-staging/`, check:

\- Is it plain text or markdown (or intentionally staged source text)?
\- Is the filename descriptive and sortable?
\- Is it scoped to one primary topic/purpose?
\- Does it preserve source meaning (no accidental policy drift)?
\- Does it contain authority/approval language that needs human review?
\- Does it contain sensitive data that belongs in `07-restricted/` instead?
\- Is it the best current version (not duplicate/noisy)?
\- Is it chunked appropriately for local agent processing?

If “no” to any item, fix before staging.

## Sensitive Data Handling (Updated for Knowledge Pipeline)
Because staged files may be processed by local agents and routed into operational workflows:

### Default Rule
Separate sensitive data by folder, access, and processing intent.

### Required Practices
\- Do not place secrets, API keys, passwords, tokens, or recovery codes in `04-openclaw-staging/`
\- Move or copy sensitive materials to `07-restricted/` and mark clearly
\- Redact sensitive values in otherwise-useful documents before general staging
\- Keep credentials and operational secrets in dedicated secret-management paths/tools (not knowledge docs)
\- Use role-based access for restricted staging folders

### Governance-Specific Risk
Be careful with:
\- legal/financial details
\- private security architecture specifics
\- personal identifying info
\- internal credentials/configs copied from `.env` or dashboards

### Processing Rule for Agents
Agents should treat unclear sensitivity as **restricted-by-default** and flag for human review.

## File Format Standards (Still Important)
### Preferred for staged knowledge
\- `.md` (primary)
\- `.txt` (raw/normalized source text)
\- `.csv` (structured tabular exports)
\- `.json` (structured system outputs)

### Avoid as staging endpoints
\- `.rtf` (rich text formatting noise)
\- mixed binary docs without text extraction
\- giant unstructured dumps when split versions are possible

## Naming Convention (Required)
Use sortable, descriptive filenames.

### Standard
`YYYY-MM-DD_domain_topic_description_v#.<ext>`

Examples:
\- `2026-02-22_governance_ops-gaps_recovery_v1.md`
\- `2026-02-22_security_mattermost-access-policy_draft_v1.md`
\- `2026-02-22_meeting_exec-council_actions_v1.md`

### Avoid
\- `notes.md`
\- `final final.md`
\- `new text document.txt`

## Markdown Output Standard (Agent-Optimized)
Staged markdown should be easy for humans and local agents to parse.

Recommended top-of-file header:
\- Title
\- Status
\- Date
\- Source
\- Domain
\- Tags
\- Sensitivity (optional)
\- Processing Tier (optional)

Example:

```md
# Mattermost Access Policy Notes
Status: Draft
Date: 2026-02-22
Source: Meeting notes \+ recovery rebuild
Domain: security-access
Tags: mattermost, tailscale, executive-council
Sensitivity: Internal
AI Processing Tier: Local First, Escalate If Needed
