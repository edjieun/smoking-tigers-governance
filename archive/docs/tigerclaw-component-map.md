---
title: TigerClaw Component Map
status: Active (living doc)
last-updated: 2026-07-19
op_task: https://ste-business-server.tailebe6d3.ts.net:8080/projects/ste-ai-buildout/work_packages/253
tier: All
---

# TigerClaw Component Map

> One document. Every running component. Who / What / Where / Why / How.
> Updated whenever a component is added, changed, or removed.

---

## System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│  NETWORK TIER                                                    │
│  OpenRouter · Tailscale · external APIs · GitHub                │
├─────────────────────────────────────────────────────────────────┤
│  ON PREMISE TIER                                                 │
│                                                                  │
│  Mac Mini (100.104.149.107)                                      │
│  ├── LM Studio :1234          inference server                   │
│  ├── OpenClaw/TigerClaw :18789  agent harness (Scout)           │
│  ├── ZeroClaw :42617          memory backend                     │
│  ├── Nerve :3080              web UI                             │
│  ├── mcp-searxng              web search MCP                     │
│  └── mcp-crawl4ai-ts          URL ingestion MCP                  │
│                                                                  │
│  M1 MacBook (ste-business-server.tailebe6d3.ts.net)              │
│  ├── OpenProjects :8080       project management                 │
│  ├── Mattermost :8065         team comms + agent I/O            │
│  └── LedgerSMB :5762          financial records                  │
├─────────────────────────────────────────────────────────────────┤
│  ON DEVICE TIER                                                  │
│  M4 Laptop                                                       │
│  ├── VS Code + Copilot        interactive planning sessions      │
│  ├── OpenCode                 code-focused AI sessions           │
│  └── Obsidian                 daily notes (YYYY-MM-DD.md)        │
└─────────────────────────────────────────────────────────────────┘
```

---

## Component Details

### LM Studio
| Field | Value |
|---|---|
| **What** | Local inference server — serves LLM completions via OpenAI-compatible API |
| **Who** | Ed Hwang (operator) |
| **Where** | Mac Mini, port 1234, bind 0.0.0.0 |
| **Why** | Provides local inference — no cloud fallback, no OpenRouter spend for scheduled jobs |
| **How** | Loads model files from disk; exposes `/v1/chat/completions` and `/v1/embeddings`; all consumers point to `http://100.104.149.107:1234/v1` |
| **Models** | Qwen3.5 9B (primary agent model), Gemma 3 4B (lightweight), nomic-embed (embeddings) |
| **Boot** | LaunchAgent: `~/Library/LaunchAgents/ai.lmstudio.server.plist` — starts on login |
| **Config** | LM Studio settings.json — `defaultContextLength: 32768`, `enableThinking: false` |

---

### OpenClaw / TigerClaw
| Field | Value |
|---|---|
| **What** | Agent harness — runs Scout agent, manages tools, channels, memory, cron jobs |
| **Who** | Ed Hwang (operator), Scout (agent) |
| **Where** | Mac Mini, gateway port 18789, loopback only |
| **Why** | Autonomous agent execution — transcript processing, OP work package creation, Mattermost I/O |
| **How** | Reads `openclaw.json`; loads Scout agent with SOUL.md + AGENTS.md; listens on Mattermost `#transcripts`; calls LM Studio for inference; writes to OP and Mattermost channels |
| **Config** | `~/.openclaw/openclaw.json` — provider: lmstudio-mini, tools: minimal, skills: none, plugins: mattermost only |
| **Agent workspace** | `~/.openclaw/workspace/` — SOUL.md, AGENTS.md, TRANSCRIPT-PROCESSOR.md, OPENPROJECTS-SPEC.md |
| **Identity** | TigerClaw (fork of OpenClaw — config + identity layer, source cleanup deferred) |

---

### ZeroClaw
| Field | Value |
|---|---|
| **What** | Memory backend — SQLite hybrid search (vector + FTS5 keyword) for cross-session recall |
| **Who** | Ed Hwang (operator) |
| **Where** | Mac Mini, port 42617, loopback only |
| **Why** | Persistent searchable memory across sessions; nomic-embed for semantic search; no external dependencies |
| **How** | Rust binary; SQLite database; embedding via `http://localhost:1234/v1` (nomic-embed from LM Studio); hybrid search: vector 0.7 + keyword 0.3 |
| **Config** | `~/.zeroclaw/config.toml` |
| **Agent workspace** | `~/.zeroclaw/agents/scout/workspace/` — SOUL.md |
| **Status** | Running independently — not yet wired into OpenClaw pipeline (see ADR-0003) |

---

### Nerve
| Field | Value |
|---|---|
| **What** | Browser-based control plane for OpenClaw/TigerClaw — chat, voice, kanban, workspace browser, session monitoring |
| **Who** | Ed Hwang (primary user) |
| **Where** | Mac Mini, port 3080, bind 0.0.0.0 (Tailscale accessible) |
| **Why** | ⚠️ **DEPRIORITIZED 2026-07-19** — fails silently on Connect. Mattermost `#tigerclaw` is the primary UI. Nerve retained for future investigation. |
| **How** | Node.js app; connects to OpenClaw gateway (:18789) via WebSocket + gateway token; served to browser |
| **Config** | `~/nerve/.env` — `GATEWAY_URL`, `GATEWAY_TOKEN`, `HOST=0.0.0.0` |
| **Boot** | launchctl: `com.nerve.server` |
| **Known issue** | Browser may need `localStorage.removeItem('oc-config')` after config changes |
| **Kanban status** | Feature exists in source (`src/features/kanban/`) — scope TBD (OP #256, #257) |

---

### mcp-searxng
| Field | Value |
|---|---|
| **What** | MCP server — provides web search tool to ZeroClaw Scout agent |
| **Who** | Ed Hwang (operator) |
| **Where** | Mac Mini, loopback, port TBD |
| **Why** | Enables Scout to search the web without calling external APIs directly |
| **How** | MCP protocol; registered in `~/.zeroclaw/config.toml`; routes queries to SearXNG search engine |
| **Install path** | `~/mcp-searxng/` |
| **Status** | Installed + built; registered in ZeroClaw config; not yet tested end-to-end |

---

### mcp-crawl4ai-ts
| Field | Value |
|---|---|
| **What** | MCP server — fetches and extracts content from URLs for Scout agent |
| **Who** | Ed Hwang (operator) |
| **Where** | Mac Mini, loopback, port TBD |
| **Why** | Enables Scout to ingest web pages, GitHub repos, docs — URL intake pipeline |
| **How** | MCP protocol; registered in `~/.zeroclaw/config.toml`; uses crawl4ai for JS-rendered page extraction |
| **Install path** | `~/mcp-crawl4ai-ts/` |
| **Status** | Installed + built; registered in ZeroClaw config; not yet tested end-to-end |

---

### OpenProjects
| Field | Value |
|---|---|
| **What** | Project management — canonical work surface for all STE projects |
| **Who** | Ed Hwang (operator + primary user), Scout agent (creates WPs), Copilot (creates WPs) |
| **Where** | M1 MacBook, port 8080, `https://ste-business-server.tailebe6d3.ts.net:8080` |
| **Why** | Single source of truth for tasks, decisions, phases, milestones — agents post OP#IDs in all output |
| **How** | OpenProject instance; REST API (Basic auth: `apikey:{OPENPROJECTS_API_KEY}`); agents POST work packages after processing |
| **Projects** | #3 ste-ops · #6 ste-website · #11 camp-audax · #12 ste-ai-buildout (TigerClaw) · #13 rma-meeting-flow |

---

### Mattermost
| Field | Value |
|---|---|
| **What** | Primary human↔Scout interface — single channel for all input/output |
| **Who** | Ed Hwang, Christine Francis, Scout-cos bot |
| **Where** | M1 MacBook, port 8065, `https://ste-business-server.tailebe6d3.ts.net:8065` |
| **Why** | Scout-cos listens in #tigerclaw; Ed posts transcripts/commands here; Scout responds + creates OP work packages |
| **How** | Scout-cos bot (MM bot token) is member of #tigerclaw; OpenClaw `chatmode: oncall`, `allowFrom: ["*"]` |
| **Channels** | **#tigerclaw** (sole active channel — all input and output) |
| **Removed** | #transcripts (renamed), #tasks, #decisions, #agent-logs — all deleted 2026-07-19 |

---

### Obsidian (On Device)
| Field | Value |
|---|---|
| **What** | Daily note capture — Ed's primary on-device writing surface |
| **Who** | Ed Hwang |
| **Where** | M4 Laptop — local app, no exposed ports |
| **Why** | Captures daily work notes (YYYY-MM-DD.md); source material for Journal Database |
| **How** | Ed writes notes in Obsidian; manually moves finished daily notes to `Discovery/docs/`; Scout intake job (OP #263) will process them into ZeroClaw journal entries |
| **Note** | Date-named files (e.g. `2026-07-19.md`) are daily notes — not canonical docs |
