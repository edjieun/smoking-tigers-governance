# User File — [Your GitHub Handle]

> **Instructions:** Copy this file to `members/<your-github-username>.md` and fill in your details.
> This file stays on your machine only — it is gitignored and must never be committed to GitHub
> or synced to the shared Google Drive.
>
> ```bash
> cp USER.template.md members/<your-github-username>.md
> ```
>
> Include your registered DID(s) in the Registered Devices section below.
> Get a DID assigned by adding your device to `members/devices.yaml` in a PR.

---

## Identity

- **Name:** [Your full name]
- **Handle:** [Your GitHub handle]
- **Location:** [City, State / Country]
- **Timezone:** [e.g. America/Los_Angeles | America/New_York | Europe/London]
- **Contact:** [Preferred channel — Signal / iMessage / Discord / email]

---

## Registered Devices

| DID | Hostname | Role |
|-----|----------|------|
| ste-did-NNN | your-hostname | [e.g. on-device workstation] |

*Active device (this machine): **ste-did-NNN***

---

## Role at STE

- **Trust level:** observer | contributor | steward  *(pick one)*
- **Projects active on:** [list OP project names, e.g. Project TigerClaw, Camp Audax]
- **What you own:** [brief description of your responsibilities]

---

## Agent Preferences

- **Harness:** Claude | Gemini | ChatGPT  *(pick one — load matching harness file)*
- **Communication style:** [e.g. direct and concise, no filler; or step-by-step with explanations]
- **Filler phrases to avoid:** [e.g. "Certainly!", "Great question!", "Absolutely!"]
- **When to ask vs. proceed:** [e.g. ask before any file moves; proceed on doc drafts without asking]
- **Preferred output format:** [e.g. bullet points, prose, tables]

---

## Hardware

- **Primary machine:** [e.g. MacBook Pro M3, Windows 11 PC, Ubuntu 22.04]
- **OS:** [macOS | Windows | Linux]
- **Local inference:** Ollama | LM Studio | none
- **Models available locally:** [e.g. qwen2.5:7b, llama3.1:8b — or "none"]

---

## Secrets Location

```
~/.ste-secrets/.env
```

Keys you should have set up:
- `OPENPROJECTS_[YOUR_NAME]_API_KEY`  — your OP API key
- `GITHUB_[YOUR_NAME]_PAT`  — your GitHub personal access token
- `COMPOSIO_API_KEY`  — if using Composio MCP (optional)
- `GEMINI_API_KEY`  — if using Gemini harness

---

## Notes

[Anything else your agent should know about how you work, your schedule, or your priorities]
