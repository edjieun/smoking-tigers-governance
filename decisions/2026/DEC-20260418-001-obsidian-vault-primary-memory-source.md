# DEC-20260418-001 — Obsidian Vault Established as Primary Memory Source for All Agents

**Decision ID:** DEC-20260418-001
**Title:** Obsidian Vault Established as Primary Memory Source for All Agents
**Status:** Approved
**Date:** 2026-04-18
**Owner / Approver:** Ed (Steward)
**Amends:** DEC-20260324-003, DEC-20260417-001, DEC-20260417-002

---

## Context

Following the adoption of QMD (DEC-20260417-001) and Linear (DEC-20260417-002), the Smoking Tigers Obsidian vault has been established as a live, agent-writable knowledge base. The vault is:

- Stored in Google Drive (`q1 Creative/Smoking Tigers/Obsidian/smoking tigers vault`)
- Versioned in GitHub (`edjieun/stm-obsidian-vault`)
- Indexed in QMD (`obsidian-stm` collection)
- Connected to OpenClaw via `obsidian-mcp-server`
- Synced via `obsidian-git` plugin (auto-commit + push every 10 min)

With the vault now functioning as a full knowledge layer, the following cleanup is required across GitHub, Notion, and Google Drive to eliminate fragmentation and establish the vault as the primary memory source for all agents.

---

## Decision

### 1. Obsidian Vault is Primary Agent Memory

The vault is the canonical source for all agent-readable organizational memory:

- Organizational overview and leadership context
- Active project context (with links to Linear issues)
- System reference documentation (tool schemas, infrastructure map)
- Standard operating procedures
- Daily session logs
- Finance schemas and reference

**All agents read from the vault first.** The vault is writable by Scout and delegated agents.

### 2. GitHub (`smoking-tigers-governance`) — Scope Narrowed

The governance repo scope is narrowed to:

**KEEP (governance artifacts only):**
- `decisions/` — formal governance decisions
- `policies/` — operational policies
- `charters/` — org charter
- `architecture/` — system architecture docs
- `agreements/` — formal agreements
- `DECISIONS_INDEX.md`, `README.md`, `LICENSE`

**MOVED TO VAULT (already copied):**
- `docs/tool-schema-*.md` → vault `05-Systems/`
- `docs/infrastructure-map.md` → vault `05-Systems/`
- `docs/ai-agent-org-chart.md` → vault `05-Systems/`
- `docs/ea-pipeline.md` → vault `06-SOPs/`
- `docs/knowledge-channel-sop.md` → vault `06-SOPs/`
- `docs/smoking-tigers-calendar-sop.md` → vault `06-SOPs/`
- `docs/sop-file-intake-mattermost.md` → vault `06-SOPs/`
- `docs/governance-overview.md` → vault `06-SOPs/`
- `docs/governance-sync.md` → vault `06-SOPs/`
- `architecture/agent-registry.md` → vault `05-Systems/`

**KEEP IN WORKSPACE (operational, not governance):**
- `scripts/` — utility scripts
- `skills/` — agent skills
- `finance/` — RevPoint records
- `projects/` — project artifacts
- `SOUL.md`, `IDENTITY.md`, `AGENTS.md`, `HEARTBEAT.md`, `TOOLS.md`, `USER.md`

### 3. Notion — Scoped to Structured Records Only

Notion remains canonical for transactional/structured data only:

**KEEP (structured records):**
- Exec Team Task Tracker (legacy reference; new tasks → Linear)
- Meetings database
- STE Initiatives DB (strategic registry)
- RevPoints Ledger
- Smoking Tigers Team (contributor directory)
- Content Kanban / Video Process
- Decisions database
- Expenses & T&E

**CLEAN UP (redundant with vault):**
- Smoking Tigers Documents — individual important docs are now referenced via vault wikilinks; no new prose documents should be created here
- Agent Activity Log → vault `04-Daily-Notes/` + Linear `agent-task` issues
- LLM Models DB → vault `05-Systems/` reference

**Rule:** Notion prose documents are frozen. New prose content goes to the vault or Google Drive. Notion is for structured records only.

### 4. Google Drive — Unchanged Role

Google Drive remains canonical for:
- Production assets (video, audio, graphics)
- Reports and external documents
- Meeting recordings
- Financial documents (contracts, invoices)

**New rule:** For Drive documents that agents need to reference, a corresponding vault note is created that summarizes the doc and links to it by URL. Agents do not fetch Drive docs directly unless performing a specific task.

### 5. Updated Vault Structure

```
00-INDEX.md             — Vault index and source map
01-Session-Logs/        — Agent session summaries
02-Knowledge-Base/      — Org overview, system references
03-Projects/            — Active project context (linked to Linear)
04-Daily-Notes/         — Daily session logs (YYYY-MM-DD.md)
05-Systems/             — Tool schemas, infrastructure, agent registry
06-SOPs/                — Standard operating procedures
07-Finance/             — RevPoint schema, finance reference
openclaw.md             — OpenClaw agent stack reference
```

### 6. Updated Agent Retrieval Order

1. **Vault** (`obsidian-stm` QMD collection or MCP server) — primary memory
2. `memory_search` — OpenClaw workspace daily files and MEMORY.md
3. `qmd query` — broader search across all indexed collections (`srv` + `obsidian-stm`)
4. **Linear GraphQL API** — issue and project status
5. Notion API — meetings, contributors, financial records
6. GitHub governance repo via `read` tool — specific policy/decision lookup
7. Google Drive API — specific document fetch
8. If not found → flag as knowledge gap

**The vault is now step 1.** This reflects that agents should find org context, project state, system references, and SOPs in the vault before querying external APIs.

### 7. Updated Canonical Source Registry

| Source | Canonical For | Agent Access | Indexed? | Phase |
|---|---|---|---|---|
| **Obsidian vault** | **All org memory, project context, system reference, SOPs, daily logs** | **MCP server + QMD `obsidian-stm`** | **Yes** | **Active — Primary** |
| OpenClaw workspace | Agent config, HEARTBEAT, daily session files | Always loaded | Yes (memory_search) | Active |
| GitHub (`smoking-tigers-governance`) | Governance decisions, policies, charters | `read` tool + QMD `srv` | Yes | Active |
| Linear | Issue tracking, project coordination, agent task audit | Linear GraphQL API | No (live) | Active |
| Notion | Meetings, contributors, financial records (structured DBs) | Notion API | No | Manual |
| Google Drive | Production assets, reports, recordings | Drive API | No | Manual |
| QMD (`srv`) | Full-text + semantic search across governance + workspace | `qmd query` | Yes | Active |
| `memory/YYYY-MM-DD.md` | Daily agent session files | memory_search | Yes | Active |
| `MEMORY.md` | Global institutional memory | Always loaded | Yes | Active |

---

## Rationale

- The vault provides a single, readable, writable, versioned knowledge layer that all agents can use without API calls
- Scoping GitHub to governance artifacts eliminates the confusion between "governance docs" and "operational reference docs"
- Freezing Notion prose documents prevents the re-fragmentation that DEC-20260324-003 was designed to stop
- Vault-first retrieval reduces API calls and latency for common agent queries

---

## Implementation (Completed 2026-04-18)

| Task | Status |
|---|---|
| Initialize git in vault, push to `edjieun/stm-obsidian-vault` | ✅ |
| obsidian-git v2.38.2 installed and configured | ✅ |
| Vault folders created: 05-Systems, 06-SOPs, 07-Finance | ✅ |
| Tool schemas migrated to vault `05-Systems/` | ✅ |
| SOPs migrated to vault `06-SOPs/` | ✅ |
| Finance schema migrated to vault `07-Finance/` | ✅ |
| `00-INDEX.md` written | ✅ |
| Update `docs/knowledge-sources.md` | ✅ (this PR) |
| DECISIONS_INDEX.md updated | ✅ (this PR) |
| Commit vault changes to `stm-obsidian-vault` | Pending — auto-commit via obsidian-git |

---

## Change History

| Date | Change | Author |
|---|---|---|
| 2026-04-18 | Initial draft and approval | Scout / Ed |
