# Discovery Workspace

**Owner:** Ed Hwang | **Last updated:** 2026-07-16
**Part of:** [Smoking Tigers AI](docs/adr/0001-smoking-tigers-ai-domain-model.md) — decentralized AI operations network

This is Ed's personal planning workspace on his local laptop. It is the root node for organizing all active projects, processing meeting transcripts, and building out the Smoking Tigers AI system.

---

## How This Workspace Works

```
Meeting (Fathom / Google Meet / Zoom)
  → Transcript  →  Transcripts/[Project]/
    → Chunks    →  chunks/             (chunk-transcript.sh)
      → Memory Cards → Memory/         (one card per topic)
        → /Process Memory Card prompt
          → docs/task-log.md           (tasks + decisions)
          → docs/open-questions.md     (unresolved questions)
```

**Key docs:**
- [`docs/adr/0001-smoking-tigers-ai-domain-model.md`](docs/adr/0001-smoking-tigers-ai-domain-model.md) — canonical domain model and architecture decisions
- [`docs/glossary.md`](docs/glossary.md) — canonical vocabulary for all agents and docs
- [`docs/project-registry.md`](docs/project-registry.md) — all active projects with status and blockers
- [`docs/task-log.md`](docs/task-log.md) — all tasks and decisions extracted from meetings
- [`docs/open-questions.md`](docs/open-questions.md) — unresolved questions from all meetings
- [`copilot/copilot-custom-prompts/Process Memory Card.md`](copilot/copilot-custom-prompts/Process%20Memory%20Card.md) — agent prompt for processing new Memory cards into the task log

**Governance rules:**
- Agents are tools, not members. Humans are accountable for agent actions.
- GitHub commits and LedgerSMB writes require human approval before execution.
- Projects require member agreement + defined outcome to be in the registry (otherwise they're **topics**).

---

## Active Projects (summary)

See [`docs/project-registry.md`](docs/project-registry.md) and `docs/projects/` for full detail.

| Project | Status | Immediate Blocker / Next Action |
|---|---|---|
| [STE Website & Community Launch](docs/projects/STE-website-community.md) | Active | Ed to draft 3 website value props; Christine iterating design |
| [Camp Audax / The Gathering](docs/projects/camp-audax-gathering.md) | Active — blocked | Victor must answer 5 questions before Brad outreach |
| [RMA New Meeting Flow](docs/project-registry.md) | Active | Friday: Ed + Sage planning session (new 3-meeting format) |
| [Smoking Tigers AI Buildout](docs/projects/smoking-tigers-ai-buildout.md) | Phase 2 ✅ | Friday: first full pipeline test with @scout + Ed+Sage transcript |

---

## Workspace Structure

```
Discovery/
├── docs/                        ← operational docs (ADRs, glossary, logs)
│   ├── adr/                     ← architecture decision records
│   ├── glossary.md
│   ├── project-registry.md
│   ├── task-log.md
│   └── open-questions.md
├── Memory/                      ← RAG corpus: atomic topic cards from meetings
├── Transcripts/                 ← raw meeting transcripts (not indexed by RAG)
├── chunks/                      ← token-safe transcript fragments
├── scripts/                     ← chunk-transcript.sh and infrastructure scripts
├── copilot/
│   └── copilot-custom-prompts/  ← agent prompts (incl. Process Memory Card)
├── RMA/                         ← RMA project notes
├── Smoking Tigers Studio/       ← STE project workspace
└── readme.md                    ← this file
```

---

## About This Workspace

This is Ed's personal planning workspace — the root node of the Smoking Tigers AI network. It runs on the M4 laptop and connects to the Mac Mini (inference + agent executor) and M1 MacBook (OpenProjects) over Tailscale.

**What this workspace does:**
- Organizes all active projects for Ed and the STE team
- Processes meeting transcripts into structured memory cards
- Feeds the Mattermost pipeline (transcript → tasks → decisions)
- Hosts the domain model, glossary, ADRs, and operational docs for the system

**Other workspaces that need to be standardized to this structure:**
- Gathering / Camp Audax workspace
- Smoking Tigers Enterprises website workspace
- Media workspace

See `docs/projects/smoking-tigers-ai-buildout.md` for the full system architecture and what's been built.

# current projects
- we have processed 5 meeting notes 
- we bypassed using local ai to work on camp audax/the gathering
- these need to be organized
- there are some pre-existing workspaces for things like the 
	- the gathering/camp audax, 
	- smoking tigers enterprises website, 
	- Media
	- that need to be organized like Discovery, to be usable with smoking tigers ai.
- these meetings notes have been organized into memory, so the mac mini should be able to do this work using local ai. we need to make sure the mac mini setup is capable of keeping projects updated from the meeting notes.

# new projects
we need a discovery processes for the different ways we scope projects
create a template for a discovery meeting agenda, with the right questions to inject into the conversation to scope what the project is
- we should come up with an agentic process
	- once meeting is done, to get the meeting notes and add them to shared memory
	- we use multiple video conferencing tools and need an SOP for all of them. for example
	- fathom
	- google meet
	- zoom
- we want to start moving data to the right source of truth
	- github
		- gov repo 
		- agent
		- code
		- etc...
	- on the m1 mac and other shared servers beyond just what is on premise at ed's
		- openprojects
			- Agents should be what uses this on behalf of a member
			- maintains the data logs for the project
			- tracks meetings
			- tracks tasks
			- tracks assignment completion
			- planning and setting dates and deadlines
			- keeping members coordinated and well communicated
			- work with ledgersmb for business operations
			- track ai token usage by models
				- public
				- local
	- ledgersmb
		- keep track of costs
			- openrouter
				- using public models costs money 
				- spending needs to be tracked
	- mattermost
		- channels need
	- obsidian
	- google
	- notion
	- etc...

# Updates to current projects
comms were sent in various channels, we should update and plan for next comms and meetings.
add transcripts and more links and knowledge resources that add more context.

I need to start finding and feeding it to the mac mini to process.

# RMA New Flow
Sage and I discussed a new flow, a three meeting flow, e.g. mondays are a planning meeting. wed are a recording meeting, fridays is for governance and reviewing what we created and making decisions about it.

we want to present this to the team on the next wednesday meeting, 
- sage and ed are meeting on Friday to do our first planning for meeting two, where we record it as a podcast
- i want to create an agenda template that we can follow that allows us to scope the requirements
- this will create meeting artifacts
- we want to create the right artifacts that we can use
- we are going to scheduling a recording session before next wed.
- 