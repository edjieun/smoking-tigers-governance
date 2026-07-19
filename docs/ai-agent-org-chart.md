# AI Agent Org Chart — v2 (Hub and Spoke)

**Last updated:** 2026-04-19  
**Architecture:** Hierarchical Matrix — Scout as Root Orchestrator

---

## Agent Fleet

```
Scout (main) — Root Orchestrator
│  Model: Claude Sonnet 4.6 (OpenRouter)
│  Channel: Mattermost default
│
├── ea — Executive Assistant (Eva)
│   Model: Claude Sonnet 4.6
│   Scope: Calendar, Notion, Google Workspace, Apple integrations
│   Channels: Discord (ea), Mattermost (ea)
│
├── sysops — System Operations (Doug)
│   Model: Qwen 2.5 14B (local)
│   Scope: Infrastructure health, service control
│   HITL: group:runtime requires human approval
│
├── knowledge-ops — Knowledge Pipeline
│   Model: Gemini 2.5 Pro (OpenRouter)
│   Scope: QMD indexing, Obsidian vault, memory digests
│
├── governance-ops — Governance Operations
│   Model: Claude Sonnet 4.6
│   Scope: Policy docs, decision registry, STEPPS quality gate
│
├── comm-ops — Communication Operations [NEW v2]
│   Model: Gemma 4 26B (local)
│   Scope: Discord/WhatsApp routing and triage
│   Cost: Zero API (local model)
│
├── business-ops — Business Operations [NEW v2]
│   Model: Qwen 2.5 7B (local)
│   Scope: Reports, document updates via MCP
│   Cost: Zero API (local model)
│
├── dev-ops — Development Operations [NEW v2]
│   Model: Claude Sonnet 4.6
│   Scope: GitHub/Linear automation, code reviews
│
├── growth-ops — Growth Operations [NEW v2]
│   Model: Gemma 4 26B (local)
│   Scope: Reddit/Twitter brand presence
│   Status: Awaiting social media credentials (STE-73)
│
├── research-ops — Research Operations [NEW v2]
│   Model: Claude Sonnet 4.6
│   Scope: Web research, competitive intelligence
│   Special: Isolated web access (group:web allowed for this agent only)
│
├── agent-ops — Agent Operations [NEW v2]
│   Model: Qwen 2.5 7B (local)
│   Scope: Fleet health, load balancing, fallback routing
│
├── sergeant-at-arms — Compliance
│   Model: Claude Sonnet 4.6
│   Scope: Access control, compliance review
│
└── christine-ea, van-ea, basil-ea — Exec EA Agents
    Model: Claude Sonnet 4.6
    Scope: Personal EA for Christine, Van (Ben), Basil
    Channels: Discord (per-account)
```

---

## Routing Rules (Scout)

| Request type | Route to |
|---|---|
| Technical/ops | sysops |
| Calendar/admin | ea |
| Knowledge/memory | knowledge-ops |
| Policy/governance | governance-ops |
| Comms/chat routing | comm-ops |
| Docs/reports | business-ops |
| Code/GitHub/Linear | dev-ops |
| Brand/social | growth-ops |
| Research/web | research-ops |
| Fleet health | agent-ops |

---

## Local vs Cloud

| Agent | Model | Cost |
|---|---|---|
| main, ea, sysops*, governance-ops, dev-ops, research-ops, sergeant-at-arms | Claude Sonnet 4.6 | OpenRouter API |
| knowledge-ops | Gemini 2.5 Pro | OpenRouter API |
| sysops | Qwen 2.5 14B | Free (local) |
| comm-ops, growth-ops | Gemma 4 26B | Free (local) |
| business-ops, agent-ops | Qwen 2.5 7B | Free (local) |

*sysops model changed to local Qwen 2.5 14B in v2

---
_v2 architecture deployed 2026-04-19_
