---
title: SOP — OpenProjects as Work Surface
status: Active
last-updated: 2026-07-19
owner: Ed Hwang
applies-to: All Discovery projects, all agents
---

# SOP: OpenProjects as Work Surface

## Purpose
OpenProjects at `https://ste-business-server.tailebe6d3.ts.net:8080` is the
**single source of truth for all active work** across Smoking Tigers Enterprises.
Every task, decision, meeting, intake item, and phase gets a work package ID.
Nothing is "in progress" without an OP#ID.

---

## Who / What / Where / Why / How

**Who:** Ed Hwang (human), Scout agent (Mac Mini), Copilot agent (M4 Laptop)
**What:** Work package tracking for all STE projects
**Where:** `https://ste-business-server.tailebe6d3.ts.net:8080` (M1 MacBook, On Premise tier)
**Why:** Replaces scattered task logs, chat notes, and daily note TODOs with one queryable surface
**How:** See API reference below; agents POST work packages, humans review in browser

---

## Discovery Workspace → OpenProjects Mapping

| Discovery artifact | OP type | Notes |
|---|---|---|
| Project (`docs/projects/*.md`) | OP Project | One OP project per Discovery project |
| Phase | Summary task (type 3) | Groups related tasks — named "PHASE X.Y — ..." |
| Task | Task (type 1) | Assigned to Ed or agent; includes device + deadline |
| Meeting | Milestone (type 2) | Marks when meeting occurred; links to Transcript |
| Daily note (YYYY-MM-DD.md) | Journal entry | Processed by Scout intake job → ZeroClaw |
| ADR | Task (type 1), tagged `doc:adr` | Links to file in `docs/adr/` |
| SOP | Task (type 1), tagged `doc:sop` | Links to file in `docs/` or gov repo |
| Open Question | Task (type 1), tagged `open-question` | Extracted from transcripts |
| Decision | Task (type 1), tagged `decision` | Extracted from transcripts |

---

## TigerClaw Tier Tags

Every work package is tagged in its description with its tier:

| Tag | Scope |
|---|---|
| `Tier: Network` | OpenRouter, Tailscale, external APIs, cloud services |
| `Tier: On Premise` | Mac Mini (inference + agents), M1 (OP + LedgerSMB), Mattermost |
| `Tier: On Device` | M4 Laptop — Obsidian, Copilot, OpenCode, interactive sessions |

---

## Project Directory

| Project | OP ID | URL | Status |
|---|---|---|---|
| **Project TigerClaw** (STE AI) | #12 | [ste-ai-buildout](https://ste-business-server.tailebe6d3.ts.net:8080/projects/ste-ai-buildout) | Active |
| STE Website & Community | #6 | [ste-website](https://ste-business-server.tailebe6d3.ts.net:8080/projects/ste-website) | Active — blocked |
| Camp Audax / The Gathering | #11 | [camp-audax-working-title](https://ste-business-server.tailebe6d3.ts.net:8080/projects/camp-audax-working-title) | Active — blocked |
| RMA — New Meeting Flow | #13 | [rma-meeting-flow](https://ste-business-server.tailebe6d3.ts.net:8080/projects/rma-meeting-flow) | Active |
| STE Operations (catch-all) | #3 | [ste-ops](https://ste-business-server.tailebe6d3.ts.net:8080/projects/ste-ops) | Active |

**Topics (no OP project):** Solarpunk, RMA Podcast (on hold — objective TBD)

---

## How Agents Reference OP

Every agent output that creates or updates a work item includes:
- Work package ID: `OP#123`
- Direct link: `https://ste-business-server.tailebe6d3.ts.net:8080/work_packages/123`

Scout (Mac Mini) creates work packages automatically from transcript processing.
Copilot (M4 Laptop) creates work packages during planning sessions.

---

## API Quick Reference

```
Base URL: https://ste-business-server.tailebe6d3.ts.net:8080
Auth: Authorization: Basic base64("apikey:{OPENPROJECTS_API_KEY}")
Note: Bearer token auth does NOT work. Always use Basic auth.

Create WP:
  POST /api/v3/projects/{project_id}/work_packages
  Body: {"subject":"...","description":{"raw":"..."},"_links":{"type":{"href":"/api/v3/types/1"}}}

Update WP status:
  PATCH /api/v3/work_packages/{id}
  Body: {"lockVersion":{n},"_links":{"status":{"href":"/api/v3/statuses/12"}}}

Work package types available:
  1 = Task
  2 = Milestone
  3 = Summary task (use for Phase groupings)

Status IDs:
  1=New  7=In progress  12=Closed  13=On hold  14=Rejected
```

Full spec: `docs/openprojects-spec-template.md`

---

## Daily Workflow

1. Open [Project TigerClaw](https://ste-business-server.tailebe6d3.ts.net:8080/projects/ste-ai-buildout) in browser
2. Use **Board** view to see tasks by status
3. Any task without an assignee → assign before starting work
4. When a planning session produces action items → they go to OP immediately
5. When a transcript is processed → Scout posts OP#IDs to `#tasks` + `#decisions`

---

## Rules

1. **No task lives only in chat.** All action items get an OP#ID before the session ends.
2. **No execution without documentation.** Every component answers: Who / What / Where / Why / How.
3. **task-log.md is a read cache only.** The live source of truth is OP.
4. **Daily notes are intake, not tasks.** Scout processes them into journal entries — not into OP tasks directly.
