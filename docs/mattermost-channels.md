---
last-updated: 2026-07-19
status: live — simplified to single channel (#tigerclaw)
---

# Mattermost — STE Channel Guide

**URL:** `https://ste-business-server.tailebe6d3.ts.net:8065`  
**Team:** `smoking-tigers-enterprises`  
**Admin:** `edlicious` (ed@quorum.one)

> **Simplified 2026-07-19** — All agent I/O consolidated to `#tigerclaw`.
> Nerve deprioritized. Legacy channels removed.

---

## Active Channels

| Channel | Purpose | Who posts |
|---|---|---|
| `#tigerclaw` | **Primary channel** — post transcripts, commands, questions. Scout-cos responds and creates OP work packages. | Humans + Scout-cos (auto) |
| `#general` | Team general chat | Humans |
| `#town-square` | Default MM channel | — |
| `#announcements` | Team announcements | Admin |

**Removed 2026-07-19:** #transcripts (renamed → #tigerclaw), #tasks, #decisions, #agent-logs, and all legacy ops channels.

---

## How it works

1. Post a transcript, command, or question to `#tigerclaw`
2. Scout-cos reads it and processes
3. Scout-cos posts results back to `#tigerclaw`
4. Scout-cos creates OpenProjects work packages and posts OP#IDs

---

## Members

| Username | Role | Channel |
|---|---|---|
| `edlicious` | Admin | All |
| `scout-cos` | Bot (OpenClaw Scout agent) | #tigerclaw |
| `christine` | Member | #tigerclaw |
| Van | Pending setup | #tigerclaw |
| Basil | Pending setup | #tigerclaw |

---

## How to post a transcript

Paste the transcript text into `#tigerclaw` with a header:

```
**Meeting:** [Title] — [Date]
**Participants:** Ed, Christine, ...

[transcript text here]
```

Scout-cos will respond with a summary and create OP tasks/decisions automatically.

---

## Access from mobile

Download Mattermost from App Store / Play Store and connect to:
`https://ste-business-server.tailebe6d3.ts.net:8065`
