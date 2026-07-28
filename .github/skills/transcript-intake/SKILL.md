---
name: transcript-intake
description: "Process a meeting transcript through the TigerClaw pipeline. Use when: a meeting has happened and needs to be processed, Ed has a raw transcript to submit, tasks or decisions need to be extracted into OpenProjects."
argument-hint: "paste transcript text or provide source (Fathom, Zoom, etc.)"
---

# Transcript Intake Skill

Submits a meeting transcript to the TigerClaw pipeline via Mattermost `#tigerclaw`,
then tracks the resulting OP work packages.

## Pipeline

```
Transcript text
  → Post to Mattermost #tigerclaw
    → Scout-cos (Mac Mini) processes automatically
      → Extracts tasks + decisions → OpenProjects WPs
      → Posts OP#IDs back to #tigerclaw
        → ZeroClaw stores memory
```

**Definition of done:** OP#IDs are visible in `#tigerclaw`.

---

## Procedure

### Step 1 — Prepare the transcript

Accepted sources:
- Fathom export (copy raw text)
- Zoom transcript (.vtt or .txt — paste text, not file attachment)
- Google Meet transcript
- Voice memo transcript (paste text directly)

⚠️ Do NOT attach files to Mattermost — OpenClaw does not read attachments. Paste text only.

### Step 2 — Post to #tigerclaw

```
Channel: #tigerclaw
URL:     https://ste-business-server.tailebe6d3.ts.net:8065
```

Format the message:

```
[Meeting name] — [YYYY-MM-DD]

[Paste full transcript text here]
```

No `@scout` mention needed — Scout-cos monitors the channel automatically.

### Step 3 — Wait for Scout response

Scout responds within ~60 seconds with:
- Summary of the meeting
- Extracted tasks (each with OP#ID)
- Extracted decisions (each with OP#ID)

If no response after 2 minutes → check Scout status (see Troubleshooting).

### Step 4 — Review and log

1. Confirm all OP#IDs are correct and assigned
2. Note any WPs that need reassignment or additional context
3. If Copilot created any WPs during the session, post their IDs to `#tigerclaw` as well
4. Update today's daily note (`YYYY-MM-DD.md`) with:
   ```
   ✅ [Meeting name] processed → OP#xxx, OP#xxx, OP#xxx
   ```

---

## Troubleshooting

| Symptom | Check |
|---|---|
| No Scout response after 2 min | SSH to Mac Mini → `launchctl list \| grep openclaw` |
| Scout responds but no OP#IDs | OpenProjects may be unreachable — check M1 MacBook is on |
Mac Mini SSH: `ssh edhwang@192.168.1.253` (or Tailscale: `100.122.103.40`)

Scout logs: `~/.openclaw/logs/` on Mac Mini

---

## Rules

- Paste text only. No Mattermost file attachments.
- One transcript per message. Don't batch multiple meetings.
- Every processed transcript produces at least one OP#ID.
