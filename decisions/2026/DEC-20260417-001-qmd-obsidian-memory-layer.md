# DEC-20260417-001 — QMD Search Index and Obsidian Vault Adopted as Active Memory Layer

**Decision ID:** DEC-20260417-001
**Title:** QMD Search Index and Obsidian Vault Adopted as Active Memory Layer
**Status:** Approved
**Date:** 2026-04-17
**Owner / Approver:** Ed (Steward)
**Supersedes / Amends:** DEC-20260324-003 (extends Phase 2 retrieval gap resolution)

---

## Context

DEC-20260324-003 established a canonical source registry and a phased plan to close retrieval gaps. Phase 2 targeted indexing the GitHub governance repo and Google Drive via knowledge-ops.

On 2026-04-17, two additional memory infrastructure components were deployed:

1. **QMD (Quick Markdown Search)** — a local hybrid vector + BM25 search engine, installed at `/opt/homebrew/bin/qmd` and configured with indexed collections. This closes the Phase 2 governance repo and project file retrieval gap with full-text + semantic search across all `.md` files.

2. **Obsidian Vault (Smoking Tigers Vault)** — a structured knowledge vault stored in Google Drive (`q1 Creative/Smoking Tigers/Obsidian/smoking tigers vault`), connected to OpenClaw via an MCP server. The vault serves as a human-readable, agent-writable knowledge base for organizational memory, project context, and daily session logs.

Both systems are now active and are added to the canonical source registry.

---

## Decision

### 1. QMD Search Index — Canonical Local Search Layer

QMD is adopted as the canonical local search layer for all Markdown content across active collections.

**Collections registered:**

| Collection | Path | Content Type | Files |
|---|---|---|---|
| `srv` | `/Users/edlicious/srv/` | Governance decisions, policies, architecture docs, q1 governance | ~200 |
| `obsidian-stm` | Smoking Tigers Obsidian vault | Organizational memory, project notes, daily logs | Grows over time |

**Embedding model:** `hf:ggml-org/embeddinggemma-300M-GGUF/embeddinggemma-300M-Q8_0.gguf` (local, via Ollama)

**Search capability:** Hybrid BM25 + vector similarity with reranking (`qmd query`)

**Maintenance:**
- Daily re-index: `~/.openclaw/workspace/scripts/qmd-index.sh` (runs `qmd update`)
- Daily re-embed: `~/.openclaw/workspace/scripts/qmd-embed.sh` (runs `qmd embed`, requires Ollama)
- Scheduled cron: 3:00 AM Pacific daily (OpenClaw cron job `qmd-daily-reindex`)

**Agent access:** Scout and all agents can invoke `qmd query "<query>"` via the `exec` tool to perform hybrid search across all indexed collections.

### 2. Obsidian Vault — Human-Readable Organizational Memory

The Smoking Tigers Obsidian vault is adopted as the canonical human-readable layer for organizational memory. It is agent-writable and human-readable.

**Location:** Google Drive shared drive — `q1 Creative/Smoking Tigers/Obsidian/smoking tigers vault`

**Local filesystem path:** `~/Library/CloudStorage/GoogleDrive-ed.hwang@quorum.one/Shared drives/q1 Creative/Smoking Tigers/Obsidian/smoking tigers vault`

**MCP Server:** `obsidian-mcp-server` configured in OpenClaw (`mcp.servers.obsidian`), pointed at vault path

**Vault Structure:**
```
01-Session-Logs/    — Agent session summaries (future)
02-Knowledge-Base/  — Reference docs: org overview, systems, tools
03-Projects/        — Active project files with task lists and context
04-Daily-Notes/     — Daily session notes (YYYY-MM-DD.md)
openclaw.md         — OpenClaw agent stack reference
```

**Write authority:** Scout (Chief of Staff) writes to the vault. Other agents may write with Scout's delegation. Ed may write directly.

**Canonical content in vault:**
- Organizational overview and leadership
- Active project context with linked Linear issues
- System reference docs (Linear, GitHub, OpenClaw)
- Daily session logs synthesized from agent activity
- ExecDB task summaries (pulled from Notion)

**Write rules:**
- **V-1: Vault is a synthesis layer** — Vault notes summarize and link to canonical sources; they do not replace them. Governance decisions remain in GitHub; tasks remain in Notion; code remains in GitHub.
- **V-2: Link, don't copy** — Use wikilinks and external URLs rather than duplicating content.
- **V-3: Frontmatter required** — All vault files must include YAML frontmatter with `tags` and `updated` fields.
- **V-4: Daily notes are ephemeral summaries** — `04-Daily-Notes/YYYY-MM-DD.md` documents what happened and what's open, not canonical state.
- **V-5: Project files reflect current state** — `03-Projects/` files are kept current as projects evolve. Stale project files must be marked `status: archived`.

### 3. Updated Source Registry

The canonical source registry from DEC-20260324-003 is extended:

| Source | Canonical For | Agent Access | Indexed? | Phase |
|---|---|---|---|---|
| OpenClaw workspace | Agent config, memory, SOPs, HEARTBEAT | Always loaded | Yes (memory_search) | Active |
| GitHub (`smoking-tigers-governance`) | Governance decisions, policies, architecture | `read` tool + QMD search | Yes (QMD `srv` collection) | **Active** |
| Notion (STM teamspace) | Projects, tasks, meetings (structured records) | Notion API | Planned Phase 3 | Manual |
| Google Drive (STM folder) | Reports, docs, production assets | Drive API | No | Manual |
| **QMD index** | **Local hybrid search across all `.md` collections** | **`qmd query` via exec** | **Yes** | **Active** |
| **Obsidian vault** | **Human-readable org memory, project context, daily logs** | **MCP server + QMD** | **Yes (QMD `obsidian-stm`)** | **Active** |
| Desktop/intake/ | Incoming documents (ephemeral) | Heartbeat / `read` tool | No | Ephemeral |
| `memory/YYYY-MM-DD.md` | Daily agent session logs | memory_search | Yes | Active |
| `MEMORY.md` | Global institutional memory | Always loaded | Yes | Active |
| `memory/shared.md` | Cross-agent operational summaries | Always loaded | Yes | Active |

### 4. Updated Agent Retrieval Order

When an agent needs information and is unsure where it lives:

1. `memory_search` (OpenClaw workspace + daily files)
2. `qmd query` — hybrid search across governance repo, project files, and vault
3. Notion API (projects, tasks, meetings)
4. GitHub governance repo via `read` tool (for specific doc retrieval after QMD surfaces it)
5. Google Drive API (specific document fetch)
6. If not found after all five → surface to Scout / flag to Ed as a knowledge gap

**QMD is now step 2** in the retrieval order, before direct Notion API calls. This closes the Phase 2 governance indexing gap.

### 5. Maintenance Responsibilities

| Task | Owner | Frequency |
|---|---|---|
| `qmd update` (re-index) | Scout (automated cron) | Daily 3 AM |
| `qmd embed` (re-embed) | Scout (automated cron) | Daily 3 AM |
| Vault project files updated | Scout | When project state changes |
| Vault daily notes written | Scout | On significant session activity |
| Vault ExecDB sync | Scout | Weekly or on major task updates |
| Add new QMD collections | Ed / Scout | As new content sources are added |

---

## Rationale

- QMD closes the Phase 2 retrieval gap defined in DEC-20260324-003 — governance docs and project files are now semantically searchable without requiring agents to know exact paths
- The Obsidian vault provides a human-readable organizational memory layer that both agents and humans can read and write, bridging the gap between agent-only memory (OpenClaw workspace) and structured tool-specific data (Notion, GitHub)
- Both components are privacy-preserving and local-first: QMD runs on-device via Ollama, and the vault is stored in the STM Google Drive rather than a third-party service
- The combination of QMD + vault + existing memory_search gives agents three complementary retrieval paths: exact workspace recall, semantic search, and structured API calls

---

## Implementation (Completed 2026-04-17)

| Task | Status |
|---|---|
| Install QMD at `/opt/homebrew/bin/qmd` | ✅ Complete |
| Register `srv` collection (`/Users/edlicious/srv/`) | ✅ Complete |
| Register `obsidian-stm` collection (vault path) | ✅ Complete |
| Initial embed: 259 chunks from 91 documents | ✅ Complete |
| Write `qmd-index.sh` and `qmd-embed.sh` maintenance scripts | ✅ Complete |
| Create daily cron job (`qmd-daily-reindex`, 3 AM Pacific) | ✅ Complete |
| Deploy Obsidian MCP server in OpenClaw config | ✅ Complete |
| Initialize vault structure (4 folders, 10 seed files) | ✅ Complete |
| Populate vault: org overview, projects, ExecDB, GitHub, Linear, daily log | ✅ Complete |
| Update `docs/knowledge-sources.md` | ✅ Complete (this PR) |

---

## Change History

| Date | Change | Author |
|---|---|---|
| 2026-04-17 | Initial draft and approval | Scout / Ed |
