# q1 Network Build Process SOP
**Version:** 1.0  
**Authors:** Ed, Hank  
**Status:** Active  
**Last Updated:** 2026-04-15  
**Repo:** https://github.com/quorum1/q1-home  

---

## Table of Contents

1. [Overview](#1-overview)
2. [Roles & Responsibilities](#2-roles--responsibilities)
3. [Feature Lifecycle](#3-feature-lifecycle)
4. [Standing Artifacts](#4-standing-artifacts)
5. [Weekly Cadence](#5-weekly-cadence)
6. [Linear Setup](#6-linear-setup)
7. [AI Agent Responsibilities](#7-ai-agent-responsibilities)
8. [Activation Checklist](#8-activation-checklist)
9. [Appendix](#9-appendix)

---

## 1. Overview

This SOP defines the end-to-end build process for the q1 Network (Quorum One) product. It governs how features move from raw idea to deployed functionality, and how humans and AI agents collaborate at each stage.

### Why This Exists

Product work without process generates drift — misaligned priorities, undocumented decisions, inconsistent output. This SOP eliminates that by defining:

- A single structured pipeline every feature follows
- Clear human/AI ownership at each stage
- Living documentation (Standing Artifacts) that keeps the system legible at any point
- A recurring weekly rhythm that keeps the pipeline moving

### What is a Feature?

Every unit of product work is called a **Feature**. Features are tracked in Linear and follow a staged lifecycle from **Seed** to **Closed**. The process is supported by always-current Standing Artifacts and a weekly grooming cadence.

### Scope

Applies to all product development on the q1 Network platform. Does not cover infrastructure-only changes, emergency hotfixes, or administrative configuration unless explicitly entered into the Feature pipeline.

---

## 2. Roles & Responsibilities

### Ed
- Product owner and build process operator
- Final decision authority on priorities, scope, and strategic alignment
- Leads weekly grooming sessions
- Approves features advancing from Design Candidate → Ready for Design
- Reviews and signs off on Design Specs before build begins
- Owns Standing Artifact governance

### Hank
- Product co-lead and design partner
- Collaborates on feature scoping and design specifications
- Drives Design Stage output (stages 4–6)
- Owns build planning and TDD drafting (stages 7–8)
- Primary liaison between design intent and AI build execution

### AI Agents
- Execution support, not decision-makers
- Invoked by Ed or Hank at defined handoff points
- Responsible for: generating design specs, drafting TDDs, running test suites, updating documentation
- Never move a feature forward in Linear without human confirmation
- Full breakdown in [Section 7](#7-ai-agent-responsibilities)

### Future Team Members
When onboarding:
- Read this SOP in full
- Review current Standing Artifacts before contributing
- Shadow one full grooming session before owning any stage
- Do not invent stages, labels, or workflow states outside what's defined here

---

## 3. Feature Lifecycle

The pipeline has five phase groups. Human/AI split is noted per phase.

---

### Phase 1 — Planning (90% Human / 10% AI)

---

#### Stage 1: Seed

**What it is:** An early idea that needs more fleshing out. Anything worth tracking but not yet clearly defined.

**Entry Criteria:**
- Someone has an idea worth capturing
- Minimum info: Title, Description, Source

**Work Process:**
- Feature created in Linear under the Ideas board, state = `Seed`
- Discussed at the weekly grooming session
- Ed and Hank talk through it and update fields in real time

**Deliverable:** Groomed feature record with:
- Cleaned Title & Description
- Priority (P1–P4)
- Size (S / M / L / XL)
- Aligned Goals (one or more strategic goal codes)

**Exit Criteria:** All required properties filled. Both Ed and Hank agree the feature is clearly enough defined to proceed.

**Human/AI Split:** Human-led. AI can clean up description prose if requested.

---

#### Stage 2: Groomed

**What it is:** Clearly defined feature ready to be formally scoped for design impact.

**Entry Criteria:**
- Passed Seed grooming
- All Stage 1 properties complete

**Work Process:**
- Async. No meeting required.
- Ed or Hank produces the Design Scope.
- Design Scope defines: which Standing Artifacts will be impacted, which systems are involved, what aspects of data model or workflows are touched.

**Deliverable:** Design Scope attached to the Linear feature (linked doc, comment, or sub-issue)

**Exit Criteria:** Design Scope exists and is specific enough to guide a designer.

**Human/AI Split:** Human-led. AI can draft initial scope from Standing Artifacts; human must review and approve.

---

#### Stage 3: Design Candidate

**What it is:** Feature is fully groomed and scoped. Candidate for entering the Design queue.

**Entry Criteria:**
- Design Scope complete
- Feature in `Design Candidate` state

**Work Process:**
- Reviewed at the weekly grooming session
- Ed and Hank assess design bandwidth for the upcoming week
- Candidates stack-ranked against each other
- Selected features marked `Ready for Design`

**Deliverable:** Prioritized list of features advanced to `Ready for Design`. Remaining candidates stay in `Design Candidate`.

**Exit Criteria:** Feature explicitly marked `Ready for Design` by end of grooming session.

**Human/AI Split:** Human-led. AI can generate summary comparison of candidates if requested.

---

### Phase 2 — Design (50% Human / 50% AI)

---

#### Stage 4: Ready for Design

**What it is:** Feature queued for active design work.

**Entry Criteria:**
- Marked `Ready for Design` during grooming
- Design Scope complete

**Work Process:** Hank picks up the feature and begins design. AI agents invoked to support spec generation.

**Human/AI Split:** Human owns direction; AI supports research and spec drafting.

---

#### Stage 5: Design Spec

**What it is:** Active design work in progress.

**Entry Criteria:**
- Feature actively being designed
- AI agent invoked

**Work Process:**
- AI drafts initial Design Spec from: Design Scope, relevant Standing Artifacts, existing system docs
- Hank reviews, edits, refines
- Ed reviews and approves

**Deliverable:** Complete Design Spec covering:
- Problem statement and solution approach
- Data model changes (if any)
- Workflow changes (if any)
- Component impact list
- UI/UX notes (if applicable)
- Open questions resolved

**Exit Criteria:** Ed and Hank both sign off.

**Human/AI Split:** AI drafts, humans review and approve.

---

#### Stage 6: Build Candidate

**What it is:** Design complete. Feature ready to enter Build queue.

**Entry Criteria:**
- Design Spec approved
- Standing Artifacts updated to reflect finalized design decisions

**Work Process:** Feature waits in `Build Candidate` until build bandwidth is allocated. No further design work at this stage.

**Exit Criteria:** Feature selected for build and marked `Prioritized Design`.

**Human/AI Split:** Human makes prioritization decision. AI uninvolved.

---

### Phase 3 — Build (20% Human / 80% AI)

---

#### Stage 7: Prioritized Design

**What it is:** Feature selected for active build. Next in line or currently being built.

**Entry Criteria:**
- Selected from Build Candidate pool
- Build bandwidth confirmed

**Work Process:** Hank and AI agent collaborate to produce Build Draft. No new design decisions — implementation planning only.

---

#### Stage 8: Build Draft

**What it is:** Draft implementation plan / TDD (Technical Design Document). One level of detail below the Design Spec.

**Entry Criteria:**
- Feature in `Prioritized Design`
- Design Spec locked

**Work Process:**
- AI drafts TDD from Design Spec and Standing Artifacts. TDD includes:
  - Implementation steps in sequence
  - File and component touchpoints
  - Test plan outline
  - Migration or schema changes
  - Risk flags
- Hank reviews and approves TDD
- Build execution begins (AI-driven, human-supervised)

**Deliverable:** Approved TDD + working implementation checked into main repo.

**Exit Criteria:** Build complete, passes initial review, ready for testing.

**Human/AI Split:** Human reviews TDD and oversees build. AI drafts, generates code, implements.

---

### Phase 4 — Testing (10% Human / 90% AI)

**Entry Criteria:** Build Draft complete, implementation checked in.

**Work Process:**
- AI runs defined test suite
- Generates test report
- Flags failures, edge cases, regressions
- Human reviews report and approves pass/fail

**Deliverable:** Test report. Feature passes or returns to Build Draft with flagged issues.

**Exit Criteria:** Tests pass. Human sign-off.

**Human/AI Split:** Human reviews and approves. AI executes tests and generates report.

> Note: Specific testing state names in Linear to be defined as this phase matures.

---

### Phase 5 — Launch (50% Human / 50% AI)

**Entry Criteria:** All tests passed. Human sign-off complete.

**Work Process:**
- AI assists with: release notes, documentation updates, deployment steps
- Human executes or approves deployment
- Post-launch monitoring

**Deliverable:** Deployed feature, updated Standing Artifacts, release notes / changelog entry.

**Exit Criteria:** Feature live and stable.

**Human/AI Split:** Human makes go/no-go call and executes deploy. AI handles prep and documentation.

> Note: Specific launch state names in Linear to be defined as this phase matures.

---

### Closed Stages

Features that are complete, cancelled, or deferred:

- `Done` — Successfully launched
- `Cancelled` — Dropped intentionally; reason noted in Linear
- `Deferred` — Paused; may return in a future cycle

No closed feature is deleted. History is preserved.

---

## 4. Standing Artifacts

Always-current documentation that serves as the authoritative input to every build stage. Not one-time deliverables — living documents.

### Artifact Registry

| Artifact | Description | Location |
|---|---|---|
| High Level ERD | Conceptual entity relationship diagram | `/docs/` |
| Detailed ERD | Full ERD with field-level detail | `/docs/` |
| Schema Documentation | Source-of-truth schema definitions | `/functions/schemas` |
| Key Workflow Docs | Narrative + diagram per major workflow | `/docs/` |
| Component List by System | All components organized by system | `/docs/systems/` |
| System Sub-Pages | Per-system: Overview, Config, Automations, etc. | `/docs/systems/<system-name>/` |

### Ownership

- **Ed** owns governance: decides what gets documented, enforces currency
- **Hank** owns content: responsible for keeping artifacts accurate as the system evolves
- **AI agents** assist with updates: draft changes to artifacts when features affect them; humans review before committing

### Currency Rule

A feature cannot advance from Design Spec → Build Candidate until all Standing Artifacts impacted by that feature's design are updated or have a documented plan to be updated at launch.

---

## 5. Weekly Cadence

### Weekly Product Grooming Session

**Frequency:** Weekly (day/time TBD by Ed and Hank)  
**Duration:** 60 minutes  
**Attendees:** Ed, Hank  

**Agenda (in order):**

1. **Seed Review** (20 min)
   - Walk through all features currently in `Seed` state
   - Discuss, update, and groom each one
   - Advance groomed features to `Groomed` state
   - Discard or defer anything that doesn't have legs

2. **Design Candidate Review** (20 min)
   - Assess current design bandwidth for the upcoming week
   - Walk through all `Design Candidate` features
   - Prioritize and mark top features as `Ready for Design`
   - Everything else stays in `Design Candidate`

3. **Pipeline Health Check** (10 min)
   - Quick scan of anything blocked, stalled, or needs a decision
   - Confirm any features ready to move between phases

4. **Misc / Parking Lot** (10 min)
   - New ideas to seed
   - Process improvements to note

**Output:** Updated Linear board. No separate meeting notes required unless a significant decision needs to be documented (in which case, log it as a Linear comment or a decision record).

---

## 6. Linear Setup

### Workflow States

Configure the following states for the Smoking Tigers team in Linear:

| State | Phase | Type |
|---|---|---|
| Seed | Planning | Unstarted |
| Groomed | Planning | Unstarted |
| Design Candidate | Planning | Unstarted |
| Ready for Design | Design | Started |
| Design Spec | Design | Started |
| Build Candidate | Design | Started |
| Prioritized Design | Build | Started |
| Build Draft | Build | Started |
| Testing | Testing | Started |
| Launch | Launch | Started |
| Done | Closed | Completed |
| Cancelled | Closed | Cancelled |
| Deferred | Closed | Cancelled |

### Labels

| Label | Purpose |
|---|---|
| `p1` / `p2` / `p3` / `p4` | Priority |
| `size-s` / `size-m` / `size-l` / `size-xl` | Feature size |
| `t2aos` | Aligned Goal: Transition to Aligned Open Source |
| `mcc` | Aligned Goal: Multi-Channel Comms |
| `a4ht` | Aligned Goal: Architect for High Trust |
| `or` | Aligned Goal: Overall Reliability |
| `security` | Aligned Goal: Information & Data Security |
| `compliance` | Aligned Goal: Compliance |
| `blocked` | Feature is blocked; needs attention |
| `agent-task` | Sub-task generated by an AI agent |

### Projects

Features live in Linear projects that map to product areas or initiatives. Current projects:

- **Trade Like Nick (TLN)**
- **AI Agent Infrastructure**
- **Operations**
- **ST:AI**

The q1 Network build work should live in its own Linear project: **q1 Network**.

### Views to Configure

- **Ideas Board** — all features in Seed / Groomed / Design Candidate, grouped by state
- **Active Design** — features in Ready for Design / Design Spec / Build Candidate
- **Active Build** — features in Prioritized Design / Build Draft / Testing / Launch
- **My Issues** — Ed and Hank personal views

---

## 7. AI Agent Responsibilities

### When Agents Are Invoked

Agents are invoked by Ed or Hank. They do not self-trigger or move features without instruction.

| Stage | Agent Role | Invocation |
|---|---|---|
| Seed | Optional: prose cleanup of descriptions | Ad hoc, on request |
| Groomed | Optional: draft initial Design Scope from Standing Artifacts | On request by Ed or Hank |
| Ready for Design | Draft initial Design Spec | Hank invokes at start of design work |
| Design Spec | Iterate on spec based on feedback | Ongoing during design |
| Build Draft | Draft TDD from approved Design Spec | Hank invokes at start of build |
| Testing | Execute test suite, generate report | Automatic at build complete |
| Launch | Draft release notes, update docs | Hank invokes pre-launch |

### What Agents Always Do After a Feature Launches

1. Update all affected Standing Artifacts
2. Write a changelog entry
3. Close the Linear issue with a summary comment

### What Agents Never Do

- Move a feature to a new state without human confirmation
- Modify the Design Spec after it has been approved
- Deploy to production
- Make priority or scope decisions

---

## 8. Activation Checklist

Use this checklist to deploy the process from scratch.

### Linear Configuration
- [ ] Create `q1 Network` project in Linear under Smoking Tigers team
- [ ] Configure all workflow states listed in Section 6
- [ ] Create all labels listed in Section 6
- [ ] Set up Ideas Board, Active Design, Active Build, and My Issues views
- [ ] Migrate existing scoped features from the Google Doc into Linear with correct states and properties

### Standing Artifacts
- [ ] Confirm High Level ERD exists and is current
- [ ] Confirm Detailed ERD exists and is current
- [ ] Confirm Schema Documentation in `/functions/schemas` is current
- [ ] Confirm Key Workflow Docs exist for all major workflows
- [ ] Confirm `/docs/systems/` index exists with at least stubs for each system
- [ ] Assign Hank as artifact owner; Ed as governance owner

### Grooming Cadence
- [ ] Ed and Hank agree on weekly grooming day/time
- [ ] Recurring calendar event created
- [ ] Meeting format shared with any future attendees

### Initial Feature Seeding
- [ ] All features from the Google Doc scoping document entered into Linear with correct state
- [ ] Priority, Size, and Aligned Goals filled in for all Seed-stage features
- [ ] Design Scopes created for any features already in Groomed state

### Process Comms
- [ ] Ed and Hank both confirm they've read this SOP
- [ ] SOP linked from the main repo README or docs index
- [ ] SOP version-controlled (stored in repo or Notion with edit history)

---

## 9. Appendix

### A. Strategic Goals Reference

| Code | Name | Description |
|---|---|---|
| T2AOS | Transition to Aligned Open Source | Move q1 Network tech stack to values-aligned open source components, one at a time |
| MCC | Multi-Channel Comms | Weave q1 Network into the comms channels people already use; enable fluid movement between platforms |
| A4HT | Architect for High Trust | Make q1 Network a high-trust environment — real people, shared safety and security |
| OR | Overall Reliability | Consistent reliability: quick page loads, low latency, high availability |
| Security | Information & Data Security | Protect member data and system integrity |
| Compliance | Compliance | Meet applicable legal, regulatory, and policy requirements |

### B. Feature Sizing Guide

Sizes are estimates of total effort, combining human and AI work.

| Size | Description | Example |
|---|---|---|
| S | Small — well-understood change, minimal surface area, < 1 day build | Config change, minor UI fix, single-field schema addition |
| M | Medium — clear scope, limited system impact, 1–3 days build | New form flow, API endpoint, moderate UI feature |
| L | Large — significant scope, multiple systems touched, 3–7 days build | New module, major workflow change, multi-table schema work |
| XL | Extra Large — high complexity, broad system impact, 1–3+ weeks build | Full new system, major platform refactor, complex integration |

Sizing is done collaboratively during Seed grooming. When in doubt, size up.

### C. Priority Reference

| Priority | Description |
|---|---|
| P1 | Critical — blocks other work or is an immediate user-facing problem |
| P2 | High — important, should be in the next design/build cycle |
| P3 | Medium — valuable but not urgent |
| P4 | Low — nice to have; may be deferred indefinitely |

### D. Key References

- Main repo: https://github.com/quorum1/q1-home
- QX3 Component DB: https://www.notion.so/quorum1/11f6f6ac689e804b93d0f3ad053f10b5
- QX3 Diagrams: https://docs.google.com/presentation/d/1CS68kFNBH_L7DQPL0wzL1SkZ31Fg9IXf4-YdpqGpxas
- Builder Methods reference: https://buildermethods.com/
- Source meeting notes: https://fathom.video/share/XycwgteXt_pHsk2o8cqpx_xwQb_PqZJG
