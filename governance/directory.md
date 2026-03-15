# Smoking Tigers Media — Member Directory

**Status:** Draft
**Owner:** Ed (Steward)
**Type:** Living Document — updated as membership changes
**Last Updated:** 2026-03-11
**Requires Approval:** Yes — pending Steward review before becoming official

---

## Purpose

This is a living directory of current STM members, their roles, project assignments, contact routing, and digital identity. It is maintained as a governance reference and is not a public document.

**Privacy note:** No phone numbers in this file. Identity records are stored here for agent access control purposes — treated as high-sensitivity. Do not restate or expose externally.

---

## Identity Framework

### What "Identity" Means Here

In the context of STM/Q1 operations, **identity** refers to the combination of:
1. **Who you are** — your legal name and governance role
2. **What account you use for what** — which email/service controls which surface
3. **What agents can touch on your behalf** — access grants per service, per agent

Identity is not just a login. It determines:
- Which Google Drive folders agents can read/write
- Which calendars agents can create events in
- Which services are managed by Scout/Eva vs. owned directly by the human
- Which accounts are high-sensitivity (Apple ID, personal email) vs. operational (agent admin)

### Identity Tiers (STM Operational Model)

| Tier | Purpose | Agent Access |
|------|---------|-------------|
| **Tier 1 — Governance/Work** | Q1 organizational work, shared drives, shared calendars | Eva + designated agents (read/write with authorization) |
| **Tier 2 — Agent Admin** | Services managed by Scout under Ed's guidance | Scout/Eva operational control |
| **Tier 3 — Apple/Hardware** | Hardware security, iCloud, Tailscale node identity | Read-only reference; no agent writes |
| **Tier 4 — Personal** | Personal subscriptions, non-work accounts | Low priority; agent access not granted |

---

## Executive Council (Stewards)

Stewards hold governance authority, capital allocation responsibilities, and Q1 alignment oversight. See `role-authority.md` for full role definitions.

---

### Ed Hwang

| Field | Detail |
|---|---|
| **Role** | Founding Steward; Governing Steward |
| **Governance Authority** | Final authority on all Class C governance decisions; founding reference implementation |
| **EA Agent** | Eva (active) |
| **Mattermost** | @ed (default contact routing) |

**Identity & Access Map:**

| Identity | Tier | Purpose | Agent Access |
|----------|------|---------|-------------|
| `ed.hwang@quorum.one` (alias `ed@quorum.one`) | Tier 1 — Work/Governance | Q1 org account; Google Workspace; Smoking Tigers Drive; shared calendars | Eva: read/write (Drive + Calendar, scoped) |
| `stai_scout@proton.me` | Tier 2 — Agent Admin | Admin account for services Scout manages (e.g., service registrations, API accounts, tool configs) under Ed's guidance | Scout: operational; Eva: operational |
| `edlicious@icloud.com` | Tier 3 — Apple/Hardware | Apple ID; iCloud; hardware security; Tailscale node identity | Reference only — no agent writes |
| `edjhwang@gmail.com` | Tier 4 — Personal | Personal email; personal subscriptions (work + non-work mix) | Low priority; not currently granted |

**Google Drive Access:**
- Primary work drive: Q1 Creative shared drive, connected to `ed.hwang@quorum.one`
- Focus folder: **Smoking Tigers** folder within Q1 Creative
- Agent write access: Eva + designated agents (scoped to Smoking Tigers folder)
- Naming convention: needs to be established (see Drive Org section below)

**Calendar Access:**
- **STM Operations Calendar** ✅ LIVE — read/write
  - Name: `Smoking Tigers — Operations`
  - ID: `ec1f7967b73d7edcdd987d1abb23a08d33bbf69bcf2590200c3651b28e925920@group.calendar.google.com`
  - Owner: `edjhwang@gmail.com` (interim — pending Q1 Workspace DWD from Esteban)
  - Agent access: Eva read/write active
- **STM Q1 Workspace Calendar** — read-only (pending DWD)
  - ID: `c_0a1749810c64ed820ef6bd861d33752c97954696cef7d25351e2e173414fa069@group.calendar.google.com`
  - Owner: `ed.hwang@quorum.one`
  - Blocked: Q1 Workspace org policy blocks service account writes until Esteban grants DWD
- **Apple calendars** (icalBuddy): iCloud CalDAV via `edlicious@me.com` — Scout read-only, personal use

**Project Assignments:**
- All active STM projects (Steward oversight)
- ST:AI — Steward / IP Owner / Founding Operator
- TLN (The Last Name) — Steward/Governance role

---

### Basil Childers

| Field | Detail |
|---|---|
| **Role** | Steward; Executive Council Member |
| **Governance Authority** | Full Steward authority within scope |
| **EA Agent** | Entitled; provisioning pending |
| **Contact** | Via Mattermost or Ed's EA for scheduling |
| **Notes** | Role assignments and project scope to be confirmed by Ed. |

**Project Assignments:**
- TLN (The Last Name) — **Creative Director**

---

### Van Nguyen

| Field | Detail |
|---|---|
| **Role** | Steward; Executive Council Member |
| **Governance Authority** | Full Steward authority within scope |
| **EA Agent** | Entitled; provisioning pending |
| **Contact** | Via Mattermost or Ed's EA for scheduling |
| **Notes** | Role assignments and project scope to be confirmed by Ed. |

**Project Assignments:**
- TLN (The Last Name) — **Executive Producer**

---

### Christine Francis

| Field | Detail |
|---|---|
| **Role** | Steward; Executive Council Member |
| **Governance Authority** | Full Steward authority within scope |
| **EA Agent** | Entitled; provisioning pending |
| **Mattermost** | @christinefrancis |
| **EA Agent** | Eva (Christine) — active ✅ | 
| **Contact** | Via @christinefrancis on Mattermost · #svp-christine · or Ed's EA for scheduling |
| **Notes** | No defined role on TLN at this time. Steward at STM level. Co-authored ST:AI Stewards Proposal (March 2026). |

**Project Assignments:**
- TLN (The Last Name) — No defined project role at this time
- ST:AI — Co-authored Stewards Proposal (March 2026)

---

## Creator/Partners

Creator/Partners are IP originators. They hold primary IP ownership and creative/business vision for their projects. Creator/Partner classification is distinct from scoped labor.

---

### Nick

| Field | Detail |
|---|---|
| **Role** | Creator/Partner (IP Originator) |
| **Primary Project** | TLN (The Last Name) |
| **Scope** | Creator/Partner — retains primary IP ownership; not scoped labor |
| **Contact** | Via Mattermost |

---

## Contributors

Contributors perform scoped project labor or governance/strategic work. Access and entitlements are scoped to active project assignments.

---

### Niels van der Linden

| Field | Detail |
|---|---|
| **Role** | Contributor — ST:AI MVP (Product/Technical) |
| **Entity** | Personal or Tribre *(confirm — see Open Items below)* |
| **Primary Project** | Smoking Tigers AI (ST:AI) — MVP |
| **Agreement Status** | ⚠️ DRAFT — Not Executed (2026-03-11) |
| **Agreement File** | `agreements/DRAFT_2026-03-11_STAI-Niels-Contributor-Agreement.md` |
| **Contact** | TBD — connect to OpenClaw (action item from 2026-03-11 call) |
| **Notes** | Collaborating with Michael Halligan on ST:AI MVP. European rights (to operate ST:AI in Europe) to be defined in agreement. Has existing access to Smoking Tigers Notion space and Google Drive (granted previously). |

**Project Assignments:**
- ST:AI — MVP contributor (Q1 sandbox setup, product definition, agent architecture feedback)

**⚠️ Open Items — Steward Must Confirm Before Agreement Execution:**

1. **Entity** — Niels personally or Tribre (full legal name + jurisdiction)?
2. **Cash/RP split** — Niels prefers partial cash + partial RP. Is cash available? Split?
3. **Market rate** — Agreed hourly rate for his contribution type?
4. **RPM** — Suggested 3×. Confirm or adjust.
5. **Total RP** — Flows from rate × hours × RPM. Needs Exhibit A first.
6. **Exhibit A** — Specific deliverables: Q1.IS sandbox, agent onboarding, productization. Needs explicit definition.
7. **European rights** — Exclusive/non-exclusive? Territory? Revenue share % back to STM?
8. **Michael Halligan** — Separate agreement needed. Confirm scopes don't overlap.
9. **Connect Niels to OpenClaw** — Provide agent access for ST:AI knowledge base queries.
10. **Execution date** — Confirm at signing.

---

### Robert

| Field | Detail |
|---|---|
| **Role** | Contributor — Production |
| **Primary Project** | TLN (The Last Name) |
| **Scope** | Production work within TLN project scope |
| **Contact** | Via Mattermost |
| **Notes** | Production contributor. Specific scope governed by project agreement. |

---

### J. Killian

| Field | Detail |
|---|---|
| **Role** | Contributor — Contracts |
| **Primary Project** | TLN (The Last Name) |
| **Scope** | Contract work within TLN project scope |
| **Contact** | Via Mattermost |
| **Notes** | Contracts/legal contributor. Specific scope governed by project agreement. |

---

## Agent Access Control Map

This section defines what agents can access, on which accounts, and under what authority.

> **Rule:** Agents may draft, prepare, and propose. Class C actions (financial, legal, access changes) always require explicit Steward (Ed) authorization. See `agent-authority-matrix.md`.

| Agent | Identity Used | Access Granted | Access Level | Notes |
|-------|--------------|---------------|-------------|-------|
| **Scout** (main) | `stai_scout@proton.me` | Service admin accounts managed under Ed's guidance | Operational within defined scope | Does not touch Ed's personal or Apple accounts |
| **Eva** (EA) | `ed.hwang@quorum.one` via API token | Notion (read/write); Google Drive — Smoking Tigers folder (read/write pending OAuth); Google Calendar — STM Shared + work cal (read/write pending OAuth) | Read/write within authorized scope | Drive/Calendar requires OAuth setup (in progress) |
| **Scout** (main) | `edlicious@me.com` via icalBuddy | Apple Calendar (local read) | Read-only | No writes to Apple Calendar without explicit instruction |
| **Sarge** (Sergeant at Arms) | No service accounts | Governance repo review only | Read + propose | No external service access |
| **GoverOps** | No service accounts | Governance repo read/write | Read + draft | No external service access |
| **KnowledgeOps** | No service accounts | Local file system + Notion read | Read + ingest | No write to canonical sources |
| **SysOps** (Doug) | Local system | Mac Mini system operations | Scoped local ops | No access to Google/Apple services |

**Services controlled via `stai_scout@proton.me`:**
- Agent-managed API service accounts (e.g., tool registrations)
- Any new service provisioned by Scout under Ed's guidance
- Does NOT include Google Workspace (that stays on `ed.hwang@quorum.one`)

---

## Google Drive — Smoking Tigers Folder

**Drive:** Q1 Creative (shared drive)
**Account:** `ed.hwang@quorum.one`
**Target folder:** Smoking Tigers

**Current state:** Disorganized, no naming convention.

**Proposed naming convention (pending Ed approval):**
```
Smoking Tigers/
├── 00_Governance/          ← policies, charters, decision records
├── 01_Projects/
│   ├── ST-AI/
│   ├── TLN/
│   └── [project-name]/
├── 02_Agreements/          ← contracts, RTPAs, contributor agreements
├── 03_Finance/             ← budgets, rev point ledgers, invoices
├── 04_Marketing/           ← proposals, decks, brand assets
├── 05_Operations/          ← SOPs, meeting notes, working docs
└── 06_Archive/             ← completed/inactive items
```

**Agent access requirement:** OAuth token for `ed.hwang@quorum.one` scoped to Google Drive (specific folder). To be set up via `rclone` or Google API credentials. **Pending Ed authorization.**

**Notion link sync:** Once Drive is organized, Notion page links should point to canonical Drive folders. Eva maintains these links.

---

## STM Shared Calendar

**Calendar ID:** `c_0a1749810c64ed820ef6bd861d33752c97954696cef7d25351e2e173414fa069@group.calendar.google.com`
**Owner:** Ed Hwang (`ed.hwang@quorum.one`)
**Access:** Controlled by Ed. No external invites without Steward authorization.

**Proposed use:**
- STM team meetings (Stewards + active Contributors)
- Project milestones and review dates
- Agreement execution dates
- Governance deadlines

**Who gets access (Ed decides):**
- Stewards: Basil, Van, Christine — invite when ready
- Active contributors: on project-by-project basis (e.g., Niels for ST:AI work)
- No automatic access — Ed controls invite list

**Agent write access:** Eva may create events on this calendar once OAuth is configured. All event creation requires either explicit instruction or pre-approved template (e.g., meeting follow-up events).

---

## Project Role Map — ST:AI

| Role | Member | Function |
|------|--------|---------|
| Steward / IP Owner | Ed Hwang | Governance, architecture, final authority |
| Steward / Co-Proposer | Christine Francis | Co-authored Stewards Proposal |
| MVP Contributor | Niels van der Linden | Product/technical, Q1 sandbox, European rights (pending agreement) |
| MVP Collaborator | Michael Halligan | Productization (separate agreement needed) |
| Chief of Staff Agent | Scout | Coordination, memory, governance enforcement |
| EA Agent | Eva | Notion, Drive, Calendar operations |

---

## Project Role Map — TLN (The Last Name)

| Role | Member | Function |
|------|--------|---------|
| Steward (Governance) | Ed Hwang | Q1 alignment, intake oversight, final governance authority |
| Steward / Creative Director | Basil Childers | Creative direction |
| Steward / Executive Producer | Van Nguyen | Executive production oversight |
| Steward (Council) | Christine Francis | Executive Council — No defined role on TLN |
| Creator/Partner | Nick | IP originator; retains primary IP ownership |
| Production Contributor | Robert | Production execution within scoped agreement |
| Contracts Contributor | J. Killian | Contract work within scoped agreement |

---

## Contact Routing

| Situation | Route |
|-----------|-------|
| Urgent matter for Ed | Contact via Eva (EA) or Mattermost @ed |
| Reaching a Steward | Contact via Mattermost or their EA agent |
| Project coordination (ST:AI) | Route to Ed or Niels via Mattermost |
| Project coordination (TLN) | Route to relevant contributor via Mattermost |
| Governance questions | Contact Ed or appropriate Steward via Mattermost |
| Contracts / legal (TLN) | Route to J. Killian via Mattermost |
| Production coordination (TLN) | Route to Robert via Mattermost |
| Service admin / tool issues | Route to Scout via #executive |

---

## Next Steps — Infrastructure (Pending)

| Item | Owner | Status |
|------|-------|--------|
| Google OAuth setup for Eva (Drive + Calendar) — `ed.hwang@quorum.one` | Ed + Scout | ⏳ Pending — requires OAuth credentials |
| ~~Install Google API client on Mac Mini~~ | ~~Scout~~ | ✅ Done — google-api-python-client installed |
| ~~Google service account setup~~ | ~~Ed + Scout~~ | ✅ Done — stai-eva-agent@smoking-tigers-agents.iam.gserviceaccount.com |
| ~~Wire Drive access for Eva~~ | ~~Scout~~ | ✅ Done — Smoking Tigers folder read/write active |
| ~~Wire Calendar access for Eva~~ | ~~Scout~~ | ✅ Done — STM Operations Calendar read/write active |
| Organize Smoking Tigers Drive folder + apply naming convention | Eva | ⏳ Ready — pending Ed go-ahead |
| Update Notion links to point to organized Drive folders | Eva | ⏳ Blocked on Drive org |
| Share STM Operations Calendar with Stewards | Ed | ⏳ Pending Ed decision on who gets invited |
| Get DWD from Esteban (Q1 Workspace admin) | Ed → Esteban | ⏳ Pending — unlocks Q1 Workspace calendar write |
| Connect Niels to OpenClaw agent access | Ed + Scout | ⏳ Action item from 2026-03-11 call |
| Michael Halligan contributor agreement | Ed | ⏳ Draft needed — scope TBD |

---

## Maintenance Notes

- This directory is a living document. Update when membership changes.
- Changes to Steward assignments require a governance decision record.
- Identity records are high-sensitivity — no personal emails/phones exposed externally.
- Agent access changes (add/remove) require explicit Steward (Ed) authorization.
- All contact routing uses Mattermost or EA agents.

---

*This document is a Draft. Not approved for operational use until reviewed and approved by Ed Hwang (Steward).*
