# Canonical Knowledge Source Registry

**Last Updated:** 2026-04-17
**Owner:** Ed (Steward)
**Governing Decisions:** DEC-20260324-003, DEC-20260417-001, DEC-20260417-002

---

## Source Registry

| Source | Canonical For | Agent Access Method | Indexed? | Phase |
|---|---|---|---|---|
| OpenClaw workspace | Agent config, memory, SOPs, HEARTBEAT | Always loaded | Yes (memory_search) | Active |
| GitHub (`smoking-tigers-governance`) | Governance decisions, policies, architecture docs | `read` tool + `qmd query` | Yes (QMD `srv`) | Active |
| **Linear** | **Issue tracking, project coordination, agent task audit trail** | **Linear GraphQL API** | **No (live API)** | **Active** |
| Notion (STM teamspace) | Meetings, contributor records, strategic initiatives, financial records | Notion API | Planned Phase 3 | Manual |
| Google Drive (STM folder) | Reports, docs, production assets | Drive API | No | Manual |
| QMD search index | Local hybrid search across all `.md` collections | `qmd query` via exec | Yes | Active |
| Obsidian vault | Human-readable org memory, project context, daily logs | MCP server + QMD | Yes (QMD `obsidian-stm`) | Active |
| Desktop/intake/ | Incoming documents (ephemeral) | Heartbeat / `read` tool | No | Ephemeral |
| `memory/YYYY-MM-DD.md` | Daily agent session logs | memory_search | Yes | Active |
| `MEMORY.md` | Global institutional memory | Always loaded | Yes | Active |
| `memory/shared.md` | Cross-agent operational summaries | Always loaded | Yes | Active |

---

## Source Hierarchy (Conflict Resolution)

When content exists in more than one source, this hierarchy determines truth:

1. **GitHub governance repo** — policy and decisions
2. **Linear** — issue and task state
3. **Notion** — meeting records, contributor data, strategic registry
4. **OpenClaw workspace** — operational agent config
5. **Google Drive** — document artifacts

If a conflict exists between sources, agents flag it rather than resolve silently.

---

## Fragmentation Prevention Rules

**F-1: Single Source of Truth per Content Type**
- Governance decisions → GitHub repo only
- **Issue tracking and task coordination → Linear only** (new)
- Meeting records → Notion only
- Strategic initiative registry → Notion (archive) + Linear (live view)
- Agent configuration → OpenClaw workspace only
- Production assets and reports → Google Drive only

**F-5: Linear as Agent Task Surface** (new)
- AI agents create tasks in Linear, not Notion
- Agent-created issues carry the `agent-task` label
- Notion Exec Team Task Tracker is read-only legacy after 2026-04-17

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
1. `memory_search` (OpenClaw workspace + daily files)
2. `qmd query` — hybrid search across governance repo, project files, and vault
3. **Linear GraphQL API** — issue and project status (when task/project context is needed)
4. Notion API — meetings, contributors, strategic context
5. GitHub governance repo via `read` tool (specific doc after QMD surfaces it)
6. Google Drive API (specific document fetch)
7. If not found after all six → flag as knowledge gap to Scout / Ed

**QMD is step 2. Linear is step 3.**

**Agents must not fabricate answers when information is not retrievable.**

---

## QMD Collections

| Collection | Path | Content |
|---|---|---|
| `srv` | `/Users/edlicious/srv/` | Governance decisions, policies, architecture docs |
| `obsidian-stm` | Smoking Tigers Obsidian vault | Org memory, project notes, daily logs |

**Maintenance scripts:** `~/.openclaw/workspace/scripts/qmd-index.sh` and `qmd-embed.sh`
**Cron:** Daily 3 AM Pacific (`qmd-daily-reindex`)

## Obsidian Vault

**Location:** Google Drive — `q1 Creative/Smoking Tigers/Obsidian/smoking tigers vault`
**MCP server:** `obsidian-mcp-server` in OpenClaw config

**Vault structure:**
```
01-Session-Logs/    — Agent session summaries
02-Knowledge-Base/  — Reference: org overview, systems, tools
03-Projects/        — Active project files with task context
04-Daily-Notes/     — Daily notes (YYYY-MM-DD.md)
openclaw.md         — Agent stack reference
```

**Write rules:**
- V-1: Vault is a synthesis layer — summarize and link, don't replace canonical sources
- V-2: Link, don't copy content
- V-3: YAML frontmatter required on all files
- V-4: Daily notes are ephemeral summaries, not canonical state
- V-5: Project files kept current; stale files marked `status: archived`

## Retrieval Roadmap

| Phase | Task | Status |
|---|---|---|
| Phase 2 | QMD: index governance repo + project files | ✅ Complete (2026-04-17) |
| Phase 2 | Obsidian vault: human-readable memory layer | ✅ Complete (2026-04-17) |
| Phase 3 | Maintain `memory/notion-projects.md` (weekly Notion project summary) | Planned |
