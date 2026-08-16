# API Conventions — TigerClaws

> Standard patterns for all API calls made by agents in this workspace.
> Add new service sections as integrations are built out.

---

## General Rules

- **Auth secrets** live in `~/.ste-secrets/.env` — source before use, never hardcode
- **Agent keys**: each agent has its own API key per service — never share or cross-use
- **Draft ≠ Send**: POST/PATCH calls that create or modify external records require explicit human instruction
- **Error handling**: always inspect response before assuming success — log failures to the relevant OP WP

---

## OpenProjects

**Auth:** Basic — `base64("apikey:{KEY}")` — Bearer does NOT work.

```bash
source ~/.ste-secrets/.env
AUTH=$(echo -n "apikey:$OPENPROJECTS_[YOUR_NAME]_API_KEY" | base64)
```

**Base URL:** `https://ste-business-server.tailebe6d3.ts.net:8080/api/v3`

**Key patterns:**
- Always fetch `lockVersion` before a PATCH — stale version → 409
- WP creation: POST to `/projects/{id}/work_packages`
- Status update: PATCH `/work_packages/{id}` with `lockVersion` + `_links.status.href`
- Comment: POST `/work_packages/{id}/activities` with `comment.raw`
- File attach: multipart POST `/work_packages/{id}/attachments`

Full reference: `.github/skills/openprojects/SKILL.md`

---

## GitHub

**Auth:** Personal Access Token in `Authorization: Bearer` header, or via `gh` CLI.

```bash
source ~/.ste-secrets/.env
# gh CLI (preferred)
gh auth login --with-token <<< "$GITHUB_[YOUR_NAME]_PAT"
# or curl
curl -H "Authorization: Bearer $GITHUB_[YOUR_NAME]_PAT" https://api.github.com/...
```

**Key repos:**
- `edjieun/smoking-tigers-governance` — canonical governance docs
- `edjieun/mcp-searxng` — web search MCP
- `edjieun/playwright-mcp` — browser automation MCP

Full reference: `skills/github/SKILL.md`

---

## Composio

**Auth:** Platform API key (`ak_...`) in `COMPOSIO_API_KEY`.

```bash
source ~/.ste-secrets/.env
# MCP stdio server (preferred for agents with MCP support)
composio-mcp-server --api-key $COMPOSIO_API_KEY
# or REST API
curl -H "x-api-key: $COMPOSIO_API_KEY" https://backend.composio.dev/api/v1/...
```

Full reference: `skills/composio-integration/SKILL.md`

---

## Mattermost

**Auth:** Bot token or personal access token.

```bash
source ~/.ste-secrets/.env
curl -H "Authorization: Bearer $MATTERMOST_BOT_TOKEN" \
  https://ste-business-server.tailebe6d3.ts.net:8065/api/v4/...
```

**Agent I/O channel:** `#tigerclaw` (single channel as of 2026-07-19)
No other agent channels — post only here unless explicitly instructed.

---

## LM Studio (Local Inference)

**Auth:** None (local only — not exposed to network).

```bash
curl http://100.104.149.107:1234/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"qwen2.5-9b","messages":[{"role":"user","content":"..."}]}'
```

Only reachable on the STE Tailnet from Mac Mini's IP.

---

## OpenRouter

**Auth:** Bearer token.

```bash
source ~/.ste-secrets/.env
curl -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  https://openrouter.ai/api/v1/chat/completions ...
```

Use for cloud model fallbacks — tracked for cost in `scripts/openrouter-cost-tracker.py`.

---

*Last updated: 2026-07-28*
