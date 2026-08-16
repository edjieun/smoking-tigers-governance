---
project: Project TigerClaw
former-name: Smoking Tigers AI Buildout / ST:AI
status: Active — Phase 4 in progress
last-updated: 2026-07-19
members: [Ed Hwang]
op_project: https://ste-business-server.tailebe6d3.ts.net:8080/projects/ste-ai-buildout
op_id: 12
tier: Network + On Premise + On Device
objective: Build a custom on-premise AI OS — three tiers (Network / On Premise / On Device) — serving as operational backbone for all STE projects
output: Autonomous pipeline (transcript → tasks), ZeroClaw memory, Nerve kanban, TigerClaw Manual in gov repo, Journal database
deadline: Ongoing — Phase 4 next session
blocker: Pipeline end-to-end test not yet confirmed post-reconnect
---

# Project TigerClaw

> Previously: "Smoking Tigers AI Buildout" / "ST:AI" — all references now consolidate to **Project TigerClaw**

## Summary

Smoking Tigers AI is a decentralized AI operations network across Ed's 3-machine home stack (M4 Laptop + M4 Mac Mini + M1 MacBook), connected via Tailscale, with governance through GitHub and operations through Mattermost. The goal is an autonomous pipeline: meeting happens → transcript posted → agent extracts tasks/decisions → team notified.

This system also serves as the operational backbone for all other STE projects.

---

## Architecture (from ADR-0001 + ADR-0010)

| Machine | Role |
|---|---|
| **M4 Laptop** | Interactive power use, complex reasoning (Sonnet 4.6 via OpenRouter), spec coding, Copilot agent sessions |
| **M4 Mac Mini** | Local inference executor — LM Studio + OpenClaw (Scout); Qwen3.5 9B; hard local block; 24/7 background jobs |
| **M1 MacBook** | OpenProjects transparency layer + LedgerSMB |

All machines connected via **Tailscale**. Secrets in **encrypted vault** (`edjieun/ste-secrets`, private GitHub).

---

## Domain Model (from grilling session 2026-07-16)

**Core problem:** Decision-making clarity — knowing what was decided and who needs to do what — is lost after meetings.

**Definition of done:** A meeting happens → transcript goes in → tasks show up in the right people's inboxes automatically.

**Key entities:** Organization · Member · Project · Decision · Task · Open Question · Agent · Workspace · Infrastructure Node · Governance Record

**Pipeline:**
```
Meeting (Fathom / Meet / Zoom)
  → Transcript (raw text or Fathom link)
    → Posted to MM #transcripts
      → Scout (OpenClaw, Mac Mini) processes automatically
        → #decisions — extracted agreements
        → #tasks — extracted action items by owner
        → #transcripts — summary + open questions
        → Google Drive — Memory card draft
```

**Governance boundaries (human approval required):**
- GitHub commits/merges
- LedgerSMB financial records

---

## What's Built (as of 2026-07-16)

### Phase 0 ✅ — Secrets Management
- Private GitHub repo `edjieun/ste-secrets`
- AES-256 encrypted vault (`vault.tar.gz.enc`) with `.env` (15 keys) + Google credentials
- Non-interactive encrypt/decrypt via `-pass file:` (no interactive terminal prompts)
- MATTERMOST_TEAM, NOTION_API_KEY now in vault
- One gap: `TAILSCALE_AUTH_KEY` empty (Tailscale already running; needed only for fresh auth)
- Burned secret: `GOOGLE_OAUTH_CLIENT_SECRET` — needs rotation in GCP

### Phase 1 ✅ — Mac Mini as Inference Server
- LM Studio running in server mode, port 1234, Tailscale-accessible
- Models loaded: Qwen3.5 9B (primary), Gemma 3 4B, nomic-embed (embeddings)
- `ste-default` preset: system prompt configured, `enableThinking: false`
- Laptop → Tailscale → Mac Mini inference verified (`PHASE1_OK`)

### Phase 2 ✅ — OpenClaw Rebuild + Mattermost + Member SOP

**OpenClaw (Mac Mini):**
- Old agents archived: `edjieun/ste-agents-archive` (pmp-team, maven, openclaw.json)
- Old agents deleted from Mac Mini
- `openclaw.json` rebuilt: Scout only, Qwen local primary, Gemma fallback, OpenRouter registered but NOT in any agent chain
- `plugins.allow: ["mattermost"]` explicitly set
- Hermes MCP server kept (local-only, dreaming at 3am via Qwen)
- `TRANSCRIPT-PROCESSOR.md` written to Scout's workspace
- Scout's `AGENTS.md` updated with transcript trigger and model discipline rules

**Mattermost (M1 — `ste-business-server.tailebe6d3.ts.net:8065`):**

| Channel | ID | Purpose |
|---|---|---|
| `#transcripts` | `uhyi1xfac7yd9esfytouokko4h` | Trigger input — Scout listens here |
| `#tasks` | `huq58yfrejffid58ta1wqzinko` | Agent-extracted tasks |
| `#decisions` | `93pbu6muep8r5fixz51ppm7cac` | Agent-extracted decisions |
| `#agent-logs` | `hphi4p6noffbtntq7g6pyrzm7e` | Scout status + errors |

- Scout bound to `#transcripts`
- Christine's MM account created (`christine`, `yr3bqxa89bgbtc53u6bbq9xtde`)
- `mavin` + `pmp-team` bots still need deactivating (manual step)
- Team: `smoking-tigers-enterprises` (`onzu1jgfy78wt85dmr9pdo6f9y`)

**Members:**
- Ed: full access
- Christine: `#transcripts`, `#tasks`, `#decisions`
- Van, Basil: to be onboarded

**Verification test (partial):**
- STE Landing Page transcript (June 23) posted to `#transcripts`
- `scout-cos` (existing Hermes agent) processed it and posted full meeting summary
- `scout` (new local config) is connected and listening
- `#tasks` and `#decisions` not yet populated — scout-cos used old instructions; @scout is the target for Friday

### Discovery Workspace ✅
- `docs/adr/0001-smoking-tigers-ai-domain-model.md`
- `docs/glossary.md` (35+ canonical terms)
- `docs/project-registry.md`
- `docs/task-log.md` (22 tasks + 16 decisions extracted from memory)
- `docs/open-questions.md` (19 open questions)
- `docs/member-sop.md`
- `docs/mattermost-setup.md`
- `docs/mattermost-channels.md`
- `docs/projects/` (this folder)
- `copilot/copilot-custom-prompts/Process Memory Card.md`

---

## What's Next

### Phase 2 — TigerClaw Rebuild (2026-07-18) ✅

**Key decisions:**
- Renamed fork: OpenClaw → **TigerClaw** (identity + source cleanup)
- **Memory system priority**: ZeroClaw (Rust, SQLite hybrid search) + nomic-embed via LM Studio
- **Input pipeline expanded**: transcripts → email → URLs → forwarded messages → all route to memory
- **Nerve kanban** replaces Mattermost as processing/UI layer; kanban lanes define processing paths
- **Hermes-agent deferred** as MCP skill layer (not memory backend)
- Provider key collision fixed: `lmstudio` → `lmstudio-mini` (was causing phantom cloud model fallback)
- `tools.profile: minimal`, `skills.allowBundled: []`, openrouter + mattermost plugins disabled
- ZeroClaw v0.8.3 installed on Mini; config: `embedding_provider = custom:http://localhost:1234/v1`
- Governance repo: `edjieun/smoking-tigers-governance` (already existed)

**Done (2026-07-18):**
- [x] `openclaw.json` rewritten — lean TigerClaw config, no cloud fallback, minimal tools
- [x] Provider key collision fixed (`lmstudio-mini`)
- [x] ZeroClaw v0.8.3 installed on Mini (aarch64-apple-darwin)
- [x] ZeroClaw config.toml written: SQLite memory, nomic-embed, hybrid search, Tailscale tunnel
- [x] OpenRouter balance: $57.06 (down from $58.77 at session start — ~$1.71 spent today)

**Phase 3 — Pipeline Verified (2026-07-19) ✅**
- [x] Scout ↔ Mattermost reconnected (was broken by TigerClaw rebuild)
- [x] Nerve fixed: gateway URL corrected to OpenClaw :18789 (was pointing at ZeroClaw :42617)
- [x] Full pipeline verified: transcript posted → Scout extracted tasks to #tasks, decisions to #decisions
- [x] memorySearch provider fixed (lmstudio-mini → lmstudio)
- [x] Nerve health: gateway:ok

**Definition of done achieved:**
> A meeting happens → transcript goes in → tasks show up in the right people's inboxes automatically. ✅

**Remaining:**
- [ ] Nerve browser: `localStorage.removeItem('oc-config')` in Chrome DevTools (clears stale gateway URL)
- [ ] Configure ZeroClaw email channel: IMAP `ed@quorum.one`
- [ ] Van + Basil MM onboarding (pending their readiness)
- [ ] ZeroClaw memory → wire into OpenClaw pipeline (cross-session recall)
- [ ] ⚠️ Rotate `edlicious` MM admin password

### Deferred
- OpenProjects spec template for transcript processing (Task #15)
- GitHub governance repo setup (Task #19)
- Standardize other workspaces (Gathering, Media) to Discovery structure (Task #20)
- Token cost monetization model for AI infra (not decided)
- LedgerSMB integration
- `GOOGLE_OAUTH_CLIENT_SECRET` rotation in GCP
- `TAILSCALE_AUTH_KEY` refresh

---

## Cost Tracking

| Checkpoint | Balance | Spend |
|---|---|---|
| Session start (after $50 top-up) | $49.95 | — |
| ~6pm 2026-07-16 | $40.10 | ~$9.85 |
| ~7:30pm 2026-07-16 | $32.31 | ~$7.79 more (~$17.64 total) |

Agent: GitHub Copilot / Claude Sonnet 4.6 via OpenRouter

---

## Key Architecture Decisions (ADR references)

| Decision | ADR |
|---|---|
| Domain model, pipeline, governance boundaries | `docs/adr/0001-smoking-tigers-ai-domain-model.md` |
| 3-machine stack, machine roles, Mattermost dump interface | `Smoking Tigers Studio/docs/adr/0010-on-premise-ai-architecture.md` |

---

## Source Memory Cards

| Date | Topic | Card |
|---|---|---|
| 2026-07-15 | On-premise AI architecture plan | `Memory/STE - 2026-07-15 - On-Premise AI Architecture Plan.md` |
| 2026-07-16 | Domain model grilling session | `docs/adr/0001-smoking-tigers-ai-domain-model.md` |
