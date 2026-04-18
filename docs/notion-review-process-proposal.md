# Notion Review & Operations Process — Proposal
**Status:** DRAFT — Pending governance review  
**Author:** Scout (main)  
**Date:** 2026-03-18  
**Reviewers Required:** Governance Ops (⚖️), Sergeant At Arms (🔒), Ed (final authority)

---

## Problem Statement

Eva (EA) and future EA-role agents (e.g., Rosie) are doing ad hoc Notion work — no consistent schedule, no defined scope, no structured output format. Scout has been carrying coordination weight that should be distributed. Governance Ops and Sergeant At Arms have empty HEARTBEATs and underused skills. This proposal defines the process to fix all three.

---

## Goals

1. **Reliable Notion review cycle** — EA agents review and update Notion on a defined schedule
2. **Structured, local-first agent pipeline** — specialized sub-agents running on Ollama small models do the mechanical work; EA orchestrates
3. **Distributed load** — Governance Ops and SAA own their domains; Scout coordinates, not executes
4. **Defined outputs** — Tasks, meetings, and decisions recorded in STM Operations Notion with consistency
5. **Governance alignment** — SOPs, bylaws, and agent rules updated to reflect the new structure

---

## Architecture

### Agent Roles (Post-Implementation)

| Agent | Primary Role | Notion Scope | Default Model |
|---|---|---|---|
| **Eva (EA)** | EA orchestrator | Meetings, Tasks, Contacts | `qwen2.5:7b-instruct` |
| **Rosie (Christine-EA)** | EA for Christine | Meetings, Tasks (Christine-related) | `qwen2.5:7b-instruct` |
| **Governance Ops** | Decision/policy tracking | Decisions, Bylaws, Policy pages | `qwen2.5:7b-instruct` |
| **Sergeant At Arms** | Compliance/cultural integrity | Compliance log, Violations, Bylaws | `qwen2.5:7b-instruct` |
| **Scout (main)** | Coordination, triage, escalation | Cross-agent sync, MEMORY.md | `claude-sonnet-4.6` |
| **Knowledge Ops** | Nightly digest, knowledge synthesis | N/A (file-based output) | `gemini-2.5-pro` |

### New Specialized Sub-Agents (Local-Only, Ollama)

These are **spawned by EA agents** on-demand, not persistent. They run `qwen2.5:3b-instruct` for mechanical tasks.

| Sub-Agent Role | Task | Model |
|---|---|---|
| `notion-reader` | Pull Notion DB pages, extract structured data | `qwen2.5:3b-instruct` |
| `notion-writer` | Format and push updates to Notion pages | `qwen2.5:3b-instruct` |
| `task-extractor` | Parse meeting notes → structured task list | `qwen2.5:3b-instruct` |
| `meeting-formatter` | Format meeting summaries to STM standard | `qwen2.5:3b-instruct` |

> These do not need persistent sessions. EA spawns them, gets output, closes them.

---

## Notion Review Cycle (Eva's HEARTBEAT)

### Frequency: Daily (runs at EA heartbeat)

### Scope: STM Operations Notion

**Databases reviewed:**
- Meetings
- Tasks
- Projects
- People / Contacts

### Review Workflow

```
1. Pull all Notion DB entries modified in last 24h
2. For each modified entry:
   a. Classify: Meeting / Task / Project / Contact
   b. Spawn task-extractor or meeting-formatter sub-agent as needed
   c. Validate output against STM format standards (see §Output Standards)
   d. Push any corrections or enrichments back to Notion
3. Identify entries missing required fields → flag as incomplete
4. Generate daily sync report → write to workspace/agents/ea/notion-sync-YYYY-MM-DD.md
5. Post summary to #executive Mattermost channel
```

### Output Standards (Meetings)

Every Notion Meeting entry must have:
- Title (format: `[YYYY-MM-DD] Topic — Attendees`)
- Date + Time
- Attendees (linked Person records)
- Status: Scheduled / In Progress / Complete
- Summary (2–3 sentences)
- Action Items (Owner · Task · Due Date)
- Related Project (linked)

### Output Standards (Tasks)

Every Notion Task entry must have:
- Title
- Owner (linked Person)
- Status: Open / In Progress / Blocked / Done
- Due Date (if known)
- Related Project or Meeting (linked)

---

## Governance Ops HEARTBEAT (New)

### Frequency: Weekly (Mondays)

```
1. Review DECISIONS_INDEX.md in governance repo
2. Check for draft decisions older than 7 days → flag to Scout
3. Verify any new decisions have corresponding Notion entries
4. Check bylaws + SOP files for pending updates flagged by Scout or SAA
5. Post governance status report to #governance Mattermost channel
```

---

## Sergeant At Arms HEARTBEAT (New)

### Frequency: Weekly (Thursdays)

```
1. Review last week's Notion Tasks — verify all "Done" tasks have documented completion
2. Check RevPoints recommendations against IP registration status
3. Verify contributor onboarding status before job access is granted
4. Review open compliance flags from prior week
5. Post compliance report to #governance Mattermost channel
```

---

## Structural Changes Required

### Files to Create/Update

| File | Change | Owner |
|---|---|---|
| `agents/ea/HEARTBEAT.md` | Add Notion review cycle task | Scout (with Ed approval) |
| `agents/ea/SOP.md` | Add §9: Notion Review Process | Scout (with Ed approval) |
| `agents/governance-ops/HEARTBEAT.md` | Add weekly governance check | Governance Ops review → Scout writes |
| `agents/sergeant-at-arms/HEARTBEAT.md` | Add weekly compliance check | SAA review → Scout writes |
| `agents/christine-ea/HEARTBEAT.md` | Mirror Eva's Notion cycle for Christine-scope items | Scout (with Ed approval) |
| `docs/agent-model-assignments.md` | Canonical model assignment per agent + sub-agent | Scout writes |
| `docs/notion-sop.md` | STM Notion structure, field standards, update rules | EA drafts, Governance reviews |
| Governance repo `docs/sop/notion-operations.md` | Official SOP in governance | Governance Ops submits |
| Governance repo `docs/bylaws/` | Update agent authority + roles section | Governance Ops drafts, Ed approves |

### Mattermost Channels (Confirm or Create)

| Channel | Purpose |
|---|---|
| `#executive` | EA daily sync posts |
| `#governance` | Gov Ops + SAA weekly reports |
| `#ops-log` | Cross-agent operation log (automated) |

---

## Review Required Before Implementation

### Governance Ops Must:
- [ ] Review this proposal for governance alignment
- [ ] Identify any bylaw or decision conflicts
- [ ] Draft updated agent authority section for bylaws
- [ ] Propose decision record for this process change (DEC format)

### Sergeant At Arms Must:
- [ ] Confirm compliance scope is correctly represented
- [ ] Verify RevPoints / IP / onboarding checks are in correct scope
- [ ] Flag any cultural integrity concerns

### Ed Must:
- [ ] Approve model assignments (local-first for sub-agents)
- [ ] Approve HEARTBEAT schedules
- [ ] Approve bylaw updates (final authority)
- [ ] Confirm Notion database scope

---

## Open Questions (for Ed)

1. **Rosie's Notion scope** — should Rosie mirror Eva's full workflow or only Christine-related items?
2. **Sub-agent spawn method** — should EA heartbeat spawn via `sessions_spawn` (subagent mode) or should these be CLI tools Eva calls directly?
3. **Mattermost channel for SAA/GovOps reports** — use `#governance` or separate `#compliance` channel?
4. **Notion credentials** — does Rosie (christine-ea) have her own token or share Eva's?

---

## What This Does NOT Change

- Scout remains coordinator, not executor, for EA-domain work
- Knowledge Ops remains nightly digest only — no Notion writes
- Ed retains final authority on all governance decisions
- No agent sends external comms without explicit instruction

---

*This document requires review by Governance Ops and Sergeant At Arms before implementation.*
