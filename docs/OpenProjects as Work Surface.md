---
title: SOP — OpenProjects as Work Surface (Project TigerClaw)
status: Active
last-updated: 2026-07-19
owner: Ed Hwang
---

# SOP: OpenProjects as Work Surface

## Who this is for
Ed Hwang and any agent (Scout) creating or updating work on Project TigerClaw.

## What this is
OpenProjects at `https://ste-business-server.tailebe6d3.ts.net:8080` is the 
**single source of truth** for all active work. Every task, decision, meeting,
and intake item gets an OP work package ID. Nothing is "in progress" unless
it has an OP#ID.

## Where things live
| Input | OP Type | How it gets there |
|---|---|---|
| New phase of work | Epic (type 5) | Copilot or Ed creates via API/browser |
| Meeting | Milestone (type 2) | Scout creates when transcript is received |
| Transcript | Task (type 1) | Scout creates, links to Milestone |
| Task from transcript | Task (type 1) | Scout creates, child of Transcript WP |
| Decision from transcript | Task (type 1), tagged "Decision" | Scout creates |
| Open Question | Task (type 1), tagged "Open Question" | Scout creates |
| URL / web intake | Task (type 1), tagged "Intake: URL" | Scout creates |
| Email intake | Task (type 1), tagged "Intake: Email" | Scout creates |
| ADR / SOP doc | Task (type 1), tagged "Doc" | Copilot or Ed creates, links to file |
| Planning session output | Task (type 1) | Copilot creates at end of plan session |

## Why OpenProjects (not Notion, not Mattermost)
- Notion = private project context, shared with collaborators
- Mattermost = notifications and human conversation
- GitHub = governance records (ADRs, policy)
- **OpenProjects = live work state, task ownership, phase tracking**

## How agents reference OP
Every agent output that creates or updates a work item includes:
- The OP work package ID: `OP#123`
- A direct link: `https://ste-business-server.tailebe6d3.ts.net:8080/work_packages/123`

## TigerClaw tier tags
Every work package is tagged with the tier it belongs to:
- `tier:network` — cloud, OpenRouter, external APIs, Tailscale
- `tier:on-premise` — Mac Mini services, M1 services, local inference
- `tier:on-device` — M4 Laptop, Copilot, OpenCode sessions

## Opening OP daily
1. Navigate to `https://ste-business-server.tailebe6d3.ts.net:8080/projects/ste-ai-buildout`
2. Use the **Board** view to see tasks by status (New / In Progress / Done)
3. Use the **Gantt / phases** view to see Epics and their Tasks
4. Any task without an assignee needs one before work starts

## API quick reference
- Base: `https://ste-business-server.tailebe6d3.ts.net:8080`  
- Auth: `Authorization: Basic base64(apikey:$OPENPROJECTS_API_KEY)`  
- Create WP: `POST /api/v3/projects/12/work_packages`  
- List WPs: `GET /api/v3/projects/12/work_packages`  
- Full spec: `docs/openprojects-spec-template.md`

---
Reference

https://ste-business-server.tailebe6d3.ts.net:8080/projects/ste-ai-buildout/work_packages/246/activity

