---
last-updated: 2026-07-16
maintainer: Ed Hwang
source-adrs: [docs/adr/0001-smoking-tigers-ai-domain-model.md]
---

# Smoking Tigers AI — Canonical Glossary

> Terms are organized by domain. Each entry has a **canonical term**, definition, and **Avoid** note to prevent synonyms from creeping into docs and prompts.

---

## Operations & Governance

- **Smoking Tigers AI:** The umbrella organization and distributed AI operations network. Also tracked as a buildout project in its own right.
  _Avoid_: STE (that's Smoking Tigers Enterprises, a sub-entity), "the co-op" (too generic)

- **Organization:** The root entity in the domain model. Smoking Tigers AI, STE (Smoking Tigers Enterprises), Quorum1, and RMA contexts are peer organizations with relationships — not a strict hierarchy.
  _Avoid_: company, group (too vague)

- **Member:** A human participant in one or more Organizations or Projects. The same person can hold different roles across contexts (e.g., Ed is a member of both RMA and Smoking Tigers). Members are accountable for any Agent actions taken under their configuration.
  _Avoid_: user, contributor (overloaded), employee

- **Project:** A scoped effort that meets all four criteria: (1) has a GitHub repo or workspace folder, (2) has been discussed in at least one meeting, (3) has a defined outcome or deliverable, (4) has member agreement (at least one member who has agreed to participate). Things that don't meet all four are **topics**, not projects.
  _Avoid_: initiative, effort (too vague)

- **Topic:** A subject discussed in meetings that has not yet qualified as a Project. May evolve into a project when criteria are met.
  _Avoid_: project (premature), idea

- **Decision:** A recorded agreement between members. Separate from tasks — a decision is an agreement about direction or policy, not an action to perform. Extracted from meeting transcripts by an agent. Stored as a Governance Record in GitHub (requires human approval to commit).
  _Avoid_: conclusion, outcome (too vague), action item (that's a Task)

- **Task:** An action assigned to a specific Member, linked to a Project. Has an owner, a due date (ideally), and a status. Extracted from meeting transcripts by an agent. Status lifecycle: open → assigned → done.
  _Avoid_: action item (informal), to-do (informal)

- **Open Question:** A question raised during a meeting that was not resolved before the meeting ended. Flagged by an agent during transcript processing. Becomes a Decision once resolved, or a Task if action is required to answer it.
  _Avoid_: parking lot item (too informal)

- **Governance Record:** A formalized artifact in the GitHub governance repo that records a Decision. Three forms: ADR (append-only markdown), Issue (closed = decided), Living Doc (mutable, per context).
  _Avoid_: decision log entry (too vague), note

- **ADR (Architecture Decision Record):** A append-only governance record documenting a significant decision, its context, and its consequences. Stored in `docs/adr/` within a workspace. Format: status, context, decision, consequences.
  _Avoid_: decision doc (too vague)

---

## Meetings & Transcripts

- **Meeting:** An event that produces a Transcript. Linked to one or more Projects. Participants are Members. Sources: Fathom, Google Meet, Zoom.
  _Avoid_: call, sync (too informal for system context)

- **Transcript:** The raw text artifact produced by a Meeting. Processed into Chunks, then into Memory files. Source of all Decisions, Tasks, and Open Questions.
  _Avoid_: notes (that implies human curation), recording

- **Chunk:** A token-safe fragment of a Transcript, produced by `scripts/chunk-transcript.sh`. Typically ~12,000 words per chunk. Each chunk carries project/date/chunk-number context in its header.
  _Avoid_: segment, section (too generic)

- **Memory File / Card:** An atomic summary markdown file extracted from one or more Chunks, covering a single topic segment from a meeting. Stored in `Memory/`. Named `[Project] - [YYYY-MM-DD] - [Topic Slug].md`. Contains: summary, decisions, action items, key quotes, open questions.
  _Avoid_: summary doc, notes file

- **Dump Interface:** The entry point for unstructured inputs (Fathom meeting links, file paths, raw text) into the agent pipeline. Currently the Mattermost `#transcripts` channel. Target: accept any input format without hardcoded paths.
  _Avoid_: input folder, watch folder

---

## Agents & Infrastructure

- **Agent:** A software tool, not a member. Accountable to the Member who configured it. Operates as a named Role (e.g., "Meeting Processor", "Task Tracker", "Comms Drafter"), not a person identity.
  _Avoid_: bot, assistant (implies personhood), worker

- **Role:** The function an agent performs in the system. Roles are attached to agents, not people. Examples: Meeting Processor, Task Extractor, Project Tracker, Comms Drafter.
  _Avoid_: agent name (roles outlive specific agent implementations)

- **Workspace:** A VS Code workspace folder scoped to a project or context. Each workspace is a node in the Smoking Tigers AI network. All workspaces must follow consistent structure (Memory/, Transcripts/, chunks/, docs/) to be agent-usable.
  _Avoid_: folder, directory (too generic)

- **Infrastructure Node:** A physical or virtual compute resource in the Smoking Tigers AI network. Connected via Tailscale.
  _Avoid_: machine, computer (too generic)

- **Inference Server:** The M4 Mac Mini running LM Studio in server mode. Accepts API calls over Tailscale. Runs local models only. Phase 1 role: inference only, no agent harness.
  _Avoid_: compute node, AI server, home server

- **Executor:** The M4 Mac Mini running OpenClaw (Phase 2+). Receives Specs from OpenProjects or Mattermost, runs them using local models, reports completion. Hard local block enforced.
  _Avoid_: worker, slave node

- **Orchestrator:** The M4 laptop (for interactive sessions) or OpenProjects on the M1 MacBook (for async multi-step jobs). Plans and dispatches work; does not run heavy inference itself.
  _Avoid_: controller, master

- **Spec:** The unit of work in OpenProjects. Contains: inputs, outputs, ordered steps, acceptance criteria, and expected artifacts. The contract between orchestrator and executor. Replaces prompts as the primary unit of assigned work.
  _Avoid_: prompt, task, ticket (when used loosely)

- **Hard Local Block:** The OpenClaw configuration on the Mac Mini that prevents any cloud model fallback. If a task exceeds local model capability, the executor fails loudly and notifies via Mattermost — never silently routes to OpenRouter or cloud APIs.
  _Avoid_: local-only mode, offline mode

- **Token Bleeding:** The failure mode where OpenClaw silently falls back to OpenRouter/Sonnet 4.6 when local models fail tool calls — generating unexpected cloud API costs with no visibility. Root cause: LM Studio running without a system prompt.
  _Avoid_: cost overrun (too vague)

- **System Prompt Fix:** Configuring LM Studio with a system prompt so local models can handle tool calls and structured outputs. Root cause fix for token bleeding. Proven on M4 laptop; must be replicated on Mac Mini before OpenClaw is re-enabled.
  _Avoid_: LM Studio configuration (too vague)

- **Hermes Agent:** A learning/memory agent that accumulates domain knowledge over time. Resides on the M4 laptop only. Not deployed on the Mac Mini until local inference is proven stable.
  _Avoid_: learning agent (too generic)

---

## Smoking Tigers Studio (STE) Specific

- **Rev Points:** An internal asset class representing a claim on $1 USD of future revenue from the cooperative network. Minted via a Rev Token Purchase Agreement.
  _Avoid_: tokens (implies blockchain), points (too generic)

- **First Ledger (Hard Costs):** The primary financial tranche dedicated strictly to recovering hard production costs. Must reach $0 before other distributions begin.
  _Avoid_: production budget (implies pre-spend, not post-recovery)

- **IP Reversion Point:** The precise milestone where Fiat Ledger and Bonus Ledgers reach $0, triggering automatic transfer of full IP ownership back to the Creator.
  _Avoid_: ownership transfer date (implies a scheduled date, not a triggered event)

- **Buyback Engine:** The programmatic process where cash revenue automatically purchases back Rev Points from contributors at a fixed 1:1 parity ($1 USD per Rev Point), dissolving the shared IP state.
  _Avoid_: token redemption (implies voluntary action)

- **Platform Yield:** The percentage the Studio retains from all channel revenue to sustain operations and cooperative infrastructure.
  _Avoid_: cut, fee (too informal)

---

## Governance Boundaries

Actions requiring human approval before an agent can execute:

| Action | Reason |
|---|---|
| GitHub commit or merge | Permanent record; governance impact |
| LedgerSMB record creation or modification | Financial record; legal impact |
