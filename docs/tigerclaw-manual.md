---
title: TigerClaw Manual
status: In Progress (built incrementally)
last-updated: 2026-07-19
op_task: https://ste-business-server.tailebe6d3.ts.net:8080/projects/ste-ai-buildout/work_packages/254
tier: All
audience: Ed Hwang, future team members, agents reading context
---

# TigerClaw Manual

> This manual is built incrementally — each grilling session adds a section.
> It is the single place to answer: "What is TigerClaw and how does it work?"

---

## What is TigerClaw?

TigerClaw is Smoking Tigers Enterprises' on-premise AI operating system.

It is **not** a single application. It is a composed system built from the best available open-source components, tuned for STE's specific hardware and workflows. The goal is an autonomous pipeline: a meeting happens → transcript goes in → tasks land in the right people's inboxes — without anyone manually copying notes.

TigerClaw is the AI arm of STE. The other arm is Media (Smoking Tigers Studio).

---

## Three Tiers

Every component belongs to exactly one tier:

| Tier | Scope | Primary Hardware |
|---|---|---|
| **Network** | Cloud services, external APIs, Tailscale overlay | — |
| **On Premise** | Local inference + agents + services running 24/7 | Mac Mini M4 + M1 MacBook |
| **On Device** | Interactive sessions, daily capture, development tools | M4 Laptop |

---

## The Core Pipeline

```
Meeting (Zoom / Google Meet / Fathom)
  → Transcript (raw text)
    → Posted to Mattermost #transcripts
      → Scout (OpenClaw, Mac Mini) processes automatically
        → Extracts Tasks → OpenProjects work packages
        → Extracts Decisions → OpenProjects work packages
        → Posts summary → #transcripts
        → Notifies team → #tasks + #decisions
          → ZeroClaw stores memory (cross-session recall)
```

**Definition of done:** A meeting happens → transcript goes in → tasks appear in OP with OP#IDs in Mattermost.

---

## Component Quick Reference

| Component | What it does | Where | Port |
|---|---|---|---|
| LM Studio | Local inference server | Mac Mini | 1234 |
| OpenClaw/TigerClaw | Agent harness (Scout) | Mac Mini | 18789 |
| ZeroClaw | Memory backend | Mac Mini | 42617 |
| Nerve | Browser UI | Mac Mini | 3080 |
| OpenProjects | Work tracking | M1 MacBook | 8080 |
| Mattermost | Team comms + agent I/O | M1 MacBook | 8065 |
| LedgerSMB | Financial records | M1 MacBook | 5762 |

Full details: `docs/tigerclaw-component-map.md`
Port map: `docs/port-map.md`

---

## How to Use the Pipeline

### Submit a transcript
1. Copy raw meeting transcript text
2. Post to Mattermost `#transcripts` channel
3. Scout will respond within ~60 seconds with a summary
4. Check `#tasks` and `#decisions` for extracted items
5. Each item has an OP#ID — click to open in OpenProjects

### Check on Scout
- Scout status and errors: Mattermost `#agent-logs`
- Scout config: `~/.openclaw/openclaw.json` on Mac Mini
- Scout workspace: `~/.openclaw/workspace/` on Mac Mini

### Open Nerve (browser UI)
1. Navigate to `http://100.104.149.107:3080`
2. If blank: run `localStorage.removeItem('oc-config'); location.reload()` in Chrome DevTools
3. Confirm status bar shows `gateway: ok`

---

## How to Add a New Service

1. Check `docs/port-map.md` — confirm port is free
2. Add port map entry before deploying
3. Write SOP in `docs/` answering who/what/where/why/how
4. Create OP work package for the deployment task
5. Run `grill-with-docs` skill if the service needs an ADR

---

## Architecture Decisions

| Decision | ADR |
|---|---|
| Domain model + pipeline | `docs/adr/0001-smoking-tigers-ai-domain-model.md` |
| Memory system (ZeroClaw + nomic-embed) | `docs/adr/0002-tigerclaw-memory-system.md` |
| ZeroClaw ↔ OpenClaw integration | `docs/adr/0003-zeroclaw-openclaw-integration.md` (in progress) |
| Nerve kanban design | `docs/adr/0004-nerve-kanban-design.md` (pending) |
| ZeroClaw DB schema | `docs/adr/0005-zeroclaw-db-schema.md` (in progress) |

---

## Governance

- All SOPs and ADRs: `edjieun/smoking-tigers-governance`
- Live work tracking: OpenProjects #12 `ste-ai-buildout`
- Secrets vault: `edjieun/ste-secrets` (private)
- Agents read `AGENTS.md` in each workspace for context + OP config

---

## What's Still Being Built

See [Project TigerClaw in OpenProjects](https://ste-business-server.tailebe6d3.ts.net:8080/projects/ste-ai-buildout) for the current Phase 4 task list.

Key open items:
- ZeroClaw ↔ OpenClaw integration (ADR-0003)
- Nerve kanban scope definition (ADR-0004)
- ZeroClaw DB schema (ADR-0005)
- Journal database (daily notes → searchable work record)
- Email ingestion channel (`ed@quorum.one` IMAP)
- Van + Basil Mattermost onboarding
