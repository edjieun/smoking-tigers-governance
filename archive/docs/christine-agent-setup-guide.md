# Christine Francis — Agent Setup Guide
**For:** Christine's AI agent  
**Version:** 1.0 — 2026-07-21  
**Author:** Copilot Agent (generated from OP#311)  
**Post to:** Discord for Christine to hand to her agent

---

## What This Guide Does

This guide configures your AI agent to work within the STE / Smoking Tigers system. Follow each step in order. Your agent should execute these steps on your behalf where possible.

---

## Step 1: Verify Tailscale Connection

Tailscale gives you access to the STE Business Server (OpenProject, Mattermost).

1. Open the Tailscale app on your device
2. Confirm status shows **Connected** and the STE tailnet is active
3. If it shows "Session expired" or prompts for re-auth: click the login button — it's a one-click token refresh (90-day rotation)
4. Verify access: open `https://ste-business-server.tailebe6d3.ts.net:8080` in your browser — you should see the OpenProject login page

---

## Step 2: OpenProject Access

Your account is already created and active: **pinwheelsforreal@gmail.com**

1. Go to: `https://ste-business-server.tailebe6d3.ts.net:8080`
2. Log in with your Gmail account
3. You should see these projects: STE Operations, Project TigerClaw, RMA, Camp Audax
4. To get your **API key** for your agent:
   - Click your avatar → **My Account** → **Access Tokens**
   - Create a new token, copy it
   - Store it as `OPENPROJECTS_CHRISTINE_API_KEY` in your secrets file (see Step 6)

---

## Step 3: GitHub Personal Access Token

You already have one from the Coherence build weekend — use that, or create a new one.

**To create a new one:**
1. Go to: `https://github.com/settings/tokens`
2. Click **Generate new token (classic)**
3. Scopes needed: `repo`, `read:org`, `workflow`
4. Copy the token and store it as `GITHUB_CHRISTINE_PAT` in your secrets file

**Repos your agent needs access to:**
- `edjieun/smoking-tigers-governance` (read/write for governance docs)
- Any STE project repos (read)

---

## Step 4: Notion Access Token

1. Go to: `https://www.notion.so/my-integrations`
2. Click **New integration**
3. Name it: `Christine-Agent`
4. Select your Notion workspace
5. Copy the **Internal Integration Token**
6. Store as `NOTION_CHRISTINE_TOKEN` in your secrets file

**Pages to connect your integration to** (open each page → Share → invite your integration):
- STE Members DB
- STE Shared Workspace (top-level)

---

## Step 5: Google Drive Access

Your Google Drive (via `christine.francis@quorum.one` or personal Gmail) is your preferred workspace.

For your agent to read/write Google Drive files:
1. Go to: `https://console.cloud.google.com/`
2. Create a project (or use an existing one)
3. Enable the **Google Drive API**
4. Create an **OAuth 2.0 credential** (Desktop app type)
5. Download the `credentials.json`
6. Run the auth flow once to generate `token.json`
7. Store both files in your agent's secure config directory

**Alternative (simpler):** Use Google AI Studio (`aistudio.google.com`) with your `christine.francis@quorum.one` account — Gemini can read/write Drive files natively with Workspace auth.

---

## Step 6: Store Secrets

Create a secrets file at `~/.ste-secrets/.env` (or equivalent for your setup):

```bash
# STE Agent Secrets — Christine Francis
OPENPROJECTS_URL=https://ste-business-server.tailebe6d3.ts.net:8080
OPENPROJECTS_CHRISTINE_API_KEY=<your OP API key from Step 2>
GITHUB_CHRISTINE_PAT=<your GitHub token from Step 3>
NOTION_CHRISTINE_TOKEN=<your Notion token from Step 4>
```

Keep this file private — do not commit to GitHub.

---

## Step 7: Agent Identity Config

Create two files for your agent's identity (equivalent to Ed's `SOUL.md` and `USER.md`):

### `SOUL.md` — Who Your Agent Is
```markdown
# Agent Identity — Christine's STE Agent

## Role
Chief Synthesis Officer support — documentation, planning, meeting synthesis, 
governance facilitation for Smoking Tigers Enterprises.

## Primary Skills
- Coherence synthesis model (transcript → insight extraction)
- Governance facilitation (ADR creation, decision logging)
- OpenProject work package management
- Google Drive document creation and management

## Access
- OpenProject: STE Operations, TigerClaw, RMA, Camp Audax projects
- GitHub: smoking-tigers-governance repo (read/write)
- Notion: STE Members DB, STE Shared Workspace
- Google Drive: Christine's shared workspace
```

### `USER.md` — About Christine
```markdown
# User Context — Christine Francis

## Identity
- Name: Christine Francis
- Role: Chief Synthesis Officer, STE
- Email (STE): christine.francis@quorum.one
- Email (personal): pinwheelsforreal@gmail.com
- OP Account: pinwheelsforreal@gmail.com (ID:11)

## Preferences
- Prefers Google Docs over Obsidian
- Uses Claude via Quorum1 Code ($20 cap) — transitioning to Gemini
- Familiar with GitHub commit/PR workflow (Coherence build weekend)
- Comfortable with synthesis and high-level schema work; less interested in low-level infra

## Key Projects
- STE Operations (onboarding, governance)
- RMA — New Meeting Flow (Coherence TV integration)
- Camp Audax (synthesis, outreach)
```

---

## Step 8: Install the OpenProject Skill

Your agent needs the `/openprojects` skill to create and update work packages.

The skill file is in the STE governance repo:
```
https://github.com/edjieun/smoking-tigers-governance
→ .github/skills/openprojects/SKILL.md
```

1. Clone or pull the repo
2. Point your agent's harness at the skill file
3. Test: ask your agent to list open WPs in STE Operations

---

## Step 9: Verify End-to-End

Run this checklist with your agent:

- [ ] Tailscale connected — can reach `https://ste-business-server.tailebe6d3.ts.net:8080`
- [ ] OpenProject login works
- [ ] Agent can list open WPs: `/openprojects list STE Operations`
- [ ] Agent can post a comment on a WP
- [ ] GitHub PAT works: `git clone https://github.com/edjieun/smoking-tigers-governance`
- [ ] Notion token works: agent can read the STE Members DB

---

## Reference: Key Links

| Resource | URL |
|---|---|
| OpenProject | `https://ste-business-server.tailebe6d3.ts.net:8080` |
| Governance Repo | `https://github.com/edjieun/smoking-tigers-governance` |
| Notion Integrations | `https://www.notion.so/my-integrations` |
| Google AI Studio | `https://aistudio.google.com` |
| GitHub Tokens | `https://github.com/settings/tokens` |
| Tailscale Admin | `https://login.tailscale.com/admin` |

---

*Generated by Copilot Agent — OP#311 — 2026-07-21*
