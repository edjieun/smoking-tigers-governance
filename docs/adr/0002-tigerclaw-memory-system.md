---
id: ADR-0002
title: TigerClaw Memory System — ZeroClaw + nomic-embed
status: Accepted
date: 2026-07-18
deciders: [Ed Hwang]
---

# ADR-0002: TigerClaw Memory System

## Context

OpenClaw's built-in `search_memory` tool requires an embeddings model to work.
The existing config pointed at `lmstudio` (the collision key), so it was
silently falling back to cloud inference. The broader need is a memory system
that can ingest multiple input types — not just transcripts, but email, URLs,
and forwarded messages — and make them searchable across sessions.

## Decision

**ZeroClaw** (`edjieun/zeroclaw`, Rust) as the primary memory backend.

- SQLite hybrid search: vector (cosine, 0.7 weight) + FTS5 keyword (0.3 weight)
- No external dependencies — no Pinecone, no Elasticsearch, no LangChain
- `embedding_provider = "custom:http://localhost:1234/v1"` → nomic-embed served
  by LM Studio already running on Mini
- Single Rust binary (<5MB), <5MB RAM overhead, instant startup
- `zeroclaw migrate openclaw` can import existing OpenClaw memory

**Hermes-agent** (`edjieun/hermes-agent`, Python) deferred as an optional MCP
skill server — for autonomous skill creation and learning loop, not primary
memory storage. Heavier, Python runtime, not the right tool for this problem.

## Multi-source input pipeline

All input types route to ZeroClaw memory through Nerve kanban lanes:

| Lane | Source | ZeroClaw action |
|---|---|---|
| `transcript` | Meeting text | chunk → embed → store |
| `email` | IMAP `ed@quorum.one` | summarize → store |
| `url/web` | URL dropped in | crawl4ai fetch → chunk → store |
| `message-forward` | Telegram / WhatsApp | summarize → store |

## TigerClaw config changes (openclaw.json)

- Provider key: `lmstudio` → `lmstudio-mini` (fixes phantom cloud model catalog)
- `tools.profile: "minimal"` (was `"coding"`)
- `skills.allowBundled: []` (all bundled skills disabled)
- `plugins.allow: []` (allow-list cleared — explicit deny list enforced)
- Denied plugins: `openrouter`, `mattermost`, `canvas`, `nodes`, `browser`,
  `web_search`, `agents_list`, `sessions_list`, `sessions_history`,
  `sessions_send`, `sessions_spawn`, `sessions_status`
- Kept: `memory-core` (3am dreaming via Qwen), `hermes` MCP, `searxng`,
  `duckduckgo`
- Context window: 16k (was 100k — reduces memory pressure, improves stability)
- Hard local block: no cloud fallback model configured

## Consequences

- ZeroClaw agent setup requires `zerocode` TUI on Mini directly (interactive)
- Email ingestion requires app password or OAuth for `ed@quorum.one`
- Nerve install required to expose kanban UI over Tailscale
- `mcp-crawl4ai-ts` + `mcp-searxng` installs pending

## Related

- `ADR-0001`: Domain model + pipeline (transcripts, agents, Mattermost)
- `ADR-0010`: On-premise AI architecture (3-machine stack, Tailscale, LM Studio)
- `docs/projects/smoking-tigers-ai-buildout.md` — Phase 2 implementation log
