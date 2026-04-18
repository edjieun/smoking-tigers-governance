# Tool Schema: Notion
**Type:** Schema Document — Descriptive Only
**Created:** 2026-03-25
**Owner:** Ed (Steward)
**Status:** Draft

---

## Overview

Notion is the structured records layer for Smoking Tigers. It holds projects, tasks, meetings, team members, documents index, and AI operations registry. It is the primary operational workspace visible to human team members.

---

## Workspace

- **Name:** Smoking Tigers (STM teamspace)
- **Access:** Shared workspace — Ed + exec team
- **Integration token:** Active (EA agent, christine-ea agent)
- **API version:** 2022-06-28

---

## Active Databases

### STM Scope

| Database | Notion ID (short) | Purpose | Key Relations |
|----------|------------------|---------|---------------|
| Smoking Tigers Strategy DB | `2c56f6ac` | Projects and initiatives | → Meetings, → Documents |
| Smoking Tigers Documents | `2fc6f6ac` | Document registry (Google Doc links) | → Strategy DB |
| Meetings | `2af6f6ac` | Meeting records | → Strategy DB, → Exec Task Tracker |
| Smoking Tigers Team | `2ef6f6ac` | People / contributors | ← Exec Task Tracker |
| Exec Team Task Tracker | `3186f6ac` | Task tracking across exec team | → Strategy DB, → Team |
| Decisions | `3286f6ac` | Formal decision log | — |
| ST:AI Ops | `30e6f6ac` | AI agent registry | — |
| ST:AI Request Queue | `3266f6ac` | Agent task request intake | — |
| TLN Tasks | `31f6f6ac` | Trade Like Nick project tasks | — |
| LLM Models | `30e6f6ac` | AI model catalog | — |
| 📹 Content Kanban | `32d6f6ac` | Content production board | — |
| Content Planning Kanban | `cac6f6ac` | Content scheduling/planning | — |
| (Legacy) Tracking Process - FOW | `40184444` | YouTube/podcast workflow tracker | — |

### Q1 Scope (hosted in same workspace)

| Database | Notion ID (short) | Purpose |
|----------|------------------|---------|
| Q1 Service Stack DB | `3286f6ac` | Q1 services catalog |
| q1.is Feature Stack DB | `3286f6ac` | q1.is platform features |
| Client Help Desk | `3286f6ac` | Client support records |
| Milestone Progress Tracker | `9356f6ac` | Cross-project milestone tracking |

### Not Classified / Likely Legacy

| Database | Notion ID (short) | Notes |
|----------|------------------|-------|
| [archive] Directory | `2af6f6ac` | Superseded by Team DB |
| Tasks (Legacy Board) | `2e26f6ac` | Superseded by Exec Task Tracker |
| Video Process | `7656f6ac` | Possibly FOW production |
| 8 unnamed databases | Various | Status unknown — need review |

---

## Database Schema Detail (Key DBs)

### Smoking Tigers Strategy DB (Projects)
| Field | Type | Notes |
|-------|------|-------|
| Name | title | Project name |
| Owner | people | ⚠️ People picker, not Team DB relation |
| Priority | select | — |
| Lifecycle | select | — |
| Project Type | multi_select | — |
| Project Origin | select | — |
| Campaign | date | — |
| Meetings | relation → Meetings | ✅ Bidirectional |
| Project Docs | relation → Documents | ✅ |
| Forms | rich_text | — |
| Website | url | — |
| Knowledge Doc | url | — |
| Last Interaction | rollup | — |

### Smoking Tigers Documents
| Field | Type | Notes |
|-------|------|-------|
| Name | title | Document name |
| Document Type | select | — |
| Google Doc | url | Link to Google Doc artifact |
| Project | relation → Strategy DB | ✅ |
| Date | date | — |

### Meetings
| Field | Type | Notes |
|-------|------|-------|
| Meeting Title | title | — |
| Date | date | — |
| Status | status | — |
| Meeting Type | select | — |
| Platform | select | — |
| Attendees | people | ⚠️ People picker, not Team DB relation |
| Smoking Tigers Strategy DB | relation → Projects | ✅ |
| Tasks | relation → Exec Task Tracker | ✅ |
| Minutes | url | External link |
| Recording Link | url | — |
| Meeting Link | url | — |
| Cal.com Event ID | rich_text | — |
| Agenda | rich_text | — |

### Exec Team Task Tracker
| Field | Type | Notes |
|-------|------|-------|
| Name | title | — |
| Status | select | — |
| Priority | select | — |
| Due Date | date | — |
| Person | people | ⚠️ People picker |
| Assignee | relation → Team | ✅ |
| Project | relation → Strategy DB | ✅ |
| Team | select | — |
| Project / Initiative | rich_text | ⚠️ Duplicates Project relation |
| Notes | rich_text | — |
| URL | url | — |
| Last Updated | last_edited_time | — |

### Smoking Tigers Team
| Field | Type | Notes |
|-------|------|-------|
| (Not enumerated) | | Confirmed to exist; relations to other DBs incomplete |

### ST:AI Ops
| Field | Type | Notes |
|-------|------|-------|
| Function | title | — |
| agent type | rich_text | — |
| Role Description | rich_text | — |

---

## Relational Map

```
Smoking Tigers Strategy DB (Projects)
    ↔ Meetings (bidirectional)
    → Smoking Tigers Documents
    ← Exec Team Task Tracker
    
Meetings
    ↔ Smoking Tigers Strategy DB (bidirectional)
    → Exec Team Task Tracker

Exec Team Task Tracker
    → Smoking Tigers Strategy DB
    → Smoking Tigers Team

Smoking Tigers Documents
    → Smoking Tigers Strategy DB
```

---

## Access & Authentication

| Actor | Access Level | Method |
|-------|-------------|--------|
| Ed | Workspace admin | Browser / Notion app |
| EA agent (`ea`) | Read + write | API token `ntn_299082...` |
| christine-ea | Read + write | Same token (shared) |
| Other agents | None | No token |
| Q1 members | Varies by page | Direct workspace access |

---

## How It Connects to Other Tools

| Tool | Connection | Direction |
|------|-----------|-----------|
| Google Drive | Documents DB contains Google Doc URLs | Reference (URL link) |
| GitHub | Governance decisions referenced by URL | Reference only |
| Mattermost | Notion Intake Bot (`@st-notion-intake`) reads #knowledge channel | Inbound |
| OpenClaw | EA agent reads/writes via API | Bidirectional |
| Discord | No direct connection | — |

---

## STM vs. Q1 Distinction

| Dimension | STM Databases | Q1 Databases |
|-----------|--------------|--------------|
| Scope | Projects, ops, team, content, AI | Services, features, milestones, help desk |
| In same workspace | Yes | Yes |
| Agent access | EA, christine-ea (shared token) | Same token — no boundary enforcement |
| Governance | STM Steward | Q1 process |

⚠️ **Note:** STM and Q1 databases share the same Notion workspace and the same integration token. There is no access boundary between them at the API level.

---

## Known Gaps / Open Items

- 8 unnamed databases — purpose unknown, need audit
- `Owner` and `Attendees` fields are people pickers (not relations to Team DB) — reduces cross-DB query capability
- Smoking Tigers Team DB relations incomplete — not fully wired to Documents, Meetings
- No RevPoints database
- No IP Registry database
- No Revenue database
- Q1 and STM databases co-exist in one workspace with no access isolation
- Notion Intake Bot wired to Mattermost but intake workflow not fully automated
- Legacy databases (`[archive] Directory`, `Tasks (Legacy Board)`) not formally archived

---

## Canonical Role

> Notion is the **structured records and operational state layer**. Projects, tasks, meetings, and team activity live here. It is not the canonical source for governance policy (that's GitHub) or document artifacts (that's Google Drive).
