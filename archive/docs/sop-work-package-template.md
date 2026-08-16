---
title: SOP — Work Package Template Standard
status: Active
last-updated: 2026-07-19
op_task: https://ste-business-server.tailebe6d3.ts.net:8080/projects/ste-ai-buildout/work_packages/246
tier: On Premise + On Device
owner: Ed Hwang
---

# SOP: Work Package Template Standard

Every work package in OpenProjects must follow this structure.
Applies to: all projects, all assignees (human and agent).

---

## Title

Short, scannable, action-oriented. Max ~60 characters.

✅ `Write port map — all services and ports`
❌ `Write port-map.md — all services, ports, bind addresses, conflict risks`

Agent task titles start with a verb. Human task titles start with a verb.
Phase / Summary task titles start with `PHASE X.Y —`.

---

## Description

Required fields in every work package:

```
Assignee: [Name] or [Agent: Scout | Copilot]
Device: [Mac Mini | M4 Laptop | M1 MacBook | N/A]
Tier: [Network | On Premise | On Device]
Deadline: [YYYY-MM-DD | "next session" | TBD]

[Human tasks: what done looks like — one clear sentence]

[Agent tasks: step-by-step instructions the agent follows]
  1. ...
  2. ...

Output: [link to file, doc, or OP WP — required if task creates an artifact]
```

---

## People / Assignees

- All assignees must have a `@quorum.one` address
- Assign role when adding to a project (Project Manager, Member, Viewer)
- When adding a new member: draft a multi-channel invite (per their preference):
  - Channels: email · Discord · Mattermost · Slack · Telegram · WhatsApp
  - Message includes: project name, their role, what to do first, OP project link

---

## Agent Tasks — Additional Requirements

- The description **is the agent's instruction set** — not just context
- Be explicit: input → steps → output
- If the task creates a file: specify the exact output path in the description
- When complete: agent attaches the file or posts the link back to this WP
- Agent identity fields in description:
  ```
  Agent: Scout | Copilot
  Harness: OpenClaw | VS Code Copilot
  Model: qwen3.5-9b | claude-sonnet-4.6
  Device: Mac Mini | M4 Laptop
  ```

---

## Relations

Set in the **Relations** tab of the work package:

| Relation | When to use |
|---|---|
| **Blocks** | This WP must finish before another can start |
| **Blocked by** | This WP is waiting on another |
| **Parent** | This WP rolls up into a Summary task / Phase |
| **Child** | A sub-task under this WP |

Always set "Blocks" and "Blocked by" — do not leave the dependency implicit in the description text.

---

## Deadline

- Set a due date on every task
- If unknown: write `Deadline: next session` in the description, set the date field when confirmed
- Phases (Summary tasks) inherit deadline from their latest child task

---

## Estimates and Progress

- Set **Work** estimate (hours) when known
- Progress auto-updates from status:
  - New = 0% · In Progress = 50% · Closed = 100%
- Parent Summary tasks roll up from children automatically

---

## Attachments and File Links

- Attach output files directly to the WP (drag-drop in OP), **or**
- Add a link in the description to: Google Drive · GitHub file · Discovery docs path
- Agent output: always include the file link in the completion message posted to `#agent-logs`

---

## Meetings

- Link a meeting to a WP via the **Meetings** tab in OP
- Every real meeting that occurred gets a Milestone WP (type 2) in OP
- Transcripts attach to the Milestone WP as child Tasks
- Meeting WP naming: `MEETING: [Topic] — [YYYY-MM-DD]`

---

## Incremental / Long-Running Tasks

Some tasks (e.g., writing a manual, building a doc incrementally) are ongoing by nature. Rules:

- The **parent WP** tracks the overall objective (e.g., "Write TigerClaw Manual") — stays **In Progress** until the full artifact is complete
- Each **addition or section** gets its own child WP with:
  - A specific title (e.g., `TigerClaw Manual — Add: Mattermost pipeline section`)
  - A single defined endpoint (e.g., "Section written and pushed to GitHub")
  - Status set to **Closed** only when the output exists and is verifiable
- Do NOT mark the parent Done until the full output is created, reviewed, and committed
- Agent rule: attach the GitHub link or file path in the completion comment before closing
