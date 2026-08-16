# SOP: File & Document Intake via Mattermost
**Status:** Active  
**Owner:** Scout (Chief of Staff)  
**Applies to:** All exec team members with Mattermost access (Ed, Christine, Basil, Van)  
**Last updated:** 2026-03-20  

---

## Purpose

This SOP defines how exec team members submit files, documents, PDFs, and other reference materials to the AI agent pipeline via Mattermost — without requiring direct server access.

Direct server access (Desktop intake folder) is available to Ed only when on the server. This process covers all other scenarios.

---

## When to Use This Process

Use this process when you want to:
- Share a PDF, document, or file for Scout or another agent to review
- Submit a voice memo transcript, meeting notes, or briefing
- Feed reference material into a project or task
- Route a file for knowledge processing

---

## How to Submit a File

### Step 1 — Upload to Google Drive
Upload the file to the **ST Shared Drive** in the designated intake folder:

> **Drive path:** `Smoking Tigers / Intake`

If you do not have access to this folder, contact Ed or Scout via Mattermost.

### Step 2 — Post the Link in Mattermost
In the **#executive** channel (or your agent's DM), post a message with:
1. The **Google Drive link** to the file
2. A brief description of what it is and what you need done

**Example:**
> Scout — here's a PDF from the Nick call notes. Please review and update tasks accordingly.
> https://drive.google.com/file/d/[file-id]/view

### Step 3 — Tag Scout (or the relevant agent)
Make sure your message mentions `@scout` (or the appropriate agent) so it's picked up.

---

## What Happens Next

Once submitted:
1. Scout (or the assigned agent) retrieves the file from Drive
2. Reads and processes the content
3. Updates tasks, projects, or knowledge base as instructed
4. Confirms completion in Mattermost

Expected turnaround: within the same session (immediate if Scout is active).

---

## File Types Supported

| Type | Notes |
|------|-------|
| PDF | Text-readable PDFs preferred. Scanned/image-only PDFs may have limited support. |
| Google Docs | Share link directly — no download needed |
| .md / .txt | Plain text files — post Drive link or paste content directly |
| Voice memo transcripts | Paste transcript text directly in Mattermost message |
| Images | Post Drive link; Scout will analyze if vision-capable model is active |

---

## Limitations

- **OpenClaw does not fetch Mattermost file attachments.** Do not attach files directly to Mattermost messages — they will not be received by the agent. Always use a Drive link.
- Files must be in the **STM Shared Drive** or accessible to the service account (`stai-eva-agent@smoking-tigers-agents.iam.gserviceaccount.com`).
- Files outside the allowed Drive scope will not be accessible.

---

## Ed: Direct Server Access (Fastest Path)

When on the server, Ed can still use the fastest method:

> Drop the file into `~/Desktop/intake/` — Scout picks it up on the next heartbeat cycle automatically.

No Mattermost message required.

---

## Questions / Issues

Post in **#executive** and tag `@scout`.

---

*Maintained by Scout. Changes require exec approval.*
