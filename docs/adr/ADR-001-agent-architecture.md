# ADR-001: STE AI Agent Architecture

**Date:** 2026-02-25
**Status:** Draft — Pending Steward Review
**Author:** Ed Hwang
**Type:** Architecture Decision Record

---

## Context

Smoking Tigers Enterprises requires an AI operating system to
coordinate contributors, enforce governance, manage knowledge,
and support human decision-making across all STE enterprises.

This ADR establishes the foundational agent architecture for that
system.

---

## Decision

STE will operate a multi-agent AI system organized into functional
teams. Each team is led by a 7b orchestrator agent supported by
3b specialist agents for mechanical tasks.

**Governance git is the operating system.** All agents read from
the governance repository as their source of truth. No agent acts
on policy not committed to the governance repo.

---

## Agent Leads

### Scout — Chief of Staff
Primary orchestrator. Coordinates all agent leads. Routes tasks,
manages heartbeat intake, escalates to Steward on consequential
decisions.

### Sergeant At Arms — Governance & Compliance
Enforces governance in practice. Tracks contributor work, verifies
process compliance, protects cultural integrity. Governance-Ops
reports to Sarge as his intelligence arm.

### XP Lead — Contributor Experience
Owns the full contributor lifecycle. Onboarding, training, cultural
health, engagement, conflict escalation.

### SysOps — Infrastructure & Operations
Monitors all services and hardware. Traffic light protocol:
green/amber/red escalation. Manages model loading and service health.

### KnOps — Knowledge Management
Processes, curates, and surfaces knowledge. Manages document intake,
chunking, embedding, indexing, and retrieval. Operates structured
knowledge libraries.

### EA — Executive Assistant
Manages human coordination layer. Calendar, meetings, tasks,
reminders, and Notion maintenance.

### FinOps — Financial Operations
Manages RevPoints issuance and reconciliation based on governance
git. Never issues RevPoints without full compliance chain.

### Legal Lead — Contracts & Agreements
Manages all legal documents. CCA compliance, contributor agreements,
IP assignments, partnership deals.

### Job Board Lead — Job Lifecycle Management
Operates contributor job board based on governance git. Every job
has defined inputs, outputs, compensation, and RevPoints attached.

### Production Lead — Creative Operations
Pre-processes raw content so human editors focus on creative
judgment and quality gating.

### IP Registry Lead — IP Record Keeping
Maintains canonical record of all IP created across STE. Connects
artifacts to contributors, jobs, and RevPoints.

### Research & Intelligence Lead
Monitors market signals, competitor activity, and opportunities.
Produces intelligence reports for Scout and Steward.

### Client Success Lead
Manages client experience. Onboarding, health monitoring, advocacy.

### Comms Lead — TBD
Internal and external communications. Scope to be defined.

### Growth Lead — TBD
Business development and partnerships. Scope to be defined.

---

## Model Tier Policy

| Tier | Model | Use |
|------|-------|-----|
| 3b | qwen2.5:3b-instruct | Mechanical tasks — no reasoning |
| 7b | qwen2.5:7b-instruct | Orchestration, light reasoning |
| 14b | qwen2.5:14b-instruct | Complex reasoning — on-demand only |

Hardware constraint: Never run 14b and 7b simultaneously.

---

## Consequences

- All agent leads require entries in the gateway configuration
- All agents read governance git before acting on policy
- No agent may approve, finalize, or commit governance decisions
- Human-in-the-loop required for all consequential actions
- Privacy-first: all processing on owner-controlled infrastructure

---

## Related

- ADR-002: Four Pillars Agent Mapping
- ADR-003: RevPoints Compliance Chain
- ADR-004: Human-in-the-Loop Policy
