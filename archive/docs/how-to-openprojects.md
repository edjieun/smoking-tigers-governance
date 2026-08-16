---
title: How to Use OpenProjects — STE Work Surface Guide
status: Draft
last-updated: 2026-07-20
op_task: https://ste-business-server.tailebe6d3.ts.net:8080/work_packages/301
audience: Ed Hwang, Sage Harper, STE members, agents
skill-file: .github/skills/openprojects/SKILL.md
---

# How to Use OpenProjects — STE Work Surface

OpenProjects is where all STE work gets tracked. Every task, every decision that needs follow-through, gets a Work Package (WP) with an `OP#ID`. This guide covers the basics for humans and agents.

**URL:** https://ste-business-server.tailebe6d3.ts.net:8080
*(Accessible on Tailscale network only)*

---

## Projects

Every WP lives inside a project. Always know which project you're working in.

| ID | Project | What it's for |
|---|---|---|
| 3 | STE Operations | Catch-all for STE admin tasks |
| 6 | STE Website & Community | Website, member onboarding |
| 11 | Camp Audax / The Gathering | Event planning |
| 12 | Project TigerClaw | AI infrastructure (ste-ai-buildout) |
| 13 | RMA — New Meeting Flow | RMA weekly meeting structure |
| 14 | RMA Podcast | Podcast production |
| 15 | Miraval | Ed's personal projects |

---

## Work Package (WP) Basics

A **Work Package** is a task. Every action item should become a WP before the session ends.

| Field | What it means |
|---|---|
| **Subject** | Short title — what the task is |
| **Description** | Context: who, what device, what tier, deadline, output |
| **Status** | New → In progress → Closed |
| **OP#ID** | The unique ID returned when you create it (e.g. `OP#281`) |

### WP Description Template

Always fill this in when creating a WP:

```
Assignee: [Ed | Agent: Copilot | Agent: Scout]
Device:   [Mac Mini | M4 Laptop | M1 MacBook | N/A]
Tier:     [Network | On Premise | On Device]
Deadline: [YYYY-MM-DD | next session | TBD]

[One sentence: what "done" looks like]

Output: [file path or WP link]
```

### Status IDs (for API use)

| Status | ID |
|---|---|
| New | 1 |
| In progress | 7 |
| Closed | 12 |
| On hold | 13 |
| Rejected | 14 |

---

## Using OpenProjects as a Human

### Browse & view WPs
Open any project URL directly, e.g.:
- https://ste-business-server.tailebe6d3.ts.net:8080/projects/rma-podcast/work_packages
- https://ste-business-server.tailebe6d3.ts.net:8080/projects/ste-ai-buildout/work_packages

### Create a WP manually
1. Open the project
2. Click **+ Work package** (top right or sidebar)
3. Fill in Subject, Description, Type (Task), Status
4. Save — note the `OP#ID` in the URL

### Add a comment
Open any WP → scroll to the Activity section → type in the comment box → click **Save**.

---

## Using OpenProjects via Copilot (AI-assisted)

### How to invoke

Attach the skill file and give a natural language instruction:

```
#prompt:.github/skills/openprojects/SKILL.md

Create a WP in RMA Podcast for editing Episode 1 audio.
```

Or reference it in an agent session:
> "Follow the openprojects skill — create a WP in project 14 for X."

Copilot will draft the WP, confirm with you, then POST it and return the `OP#ID`.

### What Copilot can do

| Action | How to ask |
|---|---|
| Create a WP | "Create a WP for [task] in [project]" |
| List open WPs | "List open WPs in project [name or ID]" |
| Update status | "Close OP#123" / "Mark OP#123 in progress" |
| Post a comment | "Add a comment to OP#123: [text]" |
| Move work between WPs | "Move this work to OP#456" |

### Rules Copilot follows
- Always asks which project — no default
- Drafts and confirms before creating
- Uses `OPENPROJECTS_COPILOT_API_KEY` (Copilot's own key — never Ed's)
- Every session that produces action items ends with OP#IDs created
- Closes WPs when done — no stale "In progress"

---

## Using OpenProjects via API (advanced / agent use)

### Auth setup

```bash
source ~/.ste-secrets/.env
AUTH=$(echo -n "apikey:$OPENPROJECTS_COPILOT_API_KEY" | base64)
```

> ⚠️ Bearer token does NOT work. Always use Basic auth.

### Create a WP

```bash
curl -s -X POST \
  "https://ste-business-server.tailebe6d3.ts.net:8080/api/v3/projects/{PROJECT_ID}/work_packages" \
  -H "Authorization: Basic $AUTH" \
  -H "Content-Type: application/json" \
  -d '{
    "subject": "Your WP title",
    "description": {"raw": "Your description here"},
    "_links": {"type": {"href": "/api/v3/types/1"}}
  }' | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'OP#{d[\"id\"]} — {d[\"subject\"]}')"
```

### Post a comment

```bash
curl -s -X POST \
  "https://ste-business-server.tailebe6d3.ts.net:8080/api/v3/work_packages/{WP_ID}/activities" \
  -H "Authorization: Basic $AUTH" \
  -H "Content-Type: application/json" \
  -d '{"comment": {"raw": "Your comment here"}}'
```

### Close a WP

```bash
# Step 1: get the lockVersion
LV=$(curl -s "https://ste-business-server.tailebe6d3.ts.net:8080/api/v3/work_packages/{WP_ID}" \
  -H "Authorization: Basic $AUTH" | python3 -c "import sys,json; print(json.load(sys.stdin)['lockVersion'])")

# Step 2: patch the status
curl -s -X PATCH \
  "https://ste-business-server.tailebe6d3.ts.net:8080/api/v3/work_packages/{WP_ID}" \
  -H "Authorization: Basic $AUTH" \
  -H "Content-Type: application/json" \
  -d "{\"lockVersion\": $LV, \"_links\": {\"status\": {\"href\": \"/api/v3/statuses/12\"}}}"
```

### List open WPs in a project

```bash
curl -s \
  "https://ste-business-server.tailebe6d3.ts.net:8080/api/v3/projects/{PROJECT_ID}/work_packages?filters=%5B%7B%22status%22%3A%7B%22operator%22%3A%22o%22%2C%22values%22%3A%5B%5D%7D%7D%5D" \
  -H "Authorization: Basic $AUTH" | python3 -c "
import sys, json
for wp in json.load(sys.stdin).get('_embedded',{}).get('elements',[]):
    print(f'OP#{wp[\"id\"]}  {wp[\"subject\"]}')
"
```

---

## Onboarding a New Member (e.g. Sage)

To give Sage (or any STE member) access to OpenProjects:

1. **Create an OP account** for them at `https://ste-business-server.tailebe6d3.ts.net:8080/admin/users`
2. **Add them to the relevant project** (e.g. RMA Podcast #14) under Project → Members
3. **Share this guide** — `docs/how-to-openprojects.md`
4. **Share the skill file** — `.github/skills/openprojects/SKILL.md` — so their agent can use it

For their agent to create WPs autonomously, they'll need their own API key stored in their secrets file, and a modified version of the skill with their key variable.

---

## Key Files

| File | Purpose |
|---|---|
| `.github/skills/openprojects/SKILL.md` | Copilot skill — invoke via `#prompt:` |
| `docs/how-to-openprojects.md` | This guide |
| `docs/sop-openprojects-work-surface.md` | Full SOP (Ed's working process) |
