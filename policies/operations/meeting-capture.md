# Policy — Capturing Data from a Meeting (Multi-Source Inputs)
Status: Draft v1.0
Owner: Ed (Steward)
Applies To: Executive Council, Project Leads, Contributors, OpenClaw agents
Last Updated: 2026-02-23
## Purpose
Create a consistent, low-friction method for capturing meeting knowledge from multiple sources (human notes, recordings, transcripts, chat, docs, whiteboards) and converting it into usable operational knowledge, decisions, and follow-up actions.
This policy prioritizes:
\- structural integrity over speed
\- traceability of decisions
\- reduced manual burden on humans
\- OpenClaw-assisted processing with human approval gates
## Why This Exists
Meeting knowledge is often lost because it is spread across:
\- voice memos
\- Zoom recordings
\- chat threads
\- screenshots
\- Miro boards
\- Notion docs
\- stream-of-consciousness summaries
\- AI-assisted rewrites
Without a standard capture process, decisions become ambiguous, action items get missed, and governance records become unreliable.
## Policy Statement
All material meeting outputs must be captured into a standardized intake flow and transformed into:
1. **Source artifacts** (raw evidence)
2. **Working summaries** (interpreted notes)
3. **Decision logs** (approved decisions)
4. **Action records** (owners \+ deadlines)
5. **Knowledge docs** (reusable policies, workflows, or specs)
No single summary is considered authoritative unless linked to source artifacts.
## Accepted Source Types
The following are valid meeting inputs:
### Primary Source Artifacts (preferred)
\- Audio recordings (voice memos, call recordings)
\- Video recordings (Zoom, Meet, Loom)
\- Official transcripts
\- Meeting chat logs
\- Shared documents used during the meeting
\- Whiteboard exports (Miro, FigJam, screenshots)
\- Agenda documents
### Secondary Source Artifacts (supporting)
\- Personal notes
\- AI-generated summaries
\- Post-meeting recap messages
\- Slack/Mattermost threads
\- Email follow-ups
## Source Hierarchy (Conflict Resolution)
When sources conflict, use this order:
1. Recording / transcript
2. Meeting chat log during session
3. Shared meeting doc edited live
4. Notes from facilitator / designated note-taker
5. AI summary
6. Participant recollection after the fact
If a conflict remains unresolved, mark as:
\- **UNCONFIRMED**
\- assign a follow-up to verify with participants
## Required Outputs for Every Decision-Relevant Meeting
Each meeting that affects governance, operations, budget, scope, or commitments must produce:
1. **Meeting Source Package**
2. **Structured Summary**
3. **Decision Candidates**
4. **Action Register**
5. **Escalations / Open Questions**
6. **Link to canonical storage location**
## Standard Capture Workflow
### Phase 1 — Collect Raw Inputs (No Interpretation)
Goal: preserve evidence before cleanup.
Collect into a single meeting intake folder:
\- recording(s)
\- transcript(s)
\- agenda
\- chat export
\- screenshots/whiteboards
\- personal notes
\- AI rough summaries (if any)
Naming convention:
`YYYY-MM-DD_meeting-name_source-type.ext`
Examples:
\- `2026-02-22_exec-council_zoom-recording.mp4`
\- `2026-02-22_exec-council_transcript.txt`
\- `2026-02-22_exec-council_mattermost-thread.md`
### Phase 2 — Normalize Inputs
Convert to machine-readable plain text where possible:
\- `.md`, `.txt`, `.csv`, `.json` preferred
\- avoid `.rtf` when possible
\- retain original files when converting
If OCR/transcription is needed:
\- store both raw file and extracted text
\- mark extraction quality (high / medium / low confidence)
### Phase 3 — Generate Structured Summary (OpenClaw-assisted)
OpenClaw may generate a summary, but it must be structured and not treated as final truth.
Required summary sections:
\- Meeting purpose
\- Participants
\- What was reviewed
\- What was decided
\- What is proposed but not approved
\- Action items (owner, due date, dependencies)
\- Risks / blockers
\- Open questions
\- Source references
### Phase 4 — Decision Extraction
Extract **decision candidates** separately from general summary.
Each decision candidate should include:
\- title
\- statement of decision
\- scope affected
\- decision owner / approver
\- date discussed
\- status: proposed / approved / rejected / deferred
\- supporting sources
Only approved decisions move to the decision log / governance repo.
### Phase 5 — Human Approval Gate
A designated human (meeting lead, steward, or assigned operator) must review:
\- decision wording
\- ownership assignments
\- dates / deadlines
\- unresolved ambiguities
No AI-generated decision is considered final without explicit human approval.
### Phase 6 — Publish to Systems of Record
Publish outputs to appropriate systems:
\- **Raw source package** → Intake / archive
\- **Working summary** → Notion / internal ops docs
\- **Decision log** → GitHub governance repo (or decision system)
\- **Actions** → task/project system (Notion, PM board, etc.)
\- **Calendar items** → shared calendar if time-bound
## Minimum Metadata Requirements
Every meeting capture package must include:
\- Meeting title
\- Date (ISO format)
\- Timezone
\- Participants (known)
\- Facilitator / host
\- Source list (what was captured vs missing)
\- Prepared by (human and/or agent)
\- Confidence notes (if transcript/OCR quality is poor)
## Roles and Responsibilities
### Meeting Host / Facilitator
\- ensures recording and/or notes are captured
\- confirms purpose and agenda
\- assigns capture responsibility if not self-handled
### Note-Taker / Operator (Human or OpenClaw-assisted)
\- collects source artifacts
\- organizes intake folder
\- produces structured summary draft
\- extracts action items and decision candidates
### Steward / Decision Owner
\- approves decisions and commitments
\- resolves ambiguity
\- authorizes publication to governance repo / canonical records
### OpenClaw Agent(s)
May assist with:
\- transcription cleanup
\- summarization
\- action extraction
\- decision candidate extraction
\- formatting for GitHub/Notion
May not:
\- finalize decisions without human approval
\- invent approvals or owners
\- silently publish to canonical records unless explicitly configured and authorized
## Data Quality Standards
Summaries and extracted actions must avoid:
\- invented certainty
\- missing owners
\- missing dates
\- mixing “discussion” with “decision”
\- collapsing multiple decisions into one vague statement
Use explicit labels:
\- **DECIDED**
\- **PROPOSED**
\- **OPEN QUESTION**
\- **ACTION**
\- **RISK**
\- **BLOCKER**
## Security and Access
Meeting capture files may contain sensitive information.
Rules:
\- store according to role-based access
\- limit executive discussions to approved channels/repositories
\- redact private data before broader sharing
\- do not upload sensitive recordings to unsecured services
## Retention and Versioning
\- Preserve raw source artifacts whenever practical
\- Do not overwrite transcripts/summaries without versioning
\- If corrected, add version suffix:
  \- `v1`, `v2`, `final-approved`
\- Keep audit trail of what changed and why for decision-related meetings
## Output Templates (Recommended)
For each meeting, create:
\- `README.md` (metadata \+ source inventory)
\- `SUMMARY.md` (structured summary)
\- `DECISIONS.md` (decision candidates / approved decisions)
\- `ACTIONS.md` (owners \+ due dates)
\- `SOURCES/` folder (raw artifacts)
## Exceptions
If recording fails, meeting may proceed, but the facilitator must:
\- designate a note-taker
\- produce a same-day summary
\- flag lowered confidence in decision capture
## Review Cadence
This policy should be reviewed after:
\- first 5 executive meetings using the process
\- any major decision-capture failure
\- changes in tooling (OpenClaw, Notion, GitHub, calendar stack)
