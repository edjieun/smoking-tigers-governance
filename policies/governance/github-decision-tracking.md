# Policy — Using GitHub to Make and Track Decisions (OpenClaw-Facilitated)

Status: Draft v1.0
Owner: Ed (Steward)
Applies To: Executive Council, Governance Operators, OpenClaw agents
Last Updated: 2026-02-23

## Purpose

Use GitHub as a transparent, versioned system of record for governance and operational decisions without requiring executive council members to manually manage Git workflows.

OpenClaw should reduce operational burden while preserving:
- human approval
- traceability
- version history
- clear decision status

## Core Principle

**Executives should make decisions. Operators and systems should handle formatting and record-keeping.**

GitHub is the ledger of record for approved decisions, not the place where all discussion must happen.

## Policy Statement

Decision tracking in GitHub will be:
- **OpenClaw-assisted**
- **human-approved**
- **version-controlled**
- **linked to source evidence**

No decision is considered official solely because it appears in chat, a meeting summary, or an AI output.

## What Belongs in GitHub (Canonical)

GitHub should store:
- approved decision logs
- policies
- governance standards
- architecture standards
- operating procedures
- ratified role definitions
- changelogs to governance docs

GitHub should not be the primary home for:
- raw brainstorming
- stream-of-consciousness notes
- unreviewed transcripts
- temporary planning fragments

Those belong in Intake / working systems until promoted.

## Decision Lifecycle (Required)

### 1) Discussion / Discovery (Working Layer)

Sources may include:
- meetings
- chat threads
- Notion docs
- voice memos
- LM Studio / ChatGPT analysis

Output:
- draft summary
- decision candidate(s)

### 2) Drafting (Operator / OpenClaw-Assisted)

OpenClaw or an operator drafts a decision record with:
- decision title
- context
- decision statement
- rationale
- alternatives considered
- risks / tradeoffs
- owner
- date
- status
- references to source materials

### 3) Review (Human)

A designated approver (steward / exec owner) reviews:
- wording
- scope
- commitments
- owners
- implementation expectations

### 4) Approval

Decision is marked:
- Approved
- Rejected
- Deferred
- Superseded

Only **Approved** decisions become canonical in the decision log.

### 5) Publication to GitHub

OpenClaw may prepare and propose:
- file creation
- updates
- commit message draft
- PR summary draft

Human approval is required before final merge unless a narrow automation is explicitly authorized.

## Required Decision Record Format

Each decision record must include:
- **Decision ID** (unique)
- **Title**
- **Status**
- **Date**
- **Owner / Approver**
- **Context**
- **Decision**
- **Rationale**
- **Tradeoffs / Risks**
- **Impacts**
- **Dependencies**
- **References / Sources**
- **Change History** (if revised)

## Naming Convention

Decision files:
`/decisions/YYYY/DEC-YYYYMMDD-short-title.md`

Examples:
- `DEC-20260222-meeting-capture-policy.md`
- `DEC-20260222-calendar-system-standard.md`

Policy files:
`/policies/<domain>/<policy-name>.md`

## Status Definitions (Use Exactly)

- **Proposed** — drafted, not approved
- **Approved** — accepted and active
- **Deferred** — intentionally postponed
- **Rejected** — considered and not adopted
- **Superseded** — replaced by a newer decision

Do not use ambiguous labels like "done-ish," "final maybe," etc.

## Role Responsibilities

### Executive Council / Decision Owners

- decide
- approve/reject/defer
- clarify intent and scope

### Governance Operator

- prepare drafts
- ensure completeness
- maintain file structure and consistency
- link evidence and dependencies

### OpenClaw

Can:
- convert meeting outputs into decision candidates
- generate draft decision records
- check formatting consistency
- propose commits/PRs
- maintain indexes/changelogs if configured

Cannot:
- approve decisions
- assign authority not given by humans
- merge policy/decision changes without explicit authorization (unless tightly scoped automation exists)

## Human Approval Gate (Non-Negotiable)

The following require explicit human approval:
- any new policy
- any Approved decision status
- changes to governance roles or authority
- budget / legal / security commitments
- deletions of decision records
- superseding prior decisions

## GitHub Workflow Standard (Practical)

To avoid burdening execs, use this pattern:

1. Meeting / working discussion occurs in normal tools
2. OpenClaw drafts decision file(s)
3. Operator reviews and edits
4. OpenClaw prepares PR (or patch)
5. Decision owner approves content
6. Merge to governance repo
7. OpenClaw updates decision index / changelog

This keeps GitHub canonical while avoiding "everyone must learn git" friction.

## Linking to Source Evidence

Every decision record should link to one or more:
- meeting summary
- transcript
- issue / discussion thread
- Notion page
- source memo / proposal

If the underlying source is private, include an internal reference path or ID.

## Indexes and Discoverability

Maintain:
- `DECISIONS_INDEX.md` (all decisions + status)
- domain indexes (optional): ops, governance, tech, legal, calendar, security
- changelog for major policy revisions

OpenClaw may auto-maintain indexes, but changes should be reviewable.

## Handling Revisions

If a decision changes:
- do **not** silently rewrite history
- create a new decision or mark prior decision **Superseded**
- reference the replacing decision ID

Historical traceability is required.

## Security and Access

- Governance repo access should be limited by role
- Sensitive details may be split into private annex docs
- Public-facing summaries should omit private credentials / personal data / security specifics

## Failure Modes to Avoid

- Decisions buried in chat only
- AI summaries treated as approvals
- Missing owner/date/status
- One giant "notes.md" file for many decisions
- Silent edits to prior decisions without change history

## Review Cadence

Review this policy after:
- first 10 decision records
- any governance ambiguity caused by bad tracking
- tooling changes affecting GitHub/OpenClaw integration
