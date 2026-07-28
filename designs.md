# Design Decisions — TigerClaws

> Key architectural and product design decisions for this workspace.
> For formal ADRs, see `docs/adr/`. For dated operational decisions, see `decisions/2026/`.
> This file captures lightweight design intent that hasn't yet been formalized.

---

## Agent Architecture

**Session start order is fixed:**
`SOUL.md` → `USER.md` → `AGENTS.md` → `MEMORY.md` → harness file
Rationale: persona loads before context; user preferences load before constraints.

**One identity per harness:**
Each AI provider gets its own config file (`claude.md`, `gemini.md`, `codex.md`).
They all point to the same `AGENTS.md` runtime contract — harness files add only provider-specific behavior.

**USER.md is personal, not shared:**
Each member has their own `USER.md`. There is no shared USER.md.
`USER.template.md` is the portable starting point.

---

## Memory Architecture

Three layers:

| Layer | File(s) | Scope | Written by |
|---|---|---|---|
| Decision log | `MEMORY.md` | Project-level, permanent | Agent (append-only) |
| Session cards | `Memory/YYYY-MM-DD-*.md` | Topic summaries | Agent |
| Dated decisions | `decisions/2026/DEC-*.md` | Operational decisions | Agent / Ed |

ADRs (`docs/adr/`) are formal architectural records — separate from operational decisions.
**Do not merge these layers.**

---

## File Location Rules

| Content type | Where it lives |
|---|---|
| Canonical governance docs | GitHub `edjieun/smoking-tigers-governance` |
| Session outputs / generated docs | Attached to OP work packages |
| Proprietary / financial | Notion (private) |
| Team files / raw media | Google Drive |
| Local working memory | `~/Discovery/` (this folder) — not canonical |

---

## TigerClaw Tier Design

Three tiers — each has different trust/access boundaries:

| Tier | Hardware | Agents | Access |
|---|---|---|---|
| Network | Cloud | OpenRouter, GitHub Actions | Public APIs only |
| On Premise | Mac Mini M4 + M1 | Scout (OpenClaw), ZeroClaw | Full Tailnet + LM Studio |
| On Device | M4 Laptop | Copilot, OpenCode | Interactive sessions only |

On Device agents (Copilot) **do not** have persistent processes — session only.
On Premise agents (Scout) **do** have persistent processes — cron + event-driven.

---

## MCP Server Design

**Portable MCPs** (any member can run these):
- `composio-mcp-server` — stateless, API-key auth, no local data
- `obsidian-mcp-server` — reads local Obsidian vault

**Infrastructure MCPs** (STE On-Premise only):
- `mcp-searxng` — requires SearXNG instance on Mac Mini
- `mcp-crawl4ai-ts` — requires crawl4ai service on Mac Mini

Members using portable MCPs connect their own Composio account.
STE infrastructure MCPs are shared — accessed via Tailscale.

---

## Naming Conventions

| Type | Convention | Example |
|---|---|---|
| ADRs | `ADR-NNN-kebab-description.md` | `ADR-006-agent-task-delegation-tiers.md` |
| Decisions | `DEC-YYYYMMDD-NNN-kebab-description.md` | `DEC-20260303-001-calcom-scheduling-platform.md` |
| Daily notes | `YYYY-MM-DD.md` | `2026-07-28.md` |
| Versioned docs | `YYYY-MM-DD_ProjectCode_Description_vN` | `2026-07-28_TGC_OnePager_v2` |
| OP references | `OP#NNN` | `OP#357` |

---

## Open Design Questions

- [ ] Should `MEMORY.md` be split into personal (Ed) vs. project-level for Drive sharing?
- [ ] How does a new member's agent bootstrap before they have `USER.md` filled in?
- [ ] MCP server discovery: should there be a `mcp-registry.json` listing all available servers?

---

*Last updated: 2026-07-28*
