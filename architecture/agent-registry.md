# ST:AI Agent Registry

**Version:** 1.0.0  
**Last Updated:** 2026-03-27  
**Owner:** Scout (Chief of Staff)  
**Status:** Active  

> Canonical source of truth for all OpenClaw agents in the ST:AI ecosystem.  
> Machine-readable counterpart: `~/.openclaw/workspace/agents/registry.json`  
> Changes require explicit human approval.

---

## Tier 1 — Chief of Staff

| Field | Value |
|---|---|
| **ID** | `main` |
| **Name** | Scout |
| **Role** | Chief of Staff |
| **Emoji** | 🦅 |
| **Model** | `openrouter/anthropic/claude-sonnet-4.6` |
| **Workspace** | `~/.openclaw/workspace` |
| **Status** | ✅ Active |
| **Skills** | apple-notes, apple-reminders, clawhub, coding-agent, github, openai-whisper, peekaboo, video-frames |
| **Memory** | `MEMORY.md`, `memory/YYYY-MM-DD.md`, `memory/shared.md` |
| **Channels** | Mattermost (#executive, #general), iMessage |
| **Apple Access** | ✅ Yes (Notes, Reminders, Calendar, iMessage, Whisper) |
| **Google Access** | ✅ Drive, Calendar (via service account) |
| **Governance Access** | ✅ Full read/write to `smoking-tigers-governance` repo |

---

## Tier 2 — Executive Assistant

| Field | Value |
|---|---|
| **ID** | `ea` |
| **Name** | Eva |
| **Role** | Executive Assistant |
| **Emoji** | 📋 |
| **Model** | `openrouter/anthropic/claude-sonnet-4.6` |
| **Workspace** | `~/.openclaw/workspace/agents/ea` |
| **Status** | ✅ Active |
| **Skills** | apple-notes, apple-reminders, openai-whisper, google-drive, notion |
| **Memory** | `memory/shared.md` (read), daily digest (write) |
| **Channels** | Mattermost (ops channels) |
| **Apple Access** | ✅ Yes (Notes, Reminders) |
| **Google Access** | ✅ Drive, Calendar (read/write STM Operations) |
| **Notion Access** | ✅ Yes (STM workspace) |
| **Auth** | `auth.json`, `auth-profiles.json` |

---

## Tier 3 — Specialist Agents

### Governance Ops

| Field | Value |
|---|---|
| **ID** | `governance-ops` |
| **Name** | Governance Ops |
| **Role** | Governance Operations |
| **Emoji** | ⚖️ |
| **Model** | `openrouter/anthropic/claude-sonnet-4.6` |
| **Workspace** | `~/.openclaw/workspace/agents/governance-ops` |
| **Status** | ✅ Active |
| **Skills** | None configured |
| **Scope** | Charter review, decision log management, MOR compliance |
| **Governance Repo** | `edjieun/smoking-tigers-governance` → *(pending migration to org)* |

---

### Knowledge Ops

| Field | Value |
|---|---|
| **ID** | `knowledge-ops` |
| **Name** | Knowledge Ops |
| **Role** | Knowledge Processing |
| **Emoji** | 📚 |
| **Model** | `openrouter/google/gemini-2.5-pro-preview` |
| **Workspace** | `~/.openclaw/workspace/agents/knowledge-ops` |
| **Status** | ✅ Active |
| **Skills** | None configured |
| **Scope** | Nightly memory digest, session ingestion, shared memory synthesis |
| **Note** | Uses Gemini for long-context document processing |

---

### Sergeant At Arms

| Field | Value |
|---|---|
| **ID** | `sergeant-at-arms` |
| **Name** | Sergeant At Arms |
| **Role** | Governance & Compliance Lead |
| **Emoji** | 🔒 |
| **Model** | `openrouter/anthropic/claude-sonnet-4.6` |
| **Workspace** | `~/.openclaw/workspace/agents/sergeant-at-arms` |
| **Status** | ✅ Active |
| **Skills** | None configured |
| **Scope** | MOR enforcement, health state monitoring, compliance alerts |

---

### Sysops

| Field | Value |
|---|---|
| **ID** | `sysops` |
| **Name** | Doug E Dev |
| **Role** | Ops Lead — System Operations |
| **Emoji** | 🔧 |
| **Model** | `openrouter/anthropic/claude-sonnet-4.6` |
| **Workspace** | `~/.openclaw/workspace/agents/sysops` |
| **Status** | ✅ Active |
| **Skills** | None configured |
| **Scope** | Infrastructure health, server monitoring, service restarts, Cal.com |

---

## Tier 3 — Personal Executive Assistants

### Christine EA (Rosie)

| Field | Value |
|---|---|
| **ID** | `christine-ea` |
| **Name** | Rosie |
| **Role** | Executive Assistant to Christine Francis (SVP) |
| **Emoji** | 🌹 |
| **Model** | `openrouter/anthropic/claude-sonnet-4.6` |
| **Workspace** | `~/.openclaw/workspace/agents/christine-ea` |
| **Status** | ✅ Active |
| **Skills** | google-drive, notion, github |
| **Channels** | Discord (DM-only) |
| **Apple Access** | ❌ No |
| **Principal** | Christine Francis |

---

### Van EA

| Field | Value |
|---|---|
| **ID** | `van-ea` |
| **Name** | *(not configured)* |
| **Role** | Executive Assistant to Van Nguyen |
| **Emoji** | — |
| **Model** | `openrouter/anthropic/claude-sonnet-4.6` |
| **Workspace** | `~/.openclaw/workspace/agents/van-ea` |
| **Status** | ⚠️ Configured, identity incomplete |
| **Skills** | google-drive, notion |
| **Channels** | Discord (DM-only) |
| **Apple Access** | ❌ No |
| **Principal** | Van Nguyen |

---

### Basil EA

| Field | Value |
|---|---|
| **ID** | `basil-ea` |
| **Name** | *(not configured)* |
| **Role** | Executive Assistant to Basil |
| **Emoji** | — |
| **Model** | `openrouter/anthropic/claude-sonnet-4.6` |
| **Workspace** | `~/.openclaw/workspace/agents/basil-ea` |
| **Status** | ⚠️ Configured, identity incomplete |
| **Skills** | google-drive, notion |
| **Channels** | Discord (DM-only) |
| **Apple Access** | ❌ No |
| **Principal** | Basil |

---

## Deprecated / Reserved

| ID | Name | Status | Notes |
|---|---|---|---|
| `sonnetops` | SonnetOps | 🗄️ Reserved | Isolated workspace, not in active rotation |

---

## Shared Infrastructure

| Resource | Value |
|---|---|
| **Google Service Account** | `stai-eva-agent@smoking-tigers-agents.iam.gserviceaccount.com` |
| **GCP Project** | `smoking-tigers-agents` |
| **Client ID** | `103634948961445647526` |
| **Credentials Path** | `~/.openclaw/credentials/google-service-account.json` |
| **Drive Root (STM)** | `1xXxfiMp_RLRQOXp0j7N2JO3B5P71MBk1` |
| **Calendar (STM Ops)** | `ec1f7967b73d7edcdd987d1abb23a08d33bbf69bcf2590200c3651b28e925920@group.calendar.google.com` |
| **Default Model** | `openrouter/anthropic/claude-sonnet-4.6` |
| **Memory Search Model** | `nomic-embed-text` (Ollama local) |
| **Ollama Host** | `http://127.0.0.1:11434` |

---

## Open Items

| # | Item | Priority | Owner |
|---|---|---|---|
| 1 | Create GitHub org `smoking-tigers` and transfer `smoking-tigers-governance` | 🔴 CRITICAL | Ed |
| 2 | Implement CI/CD nightly MOR checks (GitHub Actions) | 🟠 HIGH | Scout |
| 3 | Isolate STM Notion Teamspace; rotate integration tokens | 🔴 CRITICAL | Ed + Scout |
| 4 | Enable Gmail API + grant DWD in Google Admin Console | 🔴 CRITICAL | Ed |
| 5 | Complete `van-ea` and `basil-ea` identity files (IDENTITY.md) | 🟠 HIGH | Scout |
| 6 | Add Discord bot tokens for van-ea and basil-ea | 🟠 HIGH | Ed |
| 7 | Convert Notion "People Pickers" → Team DB Relations | 🟠 HIGH | Scout + Ed |
