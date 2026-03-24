# Policy — Agent Memory Management

**Status:** Approved v1.0
**Owner:** Ed (Steward)
**Applies To:** All ST:AI agents operating under OpenClaw
**Last Updated:** 2026-03-24
**Governing Decisions:** DEC-20260324-001, DEC-20260324-002, DEC-20260303-006

---

## Purpose

Define how agents read, write, and manage memory — including memory tiers, boundaries, compaction, deduplication, and session-close discipline. This policy replaces informal memory behavior with explicit, auditable rules.

---

## Memory Tiers

### Tier 1 — Private Memory
- Path: `~/.openclaw/workspace/agents/<agent-id>/memory/`
- Readable by the owning agent only
- Stores agent-specific operational context: SOP notes, per-principal context, active task state
- No other agent reads or writes private memory without explicit delegation

### Tier 2 — Shared Memory
- Files: `memory/shared.md`, `memory/notion-projects.md`, `memory/drive-index.md`
- Readable by all agents at session start
- Written by knowledge-ops (nightly/weekly digest) only
- Agents propose additions — they do not write directly

### Tier 3 — Global Memory
- File: `MEMORY.md`
- Append-only by agents (no agent may edit or delete entries without Ed's explicit approval)
- Represents durable institutional knowledge: decisions, key context, permanent references
- knowledge-ops may propose new entries; Scout surfaces them to Ed

---

## Compaction and Archive

- Daily memory files (`memory/YYYY-MM-DD.md`) older than **90 days** are moved to `memory/archive/YYYY/` during each knowledge-ops nightly run
- No automatic deletion — archive files are preserved indefinitely unless Ed explicitly approves deletion
- Archive deletions older than 1 year may be proposed by Scout with Ed approval

---

## Deduplication

- knowledge-ops compares recent daily files against MEMORY.md during each nightly run
- Duplicate or near-duplicate entries are flagged in `memory/dedup-report-YYYY-MM-DD.md`
- Scout reviews dedup reports and proposes MEMORY.md edits for Ed's approval
- No automatic edits to MEMORY.md — human approval gate always applies

---

## Session-Close Discipline

Sub-agents and spawned sessions that produce durable findings must follow a checkpoint protocol before session end:

1. Write a brief `## Session Summary` to the session log or daily memory file, OR
2. Return a structured summary to Scout for Scout to write to the daily memory file

Scout is responsible for ensuring sub-agent findings reach durable memory before the session ends.

**Applies to:** ea, sysops, knowledge-ops, christine-ea, van-ea, basil-ea, and all future agent spawns.

---

## Agent Memory Assignments

| Agent | Private Memory | Reads | Writes |
|---|---|---|---|
| Scout | None | MEMORY.md, shared.md, daily files, all workspace config | Daily files (via knowledge-ops), MEMORY.md (Ed-approved) |
| ea (Eva) | `agents/ea/memory/` | Scout context, workspace config, Notion | Notion (external), private memory |
| sysops | `agents/sysops/memory/` | Scout context, workspace config | System logs, private memory |
| knowledge-ops | None | All session logs, all memory files | daily files, shared.md, archive, dedup reports |
| christine-ea | `agents/christine-ea/memory/` | Scout context (delegated), private memory | Private memory only |
| van-ea | `agents/van-ea/memory/` | Scout context (delegated), private memory | Private memory only |
| basil-ea | `agents/basil-ea/memory/` | Scout context (delegated), private memory | Private memory only |

---

## What Agents Must Never Do

- Write to MEMORY.md without Ed approval
- Write to another agent's private memory directory
- Retain principal-specific context (Ed's personal data, Christine's data, etc.) outside the owning agent's private memory
- Skip the session-close checkpoint when durable findings exist
- Fabricate answers when information is not retrievable — flag unknown = unknown

---

## Enforcement

- Scout audits memory health on-demand or during quarterly reviews
- knowledge-ops dedup reports surface drift automatically
- Ed retains final authority over MEMORY.md and archive deletion

---

## Review Cadence

- Review after any memory pipeline failure or stale shared.md detection
- Review when adding new agents
- Quarterly review of MEMORY.md for staleness (Ed-led)
