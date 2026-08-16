---
last-updated: 2026-07-16
maintainer: Ed Hwang
---

# Task Log

> All tasks extracted from meeting memory cards. Status: `[ ]` open · `[~]` in-progress · `[x]` done.
> Source links point to the Memory/ card where the task was extracted.
> Update status here AND in the source Memory card when completing a task.

---

## Project: Camp Audax / The Gathering

| # | Owner | Task | Due | Status | Source |
|---|---|---|---|---|---|
| 1 | Ed | Draft 5 questions for Victor (Camp Audax / Gathering scope, 20% allocation, STE role definition) — send to Christine on Discord | ASAP | [ ] | [Stakeholder Next Steps](../Memory/STE%20-%202026-07-14%20-%20Stakeholder%20Next%20Steps.md) |
| 2 | Christine | Send brief acknowledgment email to Brad. Hold strategic questions until Victor responds. | ASAP | [ ] | [Stakeholder Next Steps](../Memory/STE%20-%202026-07-14%20-%20Stakeholder%20Next%20Steps.md) |
| 3 | Ed | DM Zach on Signal to set up a 30-minute 1:1 this week (Zach is in Europe) | This week | [ ] | [Stakeholder Next Steps](../Memory/STE%20-%202026-07-14%20-%20Stakeholder%20Next%20Steps.md) |
| 4 | Christine | DM Murdoch on Discord (username: Frogakuda) to schedule a 1:1 discovery call | This week | [ ] | [Stakeholder Next Steps](../Memory/STE%20-%202026-07-14%20-%20Stakeholder%20Next%20Steps.md) |
| 5 | Ed | Coordinate group call week of July 21 — Murdoch, Brandon, Zach, Christine, Ed | July 21 week | [ ] | [Stakeholder Next Steps](../Memory/STE%20-%202026-07-14%20-%20Stakeholder%20Next%20Steps.md) |
| 6 | Both | Post message in Discord asking members to update to real names + LinkedIn + profile photo | This week | [ ] | [Stakeholder Next Steps](../Memory/STE%20-%202026-07-14%20-%20Stakeholder%20Next%20Steps.md) |
| 7 | Christine | Message Victor — request meeting with Brad Nye ASAP; mention October urgency | ASAP | [ ] | [Camp Audax Open Questions](../Memory/STE%20-%202026-07-08%20-%20Camp%20Audax%20Open%20Questions%20and%20STE%20Role.md) |
| 8 | Ed | Follow up with Victor on Camp Audax cost/equipment/commission structure | ASAP | [ ] | [Camp Audax Open Questions](../Memory/STE%20-%202026-07-08%20-%20Camp%20Audax%20Open%20Questions%20and%20STE%20Role.md) |

---

## Project: STE — Website & Community Launch

| # | Owner | Task | Due | Status | Source |
|---|---|---|---|---|---|
| 9 | Ed | Draft three simple value props for the website (bottleneck → solution → community CTA). Keep it non-academic. | — | [ ] | [Community Model and Membership](../Memory/STE%20-%202026-07-14%20-%20Community%20Model%20and%20Membership.md) |
| 10 | Both | Define what the "first thing" a new member does after joining — must be specific and low-friction | — | [ ] | [Community Model and Membership](../Memory/STE%20-%202026-07-14%20-%20Community%20Model%20and%20Membership.md) |
| 11 | Both | Identify 2–3 seed projects to post on community board (e.g., Camp Audax AI content, on-device research agent setup) | — | [ ] | [Community Model and Membership](../Memory/STE%20-%202026-07-14%20-%20Community%20Model%20and%20Membership.md) |

---

## Project: RMA — New Meeting Flow & STE Partnership

| # | Owner | Task | Due | Status | Source |
|---|---|---|---|---|---|
| 12 | Ed | Re-state Smoking Tigers’ offer to manage MOUs/contracts to RMA formally — not just verbally | Deferred — MOU is NOT a blocker for Ed+Sage Friday session; clarify scope on Friday call | [ ] | [RMA Situation and Team Dynamics](../Memory/STE%20-%202026-07-08%20-%20RMA%20Situation%20and%20Team%20Dynamics.md) |

---

## Project: On-Premise AI — Mac Mini Infrastructure Rebuild

| # | Owner | Task | Due | Status | Source |
|---|---|---|---|---|---|
| 13 | Ed | Create private GitHub repo; consolidate all credentials into encrypted `.env`; document restore procedure | Phase 0 | [x] done 2026-07-16 — repo: `edjieun/ste-secrets`; vault at `~/ste-secrets-repo/vault.tar.gz.enc`; 14/15 keys (❌ `MATTERMOST_TEAM` missing); ⚠️ `GOOGLE_OAUTH_CLIENT_SECRET` needs rotation in GCP | [On-Premise AI Architecture Plan](../Memory/STE%20-%202026-07-15%20-%20On-Premise%20AI%20Architecture%20Plan.md) |
| 13a | Ed | Get `MATTERMOST_TEAM` slug from MM web UI — create team first (no team exists yet); see `docs/mattermost-setup.md` Step 1 | ASAP | [ ] blocked — no MM team created yet | Task #13 follow-up |
| 13b | Ed | Rotate `GOOGLE_OAUTH_CLIENT_SECRET` in GCP console (project: `smoking-tigers-agents`) → update `google-oauth-client.json` + `.env` → re-encrypt vault → push | ASAP | [ ] | Task #13 follow-up — secret was exposed in chat log 2026-07-15 |
| 14 | Ed | Power on Mac Mini; restore credentials; configure LM Studio with system prompt; enable server mode; test over Tailscale | Phase 1 | [x] done 2026-07-16 — Qwen3.5 9B live on port 1234; `ste-default` preset with system prompt active; Tailscale→inference verified; vault cleaned and re-pushed | [On-Premise AI Architecture Plan](../Memory/STE%20-%202026-07-15%20-%20On-Premise%20AI%20Architecture%20Plan.md) |
| 15 | Ed | Write OpenProjects spec template for transcript processing (input → chunk → card writing → Google Drive + 1TB) | Phase 2 | [ ] | [On-Premise AI Architecture Plan](../Memory/STE%20-%202026-07-15%20-%20On-Premise%20AI%20Architecture%20Plan.md) |
| 16 | Ed | Configure OpenClaw Mattermost `#transcripts` listener | Phase 2 | [ ] | [On-Premise AI Architecture Plan](../Memory/STE%20-%202026-07-15%20-%20On-Premise%20AI%20Architecture%20Plan.md) |
| 17 | Ed | Validate Qwen3.5 9B orchestration capability | Phase 3 | [ ] | [On-Premise AI Architecture Plan](../Memory/STE%20-%202026-07-15%20-%20On-Premise%20AI%20Architecture%20Plan.md) |
| 18 | Ed | Evaluate Hermes agent on laptop after inference is stable | Phase 3 | [ ] | [On-Premise AI Architecture Plan](../Memory/STE%20-%202026-07-15%20-%20On-Premise%20AI%20Architecture%20Plan.md) |

---

## Project: Smoking Tigers AI Buildout *(this system)*

| # | Owner | Task | Due | Status | Source |
|---|---|---|---|---|---|
| 19 | Ed | Set up GitHub governance repo with `docs/adr/` structure | — | [ ] | Domain modeling session 2026-07-16 |
| 20 | Ed | Standardize all existing workspaces to Discovery structure (Memory/, Transcripts/, chunks/, docs/) | — | [ ] | Domain modeling session 2026-07-16 |
| 21 | Ed | Create Mattermost channels (#transcripts, #tasks, #decisions, #agent-logs); see `docs/mattermost-setup.md` | — | [ ] blocked — no MM team yet; needs Step 1 first | Phase 2 plan 2026-07-16 |
| 22 | Ed | Build/configure meeting-to-tasks agent pipeline (transcript → Memory → tasks) | — | [x] done 2026-07-16 — Scout transcript-processor deployed; TRANSCRIPT-PROCESSOR.md + AGENTS.md updated on Mac Mini | Domain modeling session 2026-07-16 |
| 23 | Ed | Archive pmp-team, maven, openclaw.json → `edjieun/ste-agents-archive` GitHub repo | Phase 2A | [x] done 2026-07-16 — repo pushed, secrets redacted | Phase 2 plan 2026-07-16 |
| 24 | Ed | Delete `~/.openclaw/agents/pmp-team` and `maven` from Mac Mini | Phase 2A | [x] done 2026-07-16 — only `main` agent remains | Phase 2 plan 2026-07-16 |
| 25 | Ed | Rebuild `openclaw.json`: Scout → Qwen local primary, no cloud fallback, pmp-team/maven removed | Phase 2B | [x] done 2026-07-16 — Qwen primary, Gemma fallback, OpenRouter stays registered but not in any agent chain | Phase 2 plan 2026-07-16 |
| 26 | Ed | Move `NOTION_API_KEY` from `openclaw.json` → vault | Phase 2B | [x] done 2026-07-16 — vault updated and pushed (commit 4713788) | Phase 2 plan 2026-07-16 |
| 27 | Ed | Write Scout transcript-processor system prompt | Phase 2B | [x] done 2026-07-16 — `TRANSCRIPT-PROCESSOR.md` written to `~/.openclaw/workspace/`; `AGENTS.md` updated | Phase 2 plan 2026-07-16 |
| 28 | Ed | Create MM channels + wire Scout binding + update vault with team slug | Phase 2C | [x] done 2026-07-16 — 4 channels created; Scout bound to #transcripts; MATTERMOST_TEAM=smoking-tigers-enterprises in vault | Phase 2 plan 2026-07-16 |
| 28a | Ed | Deactivate `mavin` and `pmp-team` bot accounts in MM System Console | Phase 2C | [ ] — manual step in MM admin UI | Phase 2 plan 2026-07-16 |
| 29 | Ed | Create Christine's MM account; add to #transcripts, #tasks, #decisions | Phase 2C | [x] done 2026-07-16 — username: christine; ID: yr3bqxa89bgbtc53u6bbq9xtde; temp password: SmokeAndMirrors2026! — send to Christine via Discord DM | Phase 2 plan 2026-07-16 |
| 30 | Ed | Write `docs/member-sop.md` | Phase 2E | [x] done 2026-07-16 | Phase 2 plan 2026-07-16 |
| 31 | Ed | Record Friday Ed+Sage planning meeting; post raw transcript to MM #transcripts as live verification test | Friday | [~] in-progress — partial verification done 2026-07-16: STE Landing Page transcript (June 23) uploaded to #transcripts; scout-cos processed it and posted full meeting summary (topics, decisions, action items). #tasks and #decisions channels not yet populated — scout-cos uses old instructions; @scout (new local-only config) needs to be used for full pipeline. Friday = first full end-to-end test with new Scout. | Phase 2 plan 2026-07-16 |
| 32 | Ed | Update OpenRouter credit balance after each test run (check openrouter.ai/activity) | Ongoing | [~] Balance at ~6:50pm 2026-07-16: $40.10 (session spend ~$9.85) | Phase 2 plan 2026-07-16 |
| 33 | Ed | Consolidate to single agent: use @scout (new local-only config) for the Friday transcript test; decommission scout-cos from #transcripts channel after Scout is confirmed working | Post-Friday | [ ] | Phase 2 plan 2026-07-16 |

## Project: M1 Server — OpenProjects + LedgerSMB Integration

| # | Owner | Task | Phase | Status | Source |
|---|---|---|---|---|---|
| 34 | Ed | Verify M1 + OpenProjects — M1 reachable, OP running, 9 existing projects found | 3A | [x] done 2026-07-16 — Basic auth confirmed; 9 projects + 11 new created (projects 12, 13) | Phase 3 plan 2026-07-16 |
| 35 | Ed | Create STE AI Buildout (id:12) + RMA Meeting Flow (id:13) projects in OP | 3A | [x] done 2026-07-16 | Phase 3 plan 2026-07-16 |
| 36 | Ed | Migrate open tasks to OpenProjects work packages (22 WPs created: #218–#239) | 3A | [x] done 2026-07-16 | Phase 3 plan 2026-07-16 |
| 37 | Ed | Update Scout TRANSCRIPT-PROCESSOR.md to write tasks+decisions to OP as primary destination | 3B | [x] done 2026-07-16 — deployed to Mac Mini with project ID map, API format, Basic auth fix | Phase 3 plan 2026-07-16 |
| 38 | Ed | Write OpenProjects spec template (docs/openprojects-spec-template.md) | 3B | [x] done 2026-07-16 — also deployed to Mac Mini as OPENPROJECTS-SPEC.md | Phase 3 plan 2026-07-16 |
| 39 | Ed | Verify LedgerSMB running on M1 | 3C | [x] done 2026-07-16 — HTTP 302 on port 5762, confirmed running | Phase 3 plan 2026-07-16 |
| 40 | Ed | Log today’s OpenRouter spend (~$17.64, 2026-07-16) as first LedgerSMB AI cost entry | 3C | [ ] — log in via browser: ste-business-server.tailebe6d3.ts.net:5762 | Phase 3 plan 2026-07-16 |
| 41 | Ed | Wire OpenRouter activity API → periodic Mac Mini job → LedgerSMB auto cost tracking | 3C | [ ] | Phase 3 plan 2026-07-16 |
| 42 | Ed | Update ADR-0001: OpenProjects = task/decision source of truth; markdown = readable cache | 3D | [ ] | Phase 3 plan 2026-07-16 |

---

## Decisions Log

> Key decisions extracted from memory cards. These are agreements — not tasks.

| Date | Project | Decision | Source |
|---|---|---|---|
| 2026-07-16 | Smoking Tigers AI | Decisions and Tasks are separate domain entities | ADR-0001 |
| 2026-07-16 | Smoking Tigers AI | Agents are tools (not members); humans are accountable for agent actions | ADR-0001 |
| 2026-07-16 | Smoking Tigers AI | Mac Mini = autonomous scheduled agent target, not just inference | ADR-0001 |
| 2026-07-16 | Smoking Tigers AI | Projects require member agreement to be real (topics without agreement are not projects) | ADR-0001 |
| 2026-07-16 | Smoking Tigers AI | GitHub commits and LedgerSMB writes require human approval | ADR-0001 |
| 2026-07-14 | STE | Victor outreach happens before Brad — he must answer the 20% allocation question first | [Stakeholder Next Steps](../Memory/STE%20-%202026-07-14%20-%20Stakeholder%20Next%20Steps.md) |
| 2026-07-14 | STE | Neil classified as "supporter" (not steward/contributor) until active contract exists | [Stakeholder Next Steps](../Memory/STE%20-%202026-07-14%20-%20Stakeholder%20Next%20Steps.md) |
| 2026-07-14 | STE | Discord standard: real names + LinkedIn + profile photos required for all members | [Stakeholder Next Steps](../Memory/STE%20-%202026-07-14%20-%20Stakeholder%20Next%20Steps.md) |
| 2026-07-14 | STE | Drop 6-week program framing; use modular discovery-led onboarding | [Community Model and Membership](../Memory/STE%20-%202026-07-14%20-%20Community%20Model%20and%20Membership.md) |
| 2026-07-14 | STE | Initial membership ask = content contribution (video/idea), not a fee | [Community Model and Membership](../Memory/STE%20-%202026-07-14%20-%20Community%20Model%20and%20Membership.md) |
| 2026-07-15 | On-Premise AI | Root cause of token bleeding: LM Studio missing system prompt → silent cloud fallback | [On-Premise AI Architecture Plan](../Memory/STE%20-%202026-07-15%20-%20On-Premise%20AI%20Architecture%20Plan.md) |
| 2026-07-15 | On-Premise AI | Secrets stored as encrypted `.env` in private GitHub repo; restore = pull + decrypt + source | [On-Premise AI Architecture Plan](../Memory/STE%20-%202026-07-15%20-%20On-Premise%20AI%20Architecture%20Plan.md) |
| 2026-07-15 | On-Premise AI | Hard local block on Mac Mini: never calls cloud; failures notify loudly via Mattermost | [On-Premise AI Architecture Plan](../Memory/STE%20-%202026-07-15%20-%20On-Premise%20AI%20Architecture%20Plan.md) |
| 2026-07-15 | On-Premise AI | Spec (not prompt) is the unit of work in OpenProjects | [On-Premise AI Architecture Plan](../Memory/STE%20-%202026-07-15%20-%20On-Premise%20AI%20Architecture%20Plan.md) |
| 2026-07-08 | RMA | RMA pivot: distribution channel for existing content, not primary producer | [RMA Situation and Team Dynamics](../Memory/STE%20-%202026-07-08%20-%20RMA%20Situation%20and%20Team%20Dynamics.md) |
| 2026-07-08 | Camp Audax | STE's role = ticket sales coordination and group/network recruitment (NOT programming design) | [Camp Audax Open Questions](../Memory/STE%20-%202026-07-08%20-%20Camp%20Audax%20Open%20Questions%20and%20STE%20Role.md) |
