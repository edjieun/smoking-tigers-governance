# Canonical Knowledge Source Registry

**Last Updated:** 2026-03-24
**Owner:** Ed (Steward)
**Governing Decision:** DEC-20260324-003

---

## Source Registry

| Source | Canonical For | Agent Access Method | Indexed? | Phase |
|---|---|---|---|---|
| OpenClaw workspace | Agent config, memory, SOPs, HEARTBEAT | Always loaded | Yes (memory_search) | Active |
| GitHub (`smoking-tigers-governance`) | Governance decisions, policies, architecture docs | `read` tool (on-demand) | Planned Phase 2 | Manual |
| Notion (STM teamspace) | Projects, tasks, meetings, structured records | Notion API | Planned Phase 3 | Manual |
| Google Drive (STM folder) | Reports, docs, production assets | Drive API / `memory/drive-index.md` | Planned Phase 2 | Manual |
| Desktop/intake/ | Incoming documents (ephemeral) | Heartbeat / `read` tool | No | Ephemeral |
| `memory/YYYY-MM-DD.md` | Daily agent session logs | memory_search | Yes | Active |
| `MEMORY.md` | Global institutional memory | Always loaded | Yes | Active |
| `memory/shared.md` | Cross-agent operational summaries | Always loaded | Yes | Active |

---

## Source Hierarchy (Conflict Resolution)

When content exists in more than one source, this hierarchy determines truth:

1. **GitHub governance repo** — policy and decisions
2. **Notion** — project/task/meeting state
3. **OpenClaw workspace** — operational agent config
4. **Google Drive** — document artifacts

If a conflict exists between sources, agents flag it rather than resolve silently.

---

## Fragmentation Prevention Rules

**F-1: Single Source of Truth per Content Type**
- Governance decisions → GitHub repo only
- Project/task status → Notion Strategy DB only
- Agent configuration → OpenClaw workspace only
- Production assets and reports → Google Drive only

**F-2: No Redundant Copies**
- Do not copy content between systems — use URL links instead
- Notion page bodies contain summary + link to canonical doc, not full content

**F-3: Notion for Structured Records**
- Projects, tasks, meetings, decisions as structured DB records
- Prose and reports belong in Google Drive or GitHub

**F-4: Google Drive for Document Artifacts**
- Reports, briefs, audit packets, production docs → Google Drive (Smoking Tigers folder)
- Notion project entries link to Drive docs

---

## Agent Retrieval Order

When an agent needs information and is unsure where it lives:
1. `memory_search` (workspace + daily files)
2. Notion API (projects, tasks, meetings)
3. GitHub governance repo via `read` tool
4. Google Drive index (`memory/drive-index.md`) or direct doc fetch
5. If not found → flag as knowledge gap to Scout / Ed

**Agents must not fabricate answers when information is not retrievable.**

---

## Retrieval Roadmap

| Phase | Task | Owner | Target |
|---|---|---|---|
| Phase 2 | Index GitHub governance decisions/policies in nightly run | knowledge-ops | 2026-04-07 |
| Phase 2 | Maintain `memory/drive-index.md` (weekly Drive doc listing) | knowledge-ops | 2026-04-07 |
| Phase 3 | Maintain `memory/notion-projects.md` (weekly Notion project summary) | knowledge-ops | 2026-04-14 |
