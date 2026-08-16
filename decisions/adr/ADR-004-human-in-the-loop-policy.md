# ADR-004: Human-in-the-Loop Policy

**Date:** 2026-02-25
**Status:** Draft — Pending Steward Review
**Author:** Ed Hwang
**Type:** Architecture Decision Record

---

## Context

AI agents operate across all STE functions. Without a clear
authority model, agents risk taking consequential actions
without human oversight. This ADR establishes the universal
policy governing what agents can do autonomously, what requires
human approval, and what is never autonomous.

---

## Decision

STE operates a human-in-the-loop model for all consequential
decisions. Agents execute, track, and enforce. Humans decide,
approve, and override.

**Agents never replace human judgment. They remove process
burden so humans can focus on what only humans can do.**

---

## Authority Classes

### Class A — Autonomous
Agents may act without prior human approval.

Permitted:
- Reading and classifying documents
- Health monitoring and status reporting
- Generating summaries and draft content
- Running embeddings and indexing
- Sending notifications and reminders
- Executing pre-approved cron jobs
- Restarting pre-approved services (allowlist only)
- Logging work and tracking activity

### Class B — Propose Only
Agents may prepare and propose. Humans approve before execution.

Requires approval:
- File moves, renames, or reorganization
- Classification changes to governed documents
- Knowledge base structural updates
- Archive decisions
- Governance document updates
- RevPoints eligibility recommendations
- Conflict resolution proposals
- New contributor access

### Class C — Never Autonomous
Agents may never perform these actions under any circumstance.

Prohibited:
- Issuing RevPoints
- Approving or finalizing governance decisions
- Committing or pushing to GitHub governance repos
- Signing or executing agreements
- Deleting source files
- Modifying the CCA or core policy documents
- Taking punitive action against contributors
- Overriding Steward decisions
- Acting on policy not in the governance repo

---

## Escalation Protocol

### 🟢 Green — Nominal
Agents proceed autonomously within Class A authority.
Log actions. No human notification required.

### 🟡 Amber — Attention Needed
Agents complete Class A actions, prepare Class B proposals,
notify relevant human. Human approves or redirects.
Agents do not wait indefinitely — escalate to Scout if
no response within defined window.

### 🔴 Red — Immediate Escalation
Agents stop all autonomous action beyond containment.
Escalate to Scout and Steward immediately.
Document the situation. Wait for human instruction.

---

## Override Policy

Humans may override any agent action or recommendation.
Overrides are logged to the governance record.
Agents accept overrides without resistance.
Repeated override patterns are flagged to Steward for
policy review — the agent configuration, not the human,
is adjusted.

---

## Privacy and Data Policy

All processing happens on owner-controlled infrastructure.
No organizational data leaves the local system without
explicit Steward authorization.
No agent connects to external services without instruction.
Sensitive content (private tier) requires 14b model and
logged access.

---

## Consequences

- Every agent file must specify its authority class per action
- Agents that exceed their authority class trigger a 🔴 red
  escalation to Scout
- Authority classes are reviewed when agent scope changes
- This policy supersedes any agent-level configuration that
  grants broader authority

---

## Related

- ADR-001: STE AI Agent Architecture
- ADR-002: Four Pillars Agent Mapping
- ADR-003: RevPoints Compliance Chain
- Agent Authority Matrix (governance policy docs)
