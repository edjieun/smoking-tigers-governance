# Policy — Linear Issue Tracking and Project Coordination

**Status:** Approved
**Owner:** Ed (Steward)
**Applies To:** All Smoking Tigers Media members and AI agents
**Last Updated:** 2026-04-17
**Governing Decision:** DEC-20260417-002

---

## Purpose

This policy defines how Linear is used as the canonical issue tracking and project coordination layer for Smoking Tigers Media. It covers human workflows, agent workflows, and the boundary between Linear and other systems (Notion, GitHub).

---

## Linear Workspace

- **Team:** Smoking Tigers (`STE`)
- **URL:** https://linear.app (team: Smoking Tigers)
- **API:** `https://api.linear.app/graphql` — authenticated via personal API key

---

## Issue Lifecycle

```
Backlog → Todo → In Progress → In Review → Done
                                          → Cancelled
                                          → Deferred
```

- **Backlog** — captured, not yet scheduled
- **Todo** — scheduled for current cycle
- **In Progress** — actively being worked
- **In Review** — awaiting review or approval
- **Done** — completed
- **Cancelled** — dropped; reason recorded in issue
- **Deferred** — paused; may return in future cycle

Issues are never deleted. Closed issues remain as historical record.

---

## Required Fields

All issues must have:
- **Title** — clear, action-oriented (verb + object)
- **Project** — must be assigned to a project
- **Priority** — must be set (no `No priority` issues)

Agent-created issues additionally require:
- **Label: `agent-task`**
- **Description** with source reference (where the task came from)

---

## Labels

| Label | Purpose | Who Uses It |
|---|---|---|
| `agent-task` | Created or managed by an AI agent | Agents only |
| `decision` | Tracks implementation of a governance decision | Agents + humans |
| `tln` | Trade Like Nick project items | All |
| `infrastructure` | Infrastructure and ops items | All |
| `blocked` | Blocked; needs human attention | All |

---

## Projects and Initiatives

**Projects** group related issues. Every issue belongs to a project.

**Initiatives** are the strategic layer above projects. They map to the STE Initiatives DB in Notion.

Project ↔ Initiative links are maintained in Linear. When a new project is added, it must be linked to its parent initiative if one exists.

---

## Agent Rules

**L-1: Label all agent issues**
All issues created by agents carry the `agent-task` label.

**L-2: Agents close what they open**
If an agent creates an issue, it is responsible for updating it when the task completes or becomes blocked.

**L-3: No duplicates**
Before creating an issue, check for an existing equivalent. Duplicate issues are cancelled, not deleted.

**L-4: Source traceability**
Issue descriptions must reference the source: Notion task ID, Discord message context, decision number, or meeting reference.

**L-5: Priority required**
Agents must set priority. Default: `Medium` if uncertain.

---

## Boundary with Notion

| Content | Goes In |
|---|---|
| Individual tasks and action items | Linear |
| Project coordination and milestones | Linear |
| Agent-generated tasks | Linear (label: `agent-task`) |
| Meeting records and agendas | Notion |
| Follow-up action items from meetings | Linear (created after meeting) |
| Contributor records, agreements | Notion |
| Financial records, RevPoints | Notion |
| Strategic initiative registry | Notion STE Initiatives DB (archive) + Linear (live) |

The Notion Exec Team Task Tracker is read-only legacy after 2026-04-17. New tasks go to Linear.

---

## Boundary with GitHub

GitHub issues (in `quorum1/q1-home` or other repos) track code-level work. Linear tracks operational and product coordination work. Do not create Linear issues for things that belong in a GitHub repo issue tracker, and vice versa.

Exception: if a code task has significant operational dependencies or stakeholder visibility, a Linear issue may be created that links to the GitHub issue.

---

## Morning Briefing

Linear is integrated into the daily morning briefing (7:00 AM Pacific). The briefing includes:
- Open and blocked issues by project
- Issues that moved to Done in the past 24 hours
- Agent-created issues requiring human review

Implementation: STE-16.

---

## Access

- **Ed (Steward)** — full access
- **All agents** — read/write via Linear GraphQL API (personal API key)
- **Other team members** — access granted by Ed as needed

---

## Review Cadence

Review this policy when:
- Linear workspace structure changes significantly
- New projects or initiatives are added
- Agent Linear workflow rules are updated

---

*Approved 2026-04-17 — Ed (Steward)*
