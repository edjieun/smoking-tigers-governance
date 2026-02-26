# ADR-002: Four Pillars Agent Mapping

**Date:** 2026-02-25
**Status:** Draft — Pending Steward Review
**Author:** Ed Hwang
**Type:** Architecture Decision Record

---

## Context

STE operates according to the Four Pillars framework. This ADR
establishes how the AI agent organization maps to each pillar,
ensuring the agent system reinforces rather than fragments the
organizational model.

---

## Decision

Every agent lead serves one or more of the Four Pillars. The
pillars compound only when all four are operational. The agent
system is designed to support all four simultaneously.

---

## Pillar Mapping

### Pillar 1 — Strategy & Structure
*The foundation before anything else can hold.*

Agents: KnOps, FinOps, Legal Lead, IP Registry,
Research & Intelligence

KnOps is the historian and librarian at AI scale. FinOps is the
bookkeeper at AI scale. Together they make organizational data
structured, searchable, and actionable — creating the data room
that supports every investor, partner, and governance conversation.

"You need a historian, a librarian, a bookkeeper — but at a scale
that only technology can handle. That's where the AI layer comes in."

### Pillar 2 — Network & Access
*The connections that take years to build — available from day one.*

Agents: XP Lead, Job Board Lead, Client Success Lead, Growth Lead

The atomic unit of the network is a defined job role with inputs,
outputs, compensation, and RevPoints attached. Job Board Lead
operates this atomic unit at scale. XP Lead ensures every
contributor who enters the network understands the culture and
is set up to succeed.

### Pillar 3 — Story & Narrative
*The story that makes the work visible and worth joining.*

Agents: Production Lead, Comms Lead

Production Lead pre-processes all raw content so human editors
focus purely on creative judgment and quality gating. Comms Lead
manages the external story — communications, press, and community
programs.

### Pillar 4 — Execution & Operations
*The layer that converts interest into outcomes.*

Agents: Scout, SysOps, Sergeant At Arms, EA

Scout coordinates everything. SysOps keeps the machines running.
Sarge ensures people and agents operate the way STE said they
would. EA manages the human coordination layer.

---

## Data as Connective Tissue

Each pillar generates data:
- Pillar 1 generates financial data, legal records, projections
- Pillar 2 generates relationship data, market intelligence
- Pillar 3 generates content, audience data, narrative feedback
- Pillar 4 generates operational data, contributor records

The agent system connects these data streams. KnOps indexes and
retrieves across all pillars. The governance repo holds the
decisions that shape all four.

---

## Failure Mode Prevention

The most common failure in values-aligned organizations is strong
Pillars 2 and 3 alongside underdeveloped Pillars 1 and 4.

The agent system is specifically designed to prevent this:
- KnOps and FinOps strengthen Pillar 1 continuously
- Sarge and SysOps strengthen Pillar 4 continuously
- All four pillars receive agent support from day one

---

## Consequences

- New agents must be assigned to one or more pillars at creation
- Pillar coverage should be reviewed when adding agent leads
- Gaps in pillar coverage are governance risks, not just
  operational gaps

---

## Related

- ADR-001: STE AI Agent Architecture
- ADR-003: RevPoints Compliance Chain
- ADR-004: Human-in-the-Loop Policy
- Smoking Tigers — The Four Pillars (internal document)
