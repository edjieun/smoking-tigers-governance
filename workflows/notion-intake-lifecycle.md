# Workflow — Notion Intake Lifecycle (Fix & Upgrade)

**Status:** Draft v1.0
**Owner:** Ed (Steward)
**Last Updated:** 2026-03-02
**Applies To:** Ed (Steward), knowledge-ops agent, OpenClaw pipeline

---

## Objective

Ed exports the Notion teamspace as a zip to the Smoking Tigers Google Drive folder.
OpenClaw ingests that export, processes it into structured knowledge, updates its memory,
and checks each project against activation eligibility criteria.

**Google Drive constraint:** Drive is too large to store locally. It stays in the cloud.
OpenClaw manages knowledge via memory files and indexed artifacts — not local Drive mirrors.

---

## Intake Lifecycle Model

```
EXPORT (Ed)
  → Google Drive: Smoking Tigers / Notion Exports / incoming/
      → Ed signals Scout via Mattermost: "Notion export ready — [date]"

PICKUP (Scout / knowledge-ops)
  → Scout triggers knowledge-ops with export path
  → knowledge-ops downloads zip from Drive to ~/Desktop/intake/
  → Extracts to notion-exports/extracted/[BATCH-ID]/

CLASSIFY (knowledge-ops)
  → Parse all pages/databases
  → Identify content types: projects, databases, meeting notes, tasks, docs
  → Build Batch Import Plan (see below)
  → Flag restricted content (financials, PII, legal drafts)
  → Post plan to #knowledge for Scout/Ed review

HUMAN REVIEW (Ed or Scout)
  → Review batch import plan in #knowledge
  → Approve, reject, or modify proposed CRUD operations
  → Explicitly approve any database writes

PROCESS (knowledge-ops, post-approval)
  → Update project knowledge files per approval
  → Write/update RAG memory artifacts (project knowledge bibles)
  → Check each project against activation eligibility (see below)
  → Write activation status report to governance repo
  → Post completion summary to #knowledge

ARCHIVE
  → Move extracted zip to notion-exports/completed/[BATCH-ID]/
  → Log to agents/update-log.md
```

---

## Trigger Logic

| Trigger | Action |
|---------|--------|
| Ed posts "Notion export ready — [date]" in #executive or #knowledge | Scout kicks off intake via knowledge-ops |
| File appears in ~/Desktop/intake/ matching `notion-export*.zip` | knowledge-ops HEARTBEAT picks it up |
| Manual Scout command in #executive | Scout spawns knowledge-ops with explicit path |

**Note:** No silent automation. Every intake cycle is Ed-initiated.

---

## Database Write Logic

### Which Hub?
All structured data writes target the governance repo as canonical record.
Notion is the working UI — not the system of record.

| Content Type | Write Target | Authority Required |
|-------------|-------------|-------------------|
| Project status updates | `projects/[project]/index.md` | Scout (auto, low-risk) |
| Project knowledge bibles | `knowledge-bible/[project]-bible.md` | Scout (propose → Ed approves) |
| Activation status | `projects/[project]/activation-status.md` | Scout (auto, based on criteria) |
| New decisions | `decisions/YYYY/DEC-[date]-[slug].md` | Ed explicit approval |
| RP / financial data | Restricted — EA handles, not knowledge-ops | Ed explicit approval |
| Policy updates | `policies/[domain]/` | Ed explicit approval always |

### Which Tables (Notion)?
knowledge-ops does not write back to Notion directly.
All Notion state changes are proposed → Ed executes manually in Notion UI.

---

## Required Properties for Activation Eligibility

A project is eligible for activation only when ALL of the following are present and documented:

### Tier 1 — Foundation (Minimum)
- [ ] Vision document — complete, locked
- [ ] Market analysis — complete
- [ ] Business Model Canvas — complete
- [ ] SWOT / SOAR — complete

### Tier 2 — Economic Structure
- [ ] RevPoints budget framework — defined (total RP, RPM bands, recovery cap)
- [ ] Cash structure — defined (initial cash need, source, timeline)
  - **No project activates without both RP AND cash structure documented**
- [ ] Rev Token Purchase Agreement — executed (or in-flight with named investor)
- [ ] Recovery pool % and cap — specified

### Tier 3 — Governance
- [ ] Project Activation Agreement — drafted (Creator + STM)
- [ ] Creator Partnership Agreement — drafted or executed
- [ ] IP ownership — explicitly documented
- [ ] Role assignments — at least Driver and Approver named (DACI)

### Tier 4 — Operational Readiness
- [ ] Job board — at least 3 atomic jobs defined
- [ ] Contributor activation plan — who, what role, what RP offer
- [ ] Project knowledge bible — initial draft exists in governance repo

**Activation gate:** Steward (Ed) must explicitly approve activation.
knowledge-ops flags eligibility — it does not activate projects.

---

## Governance Constraints

- **No project activates without RP + cash structure.** Both must be documented.
  RP-only or cash-only is insufficient — the dual-currency model requires both.

- **knowledge-ops proposes — Ed decides.** Activation eligibility reports are advisory.
  No agent can mark a project as active.

- **Restricted data stays restricted.** RP ledgers, RTPA details, financial projections
  go through EA, not knowledge-ops. knowledge-ops flags their presence in exports; does not process them.

- **Delete = radioactive.** No Notion data is deleted from governance records without Ed's
  explicit approval. knowledge-ops may archive; never delete.

- **Drive stays in cloud.** knowledge-ops downloads only the specific export zip to process.
  No bulk Drive sync. No local Drive mirrors.

---

## RAG Memory Model

OpenClaw manages knowledge through memory files, not live Drive access.

| Artifact | Location | Updated By | When |
|----------|----------|-----------|------|
| Project knowledge bible | `knowledge-bible/[project]-bible.md` | knowledge-ops | Each intake cycle |
| Project index | `projects/[project]/index.md` | knowledge-ops | Each intake cycle |
| Daily memory digest | `memory/YYYY-MM-DD.md` | knowledge-ops (nightly cron) | Every night |
| Long-term memory | `MEMORY.md` | knowledge-ops | When durable facts arise |
| Drive index | `ste-index.md` (workspace) | knowledge-ops | When Drive structure changes |

Google Drive content is referenced by index, not loaded wholesale.
knowledge-ops pulls only what it needs per job.

---

## Batch Import Plan (Required Output per Intake)

Each Notion export batch must produce:

```
Batch ID: YYYY-MM-DD_notion-export_[scope]_v[n]
Export timestamp:
Source scope: (which Notion spaces / pages / databases)
Content types found:
  - Projects: [list]
  - Databases: [list]
  - Meeting notes: [count]
  - Other: [list]
Detected changes vs last batch:
Proposed CRUD operations:
  - CREATE: [items]
  - UPDATE: [items]
  - ARCHIVE: [items]
  - RESTRICTED (EA only): [items]
Activation eligibility checks:
  - [Project]: [ELIGIBLE / NOT ELIGIBLE / PARTIAL — missing: X, Y]
Restricted content flagged:
Ambiguities / conflicts:
Recommended next steps:
```

---

## Failure Modes to Avoid

- Treating exports as self-executing instructions
- Silently updating governance repo without Ed review
- Processing RP / financial data without EA involvement
- Activating projects without Steward sign-off
- Downloading Drive contents beyond the specific export zip
- Conflating "eligible" with "approved for activation"
- Stale batch plans (always check if Notion state changed after export)

---

## Open Items (as of 2026-03-02)

- [ ] Ed's message cut off at "RP/cash structure" — confirm no additional constraints beyond what's captured here
- [ ] Drive folder path for export drops not yet confirmed — Ed to specify exact Drive folder name/path
- [ ] Download mechanism for Drive → local intake not yet built (manual for now; automation TBD)
- [ ] ste-index.md (Drive index) not yet built
- [ ] EA Notion Finance DB setup not yet complete (RP ledger, income tracking, RP→cash)

---

## Review Cadence

Review after:
- First successful end-to-end intake cycle
- Any project reaches activation eligibility
- Drive folder structure changes
- EA Notion Finance DBs go live
