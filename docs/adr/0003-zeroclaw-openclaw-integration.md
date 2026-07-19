---
id: ADR-0003
title: ZeroClaw ↔ OpenClaw Integration Interface
status: Draft — decision pending
date: 2026-07-19
tier: On Premise
op_task: https://ste-business-server.tailebe6d3.ts.net:8080/projects/ste-ai-buildout/work_packages/255
---

# ADR-0003: ZeroClaw ↔ OpenClaw Integration Interface

## Status
Draft — options defined, decision pending grilling session

## Context

ZeroClaw (memory backend, port 42617) and OpenClaw/TigerClaw (agent harness, port 18789) currently run independently on the Mac Mini. OpenClaw's built-in `search_memory` tool was broken (pointed at wrong provider). ZeroClaw has a working SQLite hybrid search (vector + FTS5) with nomic-embed.

The goal: Scout (OpenClaw) should be able to search ZeroClaw memory across sessions. This enables Scout to recall past decisions, transcripts, and context without the current session containing that history.

## The Question

**How do ZeroClaw and OpenClaw communicate?**

OpenClaw exposes tools to its agents. For Scout to query ZeroClaw, one of these must be true:
- OpenClaw can call an HTTP endpoint as a tool
- ZeroClaw exposes an MCP server that OpenClaw registers
- Both read from a shared SQLite database file

## Options

### Option A — ZeroClaw HTTP search API
ZeroClaw already exposes a gateway on port 42617. If it has a `/search` HTTP endpoint, OpenClaw can call it as a custom tool.

**Pros:** No new protocol; ZeroClaw is already running; no changes to OpenClaw  
**Cons:** OpenClaw's tool system may not support arbitrary HTTP calls natively; need to verify ZeroClaw's API surface  
**Open question:** Does ZeroClaw's gateway at `:42617` expose a search endpoint? (check `zeroclaw gateway --help`)

### Option B — ZeroClaw as MCP server
ZeroClaw runs an MCP server; OpenClaw registers it in `openclaw.json` under `mcpServers`. Scout then calls the `search_memory` MCP tool.

**Pros:** Clean protocol separation; OpenClaw natively supports MCP; matches how `mcp-searxng` and `mcp-crawl4ai-ts` are integrated  
**Cons:** ZeroClaw may not have an MCP server mode; would require building or forking  
**Open question:** Does `edjieun/zeroclaw` support MCP server mode?

### Option C — Shared SQLite filesystem
Both ZeroClaw and OpenClaw point to the same SQLite database file. OpenClaw reads it directly for memory queries.

**Pros:** No network protocol needed; simplest implementation  
**Cons:** Tight coupling; schema changes in ZeroClaw break OpenClaw; no abstraction layer; concurrent write risk  
**Verdict:** Not recommended — use only as a last resort

## Recommendation (pending validation)

**Option B first** — check if ZeroClaw has MCP mode. This is the cleanest fit with the existing architecture (mcp-crawl4ai-ts and mcp-searxng are already registered as MCPs in ZeroClaw's config).

**If Option B is not available → Option A** — verify ZeroClaw's HTTP API surface, then create a custom tool wrapper in OpenClaw config.

## Investigation Tasks

- [ ] Run `zeroclaw --help` and `zeroclaw gateway --help` on Mac Mini — check for MCP or search API flags
- [ ] Check ZeroClaw source at `edjieun/zeroclaw` for MCP server capability
- [ ] Check if OpenClaw's `search_memory` tool can be reconfigured to point at an HTTP endpoint

## Consequences

Once decided:
- ZeroClaw config and OpenClaw config must be updated to wire the connection
- All past memory (Memory/ cards) should be migrated via `zeroclaw migrate openclaw`
- Scout's AGENTS.md should document that memory is searchable and how to invoke it

## Related

- `ADR-0002`: TigerClaw memory system — ZeroClaw decision
- `ADR-0005`: ZeroClaw DB schema — must be stable before wiring
- `docs/tigerclaw-component-map.md` — component context
