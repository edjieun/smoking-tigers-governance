# EA Pipeline Definition — Phase 2
> Completed: 2026-03-03

---

## Overview

EA's pipeline covers four surfaces:
1. **Intake** — documents, voice memos, messages dropped for processing
2. **Output artifacts** — what EA produces (notes, summaries, task lists, calendar entries)
3. **Naming conventions** — how things are named so they're findable
4. **Routing** — where output goes (Notion, Google Drive, local, iMessage)

---

## 1. Intake Folder Taxonomy

### Local intake (`~/Desktop/intake/`)
Current drop zone for agent processing. Already wired to heartbeat pipeline.

**Proposed structure (flat — matches philosophy):**

```
~/Desktop/intake/
├── completed/          ← processed files move here
├── failed/             ← processing failures land here
└── [files]             ← anything dropped here gets processed next heartbeat
```

**What belongs here:**
- Voice memo transcripts (from Whisper)
- Exported Notion pages / CSVs for knowledge ops
- PDF documents for knowledge intake
- Meeting notes drafts
- Any file Ed drops that needs agent action

**What does NOT belong here:**
- Long-term project artifacts (those go to Google Drive)
- Governance docs (those go to `~/srv/q1/governance/`)
- Agent workspace files (those stay in `~/.openclaw/workspace/`)

### iCloud intake
For documents originating from iPhone/iPad — drop to iCloud, EA picks up.
**Path:** `iCloud Drive/STAI Intake/` (`~/Library/Mobile Documents/com~apple~CloudDocs/STAI Intake/`)
Renamed from "Intake Directory" on 2026-03-03.

### Voice memo intake
**Auto-transcribe** via Whisper on schedule (no manual trigger needed).
Whisper transcribes → transcript dropped to `~/Desktop/intake/` → heartbeat picks up.
EA should watch for transcripts tagged as meeting notes vs. general thoughts.

---

## 2. Output Artifact Templates

### Meeting Note
```
# [Meeting Title] — [YYYY-MM-DD]

**Type:** [One-on-one / Team / Client / All-hands]
**Attendees:** [Names]
**Duration:** [X min]

## Agenda
- 

## Notes
- 

## Decisions Made
- 

## Action Items
| Owner | Task | Due |
|-------|------|-----|
|       |      |     |

## Next Meeting
[Date / TBD]
```
**Destination:** Notion Meetings DB (create record) + URL stored in Minutes field

---

### Task Capture
```
Task: [description]
Assignee: [name]
Project: [project name]
Due: [date or TBD]
Priority: [Critical / High / Medium / Low]
Notes: [context]
```
**Destination:** Notion Tasks DB (create record)

---

### Project Brief
```
# [Project Name]

**Type:** [Internal / External]
**Owner:** [name]
**Lifecycle:** [Idea / Exploring / Activating / Active / Complete]
**Priority:** [Critical / Important / Medium]

## What it is
[1-2 sentences]

## Goals
- 

## Key Milestones
| Milestone | Target Date | Status |
|-----------|-------------|--------|
|           |             |        |

## Resources
- Docs: [link]
- Knowledge: [link]
```
**Destination:** Notion Strategy DB (create record)

---

### Daily Summary (EA → Ed)
```
## [Day], [Date] — Daily Summary

### Completed
- 

### In Progress
- 

### Needs Your Attention
- 

### Calendar Tomorrow
- [time] [event]
```
**Destination:** DM to Ed via **Mattermost**

---

## 3. Naming Conventions

### Files (local + Google Drive)
```
[YYYY-MM-DD]-[project-slug]-[descriptor].[ext]

Examples:
2026-03-03-tln-strategy-brief.md
2026-03-03-stm-meeting-notes.md
2026-03-03-q1-governance-review.pdf
```

**Rules:**
- Dates always first — enables chronological sort
- Lowercase, hyphens only (no spaces, no underscores)
- Project slug from the standard list (see below)
- Descriptors kept short (2-3 words max)

### Project Slugs (standard)
| Project | Slug |
|---------|------|
| Smoking Tigers (general) | `stm` |
| Trade Like Nick | `tln` |
| Q1 / Quorum1 | `q1` |
| Smoking Tigers AI | `stai` |
| Freedom of Will (podcast) | `fow` |
| Cal.com instance | `calcom` |

### Notion Records
Notion page titles follow the same convention where practical:
- Meetings: `[YYYY-MM-DD] [Meeting Title]`
- Tasks: `[Verb] [object] — [project slug]` (e.g. "Update governance index — stm")
- Documents: `[YYYY-MM-DD] [descriptor] — [project slug]`

---

## 4. Routing Map

| Input Type | EA Action | Destination |
|-----------|-----------|-------------|
| Voice memo transcript | Parse → meeting note or task capture | Notion (Meetings or Tasks DB) |
| Intake .md file | Route to knowledge-ops or parse directly | Notion + local q1_knowledge |
| Calendar event created | Auto-create Notion Meetings record | Notion Meetings DB |
| Calendar event completed | Prompt Ed for notes, create meeting record | Notion Meetings DB |
| Task mentioned in conversation | Create Notion task | Notion Tasks DB |
| Document dropped in intake | Classify → register in Notion Documents DB | Notion Documents DB + Google Drive link |
| Meeting notes URL | Store in Notion Meetings record | Notion Meetings DB (Minutes field) |

---

## 5. Open Items

- [x] iCloud intake folder — `STAI Intake` (renamed 2026-03-03)
- [x] Daily summaries → Mattermost DM
- [x] Voice memos → auto-transcribe via Whisper
- [ ] Google Drive API — manual until Ed makes a decision (EA stores Drive links in Notion only)
- [ ] Confirm EA has icalBuddy access to Calendar (needed for auto meeting creation)
- [ ] Set up Whisper auto-transcribe schedule (cron or LaunchAgent)
