---
last-updated: 2026-07-16
members: [Ed Hwang, Christine Francis, Van, Basil]
---

# Member SOP — Smoking Tigers AI Operations

This document explains how to participate in the Smoking Tigers AI pipeline:
submitting meeting transcripts, reviewing outputs, and staying coordinated.

---

## Who This Is For

| Member | Email | Status |
|---|---|---|
| Ed Hwang | ed.hwang@quorum.one | Active — Mattermost + Discord |
| Christine Francis | christine.francis@quorum.one | Active — Discord; MM account pending |
| Van | — | Onboarding |
| Basil | — | Onboarding |

---

## The Core Flow

```
Meeting happens
  → Someone records it (Fathom, Zoom, Google Meet)
  → Member posts raw transcript to MM #transcripts
    → Scout (AI agent) processes it automatically
      → #tasks populated with action items
      → #decisions populated with agreements
      → #transcripts gets a summary reply + open questions
```

---

## How to Submit a Meeting Transcript

### Method 1 — Paste raw text (preferred)
Copy the full transcript text from wherever it lives (Fathom, Zoom, Google Docs, anywhere) and paste it directly into Mattermost **#transcripts**.

- ✅ Works for all recording tools
- ✅ No API access needed
- ✅ Scout processes it immediately

### Method 2 — Post a Fathom link
If the meeting was recorded with Fathom, you can post the Fathom meeting URL into **#transcripts**.
Scout will attempt to fetch the transcript automatically. If it can't access the link, it will ask you to paste the raw text instead.

### Who is responsible for posting?
The **person who recorded the meeting** is responsible for posting the transcript. If that's unclear, Ed is the default owner.

For the **Ed + Sage Friday planning meeting**: Ed records and posts.

---

## Mattermost Channels

Access MM at: `https://ste-business-server.tailebe6d3.ts.net:8065`
*(Requires Tailscale to be running on your device)*

| Channel | What it's for | Who should read it |
|---|---|---|
| `#transcripts` | Post meeting transcripts here | Everyone — this triggers the pipeline |
| `#tasks` | Scout posts extracted tasks here after processing | Everyone — check for your name |
| `#decisions` | Scout posts extracted decisions here | Everyone — check for agreements that affect you |
| `#agent-logs` | Scout posts pipeline status and errors | Ed (technical monitoring) |

**To mark a task done:** Reply to the task in `#tasks` with ✅ and a brief note.
Ed or the agent will update the task log in GitHub.

---

## Discord Channels

Discord server: [https://discord.gg/hWhV5zWhM](https://discord.gg/hWhV5zWhM)

Discord is for **team coordination and shared knowledge** — not for pipeline input.

| Channel | What it's for |
|---|---|
| `#knowledge` | All execs add knowledge: links, notes, context, meeting summaries to share with the team |
| General / DMs | Coordination, questions, scheduling |

> 💡 If you're not on Mattermost yet: use Discord for now. Post your transcript link or text in `#knowledge` and tag @Ed — he will relay it to MM `#transcripts` until your MM account is set up.

---

## How to Read Project Docs

Project docs live in GitHub. You can read them without a GitHub account via direct links.
Key docs:
- [Project Registry](https://github.com/edjieun/Discovery/blob/main/docs/project-registry.md) — active projects and status
- [Task Log](https://github.com/edjieun/Discovery/blob/main/docs/task-log.md) — all tasks and decisions
- [Open Questions](https://github.com/edjieun/Discovery/blob/main/docs/open-questions.md) — unresolved questions

*(Links will be updated once the governance repo is public or shared access is set up)*

---

## Transcript Recording SOPs by Tool

### Fathom
1. Fathom auto-records and transcribes when you join a meeting
2. After the meeting, go to fathom.video → your meeting → copy the transcript text
3. Paste into MM `#transcripts`

### Google Meet
1. Start recording in Meet (you need permission from workspace admin)
2. After the meeting, the transcript is in Google Drive
3. Open it, select all, copy, paste into MM `#transcripts`

### Zoom
1. Enable cloud recording + auto-transcription in Zoom settings
2. After the meeting, go to zoom.us → Recordings → open the transcript
3. Copy text, paste into MM `#transcripts`

---

## Verification Test

The first end-to-end test will use the **Ed + Sage Friday planning meeting**:
1. Ed records the meeting
2. Ed posts the raw transcript to MM `#transcripts`
3. Scout processes it → tasks appear in `#tasks`, decisions in `#decisions`
4. Both Ed and Christine review the output

After this test, update the OpenRouter credit balance to track any cloud spend.

---

## Getting Help

- **Mattermost / pipeline issues:** Post in `#agent-logs` or DM Ed
- **Discord questions:** DM Ed or post in general
- **Project questions:** See project docs links above or ask in Discord `#knowledge`
