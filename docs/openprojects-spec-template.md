---
version: "1.0"
last-updated: 2026-07-16
purpose: Template for OpenProjects work package specs — used by Scout agent to create structured tasks from transcripts
---

# OpenProjects Spec Template — Transcript Processing

## Overview

This spec defines how Scout creates work packages in OpenProjects after processing a meeting transcript. OpenProjects is the **source of truth** for all tasks and decisions. Mattermost is the notification layer.

---

## API Reference

**Server:** `https://ste-business-server.tailebe6d3.ts.net:8080`
**Auth:** Basic — username `apikey`, password = `$OPENPROJECTS_API_KEY`
**Note:** Bearer token auth does NOT work on this instance. Always use Basic auth.

### Create Work Package
```
POST /api/v3/projects/{project_id}/work_packages
Authorization: Basic base64(apikey:{OPENPROJECTS_API_KEY})
Content-Type: application/json

{
  "subject": "[Owner]: task description",
  "description": {
    "raw": "Context, due date, source transcript date"
  },
  "_links": {
    "type": {
      "href": "https://ste-business-server.tailebe6d3.ts.net:8080/api/v3/types/1"
    }
  }
}
```

### Work Package Types
| ID | Name | Use for |
|---|---|---|
| 1 | Task | Action items from transcripts |
| 2 | Milestone | Key dates/deadlines |
| 3 | Summary task | Meeting session grouping |
| 5 | Epic | Project-level goals |

---

## Project ID Map

| Project | ID | Identifier | Route when… |
|---|---|---|---|
| Smoking Tigers — Operations | 3 | `ste-ops` | Costs, LedgerSMB, governance, catch-all |
| Smoking Tigers — Website | 6 | `ste-website` | Website copy, design, community, onboarding, stakeholders |
| Camp Audax [working title] | 11 | `camp-audax-working-title` | Camp Audax, The Gathering, Victor, Brad, satellite event |
| Smoking Tigers AI Buildout | 12 | `ste-ai-buildout` | Mac Mini, OpenClaw, Scout, Mattermost, infrastructure, OpenProjects |
| RMA — New Meeting Flow | 13 | `rma-meeting-flow` | RMA, Sage, Nikki, Kurt, meeting format |

---

## Spec: Process Transcript and Create Work Packages

**Input:** Raw transcript text (or Fathom link) posted to MM #transcripts
**Output:** Work packages in OpenProjects + notification posts in MM channels

### Step-by-step

```
SPEC: process-transcript
VERSION: 1.0

INPUTS:
  - transcript_text: string (raw text or URL)
  - posted_by: string (MM username of who posted)
  - posted_at: ISO8601 timestamp

STEPS:

  1. ACKNOWLEDGE
     - Post to MM #transcripts: "📥 Transcript received. Processing..."
     - Record: transcript length, source format

  2. EXTRACT_METADATA
     - Detect: project name/topic, meeting date, participants
     - Map to project_id using Project ID Map
     - If ambiguous: use project_id 3 (STE Operations), note ambiguity

  3. CHUNK_IF_NEEDED
     - If transcript > 8000 words: split into chunks
     - Each chunk header: project, date, chunk N of M
     - Process chunks sequentially

  4. FOR EACH CHUNK: EXTRACT
     a. DECISIONS: agreements made between participants
        - Format: "[DATE] | [PROJECT] | [Decision — one clear sentence]"
     b. TASKS: actions with an assignable owner
        - Format: "[Owner]: [task] — due [date or TBD]"
        - Owner must be a real person name or "Both" / "Team"
     c. OPEN_QUESTIONS: raised but not resolved
        - Format: "❓ [Question] — [person who raised it]"

  5. WRITE_TO_OPENPROJECTS (primary)
     For each TASK:
       - POST /api/v3/projects/{project_id}/work_packages
       - subject: "[Owner]: [task description]"
       - description.raw: "Source: MM #transcripts [date]\n[context]\nDue: [date or TBD]"
       - type: /api/v3/types/1 (Task)
       - Record returned work package ID

     For each DECISION:
       - POST /api/v3/projects/{project_id}/work_packages
       - subject: "DECISION: [decision text]"
       - description.raw: "Source: MM #transcripts [date]\nParticipants: [list]"
       - type: /api/v3/types/1 (Task)
       - Record returned work package ID

  6. POST_TO_MATTERMOST (notifications)
     To #decisions:
       "## [DATE] — [PROJECT]\nSource: #transcripts\n\n[decisions list with OP#IDs]"

     To #tasks:
       "## [DATE] — [PROJECT]\nSource: #transcripts\n\n**[Owner]**\n- [OP#NNN] [task]\n..."

     To #transcripts (summary reply):
       "✅ Done: [N] decisions, [N] tasks → OpenProjects\n[N] open questions:\n[list]\nOP project: [URL]"

  7. WRITE_MEMORY_CARD (Google Drive)
     - File: [PROJECT] - [YYYY-MM-DD] - [Topic Slug].md
     - Sections: Summary, Decisions, Action Items, Open Questions, Key Quotes

  8. POST_ERRORS (if any step failed)
     To #agent-logs:
       "❌ PIPELINE ERROR | Step: [N] | Reason: [description]"

ACCEPTANCE_CRITERIA:
  - All extracted tasks exist as work packages in OpenProjects
  - All extracted decisions exist as work packages in OpenProjects
  - #tasks and #decisions channels have notification posts with OP#IDs
  - #transcripts has a summary reply with open questions
  - No cloud model used (local only: lmstudio/qwen/qwen3.5-9b)
  - If OpenProjects unreachable: post error to #agent-logs, complete MM posts anyway
```

---

## Example Work Package Payloads

### Task
```json
{
  "subject": "Ed: DM Zach on Signal for 30-min 1:1",
  "description": {
    "raw": "Source: MM #transcripts 2026-07-16\nMeeting: STE stakeholder planning\nContext: Zach is in Europe. Assess AI engineer vs. business/strategy role.\nDue: This week"
  },
  "_links": {
    "type": {
      "href": "https://ste-business-server.tailebe6d3.ts.net:8080/api/v3/types/1"
    }
  }
}
```

### Decision
```json
{
  "subject": "DECISION: Victor outreach happens before Brad — he must answer the 20% allocation question first",
  "description": {
    "raw": "Source: MM #transcripts 2026-07-14\nMeeting: STE stakeholder planning\nParticipants: Ed Hwang, Christine Francis"
  },
  "_links": {
    "type": {
      "href": "https://ste-business-server.tailebe6d3.ts.net:8080/api/v3/types/1"
    }
  }
}
```

---

## LedgerSMB Integration (Phase 3C)

When transcript contains **financial items** (costs, budgets, compensation, expenses):
1. Note them in the Memory card under a `## Financial Items` section
2. Create a work package in project 3 (STE Ops): "FINANCE: [item description]"
3. LedgerSMB entry to be created manually by Ed until auto-integration is built

### LedgerSMB URL
`https://ste-business-server.tailebe6d3.ts.net:5762/`
(HTTP redirect on port 5762 — confirmed running)
Credentials: separate from OpenProjects — log in via browser

---

## Known Issues / Workarounds

| Issue | Workaround |
|---|---|
| Bearer token auth fails on OpenProjects | Use Basic auth: `apikey:{OPENPROJECTS_API_KEY}` |
| OpenProjects unreachable | Complete MM posts; log error to #agent-logs; note "OP pending" |
| Fathom link requires auth | Ask member to paste raw text instead |
| Transcript > context window | Chunk to 6,000 words per chunk |
| `plugins.allow` warning in OpenClaw | Already fixed — `mattermost` is in allow list |
