
# Contributor Onboarding — Smoking Tigers Enterprises
*Access guide for STE contributors: OpenProjects, Notion, Google Drive, and the TigerClaws agent workspace.*

---

## Before You Start: Your Quorum1 Account

All STE tools are tied to your **`@quorum.one` Google account**. You need this to access Google Drive and Notion.

If you don't have one yet, request from q1.

---

## What You're Getting Access To

| Tool | What it's for |
|---|---|
| **Notion** | Project spaces, member pages, governance docs, creative planning |
| **Google Drive (TigerClaws)** | The Discovery workspace — shared context for AI agents and project files |
| **OpenProjects** | Work packages, Kanban boards, roadmaps, spec-coded tasks |
| **TigerClaws agent harness** | Plug your own AI into the shared workspace to read context and create tasks |

---

## Step 1: Access Notion

Notion is where project spaces, member pages, and creative planning live. Access requires an invitation — ask Ed to grant you access to the spaces you need.

Log in using your `@quorum.one` Google account at [notion.so](https://www.notion.so).

You've already been invited. If a link shows a "request access" prompt, your invite may have expired — just let Ed know and he'll re-invite you.

### Notion Spaces

| Space | Link |
|---|---|
| Smoking Tigers Home | [Open](https://app.notion.com/p/quorum1/Smoking-Tigers-Home-2ac6f6ac689e815d8721faafa5709ca9?source=copy_link) |
| Artist / Creator Hub | [Open](https://app.notion.com/p/quorum1/Artist-Creator-Hub-DB-2af6f6ac689e809ea5e4c23b41b2c0cf?source=copy_link) |
| RMA Dashboard | [Open](https://app.notion.com/p/quorum1/Regenerative-Media-Alliance-Dashboard-33d6f6ac689e802ab3a6ea287d4fa8ec?source=copy_link) |
| The Gathering / Camp Audax | [Open](https://app.notion.com/p/quorum1/The-Gathering-Camp-Audax-3976f6ac689e8005a6cdd68db6e97786?source=copy_link) |

---

## Step 2: Access the TigerClaws Google Drive

The TigerClaws Drive is the shared project file system. You need your `@quorum.one` account to access it.

| Folder | Link |
|---|---|
| TigerClaws (root) | [Open](https://drive.google.com/drive/folders/1Rq-7tqxc6yzlOVMp7rrCugCollVzasnk) |
| Discovery workspace | [Open](https://drive.google.com/drive/folders/1rx2r5T4hQO9A2ePytJXsuuYOfA5kuCgz?usp=sharing) |

The **Discovery** folder is the main workspace your AI agent will use. It contains all project context, harness files, and shared docs.

---

## Step 3: Connect to the Private Network (Tailscale)

Our server is private — you need Tailscale to reach it.

**Download:** [tailscale.com/download](https://tailscale.com/download)
Available for Mac, Windows, iOS, Android.

> **Already using Tailscale for something else?** That's fine — you can be on multiple tailnets. The STE invite link adds the STE network alongside your existing one. You can switch between them.

You've already been invited to the STE tailnet. Check your email for the Tailscale invite. If you can't find it or it expired, ask Ed and he'll send a new one.

Tailscale runs quietly in the background after setup. You don't need to think about it again.

---

## Step 4: Log Into OpenProjects

Once Tailscale is connected:

**Open this URL in your browser:**
```
https://ste-business-server.tailebe6d3.ts.net:8080
```

You've already been invited — check your email for credentials. If you didn't receive them or need a re-invite, message Ed.

The **RMA project** is already set up in there — you'll see it when you log in. It has Kanban boards, work packages, and task breakdowns ready to go.

---

## Step 5: Create Your Personal Access Token

Your AI agent needs an API key to create and update tasks on your behalf.

1. Log into OpenProjects
2. Click your **avatar** (top right)
3. Go to **My Account → Access Tokens**
4. Click **+ Add access token**
5. Give it a name (e.g. `my-agent`)
6. Copy the token — **you only see it once**
7. Save it somewhere safe (recommended: `~/.ste-secrets/.env` as `OPENPROJECTS_[YOUR_NAME]_API_KEY`)

---

## Step 6: Set Up Your Agent Harness

Open the **Discovery** folder from Google Drive in your AI tool of choice (Claude, Copilot, Gemini, ChatGPT).

1. Open the folder in your AI tool
2. Read `START_HERE.md` first — it walks you through the full setup
3. Based on your tool, load the matching harness file:

| You're using | Read this |
|---|---|
| Claude / GitHub Copilot | `claude.md` |
| Gemini / OpenCode + Gemini | `gemini.md` |
| ChatGPT / Codex | `codex.md` |

4. Create your personal user file (stays local, never shared):
   ```
   cp USER.template.md members/<your-github-username>.md
   # edit with your name, timezone, and preferences
   ```

5. Store your OP API key in your local secrets file:
   ```
   # ~/.ste-secrets/.env
   OPENPROJECTS_[YOURNAME]_API_KEY=your-token-here
   ```

6. On every session start, your agent should read in this order:
   - `SOUL.md`
   - `members/<your-github-username>.md` (your user file)
   - `AGENTS.md`
   - `MEMORY.md`
   - Your harness file

---

## Step 7: Find Your Project in OpenProjects

Once you're logged in, look for your project(s) in the left sidebar. Ed will confirm which ones you've been added to.

From there you can:
- View the **Kanban board** (Boards view)
- See open **Work Packages** (task list)
- Check the **Roadmap** (timeline view)
- Add comments, update status, assign tasks

Your agent can also interact with OpenProjects directly using your API key — creating tasks from meeting notes, updating statuses, and logging decisions automatically.

---

## Questions?

Reach out to Ed on Telegram or DM Scout in Mattermost once you're connected.

---

*This doc is maintained in the Discovery workspace → `docs/contributor-onboarding.md`*
