---
id: AGENT_HARNESS_GUIDE
title: Agent Harness Guide
type: Guide
status: active
owner: Hobbes
authors:
  - Copilot Agent
  - Hobbes
---

## Purpose

Explains where shared agent harness configs live and how STE members use them with their local AI-assisted operating environment.

## Where the harness lives

Shared agent runtime configs, skills, and templates were migrated to a dedicated public repository under separate rules from this governance repo:

**Repo:** https://github.com/edjieun/ste-agent-harness (default branch `main`)

It contains:
- `.agents/skills/` — agent skill definitions (domain-modeling, grill-with-docs, etc.)
- `.github/skills/` — GitHub Copilot skills (openprojects, transcript-intake)
- `.github/workflows/nightly-mor-check.yml` — nightly monitoring workflow
- `skills/` — standalone agent skills (composio-integration, github)
- Shared runtime templates — `AGENTS.md`, `SOUL.md`, `MEMORY.md`, `TASKS.md`, `TOOLS.md`, `HEARTBEAT.md`, `START_HERE.md`, `IDENTITY.md`, `USER.template.md`
- `gemini.md`, `claude.md`, `codex.md`, `debugging.md`, `designs.md` — agent harness reference docs
- `copilot/` — GitHub Copilot custom prompts and session helpers

## How to use it

1. Clone this repo alongside your local workspace: `gh repo clone edjieun/ste-agent-harness`
2. Copy the runtime template files you need into your local agent workspace.
3. Customize `USER.md` locally only — it is gitignored by design. Personal files stay out of the repo.
4. Governance (policies, decisions, SOPs) is always authoritative here: **`edjieun/smoking-tigers-governance`**.

## Rules

- The harness repo contains **shared configs and templates only** — no operational data, secrets, or private notes.
- Both repos are public. Follow the Zero Private Data rule (see `guides/PRIVACY_HANDLING.md`).
- The harness repo is governed by the policies in this governance repository.