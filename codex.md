# ChatGPT / OpenAI Harness Config — TigerClaws

> For agents running via: ChatGPT (chat.openai.com), Custom GPTs, OpenAI API, or GitHub Copilot (OpenAI models).

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

## Custom GPT Setup

To use this workspace with a Custom GPT:

1. Create a new Custom GPT at `chat.openai.com/gpts`
2. In **Instructions**, paste the contents of `AGENTS.md` + `SOUL.md`
3. In **Knowledge**, upload: `USER.md`, `MEMORY.md`, `TOOLS.md`
4. Enable **Code Interpreter** and **Web Browsing** as needed
5. For OP access, add an **Action** using the OpenProjects API — see `.github/skills/openprojects/SKILL.md` for the curl patterns; translate to OpenAPI schema for GPT Actions

---

## OpenAI API Usage

- **API Key:** your own `OPENAI_API_KEY` in `~/.ste-secrets/.env`
- **Model:** `gpt-4o` (primary), `gpt-4o-mini` (lightweight tasks)
- **Context:** 128k tokens — prioritize `AGENTS.md`, `MEMORY.md`, and current task files
- Use `OPENPROJECTS_[YOUR_NAME]_API_KEY` for all OP operations — never another member's key
- Draft ≠ Send: all posts to Mattermost, OP, or external services require explicit instruction

---

## MCP / Tool Access

OpenAI does not natively support MCP stdio servers. Options:

| Option | How |
|---|---|
| Composio via REST | Use Composio REST API directly (no MCP needed) — see `skills/composio-integration/SKILL.md` |
| GPT Actions | Define OpenAPI schemas for OP, GitHub, Drive — add as GPT Actions |
| Local MCP bridge | Use an MCP-to-OpenAI bridge if available on your machine |

---

## Behavior Notes

- No markdown in Mattermost DMs or Discord casual channels
- Every action item gets an OP work package ID before the session ends

---

## Reference

| Doc | Purpose |
|---|---|
| `AGENTS.md` | Full runtime contract |
| `SOUL.md` | Persona |
| `TOOLS.md` | Available tools |
| `.github/skills/openprojects/SKILL.md` | OP API operations |
| `skills/composio-integration/SKILL.md` | App integrations |
| `docs/tigerclaw-manual.md` | System overview |
