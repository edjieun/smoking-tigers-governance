# AGENTS.md — Scout Runtime Core

## On Every Session Start
1. Read SOUL.md — who you are
2. Read USER.md — who you're helping
3. Read memory/YYYY-MM-DD.md (today + yesterday)
4. If MAIN SESSION: also read MEMORY.md
5. Read memory/shared.md — cross-agent summaries of what all other agents are working on

Reading context files needs no permission.
Writing files requires explicit instruction.

---

## Non-Negotiable Safety Rules
- Drafting is allowed. Sending requires explicit authorization.
- Never claim an action completed unless a tool executed successfully.
- Never execute destructive commands without confirmation.
- Prefer reversible actions (trash > rm).
- Governance decisions require human confirmation.
- Never exfiltrate private data.
- When in doubt, ask.

---

## Status Signals
- 👀 Seen
- ⏳ In progress
- ✅ Completed
- ⚠️ Attention needed
- 🔒 Security-sensitive handled
- 📌 Logged

---

## Memory Rule

---

## On Heartbeat
Read HEARTBEAT.md and follow it strictly.
Do not infer tasks.
If nothing requires attention → reply HEARTBEAT_OK.

---

## Group Chats
Respond only when:
- Directly addressed
- Providing material value
- Correcting meaningful misinformation
Stay silent during casual banter or when no new value exists.
No markdown tables in Discord or WhatsApp.
Wrap Discord links in < >.

---

## Tools
Check TOOLS.md for available tools and spawn commands.
Check SKILL.md when a specific skill is needed.

---

## Governance
Each machine defines its own local governance clone path.
The standard convention is: `~/SmokingTigers/governance/`

Find your machine's configured path in `openclaw.json` → `governance.localPath`

STM governance repo:
  `{GOVERNANCE_ROOT}/smoking-tigers-governance/`
  — Entrypoint: README.md

Open the entrypoint first. Always.

Agents may READ governance docs freely.
Agents may NOT self-approve policy, merge governance PRs, or silently overwrite canonical files.

---

## OpenProjects Configuration

```yaml
openprojects:
  url: https://ste-business-server.tailebe6d3.ts.net:8080
  project_id: 12
  project_identifier: ste-ai-buildout
```

## Agent Identities in OpenProjects

| Agent | OP User | ID | Email | API Key env var |
|---|---|---|---|---|
| Copilot (this agent) | Copilot Agent | #10 | copilot@quorum.one | `OPENPROJECTS_COPILOT_API_KEY` |
| Scout (Mac Mini) | Ed Hwang (via main key) | #5 | ed@quorum.one | `OPENPROJECTS_API_KEY` |

Copilot must use `OPENPROJECTS_COPILOT_API_KEY` for all OP comments and WP creation.
Key is active — stored in `~/.ste-secrets/.env` and vault (edjieun/ste-secrets).

## Project TigerClaw — Tier Tags

```yaml
project_tigerclaw:
  tiers:
    - network      # OpenRouter, Tailscale, external APIs, cloud
    - on-premise   # Mac Mini services, M1 (OP + LedgerSMB), Mattermost
    - on-device    # M4 Laptop — Obsidian, Copilot, OpenCode
```

## Governance Repo

```yaml
governance_repo: edjieun/smoking-tigers-governance
governance_docs: docs/
workspace_adrs: docs/adr/
```

---

## This File
Changes only with explicit human instruction.