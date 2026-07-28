# START HERE — TigerClaws Agent Workspace

**What this is:** The shared project workspace for Smoking Tigers Enterprises (STE).
Any STE member can open this folder with their agent of choice and get a working context immediately.

---

## 1. What You Need Before Starting

| Requirement | Where to get it |
|---|---|
| Tailscale connected to STE tailnet | Ask Ed — one-click join link |
| OpenProjects account | `https://ste-business-server.tailebe6d3.ts.net:8080` — ask Ed to create your account |
| Your OP API key | OP → avatar → My Account → Access Tokens → create one |
| GitHub access | Personal Access Token — scopes: `repo`, `read:org`, `workflow` |
| Your AI harness (Claude, Gemini, or ChatGPT) | Your own account |

Sensitive keys go in your local secrets file — **never commit them to this folder.**
Recommended location: `~/.ste-secrets/.env`

---

## 2. Set Up Your User File

Create your personal user file and device enrollment:

```bash
# 1. Add your device to members/devices.yaml (get next available DID, e.g. ste-did-003)

# 2. Create your enrollment file
cp members/template.yaml members/<your-hostname>.yaml
# edit with your details — include your DID

# 3. Create your personal user file (gitignored — stays local)
cp USER.template.md members/<your-github-username>.md
# edit with your name, timezone, preferences, and DID(s)
```

`members/<your-github-username>.md` is your personal file — gitignored, never committed or synced.
Submit a PR with `devices.yaml` + `<hostname>.yaml` only.

---

## 3. Choose Your Agent Harness

Load the right harness config for your AI tool:

| You're using | Read this file |
|---|---|
| Claude (Anthropic) / GitHub Copilot / VS Code | `claude.md` |
| Gemini (Google) / OpenCode + Gemini | `gemini.md` |
| ChatGPT / OpenAI Codex | `codex.md` |

Each harness file tells your agent how to operate in this workspace.

---

## 4. What Your Agent Reads on Session Start

Your agent should load these files at the start of every session, in order:

1. `SOUL.md` — who the agent is (Chief of Staff persona)
2. `USER.md` — who it's helping (your personal file)
3. `AGENTS.md` — the full runtime contract (safety rules, OP config, workspace layout)
4. `MEMORY.md` — long-running project decision log
5. Your harness file (`claude.md` / `gemini.md` / `codex.md`)

Then check today's daily note if one exists (`docs/YYYY-MM-DD.md`).

---

## 5. Active Projects

All work is tracked in OpenProjects. Requires Tailscale.
URL: `https://ste-business-server.tailebe6d3.ts.net:8080`

| Project | ID | What it is |
|---|---|---|
| Project TigerClaw | 12 | AI infrastructure buildout |
| STE Operations | 3 | Catch-all ops tasks |
| STE Website & Community | 6 | Website + member community |
| Camp Audax / The Gathering | 11 | Event coordination |
| RMA — New Meeting Flow | 13 | Recording/meeting workflow |

---

## 6. Key Docs to Orient Quickly

| Need | File |
|---|---|
| What is TigerClaw? | `docs/tigerclaw-manual.md` |
| What's running where? | `docs/infrastructure-map.md` |
| What ports/services? | `docs/port-map.md` |
| Agent roles | `docs/ai-agent-org-chart.md` |
| Policies | `governance/policies/` |
| Decision log | `decisions/2026/` |
| Architecture decisions | `docs/adr/` |
| Session memory cards | `Memory/` |

---

## 7. MCP Servers Available

Full setup instructions: `docs/tigerclaw-component-map.md`

**Portable — run on your own machine:**

| Server | Purpose | Setup |
|---|---|---|
| `composio-mcp-server` | 600+ app integrations (GitHub, Drive, Notion, etc.) | `skills/composio-integration/SKILL.md` |
| `obsidian-mcp-server` | Obsidian vault memory access | Install via npm; point at your vault |

**STE On-Premise — Mac Mini, requires Tailscale:**

| Server | Purpose | Host |
|---|---|---|
| `mcp-searxng` | Web search | `100.104.149.107` |
| `mcp-crawl4ai-ts` | URL ingestion | `100.104.149.107` |

---

## 8. Ground Rules

- **Draft ≠ Send.** Drafting anything is fine. Sending to Mattermost, OP, or external services requires explicit human instruction.
- **No destructive actions without confirmation.** Prefer reversible operations (move > delete).
- **Every action item gets an OP work package ID** before the session ends.
- **Secrets stay local.** Never commit `~/.ste-secrets/` or `USER.md` to Drive or GitHub.
- **This folder is local working memory** — not canonical. Canonical docs live in GitHub (`edjieun/smoking-tigers-governance`) and OpenProjects.

---

*TigerClaws workspace v1 — 2026-07-28*
