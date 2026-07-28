# Gemini Harness Config — TigerClaws

> For agents running via: Google Gemini (gemini.google.com), OpenCode + Gemini, or Gemini API via quorum.one Google Workspace.

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

## Gemini via quorum.one (STE Standard)

STE routes Gemini through the `quorum.one` Google Workspace account.

- **Model:** Gemini 2.5 Pro (primary), Gemini 2.0 Flash (lightweight / fast tasks)
- **API Key:** `GEMINI_API_KEY` in `~/.ste-secrets/.env`
- **Context window:** 1M tokens — load full project files freely
- **Cost:** covered under quorum.one workspace quota

---

## OpenCode + Gemini Setup

If using OpenCode as your harness with Gemini as the model:

1. Set model in OpenCode config: `provider: google`, `model: gemini-2.5-pro`
2. Place `GEMINI_API_KEY` in OpenCode's env config
3. OpenCode reads `AGENTS.md` automatically from workspace root
4. Add MCP servers to `.opencode/config`:
   - `composio-mcp-server` — see `skills/composio-integration/SKILL.md`
   - `obsidian-mcp-server` — point at your local Obsidian vault

---

## Christine's Setup (reference)

For a complete new-member walkthrough of Gemini on-device setup, see:
`docs/christine-agent-setup-guide.md`

Published SOP: OP#321 (in progress — `[Network Node] Draft Gemini on-device AI setup SOP`)

---

## Behavior Notes

- Use `OPENPROJECTS_[YOUR_NAME]_API_KEY` for all OP operations — never another member's key
- Draft ≠ Send: all posts to Mattermost, OP, or external services require explicit instruction
- Knowledge-ops and research tasks: Gemini preferred over Claude (larger context, native Google integration)
- No markdown in Mattermost DMs or Discord casual channels

---

## Reference

| Doc | Purpose |
|---|---|
| `AGENTS.md` | Full runtime contract |
| `SOUL.md` | Persona |
| `docs/Gemini Integration.md` | Gemini integration details |
| `docs/tigerclaw-manual.md` | System overview |
| `docs/infrastructure-map.md` | Hardware + services |
| `skills/composio-integration/SKILL.md` | MCP app integrations |
