---
last-updated: 2026-07-19
status: live
---

# Mattermost — STE Channel Guide

**URL:** `https://ste-business-server.tailebe6d3.ts.net:8065`  
**Team:** `smoking-tigers-enterprises`  
**Admin:** `edlicious` (ed@quorum.one)

---

## Channels

| Channel | Purpose | Who posts |
|---|---|---|
| `#transcripts` | Drop meeting transcripts here. Scout processes automatically. | Humans |
| `#tasks` | Scout-extracted action items from transcripts | Scout (auto) |
| `#decisions` | Scout-extracted decisions from transcripts | Scout (auto) |
| `#agent-logs` | Scout status, errors, job completions | Scout (auto) |

## How it works

1. You drop a meeting transcript (text or summary) into `#transcripts`
2. Scout reads it, extracts decisions and tasks
3. Scout posts extracted tasks to `#tasks`, decisions to `#decisions`
4. Open questions are surfaced in `#agent-logs`

## Members

| Username | Role | Channels |
|---|---|---|
| `edlicious` | Admin | All |
| `scout` | Bot (Scout agent) | All |
| `christine` | Member | #transcripts, #tasks, #decisions |
| Van | Pending setup | TBD |
| Basil | Pending setup | TBD |

## Scout bot account

- Username: `scout`
- Token stored in: `~/.openclaw/channels.mattermost.accounts.default.botToken`
- Bound to `#transcripts` — Scout listens for new messages there

## Access from mobile

Download Mattermost from App Store / Play Store and connect to:
`https://ste-business-server.tailebe6d3.ts.net:8065`

## Posting a transcript for processing

Just paste the transcript text into `#transcripts`. You can mention `@scout` to
trigger immediate processing, or Scout will pick it up on the next message event.

Format hint — paste with a header so Scout knows the context:
```
**Meeting:** [Title] — [Date]
**Participants:** Ed, Christine, ...

[transcript text here]
```
