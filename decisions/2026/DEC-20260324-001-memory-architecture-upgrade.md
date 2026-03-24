# DEC-20260324-001 — Memory Architecture Upgrade: Compaction, Deduplication, and Session Boundary Discipline

**Decision ID:** DEC-20260324-001
**Title:** Memory Architecture Upgrade — Compaction, Deduplication, and Session Boundary Discipline
**Status:** Approved
**Date:** 2026-03-24
**Owner / Approver:** Ed (Steward)
**Supersedes / Amends:** DEC-20260303-006 (extends; does not replace)
**Audit Source:** OpenClaw System Audit — 2026-03-24 (Google Doc)

---

## Context

The 2026-03-24 system audit identified three structural gaps in the current memory architecture (DEC-20260303-006):

1. **No compaction or archive pipeline** — daily memory files accumulate indefinitely. DEC-006 approved a 90-day rolling archive in policy, but the archive step was never implemented in the knowledge-ops nightly job.
2. **No deduplication** — MEMORY.md and daily `memory/YYYY-MM-DD.md` files contain overlapping content. No deduplication pass runs at any point.
3. **No session-close → memory write discipline** — sub-agents and spawned sessions end without a defined checkpoint. Context from sub-agent work is frequently lost unless Scout manually narrates findings into a later session.

These gaps cause memory fragmentation, unbounded file growth, and unreliable context continuity.

---

## Decision

### 1. Archive Compaction — Implemented in Knowledge-Ops Nightly Run

The existing 90-day rolling archive policy (DEC-006) is confirmed and **must now be implemented** in the knowledge-ops nightly job:

- During each nightly run, knowledge-ops checks `memory/` for daily files older than 90 days
- Eligible files are moved to `memory/archive/YYYY/` (not deleted)
- knowledge-ops logs any files moved in that night's completion message to `#executive`
- Archive deletion requires explicit Ed (Steward) approval — no automatic deletion

**Target:** First implementation by 2026-04-01.

### 2. Deduplication Pass

A deduplication check is added to the knowledge-ops nightly run:

- Compare recent daily memory files against MEMORY.md
- Flag (but do not auto-delete) entries in MEMORY.md that are verbatim or near-verbatim duplicates of entries already in daily files
- Produce a brief `memory/dedup-report-YYYY-MM-DD.md` when duplicates are found
- Scout reviews dedup reports and proposes MEMORY.md edits for Ed's approval

MEMORY.md remains **append-only by agents** unless Ed explicitly approves an edit or deletion.

### 3. Session-Close → Memory Checkpoint Protocol

All sub-agents and spawned sessions that produce durable findings must follow a checkpoint protocol:

**Required for sub-agents that:**
- write files
- query or update external services (Notion, Drive, Calendar)
- make decisions or document findings

**Checkpoint format (minimum):**
At session end, the sub-agent must either:
(a) Write a brief `## Session Summary` block to its session log or daily memory file, OR
(b) Return a structured summary to Scout for Scout to write to `memory/shared.md` or the daily file

**Scout responsibility:**
After receiving sub-agent results, Scout must ensure any durable findings are written to the current day's memory file before the session ends.

**This protocol applies to:** ea, sysops, knowledge-ops, christine-ea, and any future agent spawns.

---

## Rationale

- Memory compaction was approved in DEC-006 but never built — this decision activates it
- Deduplication reduces noise in MEMORY.md and makes memory_search more reliable
- Session checkpoint discipline prevents the most common cause of context loss: sub-agent work that never makes it to durable memory
- All changes are conservative — archive-not-delete, flag-not-purge, checkpoint-not-force-write

---

## Implementation Targets

| Task | Owner | Target |
|---|---|---|
| Implement archive compaction in knowledge-ops nightly job | knowledge-ops / sysops | 2026-04-01 |
| Add dedup pass to nightly job | knowledge-ops | 2026-04-07 |
| Update knowledge-ops HEARTBEAT.md with new steps | Scout | Immediate |
| Write session checkpoint protocol into all agent AGENTS.md files | Scout | 2026-03-28 |
| Verify nightly job running and healthy | sysops | 2026-03-25 |

---

## Tradeoffs / Risks

- Dedup report adds a small nightly overhead — acceptable
- MEMORY.md dedup is proposal-only (human gate) — low risk of accidental data loss
- Checkpoint protocol requires sub-agents to have well-scoped session end behavior — may need iteration

---

## Change History

| Date | Change | Author |
|------|--------|--------|
| 2026-03-24 | Initial draft and approval | Scout / Ed |
