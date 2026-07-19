# Governance Sync — Phase 4
> Completed: 2026-03-03
> Grounded in: agent-authority-matrix.md, github-decision-tracking.md

---

## The Core Question

**When something happens or is decided — where does it go and who reviews it?**

Two routing destinations:
1. **GitHub** — canonical, versioned, permanent record
2. **Sergeant-at-Arms** — compliance check, RevPoints eligibility, conflict escalation

---

## Decision Routing: GitHub Issue Required

Create a GitHub decision record (`decisions/2026/DEC-YYYYMMDD-title.md`) when:

| Trigger | Examples |
|---------|---------|
| New policy adopted or changed | AI model routing policy, agent authority update |
| Governance role or authority change | New Steward, agent authority expansion |
| Architecture decision made | Choosing Cal.com, adopting Tailscale-only binding |
| Integration with security impact | New API token scoped, new service exposed |
| Infrastructure standard set | Docker network isolation, DHCP reservation |
| Tooling cost commitment | Paid service added (e.g. Notion API upgrade) |
| RevPoints policy change | Eligibility rules, RP-to-cash structure |
| Workflow adopted as official | Meeting capture policy, knowledge staging |
| Anything previously discussed becoming canonical | Decisions made in chat that need a permanent record |

**Who drafts:** governance-ops (Class B — propose only)
**Who approves:** Ed (Steward) — always
**Who merges:** Scout prepares PR, Ed approves

**Format:** `decisions/2026/DEC-YYYYMMDD-short-title.md`
Required fields: Decision ID, Title, Status, Date, Owner, Context, Decision, Rationale, Tradeoffs, References

---

## Decision Routing: Sergeant-at-Arms Review Required

Escalate to SAA when:

| Trigger | Why |
|---------|-----|
| RevPoints issuance recommendation | SAA verifies full eligibility chain before any RP is recorded |
| Contributor onboarding | SAA confirms governance compliance before contributor is active |
| Contributor offboarding | SAA checks open obligations, IP assignments |
| Suspected policy violation | SAA investigates, classifies (🟡 AMBER / 🔴 RED), routes appropriately |
| Conflict between contributors | SAA mediator process, escalates RED to Scout + Steward |
| IP artifact registration | SAA verifies contributor attribution is correct before registering |
| Any action where compliance is unclear | Default: route to SAA before proceeding |

**SAA authority:** Enforce, log, notify. Never act autonomously on RED — always escalates to Scout + Steward.
**SAA cannot:** Author governance content, commit to GitHub, act unilaterally on serious violations.

---

## Decision Routing: Neither Required (Class A — Autonomous)

Agents can act without GitHub record or SAA review when:

| Action type | Examples |
|------------|---------|
| Summaries and drafts | Meeting summaries, decision candidates, status reports |
| Formatting and classification | Classify intake files, format markdown, generate templates |
| Internal task management | Create/update Notion tasks, update task status |
| Read-only queries | Notion database queries, GitHub reads, calendar lookups |
| Scheduled maintenance | Memory digest, heartbeat tasks, log rotation |
| Notification delivery | Daily summaries, reminders, status pings |

---

## The Full Routing Matrix

| What happened | GitHub record | SAA review | Human approval |
|--------------|:-------------:|:----------:|:--------------:|
| New policy adopted | ✅ | — | ✅ Ed |
| Architecture decision | ✅ | — | ✅ Ed |
| Security/integration change | ✅ | — | ✅ Ed |
| Governance role change | ✅ | — | ✅ Ed |
| RevPoints issuance | ✅ (after) | ✅ (before) | ✅ Ed |
| Contributor onboarding | — | ✅ | ✅ Ed |
| Policy violation suspected | — | ✅ | ✅ Ed (if RED) |
| IP artifact registered | ✅ | ✅ | ✅ Ed |
| Workflow adopted officially | ✅ | — | ✅ Ed |
| Meeting occurred | — | — | — (EA handles) |
| Task created/updated | — | — | — (EA handles) |
| Infrastructure change executed | ✅ | — | ✅ Ed (pre-approval) |
| Draft prepared by agent | — | — | Review before finalize |

---

## Practical Flow for Agents

### When Scout or governance-ops identifies a decision:
1. Draft the decision record (Class B — propose only)
2. Post draft in #executive or #governance for Ed's review
3. Ed approves wording
4. governance-ops prepares PR to governance repo
5. Ed merges (or delegates merge with explicit authorization)
6. DECISIONS_INDEX.md updated

### When a RevPoints situation arises:
1. Contributor work output confirmed
2. SAA runs eligibility chain check (Job output → Hours → IP → Compliance → No open conflicts)
3. SAA posts verification result in #governance
4. governance-ops drafts RP issuance record
5. Ed approves
6. GitHub record created

### When a compliance concern surfaces:
1. SAA classifies: 🟢 OK (log only) / 🟡 AMBER (notify contributor, log) / 🔴 RED (escalate to Scout + Ed immediately)
2. Scout does not act autonomously on RED — presents to Ed
3. Ed decides next step

---

## What Today's Work Needs Logged

Based on today's session, these decisions need GitHub records drafted:

| Item | Decision ID | Status |
|------|-------------|--------|
| Cal.com adopted as scheduling layer | DEC-20260303-001 | Needs draft |
| Mattermost + Cal.com to bind Tailscale IP only | DEC-20260303-002 | Needs draft (pending sysops diff approval) |
| Notion API integration adopted (STM teamspace, read+write) | DEC-20260303-003 | Needs draft |
| STAI Intake folder established in iCloud | DEC-20260303-004 | Needs draft |
| EA pipeline defined (intake, templates, naming, routing) | DEC-20260303-005 | Needs draft |
| Memory pipeline architecture adopted | DEC-20260303-006 | Needs draft |

Want governance-ops to draft all six? Ed approves, then they get merged in one batch.
