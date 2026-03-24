# DEC-20260324-003 — Knowledge Source Unification: Canonical Sources, Retrieval Gaps, and Fragmentation Policy

**Decision ID:** DEC-20260324-003
**Title:** Knowledge Source Unification — Canonical Sources, Retrieval Gaps, and Fragmentation Policy
**Status:** Approved
**Date:** 2026-03-24
**Owner / Approver:** Ed (Steward)
**Audit Source:** OpenClaw System Audit — 2026-03-24 (Google Doc)

---

## Context

The 2026-03-24 audit identified HIGH fragmentation risk across knowledge sources:

- Knowledge is split across 5+ sources: OpenClaw workspace files, Notion, Google Drive, GitHub governance repo, local intake folder, and daily memory files
- Notion is not indexed — only queryable by direct API call
- Google Drive documents are not in any retrieval pipeline
- GitHub governance docs are not retrievable without a manual `read` tool call
- No unified search exists across these sources
- Agents cannot reliably retrieve information unless they know exactly where to look

This creates operational risk: agents make decisions based on incomplete context, governance docs go unread, and institutional knowledge fragments across tools.

---

## Decision

### 1. Canonical Source Registry

The following source registry defines what each system is canonical for:

| Source | Canonical For | Agent Access | Indexed? |
|---|---|---|---|
| OpenClaw workspace (`~/.openclaw/workspace/`) | Agent config, memory, SOPs, HEARTBEAT | Direct (always loaded) | Yes (memory_search) |
| GitHub (`smoking-tigers-governance`) | Governance decisions, policies, architecture | Read tool (on-demand) | No — see §3 |
| Notion (STM teamspace) | Projects, tasks, meetings, decisions (structured) | Notion API | No — see §3 |
| Google Drive (STM folder) | Docs, media, production assets | Drive API | No — see §3 |
| Desktop/intake/ | Incoming documents for processing | Heartbeat / read tool | No (ephemeral) |
| memory/YYYY-MM-DD.md | Daily agent session logs | memory_search | Yes |
| MEMORY.md | Global institutional memory | Always loaded | Yes |
| memory/shared.md | Cross-agent operational summaries | Always loaded | Yes |

**Duplication rule:** If content exists in more than one source, the hierarchy is:
1. Governance repo (GitHub) — policy/decisions
2. Notion — project/task/meeting state
3. OpenClaw workspace files — operational config
4. Google Drive — document artifacts

When a conflict exists, the higher-ranked source takes precedence. Agents must flag conflicts rather than resolve them silently.

### 2. Fragmentation Prevention Rules

Agents must follow these rules to prevent knowledge fragmentation:

**Rule F-1: Single Source of Truth per Content Type**
- Governance decisions → GitHub repo only (not also in Notion notes or Google Docs)
- Project status → Notion Strategy DB only
- Agent config → OpenClaw workspace only
- Production assets → Google Drive only

**Rule F-2: No Redundant Copies**
- Agents must not create duplicate records across systems
- If content must reference something in another system, use a URL link — do not copy content

**Rule F-3: Notion as Structured Project/Task Store**
- Notion is the canonical store for: projects, tasks, meetings, decisions (structured DB records)
- Prose documents belong in Google Drive or GitHub — not in Notion page bodies
- Notion page bodies may contain a summary + link to the canonical doc, not the full content

**Rule F-4: Google Drive for Document Artifacts**
- Reports, briefs, audit packets, production docs → Google Drive (Smoking Tigers folder)
- Notion project entries link to Drive docs, not the other way around

### 3. Retrieval Gap Resolution (Phased)

The following gaps must be addressed in priority order:

#### Phase 1 — Immediate (Manual-access acceptable)
- GitHub governance repo: Scout reads on-demand using `read` tool when governance context is needed
- Google Drive docs: Scout fetches on-demand using Drive API when a doc is referenced
- **No indexing required** — document these as manual-access paths

#### Phase 2 — Short-term (knowledge-ops builds retrieval)
- Add GitHub governance repo to knowledge-ops indexing pipeline
  - Target: knowledge-ops ingests governance `/decisions/2026/` and `/policies/` on nightly run
  - Output: indexed chunks available via memory_search
- Add Google Drive document listing to knowledge-ops context
  - Target: knowledge-ops maintains a `memory/drive-index.md` updated weekly with doc titles and URLs
  - Does not require full-text indexing — URL registry is sufficient for now

#### Phase 3 — Medium-term (structured retrieval)
- Notion project DB: knowledge-ops pulls active projects weekly and writes summary to `memory/notion-projects.md`
- This makes project context available via memory_search without a live API call each time

### 4. Agent Behavior Rules for Knowledge Retrieval

When an agent needs information and is unsure where it lives:
1. Check `memory_search` first (workspace + daily files)
2. If not found: check Notion via API (projects, tasks, meetings)
3. If not found: check GitHub governance repo via `read` tool
4. If not found: check Google Drive index or fetch specific doc
5. If not found after all four: surface to Scout / flag to Ed as a knowledge gap

Agents must not fabricate answers when information is not retrievable. Flag unknown = unknown.

---

## Rationale

- Fragmentation across 5+ sources is the root cause of inconsistent agent behavior
- A canonical source registry eliminates ambiguity about where truth lives
- Phased retrieval gap resolution is practical — Phase 1 costs nothing, Phase 2 is low-effort, Phase 3 is built over time
- Duplication prevention rules are the highest-leverage intervention: stop the problem from growing

---

## Implementation

| Task | Owner | Target |
|---|---|---|
| Publish canonical source registry to workspace (`docs/knowledge-sources.md`) | Scout | 2026-03-25 |
| Add fragmentation rules to AGENTS.md | Scout | 2026-03-28 |
| knowledge-ops: add governance repo ingestion to nightly run | knowledge-ops | 2026-04-07 |
| knowledge-ops: create and maintain `memory/drive-index.md` | knowledge-ops | 2026-04-07 |
| knowledge-ops: add Notion project summary to weekly run | knowledge-ops | 2026-04-14 |

---

## Change History

| Date | Change | Author |
|------|--------|--------|
| 2026-03-24 | Initial draft and approval | Scout / Ed |
