---
title: Christine's Agent Workflow Assignment
project: STE Website & Community (OP #6)
assigned-to: Christine Francis
assigned-by: Ed Hwang
date: 2026-07-20
status: Assigned
op_wp: TBD
---

# Your Assignment: Connect Claude to the STE Workflow

This doc is for Christine. It walks you through how to connect your AI agent (Claude) to what Ed has been building — so your agent can access our shared memory, create and update work packages, and help you execute tasks without needing to ask Ed for context every time.

**Time to complete:** ~30–45 minutes for the setup. First task takes another 30 min.

---

## The Big Picture

Here's the workflow pattern we are using at STE:

```
Meeting → Transcript → Spec (plain language) → Work Package (OP) → Agent executes → Reports back to OP
```

You don't need to write code. You don't need to use the terminal. You give your agent:
1. **Context** — who we are, what we're building, what's off limits
2. **A skill** — how to talk to OpenProjects (our task tracker)
3. **A spec** — what you want done, in plain language

Your agent handles the rest.

---

## Step 1: Give Claude STE Context (5 min)

**What to do:** Create a new Claude Project (or open your existing STE one). Add this file as a Project Instruction or drop it in the conversation:

```
File: AGENTS.md
Location: Discovery workspace root
```

**What this gives your agent:**
- Who Ed is, who you are, what STE is building
- What's in scope for agents vs. what requires human decision
- The OP project IDs, Mattermost channels, and workspace layout
- The safety rules (draft ≠ send, no destructive actions without confirmation)

> **Tip:** You can copy-paste the AGENTS.md content directly into a Claude Project Instruction, or ask Ed to share the file via Google Drive or Discord.

---

## Step 2: Give Claude the OpenProjects Skill (5 min)

**What to do:** At the start of any session where you want to create or update work packages, attach this file or paste its contents:

```
File: .github/skills/openprojects/SKILL.md
Location: Discovery workspace
```

**What this gives your agent:**
- The OP project IDs (Website = #6, Camp Audax = #11, etc.)
- How to create, update, and comment on work packages
- The WP description template to use
- Auth details (your agent will need an API key — see Step 3)

---

## Step 3: Get Your OP API Key (2 min)

Ask Ed to:
1. Create a Copilot Agent account for you in OpenProjects, OR
2. Add you as a user to Projects #6 (Website) and #11 (Camp Audax)
3. Generate a Personal API Token for you at: `https://ste-business-server.tailebe6d3.ts.net:8080/my/access_token`

Store the token somewhere safe (password manager or secure note). Your agent will use it like this:

```
AUTH = base64("apikey:YOUR_TOKEN_HERE")
```

> **Note:** You need Tailscale running on your machine to reach the OP server. Confirm with Ed if you don't have it set up.

---

## Step 4: The Spec Coding Pattern (10 min to learn, forever to use)

This is the core of the workflow. Instead of writing code yourself, you write a **spec** — a plain-language description of what you want — and your agent executes it.

### Example: Website copy change

Instead of:
> "I need to update the hero section text"

Write a spec:
```
Spec: Update website hero section

Current text: [paste current text]
New text: [what you want it to say]
File: index.html (or whatever Christine knows the file to be)
GitHub repo: [repo name]
Branch: main

Done when: the change is committed and live at smokingtigers.enterprises
```

Then tell Claude:
```
Follow the spec above. Create a WP in OP Project #6 for this change, 
make the edit in the GitHub repo, commit it, and post the result back 
to the WP as a comment.
```

### Example: Extracting action items from a meeting

After any call with Ed:
```
Here are my notes from today's meeting: [paste notes]

Extract all action items. For each one:
1. Create a work package in the appropriate OP project
2. Set the assignee (Ed or Christine)
3. Set status to New
4. Return the OP#IDs
```

---

## Step 5: Your First Task (30 min)

**Assignment:** Use Claude + the OP skill to update the STE Website project.

1. **Open Claude.** Add AGENTS.md context + attach the OP skill file.

2. **Ask your agent to list open WPs in Project #6:**
   ```
   List all open work packages in OP Project #6 (STE Website & Community).
   ```

3. **Pick one of your assigned WPs and update it.** Your open WPs as of 2026-07-20:

   | OP# | Task |
   |---|---|
   | OP#285 | Research 5–8 AI Ops consortium partners (PandaBlocks is the anchor) |
   | OP#286 | One-pager for David Witzel / Hodgson / Bobby Fishkin (The Gathering invite) |
   | OP#205 | Write hero section copy (this is blocked on Ed drafting 3 value props first) |

4. **For OP#285:** Ask your agent:
   ```
   I've been researching AI Ops companies for the STE consortium. 
   Here's what I have so far: [your notes].
   Post this as a comment on OP#285 and update its status to In Progress.
   ```

5. **Post the OP#ID back to Ed** (Discord or WhatsApp) so he knows you're in the system.

---

## Step 6: Website Deploy Workflow (when you're ready)

The website code lives on GitHub. Your agent can make changes and push them.

```
Local edit (VS Code) → Commit → Push to GitHub → Auto-deploys to smokingtigers.enterprises
```

**What your agent needs:**
- GitHub repo access (you already have write access — both your handles were added June 23)
- VS Code with GitHub Copilot OR Claude with a code execution tool enabled

**The pattern:**
```
Spec: Change [this section] of the website to [this].
File: [filename]
Repo: [repo URL]
Done when: committed to main branch and visible at smokingtigers.enterprises
```

---

## The Transcript Intake Pattern (bonus — for after our first few sessions)

Once you're comfortable with OP, you can use the transcript intake skill to turn any meeting into WPs automatically.

```
File: .github/skills/transcript-intake/SKILL.md
```

After a call with Ed:
1. Export or paste the transcript
2. Attach the transcript-intake skill
3. Tell your agent: "Process this transcript. Extract decisions, action items, and open questions. Create WPs for all action items."

Your agent will create the WPs, post the summary, and return OP#IDs.

---

## Quick Reference

| What you want | How to ask Claude |
|---|---|
| See open tasks | "List open WPs in Project #6" |
| Create a task | "Create a WP in Project #6 for [task]" |
| Update a task | "Mark OP#285 as In Progress" |
| Add notes | "Post a comment on OP#285: [your update]" |
| Close a task | "Close OP#285" |
| Process meeting notes | Use transcript-intake skill |
| Make a website change | Write a spec → agent commits to GitHub |

---

## Files You Need

| File | Where to get it | What it's for |
|---|---|---|
| `AGENTS.md` | Discovery workspace root | STE context for your agent |
| `.github/skills/openprojects/SKILL.md` | Discovery workspace | OP skill |
| `.github/skills/transcript-intake/SKILL.md` | Discovery workspace | Transcript → WPs |
| `docs/how-to-openprojects.md` | Discovery workspace | Human-readable OP guide |
| `docs/projects/STE-website-community.md` | Discovery workspace | Website PRD + open WPs |

**Ask Ed to share these files** via Google Drive or Discord if you don't have access to the Discovery workspace directly.

---

## Questions?

Ping Ed on Discord or WhatsApp. If you get stuck on the API key or Tailscale setup, that's the most likely blocker — flag it and Ed can sort it in 5 minutes.
