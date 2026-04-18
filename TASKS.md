# TASKS.md — Active Delegation Tracker

> Scout maintains this file. Updated as tasks are assigned, completed, or blocked.
> Suggest workflow changes as patterns emerge.

---

## Status Key
- 🔵 Open — not yet started
- ⏳ In Progress
- ✅ Done
- ⚠️ Blocked / needs attention
- 🔁 Recurring
- 🚫 Held — waiting on build phase completion

---

## Truncated Message Log

| Date | Cut-off Text | Status |
|------|-------------|--------|
| 2026-03-02 13:52 | "Also need to t..." | 🚫 Held — no action until build phase complete |
| 2026-03-02 15:34 | "RP/cash structure" — confirm nothing missing | 🚫 Held — no action until build phase complete |
| 2026-03-05 09:42 | "In particular this week's executive call, yesterday's call with Christine and today's call with Niel's" — message cut mid-sentence | Captured — meeting intake task created below |
| 2026-03-06 16:28 | "I might move either mattermost or cal.com to a remot..." | 🔵 Captured — infrastructure migration decision pending (see Cal.com section below) |

---

## 2026-03-09

### Knowledge Capture
| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| ✅ | Capture weekend work (Doug/sysops) into memory + TASKS.md | Scout | Completed — memory/2026-03-07.md and memory/2026-03-08.md updated |

### Infrastructure — Migration to Q1 Hosted GCP
| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| ✅ | Email Esteban Montero: GCP environment choice (region/tier) | **Ed** | Written doc sent 2026-03-16 via Slack DM. Esteban recommended containerized environment — Ed approved. |
| 🔵 | Migrate Smoking Tigers Mattermost to Q1 GCP | Scout / Doug (sysops) | Awaiting Esteban provisioning (containerized env confirmed) |
| 🔵 | Migrate Smoking Tigers Cal.com to Q1 GCP | Scout / Doug (sysops) | Awaiting Esteban provisioning (containerized env confirmed) |

### Stripe + Banking — Smoking Tigers
| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| ✅ | Draft Stripe + banking business case document | **Scout → Ed review → Esteban** | Written doc sent by Ed via Slack DM 2026-03-16 |
| ✅ | Send written Stripe/banking request to Esteban | **Ed** | Sent 2026-03-16 via Slack DM |

---

## 2026-03-07 — 2026-03-08 (Weekend)

### Docker / Colima — Memory Increase
| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| ✅ | Increase Colima memory from 8GB → 12GB | Scout | `~/.colima/default/colima.yaml` → `memory: 12`; confirmed 11.66 GiB live at 15:24 Sat |

### Cal.com Docker Build — Source Rebuild (Doug / sysops)
| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| ✅ | Diagnose Cal.com URL mismatch root cause | Doug (sysops) |  `replace-placeholder.sh` length mismatch (21 vs 47 chars) corrupts Next.js bundle; must rebuild from source |
| ✅ | Design multi-stage Dockerfile (clone v6.2.0, NODE_OPTIONS=8192) | Doug (sysops) + Ed | node:20-alpine, clone v6.2.0, yarn --frozen-lockfile, turbo build filter=@calcom/web |
| ⚠️ | Execute Cal.com Docker build from source | Doug (sysops) | **FAILED** — exit code 1 at 18:09 Sat; `turbo.json` outputs config error + DATABASE_URL placeholder issue. Needs investigation + restart |
| 🔵 | Fix turbo.json outputs config and restart build | Doug (sysops) | Next step: pull full error, correct outputs key, refire build |

### Cal.com + Mattermost — Exec Remote Access (Doug / sysops)
| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| ✅ | Confirm both services healthy via Tailscale | Doug (sysops) | Mattermost: `https://edlicious-server.tailebe6d3.ts.net` ✅ Cal.com: `https://edlicious-server.tailebe6d3.ts.net:8443` ✅ |
| ✅ | Cal.com live test — no hostname leakage | Doug (sysops) | Auth redirect to `/auth/login` correct; NEXT_PUBLIC_WEBAPP_URL set properly |
| 🔵 | Send Tailscale invites to Basil, Van, Christine | **Ed** | Exec deadline was 3 PM Sun — still pending. Via Tailscale admin: `https://login.tailscale.com/admin/users` |
| 🔵 | Exec Tailscale onboarding (each person installs + joins tailnet) | Ed → Basil/Van/Christine | After invites sent |

---

## 2026-03-06

### Clarifications Confirmed
- **Ben = Van** (no new EC members)
- **Memo 2 person = Esteban** — wants to meet next week re: decommissioning an instance + continuity/comms for projects
- **Cal.com fix**: HELD — Ed may migrate Mattermost or Cal.com to a remote host; do not invest in current local fix
- **Exec Tailscale/MM access**: Ed can already access remotely → functionality confirmed for execs; execs should only interact with their assigned agent (scoped access)

### Infrastructure — Remote Migration (Decision Pending)

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| 🔵 | Evaluate: move Mattermost vs Cal.com to remote host | Ed → Scout | Ed flagged this; Scout to surface options when asked |
| 🚫 | Cal.com redirect fix (local) | — | HELD — blocked on migration decision |

### Esteban — Meeting Next Week

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| ✅ | Schedule + hold call with Esteban | Ed / Eva | Done — Impromptu Zoom 2026-03-09. Topics covered: GCP migration + Stripe/banking. See memory/2026-03-09.md |

### AI Agent Org Chart

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| ⏳ | Draft AI agent org chart (usage rate + cost tracking, for Christine + audit) | Scout | Approved by Ed 2026-03-06 — in progress |

### EC Governance Rules

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| 🔵 | Draft EC governance rules (Ed, Christine, Basil, Van) | Scout → Ed review | From voice memo; no new members confirmed |
| 🔵 | Draft AI/consumer ops rules (from Christine + Ed discussion) | Scout → Ed review | Companion to org chart |
| 🔵 | Define Niels role expectations for Christine's awareness | Scout → Ed review | Niels building Q1.is MVP with Ed |

### Exec Onboarding — Tailscale + Mattermost

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| ⏳ | Draft exec Tailscale + Mattermost onboarding guide | Scout | Execs scoped to assigned agent only; Ed already confirmed remote access works |

### Cal.com Usage + Notion Meeting Space

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| 🔵 | Draft Cal.com usage guide for execs | Scout | Independent of fix — draft now |
| 🔵 | Cal.com + scheduling plugin (Zapier/Buildstep?) | Scout | Basil raised on Sunday EC call; identify plugin + integration path |
| 🔵 | Notion meeting prep space (scheduling, agendas, decisions) | Eva (EA) | Add to Notion architecture scope |

### People + Relationships

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| 🔵 | David Hodgins — front-end / sell-in connection with Niels / Q1.is | Ed | Noted from voice memo; potential connection piece |

---

## 2026-03-05

### Cal.com Fix (Roadblock)

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| ⚠️ | Cal.com redirect still broken | doug (sysops) | Ed remote all day (no laptop). Roadblock. Resumed when Ed available. |


### Governance — DEC-20260303-006 Amendment

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| ✅ | Memory Pruning Policy drafted into DEC-006 | Scout | Approved by Ed (Steward) 2026-03-05 |

### Meeting Note Intake — This Week (URGENT)

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| 🔵 | Process: This week's Executive Council call | Eva (EA) / knowledge-ops | Source: Fathom recording link OR Google Doc (Gemini notes + transcript). Ed to provide link/doc. |
| 🔵 | Process: Call with Christine (yesterday) | Eva (EA) / knowledge-ops | Source: Fathom link OR Google Doc. Ed to provide. |
| 🔵 | Process: Call with Neil (today) | Eva (EA) / knowledge-ops | Source: Fathom link OR Google Doc. Ed to provide after call. |
| 🔵 | Define meeting note processing workflow | Eva (EA) | Standard SOP: Fathom link or Google Doc → extract key decisions, action items, project notes → populate Notion Meeting DB |

### Notion Architecture

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| 🔵 | Eva coordinates local agents to design all hub schemas | Eva (EA) | Artist/Creator Hub, Producer Hub, Business Hub, Document Library, Task DB wiring — all for Ed review |
| 🔵 | Design Notion Meeting DB schema | Eva (EA) | Must support: Fathom recording links, Google Doc links, Gemini-drafted transcripts, action items, decisions, project references |
| 🔵 | Design meeting note processing pipeline | Eva (EA) | How meetings flow from source (Fathom/Google Doc) → Meeting DB → project tasks |

### EA Expansion

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| 🔵 | Write Executive Council EA setup guide | Scout | How to provision EA for Basil, Van, Christine; standard template |

### Governance

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| 🔵 | Update GitHub governance repo — pending decisions (DEC-20260303-001 through 006) | governance-ops → Ed | DEC-006 shown above; all 6 are Approved |

### Legal Infrastructure

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| 🔵 | Draft CCA (Creator Content Agreement) | contract-drafting agent (TBD) | Build phase — draft ready for Ed review |
| 🔵 | Draft Contribution Agreement — TLN (Nick) | contract-drafting agent (TBD) | Nick is NOT signing RTPA. He purchases right to use Ed's RP. Agreement states Nick is launching TLN. Must work in synergy with CCA. |
| 🔵 | Draft Terms of Service | contract-drafting agent (TBD) | Covers rev points transactions |
| 🔵 | Stripe setup — write business case for Esteban | Scout → Ed → Esteban | Path confirmed 2026-03-09: written request to Esteban Montero (Q1). No longer blocked on Q1 Foundation formal process |

### TLN — Oral Agreements

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| 🚫 | Resolve oral agreements (money + content, no signed contracts) | Ed | Held — agreements on hold until build phase complete |

---

## 2026-03-04

### Notion Hub Architecture

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| 🔵 | Design Artist/Creator Hub schema in Notion | Eva (EA) | Nick's view: backlog, sessions, deliverables. Any IP creator. TLN = Nick. Eva coordinates local agents → for Ed review |
| 🔵 | Design Producer Hub schema in Notion | Eva (EA) | Robert/Basil view: session notes, pipeline, Riverside recordings, Drive links |
| 🔵 | Design Business Hub schema in Notion | Eva (EA) | Distribution, sponsors, rev point accounting, financial accounting |
| 🔵 | Design Document Library DB | Eva (EA) | Separate from hubs — stores docs, guidelines, accounting reports with Drive links |
| 🔵 | Wire hubs to Task DB | Eva (EA) | Each hub owns different parts of IP production workflow |

### EA Expansion — Executive Privilege

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| 🔵 | Write Executive Council EA setup guide | Scout | Standard playbook for provisioning EA for Basil, Van, Christine |
| 🔵 | Provision EA agent for Basil | Scout/Ed | After setup guide approved |
| 🔵 | Provision EA agent for Van | Scout/Ed | After setup guide approved |
| 🔵 | Provision EA agent for Christine | Scout/Ed | After setup guide approved |
| 🔵 | Define specialist sub-agents for EA | Basil's EA | Content production: keywords, titles, research, transcription |

### Governance Updates

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| 🔵 | Add member rights section to governance repo | governance-ops → Ed | Delineate: Executive Council / Contributors / Supporters |
| 🔵 | Update STM directory with relationships | Scout/Eva | Tie contributor roles, project assignments, contact relationships |
| 🔵 | Update agent authority matrix for per-Steward EA agents | governance-ops → Ed | Reflect Basil/Van/Christine EA permissions and scope |

### Legal Infrastructure

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| 🔵 | Draft CCA (Creator Content Agreement) template | contract-drafting agent (TBD) | Standard agreement for creators |
| 🔵 | Draft Creator Agreement template | contract-drafting agent (TBD) | Separate from CCA |
| 🔵 | Define Terms of Service | contract-drafting agent (TBD) | Covers rev points transactions |
| 🚫 | Set up Stripe for online transactions | Scout → Q1 Foundation | Requires Q1 Foundation formal request per Q1 governance |
| 🔵 | Define specialist agent roster | Scout → Ed | Contract drafting, compliance, etc. |
| 🚫 | TLN: Resolve current oral agreements | Ed | Held — on hold until build phase complete |

### Cal.com Fix (roadblock)

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| ⚠️ | Build custom Cal.com Docker image with baked URL | doug (sysops) | Ed remote all day (no laptop) — roadblock. Resume when Ed available. |

---

## 2026-03-03

### Cal.com — Next Steps

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| ✅ | Cal.com installed and accessible | sysops | http://100.122.103.40:3000 — Ed logged in, dashboard working |
| ✅ | Ed account created | Scout | ed@quorum.one — change password in settings |
| 🔵 | Connect Google Calendar to Cal.com | Ed | Requires Google OAuth in Cal.com settings — Ed must authorize |
| 🔵 | Connect Notion app in Cal.com | Ed | Cal.com Notion integration → auto-creates meeting notes |
| 🔵 | Set up shared STM Google Calendar | Ed | Create shared Google Calendar for all Stewards |
| 🔵 | Connect shared Google Calendar → Notion | Scout/EA | Sync calendar events to Notion Meetings DB |
| 🔵 | Connect shared Google Calendar → Cal.com | Ed/Scout | Team calendar visibility in Cal.com scheduling |
| 🔵 | Invite STM members (Basil, Van, Christine) | Ed → Scout | Scout can draft invite workflow once members have Tailscale access |
| 🔵 | Change Cal.com admin password | Ed | Current: STM2026!calcom — change via profile settings |
| 🔵 | Cal.com member onboarding process | Scout | Define how each Steward gets access and sets up their booking page |

### Phase 4 — Governance Sync

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| ✅ | Decision routing defined | Scout | GitHub vs SAA vs autonomous — full matrix in docs/governance-sync.md |
| 🔵 | Draft 6 decision records from today | governance-ops | DEC-20260303-001 through 006 — awaiting Ed approval to proceed |
| 🔵 | Batch merge approved decisions | governance-ops → Ed | Ed reviews drafts, approves, governance-ops prepares PR |

### Phase 2 — EA Pipeline Definition

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| ✅ | Intake folder taxonomy defined | Scout | ~/Desktop/intake/ structure confirmed; iCloud intake path TBD |
| ✅ | Output artifact templates defined | Scout | Meeting note, task capture, project brief, daily summary templates |
| ✅ | Naming conventions defined | Scout | YYYY-MM-DD-[slug]-[descriptor] format; project slugs standardized |
| ✅ | Routing map defined | Scout | Voice memo → Notion, calendar → Notion, tasks → Notion Tasks DB |
| ✅ | Define iCloud intake folder | Ed | Renamed to STAI Intake — ~/Library/Mobile Documents/com~apple~CloudDocs/STAI Intake/ |
| ✅ | Daily summary channel decision | Ed | Mattermost DM |
| ✅ | Voice memo automation | Ed | Auto-transcribe via Whisper |
| ✅ | Google Drive API for EA | Ed | **Completed 2026-03-12.** Service account `stai-eva-agent@smoking-tigers-agents.iam.gserviceaccount.com` (project: `smoking-tigers-agents`). Credentials at `~/.openclaw/credentials/google-service-account.json`. Drive: STM folder (ID: `1xXxfiMp_RLRQOXp0j7N2JO3B5P71MBk1`) read/write via Q1 Workspace (`ed.hwang@quorum.one`). Auth wired into EA + christine-ea. |
| ✅ | Google Calendar access for EA | Ed | **Completed 2026-03-12.** STM Operations calendar (edjhwang@gmail.com, read/write) + Q1 Workspace calendar (ed.hwang@quorum.one, read-only pending DWD). Config: `~/.openclaw/credentials/google-config.json`. |
| 🔵 | Upgrade Q1 Workspace calendar → read/write | Ed → Esteban | Requires Domain-Wide Delegation grant from Esteban (Q1 Workspace admin). |
| 🔵 | Whisper auto-transcribe schedule | Scout | Set up cron/LaunchAgent for Voice Memos folder |
| 🔵 | Confirm EA icalBuddy Calendar access | Scout | Needed for auto meeting creation in Notion |

### Phase 1 — Infrastructure Clarity

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| ✅ | Network map documented | Scout | T-Mobile→Linksys→Mac Mini; Tailscale overlay (4 devices); doc: docs/infrastructure-map.md |
| ✅ | Services inventory | Scout | Mattermost (8065), Cal.com (3000), Ollama (loopback), OpenClaw (loopback) |
| ✅ | Storage layout documented | Scout | Local paths, Google Drive (Shared/q1 creative/smoking tigers), iCloud, GitHub |
| ✅ | Security boundaries documented | Scout | Apple data = Scout + EA only (FDA). Agent authority scoped per AGENTS.md |
| ✅ | Cal.com Docker install | sysops | Deployed: cal-app, cal-postgres, cal-redis — isolated from mm-net |
| ✅ | Reserve Mac Mini LAN IP in Linksys | Ed | 192.168.1.132 reserved (MAC: D2:D0:B0:50:66:4E) — already existed |
| ✅ | Lock Mattermost + Cal.com to Tailscale IP | Scout + Ed | Implemented 2026-03-04: loopback bind + Tailscale Serve. MM: tailebe6d3.ts.net/, Cal.com: tailebe6d3.ts.net/calcom |
| 📌 | Tailscale ACL policy | Scout | Known gap — revisit when external collaborators (Basil/Van/Christine) added |

### Backlog Clearance

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| ✅ | Verify ea, sysops, saa respond to DMs | Ed | Confirmed — Sarge and EA both responded to DMs |
| ✅ | Fix knowledge-ops memory digest delivery error | Scout | Cron was failing: `No delivery target resolved for channel "mattermost"`. Fixed: set delivery.to = channel:krzyoit3gjgkuqqxenf6e7qscw (#executive) |
| ✅ | Test memory pipeline end-to-end | Scout | Ran knowledge-ops manually — memory/2026-03-03.md written successfully (9 work items, 3 decisions) |
| ✅ | Governance-ops + sergeant-at-arms workspace audit | Scout | Both verified — governance-ops AGENTS.md and SAA AGENTS.md are solid and properly scoped |

---

## 2026-03-02

### Infrastructure

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| ✅ | Bind governance-ops to Mattermost bot | Scout | Bot: `st-build-governance-ops-bot` — added to #executive |
| ✅ | Bind knowledge-ops to Mattermost bot | Scout | Bot: `st-build-knowledge-ops-bot` — added to #executive + #knowledge |
| ⚠️ | Verify gateway picked up new bot bindings | Scout | Gateway restart issued; confirm bots are live and responding |

### Knowledge Workflow

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| ✅ | Draft Notion Intake Lifecycle workflow | Scout | `workflows/notion-intake-lifecycle.md` written; DEC-20260302-001 filed (Draft) |
| ✅ | Retire full teamspace export model | Scout | Too large; replaced with project-scoped paste/file-drop intake |
| ✅ | Trade Like Nick knowledge intake | knowledge-ops | Completed by knowledge-ops — project bible and profile updated |
| ✅ | Process TLN knowledge paste into project bible | knowledge-ops | Done — `knowledge-bible/trade-like-nick-bible-v1.0.md` exists |
| 🔵 | Ed to confirm truncated activation constraints | Ed | 15:34 message cut off at "RP/cash structure" — confirm nothing missing |
| ✅ | #knowledge channel SOP | Scout | `docs/knowledge-channel-sop.md` written; knowledge-ops AGENTS.md updated with output channel |
| 🔵 | Draft intake source map | Scout | All sources: Voice Memos, iCloud, Desktop intake, Notion exports, Drive, GitHub, Mattermost |
| 🔵 | EA: Set up Notion Finance DBs | EA | RP ledger, income tracking, RP→cash — required before financial intake works |
| 🔵 | Complete Ed's truncated request (13:52) | Ed | Message cut off at "Also need to t..." — still pending |

### Open Items (carried from earlier today)

| Status | Task | Agent/Owner | Notes |
|--------|------|-------------|-------|
| ✅ | Debug knowledge-ops memory digest | Scout / knowledge-ops | Fixed — delivery target was missing; pre-processing script working |
| ✅ | Verify ea, sysops, saa respond to DMs | Ed | Confirmed via DM |
| ✅ | Governance-ops + sergeant-at-arms workspace audit | Scout | Both verified clean |
| 🔵 | knowledge-ops SOURCES.md / knowledge index | knowledge-ops | Referenced but not built |

---

## Workflow Notes

### Observed Pattern
Ed delegates infrastructure tasks (bot bindings, config) and workflow design tasks in the same session.
Risk: config work is confirmed but downstream workflow design work goes untracked.

### Suggestion
After each infrastructure task completes → immediately draft the corresponding SOP or channel structure before moving on.
Prevents "bot exists but nobody knows how to use it" state.

### Next Logical Step
Before adding more bots or channels: define the #knowledge channel SOP and intake source map.
Without that, knowledge-ops has no operating instructions.

---

---

## 2026-03-20 — Voice Memo Work Log

> Source: voice memo transcript (2026-03-20 ~07:04 PDT). PDF attached was empty (0 bytes — no data).

---

### 📥 File & Document Intake Process — Mattermost + Notion

> Context: Direct server access (Desktop intake folder) only works for Ed on the server. A Mattermost-native process is needed for Ed when remote, and for Christine + other exec members who never have direct access.

| Status | Task | Owner | Notes |
|--------|------|-------|-------|
| ✅ | Design Mattermost file intake process for exec team | Scout | Process: upload to STM Drive → post link in #executive → tag @scout. SOP written 2026-03-20. |
| ✅ | Document Notion-based intake process for all team space members | Scout | SOP published to Notion → OPs: SOPs, Guidelines, Agreements. [View](https://www.notion.so/SOP-File-Document-Intake-via-Mattermost-3296f6ac689e81c69342d84b862bc62d) |
| 🔵 | Evaluate whether OpenClaw Mattermost inbound file fetch can be enabled or worked around | Scout | Check for config options, workarounds, or upcoming support. If not feasible, document the gap and design around it. |
| 🔵 | Add intake SOP to exec onboarding materials | Scout | Once process is defined, fold into exec onboarding guide |

---

### 🟦 Task: Read Morning Intake Report
| Status | Task | Owner | Notes |
|--------|------|-------|-------|
| 🔵 | Read today's morning intake report (this document) | **Ed** | **First task of the day.** See: `docs/reports/2026-03-20-morning-intake.md` |

---

### 🔧 AI Ops — Channel Session Work Times + Agent Models

| Status | Task | Owner | Notes |
|--------|------|-------|-------|
| 🔵 | Configure Christine's agent channel session to work during her scheduled hours | Scout | Ensure her agent is active only during her work window |
| ✅ | Verify Rosie is using correct models | Scout | Confirmed 2026-03-20: Rosie (christine-ea) running `openrouter/anthropic/claude-sonnet-4.6` ✅ |
| 🔵 | Post proposed changes to Notion AI Ops plan for Ed review | Scout | Ed approves changes via Notion comments — this is the approval channel |

---

### 🏛️ GitHub Governance — AI Ops Rules Update

| Status | Task | Owner | Notes |
|--------|------|-------|-------|
| 🔵 | Update GitHub governance repo to include server config backups | governance-ops | Repo should contain config backups of servers in use (how they're configured) |
| 🔵 | Define AI Ops governance rules: what can be changed in Notion vs. what requires exec review | governance-ops → Ed | Changes to config/agent files: recordable in Notion, but must be funneled to exec team for review + approval before execution |
| 🔵 | Document decision chain for AI Ops changes (Notion → Exec review → Execute) | Scout / governance-ops | Formalize the flow so no direct Notion-only changes bypass exec review |
| 🔵 | Add agent model profiles to governance repo | governance-ops | Include agent profiles + their teams — even if not displayed publicly |
| 🔵 | Create AI Ops agent team section (similar to ST directory structure) | Scout | Need a base section in both governance repo and Notion for agent profiles + teams |
| 🔵 | Reorganize Notion accordingly (agent profiles + teams section) | Eva (EA) | Align with new AI Ops governance structure |

---

### 🎯 Notion — Scout Section as Team Interaction Hub

| Status | Task | Owner | Notes |
|--------|------|-------|-------|
| 🔵 | Designate Notion "Scout" section as the primary space for team to interact with AIs | Scout / Eva (EA) | Refine workspaces, get work done, configure agents, track decisions — all via this section |
| 🔵 | Ensure all workspace config changes tracked in Scout Notion section | Scout | Decisions logged, workspace changes visible to team |

---

### 📞 TLN / Nick — Pre-Call Prep

| Status | Task | Owner | Notes |
|--------|------|-------|-------|
| 🔵 | Schedule call with Nick (TLN) | **Ed** | Set up the call |
| 🔵 | Get notes from Basil before the Nick call | **Ed** | Pull Basil's notes to inform agenda |
| 🔵 | Build call agenda using Basil's notes | Scout / Eva (EA) | Update agenda before the call |
| 🔵 | Add to Nick call agenda: compliment his use of comms | **Ed** | Highlight his great use of WhatsApp + Slack to forward messages to the group — note this is tracked and used to update the vision plan |

---

### 📊 Notion Dashboard + Cal.com Integration

| Status | Task | Owner | Notes |
|--------|------|-------|-------|
| 🔵 | Define Ed's primary dashboard in Notion | Scout / Eva (EA) | Ed confirmed: Notion is the dashboard. Needs to surface Cal.com features (scheduling, booking, recording sessions). |
| 🔵 | Integrate Cal.com scheduling into Notion workflow | Scout / Eva (EA) | Surface Cal.com booking links, upcoming sessions, and recording scheduling directly in Notion. Define which pages/DBs link to Cal.com. |
| 🔵 | Add Rosie (Christine's EA) location to session config | Scout | ✅ IDENTITY.md updated: Christine is in Brisbane, AU (AEST/AEDT). Session scheduling and calendar work should account for this timezone. |

---

### 🎬 TLN / Nick — Video Recording Scheduling Process

| Status | Task | Owner | Notes |
|--------|------|-------|-------|
| 🔵 | Design process for Nick to schedule recording sessions from his dashboard | Scout / Eva (EA) | Nick should be able to add a meeting from his dashboard and invite Robert, Basil, and/or Ed |
| 🔵 | Recording sessions use Riverside | **Ed** | Process must accommodate Riverside recording workflow |
| 🔵 | Link content preparation data to recording session (video type, sections, time, date, Riverside link) | Scout / Eva (EA) | Session record should pull from content prep: video type, sections to record, all relevant detail |
| 🔵 | Build out recording session scheduling in Cal.com or Notion | Scout | Determine the right tool; design the flow |

---

*Last updated: 2026-03-20 07:10 PDT by Scout*
