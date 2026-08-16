# Smoking Tigers — Google Drive System Design
**Status:** Draft — 2026-03-17
**Owner:** Scout (Chief of Staff)
**Relates to:** Google Drive, Notion, Agent Automation

---

## Overview

The "Smoking Tigers" Google Drive (formerly "Smoking Tigers Media Group") is the shared file hub for the team. This document defines the folder architecture, naming conventions, tagging strategy, Notion integration, and the agent-based intake/organization pipeline.

---

## 1. Folder Structure

```
📁 Smoking Tigers/                        ← Root (shared drive, Q1 Creative)
  📁 _INTAKE/                             ← Drop zone: auto-organized by agents
  📁 Operations/
    📁 SOPs/
    📁 Contracts/
    📁 Finance/
    📁 Legal/
  📁 Projects/
    📁 [Project Name]/                    ← One folder per active project
      📁 Assets/
      📁 Deliverables/
      📁 Meetings/
  📁 People/
    📁 Team/
    📁 Partners/
    📁 Clients/
  📁 Marketing/
    📁 Brand/
    📁 Content/
    📁 Social/
  📁 Technology/
    📁 Infrastructure/
    📁 AI Systems/
    📁 Documentation/
  📁 Archive/                             ← Completed/inactive work
```

### Design Principles
- `_INTAKE/` sorts first alphabetically — it's the landing zone, not storage
- Depth max: 3 levels under root (agents navigate; humans don't get lost)
- No personal folders in the shared drive — use `People/` for org-relevant docs only
- Archive gets a copy; originals stay in place until explicitly moved

---

## 2. Naming Convention

### Files
```
YYYY-MM-DD_[Category]_[Subject]_[Version].[ext]
```
Examples:
- `2026-03-17_SOP_GoogleDrive-Onboarding_v1.pdf`
- `2026-03-17_Meeting_DavidHodgson-ProjectReview_Notes.md`
- `2026-03-17_Contract_TLN-ServiceAgreement_v2.docx`

### Folders (Projects)
```
[YYYY-MM]_[ProjectName]
```
Example: `2026-03_SXMCampaign`

### Tags (applied in Notion — see Section 4)
- Category: `ops`, `project`, `marketing`, `tech`, `finance`, `legal`, `people`
- Status: `draft`, `review`, `final`, `archived`
- Access: `internal`, `partner`, `client`, `public`
- Team: `stm`, `q1`, `tln`, `external`

---

## 3. Intake Pipeline (Agent-Automated)

### How it works
1. Team member drops file into `_INTAKE/` (or Google auto-saves there)
2. A **Drive Intake Agent** (runs on schedule or trigger) scans `_INTAKE/`
3. Agent:
   - Reads file name, type, contents (if text/doc)
   - Infers: category, project association, date, version
   - Renames to naming convention
   - Moves to correct folder
   - Creates or updates Notion record with tags + Drive link
4. Original `_INTAKE/` entry is cleared

### Intake Agent Trigger Options (to be decided)
- [ ] Scheduled (e.g., every 30 min via cron)
- [ ] On-demand (slash command or Mattermost trigger)
- [ ] Webhook (Google Drive push notification — preferred long-term)

### Fallback
If agent cannot confidently categorize a file → moves to `_INTAKE/_REVIEW/` and posts in #operations for human triage.

---

## 4. Notion Integration

Each file processed by the intake agent gets a record in a **Smoking Tigers Files** Notion database:

| Field | Type | Notes |
|---|---|---|
| Name | Title | Formatted name (convention-compliant) |
| Drive Link | URL | Direct Google Drive link |
| Category | Select | ops, project, marketing, tech, etc. |
| Status | Select | draft, review, final, archived |
| Access Level | Select | internal, partner, client, public |
| Team | Multi-select | stm, q1, tln, external |
| Project | Relation | Links to Projects DB |
| People | Relation | Links to People/Directory DB |
| Date | Date | File date (from name or metadata) |
| Added By | Text | Auto-detected from Drive metadata if possible |
| Tags | Multi-select | Freeform for search |
| Agent Processed | Checkbox | True if auto-filed by agent |

This makes everything findable via Notion search and filterable by project, person, status, or access level — no digging in Drive folders needed.

---

## 5. SOPs

### SOP A: Users WITH quorum.one accounts
1. **Never save directly to personal My Drive for shared work** — always use the shared "Smoking Tigers" drive
2. Default save location for new Docs/Sheets/Slides: `Smoking Tigers/_INTAKE/`
3. Name files with your best guess at convention — agent will clean up
4. If unsure where something belongs, drop in `_INTAKE/` and tag it in Mattermost `#operations`
5. All meeting notes go to `_INTAKE/` immediately after the meeting
6. Contracts and legal docs: drop in `_INTAKE/`, ping Scout in #operations

### SOP B: Users WITHOUT quorum.one accounts (external collaborators)
1. You will be invited to specific shared folders only — not root access
2. Drop shared files into the folder you were invited to
3. Do not create new top-level folders
4. Request Scout or Ed to move files if you're unsure
5. For sensitive docs: use the secure upload link (to be set up — see open items)

### SOP C: Agents (automated)
1. Agents read from `_INTAKE/` and write to structured folders only
2. Agents do not delete files — only move
3. Agents log all actions to `Technology/AI Systems/agent-activity-log.md`
4. Failed categorizations land in `_INTAKE/_REVIEW/`

---

## 6. Calendar SOP (Cross-Reference)

**Pending separate doc: `smoking-tigers-calendar-sop.md`**

Covers:
- quorum.one calendar setup
- "Smoking Tigers" shared calendar subscription
- "The Big Picture" view configuration
- Platform-by-meeting-type rules (Meet / Zoom / Riverside / Discord)
- Cal.com onboarding per user type

---

## 7. Open Items / Prerequisites

| Item | Owner | Status |
|---|---|---|
| Reshare renamed "Smoking Tigers" Drive folder with service account `stai-eva-agent@...` | Ed | ⏳ Needed |
| Update `google-config.json` folder name field to "Smoking Tigers" | Scout | Ready when above done |
| Update Drive folder ID in config if it changed with rename | Scout | Ready when above done |
| Confirm Drive folder ID unchanged after rename | Ed | ⏳ Needed |
| Create `_INTAKE/` subfolder in Drive root | EA / Scout | After reshare |
| Build Notion "Smoking Tigers Files" database | EA | After schema approved |
| Build Drive Intake Agent (classify + rename + move + log to Notion) | sysops | After DB exists |
| Decide intake trigger method (cron / on-demand / webhook) | Ed | Decision needed |
| Set up external collaborator secure upload link | Ed / sysops | Later |

---

## 8. Decision Log

| Date | Decision | Made By |
|---|---|---|
| 2026-03-17 | Root folder renamed "Smoking Tigers" (from "Smoking Tigers Media Group") | Ed |
| 2026-03-17 | `_INTAKE/` = primary drop zone, agent-processed | Scout (proposed) |
| 2026-03-17 | Notion DB = source of truth for file discovery (not Drive search) | Scout (proposed) |

---

*This document should be pushed to Notion (ST:AI Ops or Operations DB) once schema is confirmed.*
