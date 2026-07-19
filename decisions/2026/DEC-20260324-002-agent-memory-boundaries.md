# DEC-20260324-002 — Agent Memory Boundaries: Private, Shared, and Handoff Rules

**Decision ID:** DEC-20260324-002
**Title:** Agent Memory Boundaries — Private, Shared, and Handoff Rules
**Status:** Approved
**Date:** 2026-03-24
**Owner / Approver:** Ed (Steward)
**Audit Source:** OpenClaw System Audit — 2026-03-24 (Google Doc)

---

## Context

The 2026-03-24 audit found that no agent — including the four EA agents — has defined memory boundaries. Currently:

- ea (Eva) has no private memory file; all context lives in Scout's session
- christine-ea is deployed but has no memory definition at all
- van-ea and basil-ea do not exist yet
- No rules specify what is private vs shared vs handoff-eligible memory for any agent
- Agents writing to shared memory (MEMORY.md, shared.md) have no guardrails

This creates risk of context leakage between agents, stale shared memory, and confusion about what each agent "knows" across sessions.

---

## Decision

### Memory Tier Definitions

All agents in the ST:AI system operate under a three-tier memory model:

#### Tier 1 — Private Memory
- Files readable only by the assigned agent
- Location: `~/.openclaw/workspace/agents/<agent-id>/memory/`
- Content: agent-specific operational context, SOP notes, per-principal context
- Not shared with other agents unless explicitly exported to Tier 2 or 3
- Only the owning agent writes to its private memory

#### Tier 2 — Shared Memory (Cross-Agent Read)
- Files: `memory/shared.md` (and future `memory/executive-shared.md`)
- Readable by all agents at session start
- Written by: knowledge-ops (nightly digest) only
- Agents may *propose* additions to shared memory but do not write directly
- Proposals routed through Scout → knowledge-ops digest

#### Tier 3 — Global Memory (Human-Curated)
- File: `MEMORY.md`
- Append-only by agents (no agent may edit or delete existing entries without Ed approval)
- Knowledge-ops may propose new MEMORY.md entries; Scout surfaces them to Ed
- Entries represent durable institutional knowledge, not session logs

---

### Per-Agent Memory Assignment

#### Scout (main)
- Reads: MEMORY.md, memory/shared.md, memory/YYYY-MM-DD.md, all workspace config
- Writes: memory/YYYY-MM-DD.md (via nightly knowledge-ops), MEMORY.md (Ed-approved appends only)
- Private memory: None (Scout is orchestration layer — its context is the global context)

#### ea (Eva)
- Reads: Scout session context, workspace config, Notion (external)
- Writes: Notion (Meetings DB, ExecDB) — external store as EA memory
- Private memory: `agents/ea/memory/` — for Ed-specific EA context (scheduling patterns, follow-up state)
- Handoff: summarize active EA items to Scout at end of delegated session

#### sysops (Doug)
- Reads: Scout session context, workspace config
- Writes: system logs, optional `agents/sysops/memory/` for infrastructure state
- Private memory: `agents/sysops/memory/` — for runtime state, known issues, infra notes
- Stateless sessions acceptable for most tasks; persistent memory only for infrastructure continuity items

#### knowledge-ops
- Reads: all session JSONL logs, all memory files
- Writes: `memory/YYYY-MM-DD.md`, `memory/shared.md`, `memory/dedup-report-*.md`, `memory/archive/`
- Private memory: None — knowledge-ops is the memory pipeline, not an operational agent
- Must not write to MEMORY.md without proposing via Scout + Ed approval

#### christine-ea
- Reads: Scout context (via delegation), `agents/christine-ea/memory/`
- Writes: `agents/christine-ea/memory/` (Christine-specific context only)
- Private memory: `agents/christine-ea/memory/` — Christine's preferences, active tasks, channel state
- Handoff: deliver structured summary to Scout when delegated tasks complete
- Scope: Christine Francis personal/organizational support — not general STM knowledge

#### van-ea (when deployed)
- Reads: Scout context, `agents/van-ea/memory/`
- Writes: `agents/van-ea/memory/` (Van-specific context only)
- Private memory: `agents/van-ea/memory/`
- Scope: Van exec coordination and community growth support

#### basil-ea (when deployed)
- Reads: Scout context, `agents/basil-ea/memory/`
- Writes: `agents/basil-ea/memory/` (Basil-specific context only)
- Private memory: `agents/basil-ea/memory/`
- Scope: Basil creative leadership support, VP-style workflow support

---

### Cross-Agent Handoff Protocol

When Scout delegates work to a sub-agent, the delegation must include:
1. **Task scope** — what the sub-agent is being asked to do
2. **Context passed** — what Scout is sharing from global memory for this task
3. **Memory boundary** — what the sub-agent should NOT retain privately (e.g., Ed's personal details)

When a sub-agent returns, it must provide:
1. **Findings / outcome summary** (structured, not raw session log)
2. **Any durable items** that should be written to memory (flagged for Scout to write)
3. **Status** of any Notion/Drive/Calendar changes made

Scout is responsible for writing durable sub-agent findings into the day's memory file.

---

## Rationale

- Private memory prevents EA agents from leaking principal-specific context to other agents
- Clear write authority prevents multiple agents from overwriting each other's memory
- Handoff protocol prevents the most common source of context loss (sub-agent work that never makes it to durable memory)
- Global memory (MEMORY.md) human-gate prevents agent drift from accumulating in the institutional record

---

## Implementation

| Task | Owner | Target |
|---|---|---|
| Create `agents/ea/memory/` directory + README | Scout | 2026-03-25 |
| Create `agents/sysops/memory/` directory + README | Scout | 2026-03-25 |
| Create `agents/christine-ea/memory/` directory + README | Scout | 2026-03-25 |
| Add memory boundary instructions to each agent's AGENTS.md | Scout | 2026-03-28 |
| Add handoff protocol to ea, sysops, knowledge-ops HEARTBEAT | Scout | 2026-03-28 |
| Create van-ea + basil-ea memory dirs (when bot tokens received) | Scout | On deployment |

---

## Change History

| Date | Change | Author |
|------|--------|--------|
| 2026-03-24 | Initial draft and approval | Scout / Ed |
