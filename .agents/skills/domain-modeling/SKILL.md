---
name: domain-modeling
description: A structured interview for defining the entities, relationships, lifecycle states, governance boundaries, and OpenProjects schema mapping for a system or project. Used as a sub-skill within grill-with-docs or standalone when designing a new domain.
---

# domain-modeling — Skill Instructions

## Purpose
Produce a precise domain model: the core objects in a system, how they relate,
what their lifecycle looks like, and how they map to OpenProjects work package types.

## When to use this skill
- Designing a new project's data model
- Answering "what are the things in this system?"
- Mapping a domain to a database schema or OP structure
- Before writing ADRs or SOPs for a complex system

---

## Step 1 — Identify core entities

Ask: "What are the main *things* in this system?"

For each entity, capture:
- **Name** (canonical — no synonyms)
- **Definition** (one sentence — precise)
- **Avoid** (synonyms that must not be used)

Push for precision. "Data" is not an entity. "Transcript" — a raw text artifact produced by a meeting — is an entity.

---

## Step 2 — Map relationships

For each pair of entities that interact, define:
- **Direction:** A → B (one-way) or A ↔ B (bidirectional)
- **Cardinality:** one-to-one, one-to-many, many-to-many
- **Verb:** what the relationship *does* (produces, belongs to, extracts, assigns)

Example:
```
Meeting → has one → Transcript
Transcript → produces many → Tasks
Task → assigned to one → Member
Member → belongs to many → Projects
```

---

## Step 3 — Define lifecycle states

For each entity that changes over time, define its states:

```
[Entity]: state1 → state2 → state3
           ↓ on what event      ↓ on what event
```

Example:
```
Task: New → In Progress → Done
           ↓ assigned     ↓ completed
           → On Hold      → Rejected
```

---

## Step 4 — Define governance boundaries

Ask: "Where does human approval become required?"

For each boundary, record:
- **Action** (what the agent wants to do)
- **Requires human approval:** yes/no
- **Reason** (why human is required)

Example:
```
Agent writes GitHub commit → Requires human approval (governance record)
Agent creates OP work package → No approval needed (operational task)
Agent records LedgerSMB entry → Requires human approval (financial record)
```

---

## Step 5 — Map entities to OpenProjects types

For each entity, define how it maps to an OP work package:

| Entity | OP Type | Parent WP | Tag | Notes |
|---|---|---|---|---|
| Phase | Summary task (3) | Project | — | Named "PHASE X.Y — ..." |
| Meeting | Milestone (2) | Project | — | Links to Transcript |
| Transcript | Task (1) | Meeting milestone | — | Source URL in description |
| Task (extracted) | Task (1) | Transcript WP | — | Assigned to Member |
| Decision | Task (1) | Transcript WP | `decision` | — |
| Open Question | Task (1) | Transcript WP | `open-question` | — |
| ADR/SOP doc | Task (1) | Phase | `doc:adr` or `doc:sop` | Links to file |

Adapt this table for the specific domain being modeled.

---

## Step 6 — Assign TigerClaw tiers

For each entity or component, assign a tier:
- **Network** — cloud, external APIs, Tailscale, OpenRouter
- **On Premise** — Mac Mini services, M1 services, local inference, agents
- **On Device** — M4 Laptop apps, Obsidian, Copilot, OpenCode

---

## Output

Produce a domain model document:

```markdown
# Domain Model — [System Name]
Date: [YYYY-MM-DD]

## Entities
| Entity | Definition | Avoid |
|---|---|---|
| ... | ... | ... |

## Relationships
[entity diagram or table]

## Lifecycle States
[per entity]

## Governance Boundaries
[table]

## OpenProjects Mapping
[adapted table from Step 5]

## TigerClaw Tier Assignments
[per entity/component]
```

This document feeds directly into the ADR in `grill-with-docs` Step 3.
