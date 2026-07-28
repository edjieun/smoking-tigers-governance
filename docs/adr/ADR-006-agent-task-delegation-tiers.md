# ADR-006: Agent Task Delegation Tiers

**Date:** 2026-07-20
**Status:** Draft — In Progress
**Author:** Ed Hwang
**Related WP:** [OP#296 — Day Planning + Task Delegation Across Agent Tiers](https://ste-business-server.tailebe6d3.ts.net:8080/work_packages/296)
**Type:** Architecture Decision Record

---

## Context

STE currently operates using a Human + Copilot + OpenRouter/Sonnet loop for all tasks — the most expensive and attention-intensive configuration. As TigerClaw matures with on-premise and on-device agents, tasks should be delegated to the lowest-cost, most-capable tier that can handle them.

Four tiers exist:
- **Human (Ed)** — judgment, relationships, approvals, creative direction
- **Copilot (On Device / M4 Laptop)** — interactive planning, drafting, analysis, VS Code-integrated work
- **Scout / OpenClaw (On Premise / Mac Mini)** — background automation, OP updates, Mattermost I/O, transcript processing
- **Network / OpenRouter** — heavyweight inference, external API calls, tasks requiring cloud models

Without a delegation policy, all tasks default to Human + Copilot, creating cost and attention overhead.

---

## Decision

*(To be defined — this ADR is a stub pending a dedicated session)*

Define a task classification matrix that maps task types to appropriate tiers. Key categories to address:

1. Routine ops (Mattermost messages, OP updates, heartbeat) → Scout
2. Interactive drafting, planning, analysis → Copilot
3. Judgment calls, approvals, external relationships → Human
4. Heavy inference, large context tasks → OpenRouter (with cost awareness)

---

## Consequences

*(TBD)*

---

## Open Questions

- [ ] What are the trigger conditions for escalating from Scout → Copilot → Human?
- [ ] How does daily planning get initiated? (Copilot morning briefing? Scout heartbeat?)
- [ ] What does the delegation handoff protocol look like in practice?

---

## Next Step

Run `grill-with-docs` skill on this ADR to fully define the decision and consequences.
