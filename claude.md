# Claude / Copilot Harness Config — TigerClaws

> For agents running via: Anthropic Claude (claude.ai), GitHub Copilot (VS Code), or any Anthropic API consumer.

---

## Session Start Protocol

On every session start, read in this order:

1. `SOUL.md` — persona
2. `USER.md` — who you're helping
3. `AGENTS.md` — primary runtime contract (safety rules, workspace layout, OP config)
4. `MEMORY.md` — project decision log
5. This file

Then check today's daily note if one exists (`docs/YYYY-MM-DD.md`).

---

## GitHub Copilot (VS Code)

- Skills are invoked by attaching `#prompt:SKILL.md` files in chat
- Available skills:
  - `.github/skills/openprojects/SKILL.md` — OP work package operations
  - `.github/skills/transcript-intake/SKILL.md` — transcript processing pipeline
  - `.agents/skills/grill-with-docs/SKILL.md` — ADR + SOP generation
  - `.agents/skills/domain-modeling/SKILL.md` — domain modeling interviews
- Plan mode: research first, save plan to `/memories/session/plan.md` before implementing
- Copilot identity in OP: **Copilot Agent (#10)**, key: `OPENPROJECTS_COPILOT_API_KEY`
- Workspace instructions: `.github/copilot-instructions.md`

---

## Claude API / claude.ai

- Use `OPENPROJECTS_[YOUR_NAME]_API_KEY` for all OP operations — never another member's key
- Draft ≠ Send: all posts to Mattermost, OP, or external services require explicit instruction
- No markdown in Mattermost DMs or Discord casual channels
- Model: Claude Sonnet 4.x (primary) or latest available
- Fallback via OpenRouter: `anthropic/claude-sonnet-4-6`
- Context: use full context window — don't truncate session files

---

## OpenClaw / TigerClaw Harness (Mac Mini)

If running as a scheduled or autonomous agent via OpenClaw:

- Config: `~/.openclaw/openclaw.json`
- Agent workspace: `~/.openclaw/workspace/` — contains `SOUL.md`, `AGENTS.md`, `TRANSCRIPT-PROCESSOR.md`
- Provider: `lmstudio-mini` (local inference, Mac Mini)
- Mattermost channel: `#tigerclaw` — single agent I/O channel

---

## Reference

| Doc | Purpose |
|---|---|
| `AGENTS.md` | Full runtime contract |
| `SOUL.md` | Persona |
| `TOOLS.md` | Available tools and spawn commands |
| `.github/skills/openprojects/SKILL.md` | OP API operations |
| `docs/tigerclaw-manual.md` | System overview |
| `docs/infrastructure-map.md` | Hardware + services |
