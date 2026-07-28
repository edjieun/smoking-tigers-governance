# Policy — Shared Calendars and Meeting Scheduling
Status: Draft v1.0
Owner: Ed (Steward)
Applies To: Executive Council, Project Leads, Contributors, OpenClaw scheduling support
Last Updated: 2026-02-23
## Purpose
Create a consistent scheduling and calendar system for Smoking Tigers operations that:
\- reduces back-and-forth coordination
\- supports global collaborators across time zones
\- improves meeting reliability
\- provides a foundation for time/accountability tracking
\- integrates with existing tools (Google Calendar, optional Cal.com, OpenClaw workflows)
## Principles
1. **One source of truth per calendar type**
2. **Timezone clarity is mandatory**
3. **Scheduling should be async-first**
4. **Humans decide priorities; systems handle logistics**
5. **Calendar entries should support operational reporting when appropriate**
## Calendar Architecture (Recommended)
Use separate shared calendars by function instead of one overloaded calendar.
### Core Calendars
1. **Executive Council Calendar**
   \- executive meetings
   \- strategy sessions
   \- governance deadlines
2. **Organization Operations Calendar**
   \- all-hands
   \- recurring ops cadences
   \- shared deadlines / launches
3. **Project Calendars** (one per major project/LOB as needed)
   \- planning sessions
   \- production milestones
   \- client meetings
   \- reviews
4. **Events / External Calendar** (optional)
   \- public events
   \- partnerships
   \- conferences
   \- speaking engagements
5. **Contributor Work Blocks / Capacity Calendar** (optional but recommended)
   \- planned work sessions
   \- office hours
   \- availability blocks (if used for hour tracking)
## Policy Statement
All recurring operational meetings must live on a shared calendar, not only in chat threads.
Meeting invitations must include:
\- title
\- owner/host
\- timezone-aware time
\- purpose (short)
\- meeting link (if remote)
\- expected attendees
\- prep requirements (if any)
## Scheduling Standard (How Group Meetings Get Scheduled)
To avoid endless back-and-forth, use a structured process:
### Step 1 — Define the Meeting Type
Before scheduling, identify:
\- decision meeting / working session / status sync / review / social
\- required attendees vs optional attendees
\- desired duration
\- deadline for when it must happen
### Step 2 — Use Availability Windows, Not Open-Ended Polling
Organizer proposes 2–5 time windows based on known constraints.
Avoid “When are you free?” messages to groups.
Preferred tools:
\- Google Calendar availability checks
\- Cal.com group scheduling (if implemented)
\- structured poll with time-zone normalized options
### Step 3 — Timezone Normalization
All scheduling proposals should include:
\- primary timezone reference (e.g., PT)
\- converted times for key regions when needed
\- date written explicitly (e.g., Tue, Feb 24, 2026\)
### Step 4 — Lock and Publish
Once confirmed:
\- create calendar invite
\- include agenda/prep links
\- post a confirmation message in the relevant channel
\- update any project tracker if meeting affects milestones
## Recurring Meetings
Recurring meetings must have:
\- clear owner
\- documented purpose
\- cadence (weekly, biweekly, monthly)
\- review date (to avoid zombie meetings)
Every recurring meeting should be reviewed at least quarterly:
\- keep
\- adjust
\- pause
\- retire
## Meeting Metadata Standard (Minimum)
Each operational meeting event should contain:
\- purpose / objective (1–3 lines)
\- host / decision owner
\- link to agenda or notes doc
\- who must attend
\- whether attendance counts toward tracked hours
\- tags (optional): exec, project, ops, client, production
## Cancellation / Rescheduling Rules
\- Cancel/reschedule as early as possible
\- Update calendar first, then message channel
\- Include reason if decision-critical
\- If a decision meeting slips, assign owner to reschedule immediately
## Calendar Hygiene Rules
Do:
\- use consistent naming
\- include links and context
\- mark recurring events clearly
\- use shared calendars for shared work
Do not:
\- rely on chat alone for confirmed meetings
\- create duplicate invites for the same meeting
\- leave placeholder events with no owner/purpose
\- bury required prep in random messages only
## OpenClaw Role in Scheduling (Assistive)
OpenClaw may:
\- draft scheduling proposals
\- summarize availability constraints
\- prepare event descriptions
\- generate reminders/checklists
\- route actions after meetings
OpenClaw may not:
\- finalize commitments on behalf of a human without authorization
\- infer attendance requirements if unclear
\- create calendar entries in systems where it lacks approved access
## Tooling Guidance (Current \+ Optional)
### Current Base (recommended minimum)
\- Google Calendar (shared calendars \+ invites)
\- Shared docs for agendas/notes
\- Mattermost/Slack for notifications
### Optional Upgrade
\- Cal.com for cleaner booking and group scheduling workflows
\- OpenClaw integration for meeting prep/post-meeting summaries
## Reporting / Hours Tracking Alignment
If calendar data is used for hour tracking:
\- tag eligible events clearly
\- distinguish meetings vs focused work blocks
\- do not assume attendance \= productive contribution without role context
\- use calendar as an input, not sole payroll truth (unless policy explicitly says so)
## Security / Access
\- Executive calendar visibility should follow role access
\- Sensitive meetings may use private event details
\- Avoid exposing confidential notes links on broad calendars
## Review Cadence
Review after:
\- first month of use
\- first cross-timezone scheduling failures
\- rollout of Cal.com or OpenClaw calendar automation
