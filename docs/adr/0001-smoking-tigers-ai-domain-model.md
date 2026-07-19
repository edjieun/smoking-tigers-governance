---
status: Accepted
date: 2026-07-16
participants: [Ed Hwang]
tags: [domain-model, architecture, governance, agents, pipeline]
---

# ADR-0001: Smoking Tigers AI — Domain Model and System Architecture

## Status
Accepted

## Context

Smoking Tigers AI is a decentralized AI operations network spanning multiple workspaces, devices, and data sources. The core problem identified in a domain modeling session on 2026-07-16:

> Decision-making clarity — knowing what was decided, and who needs to do what — is lost after meetings. Memory/ files exist but lead nowhere actionable.

The system requires a canonical domain model to guide all future agent design, workspace structure, and governance tooling.

## Decision

We adopt the following domain model for Smoking Tigers AI:

### Core Entities

| Entity | Definition |
|---|---|
| **Organization** | Root entity. Smoking Tigers AI is both the umbrella org AND a tracked buildout project. Peer orgs (STE, Quorum1, RMA-context) relate to it but are not sub-orgs. |
| **Member** | A human participant in one or more Organizations or Projects. Same person can operate in multiple project contexts simultaneously. Members are accountable for all Agent actions they configure. |
| **Project** | Requires: a GitHub repo OR workspace folder + at least one meeting discussion + a defined outcome/deliverable + member agreement. Projects are NOT declared unilaterally — they require at least one member who has agreed to participate. RMA-type = multi-party operating agreements, more complex governance. |
| **Decision** | A recorded agreement between members. Separate from tasks. Extracted from meeting transcripts by an agent. Stored as a Governance Record in GitHub. |
| **Task** | An action assigned to a specific Member, linked to a Project. Status lifecycle: open → assigned → done. Extracted from meeting transcripts by an agent. |
| **Meeting** | An event that produces a Transcript. Linked to one or more Projects. Sources: Fathom, Google Meet, Zoom. |
| **Transcript** | Raw artifact from a Meeting. Processed into Chunks → Memory files → (target) Decisions + Tasks + Open Questions. |
| **Open Question** | A question raised in a meeting that was never resolved. Becomes a Decision once resolved, or a Task if action is needed to answer it. |
| **Agent** | A tool, not a member. Accountable to the Member who configured it. Operates as a named Role (e.g., "Meeting Processor", "Task Tracker"), not a person. |
| **Workspace** | A VS Code workspace folder scoped to a project or context. Each workspace is a node in the network. Must follow consistent structure to be agent-usable. |
| **Infrastructure Node** | A physical or virtual compute resource (Mac Mini, M4 Laptop, M1). Connected via Tailscale. Mac Mini = primary autonomous scheduled agent target. |
| **Governance Record** | A formalized artifact in the GitHub governance repo recording a Decision. Types: ADR (append-only), Issue (closed = decided), Living Doc (mutable per context). |

### Key Relationships

- Organization → has many Members, Projects, Agents
- Member → belongs to many Organizations, owns Tasks, configures Agents
- Project → has many Meetings, Decisions, Tasks, Members (via agreement)
- Meeting → has one Transcript, many Members (participants)
- Transcript → produces Chunks → produces Memory Files → (target) Decisions + Tasks + Open Questions
- Decision → stored as Governance Record in GitHub (requires human approval for commit)
- Task → assigned to Member, linked to Project
- Agent → runs on Infrastructure Node, accountable to Member, operates on Workspaces

### Target Pipeline

```
Meeting (Fathom / Google Meet / Zoom)
  → Transcript (raw)
    → Chunks (chunk-transcript.sh)
      → Memory/ files (atomic summary cards)
        → Agent: extract Decisions → Governance Record (GitHub, pending human approval)
        → Agent: extract Tasks → assign to Members (Mattermost notification)
        → Agent: update Project status/summary doc
        → Agent: draft follow-up comms (Mattermost)
        → Agent: flag Open Questions → surfaced for next meeting agenda
```

### Governance Boundaries (Human Approval Required)
- GitHub commits and merges
- LedgerSMB financial record creation or modification

## Definition of Done

> A meeting happens → transcript goes in → tasks show up in the right people's inboxes automatically.

## Consequences

- All new workspaces must follow the Discovery workspace structure (Memory/, Transcripts/, chunks/, docs/) to be agent-usable.
- Agents must never be granted autonomous GitHub write access or LedgerSMB write access without explicit human approval per action.
- The Mac Mini must eventually run a scheduled agent harness (not just inference) to process transcripts without the laptop being on.
- Projects that lack member agreement or a defined outcome are classified as **topics**, not projects, and are not tracked in the project registry.

## Out of Scope (Explicitly Deferred)
- Token cost monetization model for AI infrastructure
- LedgerSMB integration implementation details
- Obsidian / Notion / Google sync specifics
