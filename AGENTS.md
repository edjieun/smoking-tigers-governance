# AGENTS.md — Scout Runtime Core

## On Every Session Start
1. Read SOUL.md — who you are
2. Read `members/<github-username>.md` — who you're helping (personal user file; gitignored, machine-local)
   - Ed's file: `members/edjieun.md`
   - See `members/README.md` for other operators
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
| Copilot (this agent) | Copilot Agent | #10 | copilot.ste.eh@quorum.one | `OPENPROJECTS_COPILOT_API_KEY` |
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

## Workspace Layout (Discovery)

This workspace is the **shared knowledge surface** for Ed, Copilot, OpenCode, and TigerClaw agents.

| Path | What it is |
|---|---|
| `SOUL.md` | Agent identity (Chief of Staff persona) |
| `USER.md` | About Ed — preferences, environment |
| `TOOLS.md` | Available tools and spawn commands |
| `MEMORY.md` | Long-running decision log (append-only) |
| `TASKS.md` | Active task tracker (Scout-maintained) |
| `HEARTBEAT.md` | Periodic task definitions |
| `Memory/` | Atomic summary cards (agent-written) |
| `Transcripts/` | Raw meeting transcripts |
| `chunks/` | Chunked transcript segments |
| `docs/` | Structured docs, SOPs, ADRs, archived daily notes |
| `docs/YYYY-MM-DD.md` | Archived daily notes (moved from root after day ends) |
| `YYYY-MM-DD.md` (root) | **Active** daily note — raw working memory, not canonical |
| `scripts/` | Automation scripts |
| `skills/` | Agent skill definitions |
| `governance/` | Local governance clone (read freely, never self-approve) |

Key docs to orient quickly:
- [TigerClaw Manual](docs/tigerclaw-manual.md) — what the system is and how it works
- [Infrastructure Map](docs/infrastructure-map.md) — hardware, ports, network
- [Mattermost Channels](docs/mattermost-channels.md) — `#tigerclaw` is the single agent I/O channel (as of 2026-07-19)
- [Port Map](docs/port-map.md) — all service ports
- [AI Agent Org Chart](docs/ai-agent-org-chart.md) — agent roles and hierarchy

---

## Current System State (as of 2026-07-19)

- **Primary agent I/O:** Mattermost `#tigerclaw` (transcripts in → tasks/decisions out)
- **Nerve:** Deprioritized — do not build on it
- **OpenProjects:** Active work surface — all tasks tracked as work packages
- **ZeroClaw:** Memory backend (Mac Mini, port 42617)
- **Scout-cos:** On-premise agent on Mac Mini via OpenClaw

---

## This File
Changes only with explicit human instruction.