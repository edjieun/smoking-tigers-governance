# TOOLS.md – Local Setup
Environment-specific configuration.
This file documents capabilities. It does not grant authority.

---

## User Context
All tools execute within the current macOS user context.
Apple ecosystem access (iCloud, Messages, Calendar, Reminders, Notes, Keychain)
is permitted for Scout (Chief of Staff) only.
Other agents must not run under a user account with Apple login enabled.

---

## Models (Ollama @ http://127.0.0.1:11434)

| Model | Tag | Purpose |
|---|---|---|
| qwen2.5 14B | qwen2.5:14b-instruct | Scout default, complex reasoning |
| qwen2.5 7B | qwen2.5:7b-instruct | Specialist agents, light reasoning |
| qwen2.5 3B | qwen2.5:3b-instruct | Mechanical tasks, formatting, extraction |
| nomic-embed-text | nomic-embed-text:latest | Embeddings only |
| lfm2.5-thinking | lfm2.5-thinking:1.2b | Reserved for future use |

Scout runs on qwen2.5:14b-instruct by default.
Claude Opus may be used only when explicitly configured or instructed.

---

## Spawnable Agents
- `ea` — Executive Assistant (calendar, notes, reminders, email)
- `sysops` — System Operations (health checks, monitoring, security)

Spawn with:
`sessions_spawn(agentId: "ea"|"sysops", task: "...")`

Spawning must follow Safety and External rules in AGENTS.md.

---

## Apple Integrations (Scout Only)
Available only when running under Apple-enabled macOS user.

| Tool | Purpose |
|---|---|
| memo | Notes |
| remindctl | Reminders |
| icalBuddy | Calendar |
| Whisper | Local speech-to-text |
| iMessage | External surface |

Rules:
- No Apple tool use from non-Scout agents.
- iMessage always requires explicit instruction.
- Draft before send.
- Treat Messages and Keychain as high-sensitivity surfaces.

---

## Security Notes
- No agent runs as root unless explicitly required.
- Do not grant Full Disk Access unnecessarily.
- Apple access is enforced by macOS user separation, not agent policy alone.
- Future agents should run under a non-iCloud macOS user.

---

Keep this file factual. No behavioral rules here.