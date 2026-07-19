# Tool Schema: OpenClaw
**Type:** Schema Document — Descriptive Only
**Created:** 2026-03-25
**Owner:** Ed (Steward)
**Status:** Draft

---

## Overview

OpenClaw is the AI agent runtime platform that orchestrates all STM agents. It runs on the Mac Mini, manages agent lifecycles, handles channel integrations (Mattermost, Discord, iMessage), and provides the workspace environment for all agent operations.

---

## Deployment

- **Host:** Mac Mini M4 (edlicious-server)
- **OS:** macOS (Darwin 25.3.0, arm64)
- **Install path:** `/opt/homebrew/lib/node_modules/openclaw/`
- **Config file:** `~/.openclaw/openclaw.json`
- **Gateway:** `127.0.0.1:18789` (loopback only — not publicly exposed)
- **Node version:** v25.6.1
- **Runtime model (default):** `openrouter/anthropic/claude-sonnet-4.6`

---

## Workspace Structure

```
~/.openclaw/workspace/               ← Global agent workspace
├── AGENTS.md                        — Agent runtime rules
├── SOUL.md                          — Scout persona and principles
├── IDENTITY.md                      — Scout role definition
├── MEMORY.md                        — Global institutional memory
├── USER.md                          — Ed's profile and preferences
├── TOOLS.md                         — Local tool configuration
├── HEARTBEAT.md                     — Periodic task definitions
├── TASKS.md                         — Active task backlog
├── DECISIONS_INDEX.md               — Decision log index
├── docs/                            — Reference and schema documents
├── memory/                          — Daily session logs + shared agent memory
│   ├── YYYY-MM-DD.md                — Daily logs (per agent)
│   └── shared.md                    — Cross-agent operational summary
├── agents/                          — Per-agent workspaces
│   ├── ea/                          — Executive Assistant
│   ├── sysops/                      — System Operations
│   ├── governance-ops/              — Governance Operations
│   ├── knowledge-ops/               — Knowledge Operations
│   ├── sergeant-at-arms/            — Sergeant at Arms
│   ├── basil-ea/                    — Basil's EA
│   ├── christine-ea/                — Christine's EA (Rosie)
│   ├── van-ea/                      — Van's EA
│   └── update-log.md                — Agent activity log
├── decisions/                       — Formal decision records
├── policies/                        — Policy documents
├── governance/                      — Governance artifacts
├── architecture/                    — System architecture docs
├── workflows/                       — Operational workflows
├── scripts/                         — Utility scripts
├── skills/                          — Custom skills (GitHub skill lives here)
├── knowledge-ops/                   — Knowledge pipeline artifacts
├── finance/                         — Financial records
├── projects/                        — Active project artifacts
├── logs/                            — System logs
└── _incoming/                       — Document intake staging area
```

---

## Agent Registry

| Agent ID | Name | Model | Workspace | Mattermost Bot | Discord Bot |
|----------|------|-------|-----------|---------------|-------------|
| `main` | Scout (Chief of Staff) | claude-sonnet-4.6 | `~/.openclaw/workspace/` | @st-build-cos-bot | None |
| `ea` | Executive Assistant (Eva) | claude-sonnet-4.6 | `agents/ea/` | @st-build-ea-bot | EA bot (`exec-ed`) |
| `sysops` | System Operations | claude-sonnet-4.6 | `agents/sysops/` | @st-build-sysops-bot | None |
| `governance-ops` | Governance Operations | claude-sonnet-4.6 | `agents/governance-ops/` | @st-build-governance-ops-bot | None |
| `knowledge-ops` | Knowledge Operations | claude-sonnet-4.6 | `agents/knowledge-ops/` | @st-build-knowledge-ops-bot | None |
| `sergeant-at-arms` | Sergeant at Arms | — | `agents/sergeant-at-arms/` | @st-build-saa-bot | None |
| `basil-ea` | Basil's EA | — | `agents/basil-ea/` | — | basil-ea bot |
| `christine-ea` | Christine's EA (Rosie) | — | `agents/christine-ea/` | @rosie | christine-ea bot |
| `van-ea` | Van's EA | — | `agents/van-ea/` | — | van-ea bot |

**Max concurrent agents:** 4  
**Max concurrent subagents per session:** 2

---

## Model Configuration

### Ollama (Local — `http://127.0.0.1:11434`)

| Model | Tag | Context Window | Purpose |
|-------|-----|----------------|---------|
| Qwen 2.5 14B | `qwen2.5:14b-instruct` | 32,768 | Scout default (local) |
| Qwen 2.5 7B | `qwen2.5:7b-instruct` | 32,768 | Specialist agents |
| Qwen 2.5 3B | `qwen2.5:3b-instruct` | 32,768 | Mechanical tasks |
| nomic-embed-text | `nomic-embed-text:latest` | — | Embeddings (memory search) |

### OpenRouter (Cloud)

| Alias | Provider Model | Use |
|-------|---------------|-----|
| `openrouter/anthropic/claude-sonnet-4.6` | Anthropic Claude | All active agents (current default) |
| `openrouter/auto` | Auto-selected | Available |

---

## Channel Integrations

| Channel | Status | Scope |
|---------|--------|-------|
| Mattermost | ✅ Active | All STM agents — primary internal surface |
| Discord | ✅ Active (limited) | EA in #exec-ed only; other bots inactive |
| iMessage | ⚠️ Disabled | Configured, not enabled |
| Notion (via EA) | ✅ Active | EA reads/writes Notion via API |
| Google Drive (via EA) | ✅ Active | EA reads/writes via service account |

---

## Memory Architecture

| Layer | File(s) | Scope | Loaded By |
|-------|---------|-------|-----------|
| Global institutional memory | `MEMORY.md` | All agents | Always loaded |
| Cross-agent shared memory | `memory/shared.md` | All agents | Always loaded |
| Daily session logs | `memory/YYYY-MM-DD.md` | Per session | Loaded at start |
| Agent-specific memory | `agents/{id}/memory/` | Per agent | Agent-specific |

**Memory search:** Hybrid vector + text (nomic-embed-text, Ollama)  
**Temporal decay:** Enabled (30-day half-life)  
**Compaction mode:** `safeguard` (flush at 4,000 tokens soft threshold)

---

## Skills Available

| Skill | Location | Purpose |
|-------|----------|---------|
| apple-notes | `openclaw/skills/apple-notes/` | Apple Notes via `memo` CLI |
| apple-reminders | `openclaw/skills/apple-reminders/` | Apple Reminders via `remindctl` |
| coding-agent | `openclaw/skills/coding-agent/` | Delegate to Codex/Claude Code |
| clawhub | `openclaw/skills/clawhub/` | Install/publish skills from ClawHub |
| github | `workspace/skills/github/` | `gh` CLI — issues, PRs, API |
| openai-whisper | `openclaw/skills/openai-whisper/` | Local speech-to-text |
| peekaboo | `openclaw/skills/peekaboo/` | macOS UI capture/automation |
| video-frames | `openclaw/skills/video-frames/` | Extract frames/clips via ffmpeg |

---

## Key External Credentials

| Service | Location | Scope |
|---------|----------|-------|
| Notion API token | `agents/ea/auth.json` | EA + christine-ea (shared) |
| Google Drive service account | `~/.openclaw/credentials/` | EA |
| GitHub `gh` CLI | System (`~/.config/gh/`) | Scout only |
| Anthropic API | `openclaw.json` | All agents via OpenRouter |
| Discord bot tokens | `openclaw.json` | Per-agent |
| Mattermost bot tokens | `openclaw.json` | Per-agent |

---

## How It Connects to Other Tools

| Tool | Connection | Direction |
|------|-----------|-----------|
| Mattermost | Native integration — all agents bound | Bidirectional |
| Discord | Native integration — EA bound to #exec-ed | Bidirectional |
| Notion | EA agent via API token | Bidirectional |
| GitHub | Scout via `gh` CLI | Bidirectional (with instruction) |
| Google Drive | EA via service account | Bidirectional |

---

## STM vs. Q1 Distinction

| Dimension | STM | Q1 |
|-----------|-----|----|
| Scope | All STM agent operations | OpenClaw is not a Q1 tool |
| Access | Ed (admin), agents via tokens | No Q1 access to this instance |
| Data residency | Mac Mini (local + iCloud) | Separate |

*OpenClaw is fully STM-scoped. Q1 does not use or have access to this instance.*

---

## Known Gaps / Open Items

- Gateway runs on loopback only — no remote management interface
- `@sonnetops-bot` present in Mattermost but not mapped to a configured agent
- `basil-ea` and `van-ea` agents have Discord tokens but no workspace or channel configuration
- `sergeant-at-arms` agent not fully configured
- GitHub token not provisioned for EA or governance-ops (read-only Phase 2 item)
- No formal backup/restore procedure for OpenClaw config or workspace
- iMessage integration disabled — pending decision on activation
- Mac Mini DHCP not reserved — service disruption risk if IP changes

---

## Canonical Role

> OpenClaw is the **AI agent runtime and orchestration layer**. It is the operating system for the agent network. Everything else (Mattermost, Notion, GitHub, Discord) is a surface or data layer that OpenClaw agents interact with.
