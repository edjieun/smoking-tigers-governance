# ADR-003: RevPoints Compliance Chain

**Date:** 2026-02-25
**Status:** Draft — Pending Steward Review
**Author:** Ed Hwang
**Type:** Architecture Decision Record

---

## Context

RevPoints are the contributor compensation mechanism across STE
enterprises. Accurate issuance requires verified work, documented
output, and governance compliance. Without a defined chain,
RevPoints cannot be issued accurately and the contributor economy
breaks down.

---

## Decision

No RevPoints are issued without the full compliance chain
completing successfully. Every step is verified by a designated
agent. No step can be skipped or bypassed.

---

## The Chain

```
1. Job Board Verifier confirms output
   ↓
2. Sarge Tracker logs effort and hours
   ↓
3. IP Registry Registrar logs artifact
   ↓
4. Sergeant At Arms verifies governance compliance
   ↓
5. FinOps RevPoints Engine issues RP
   ↓
6. FinOps Ledger records transaction
   ↓
7. Governance git updated
```

---

## Step Definitions

### Step 1 — Output Confirmation
Job Board Verifier confirms the deliverable exists, matches the
job specification, and meets minimum quality requirements.
No subjective quality judgment — mechanical verification only.

### Step 2 — Effort Logging
Sarge Tracker records hours logged, effort documented, and
contributor activity against the specific job. Must be traceable
to a job ID, a contributor, and a time period.

### Step 3 — IP Registration
IP Registry Registrar logs the artifact created — what it is,
who created it, what job it came from, and what enterprise it
belongs to. Establishes provenance before compensation.

### Step 4 — Governance Compliance
Sergeant At Arms verifies the contributor followed prescribed
workflow, onboarding is complete, no open violations exist,
and no conflicts are unresolved. Issues compliance clearance.

### Step 5 — RP Issuance
FinOps RevPoints Engine issues the RevPoints based on the
job's defined RP band from the governance repo. Issues only
after receiving compliance clearance from Step 4.

### Step 6 — Ledger Recording
FinOps Ledger records the transaction — contributor, amount,
job, enterprise, date, and chain verification status.

### Step 7 — Governance Update
Governance git updated with the completed transaction record.
Creates the auditable trail.

---

## Failure Handling

If any step fails:
- Chain stops at the failing step
- Sarge notifies contributor of what is missing
- No RP issued until chain completes
- Disputes escalated to Scout and Steward

---

## Authority

- Agents verify. Agents do not decide.
- FinOps issues RP. No other agent issues RP.
- Sarge clears compliance. No other agent clears compliance.
- Steward is final authority on disputed issuance.

---

## Consequences

- All job completions must flow through this chain
- No manual RP issuance outside this chain without
  Steward authorization and governance record
- Chain applies to all STE enterprises and all
  contributor types

---

## Related

- ADR-001: STE AI Agent Architecture
- ADR-004: Human-in-the-Loop Policy
- Collective Contribution Agreement (CCA)
- RevPoints Allocation Policy
