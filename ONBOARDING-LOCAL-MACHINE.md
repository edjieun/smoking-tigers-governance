# **Onboarding — Local Machine Using the Smoking Tigers Governance Repository**

Status: Draft v1.0

Owner: Ed (Steward)

Applies To: Executive Council and authorized operators running local OpenClaw instances

Last Updated: 2026-02-23

## **Purpose**

This guide explains how to onboard a local machine to use the Smoking Tigers Governance Repository as a shared governance layer for a local OpenClaw instance.

The goal is:

* local execution

* shared governance

* explicit authority boundaries

* safe contribution back to the governance model

## **Operating Model in One Line**

**Your machine runs locally. The governance repo provides the shared operating rules.**

## **Before You Start**

You should have:

* a local machine you control (Mac/Linux recommended)

* Git installed

* access to the Smoking Tigers governance repo

* a local OpenClaw instance (installed or planned)

* a local model runtime (e.g., Ollama) if you plan to use local agents

* permission to participate in governance contributions (if contributing changes)

## **What This Repo Gives You**

This repo is intended to provide shared:

* governance policies

* workflow SOPs

* agent behavior standards

* templates/checklists

* automation patterns/tools

* skills / operating patterns

It is **not** your local knowledge base and does **not** replace your local machine setup.

## **What Must Stay Local**

Keep these local (or in approved restricted systems), not in the governance repo:

* API keys / tokens / passwords

* .env files

* machine-specific secrets

* private local logs

* personal notes/journals (unless intentionally shared)

* raw Notion exports / private working knowledge not approved for promotion

* sensitive infra configs that expose your security posture

When in doubt: **local/restricted by default**.

---

## **Step 1 — Clone the Governance Repository**

Clone the repo to a stable local path on your machine.

Suggested pattern (example):

* \~/SmokingTigers/governance/

Use your standard Git method (SSH/HTTPS) per your access setup.

### **Notes**

* Keep this repo versioned and pull updates regularly.

* Do not mix unrelated local working files into the repo.

---

## **Step 2 — Review Core Governance Documents First (Required)**

Before using agents against governance docs, read the core files that define authority and resource behavior.

### **Minimum required reading**

1. **AI Resource Stewardship and Model Routing**

   * local-first usage

   * premium model escalation rules

   * budget/credit discipline

2. **Agent Authority Matrix**

   * what agents can do

   * what requires human approval

   * restricted actions

3. **GitHub Decision / Governance Tracking Policy**

   * how changes become official

   * draft vs approved distinctions

   * review/merge expectations

4. **Repo Purpose and Operating Model**

   * shared governance layer concept

   * what is shared vs local

   * contribution expectations

5. Role-relevant workflow docs

   * e.g., meeting capture, staging workflow, access/security workflows, sysops SOPs

### **Why this is required**

Without this step, local agents may:

* overreach authority

* generate policy drift

* burn premium credits unnecessarily

* confuse drafts with approved governance

---

## **Step 3 — Configure Your Local OpenClaw Instance to Use Governance Docs (Read-First)**

Connect your local OpenClaw workflow to the governance repo as a **read-first governance source**.

### **Practical rule**

Treat the repo as:

* policy \+ procedure reference

* shared agent behavior standard

* approved template source

Do **not** treat it as:

* a place for local secrets

* a free-for-all scratchpad

* auto-write target for agent-generated governance changes

### **Recommended local pattern**

* local OpenClaw instance reads governance repo docs

* local knowledge/project data remains separate

* proposed governance updates are drafted separately, then submitted through review

---

## **Step 4 — Separate Local Knowledge from Shared Governance**

Set up your local folders so governance and local knowledge are distinct.

### **Recommended split (example)**

* \~/SmokingTigers/governance/ → shared governance repo

* \~/SmokingTigers/local-knowledge/ → local notes, staging, project-specific materials

* \~/SmokingTigers/openclaw/ → local instance config/workspace (as applicable)

* \~/SmokingTigers/restricted/ → local secrets/restricted materials (not in repo)

This prevents accidental commits of sensitive data and keeps governance clean.

---

## **Step 5 — Adopt Shared Conventions (Required)**

When working with governance artifacts, use repo conventions for:

* file naming

* status labels (Draft, Proposed, Approved, Superseded)

* explicit approval language

* no-silent-write behavior

* logging/review practices where defined

### **Non-negotiable rule**

Your machine/agents must not mark governance content as approved without human authorization.

---

## **Step 6 — Configure Local Agents to Respect Governance Boundaries**

Before running local agents on governance work, add or confirm directives that enforce:

* local-first model routing

* no invented approvals

* no policy creation without explicit steward/authorized request

* no silent writes to canonical governance files

* draft/proposed labeling for unapproved outputs

### **Minimum behavior expected from agents**

Agents may:

* review

* summarize

* format

* flag ambiguities

* draft proposals (when requested)

Agents may not:

* self-approve policy

* merge governance changes

* rewrite policy meaning without instruction

* silently overwrite canonical files

---

## **Step 7 — Start with a Safe Use Case (Recommended)**

Do not begin by letting agents rewrite governance policy.

Start with one low-risk task, such as:

* structure check on a workflow doc

* ambiguity scan

* formatting cleanup

* cross-reference suggestions

* index generation for existing docs

This helps validate your local setup safely.

---

## **Step 8 — Contributing Governance Improvements (Allowed, But Governed)**

Your machine and workflows may reveal improvements. These are welcome.

### **Allowed contributions**

* policy clarifications

* workflow improvements

* tooling/automation docs

* templates/checklists

* bug fixes in procedures

* naming/structure improvements

### **Required contribution pattern**

1. Draft the proposed change

2. Label clearly as Proposed / draft

3. Explain:

   * what problem it solves

   * what changed

   * who it affects

4. Submit through the repo review process (issue / PR / agreed workflow)

5. Wait for human approval before treating it as adopted

### **Important**

A local improvement is not shared governance until reviewed and approved.

---

## **Step 9 — Update and Sync Discipline**

Because multiple machines may depend on this repo:

* pull updates regularly

* review changelogs / decision notes

* avoid local divergence in governance files

* document local adaptation needs if a change impacts your workflows

If a governance update breaks your local process, propose a fix through the normal contribution path.

---

## **Step 10 — Security and Stewardship Checklist (Quick)**

Before considering your machine “onboarded,” confirm:

* Governance repo cloned locally

* Core governance docs reviewed

* Local knowledge separated from shared governance repo

* Secrets excluded from governance repo

* Agent directives enforce no policy self-approval

* Local-first model routing is configured

* First low-risk test task completed

* Contribution workflow understood

---

## **Recommended Local Machine Directory Map (Example)**

This is an example only; adapt to your environment.

* \~/SmokingTigers/governance/

* \~/SmokingTigers/openclaw/

* \~/SmokingTigers/local-knowledge/

* \~/SmokingTigers/local-knowledge/staging/

* \~/SmokingTigers/restricted/

* \~/SmokingTigers/tools/automation/

Keep the boundaries clear.

---

## **Common Mistakes to Avoid**

* putting .env files or API keys in the governance repo

* treating drafts as approved policy

* letting agents auto-rewrite governance files

* skipping core policy review before running local agents

* mixing local project knowledge with shared governance assets

* creating local conventions that conflict with repo standards without proposing updates

* burning premium model credits on low-value prep work

---

## **Escalation and Questions**

If something is unclear:

* default to **read-only / local-only**

* label outputs as draft/proposed

* preserve human approval gates

* raise the question through the governance review channel/process

When in doubt, choose the safer path.

---

## **Onboarding Completion Statement (Suggested)**

A machine can be considered onboarded when it:

* uses the governance repo as a shared governance layer,

* preserves local/secret boundaries,

* runs local agents within governance constraints,

* and contributes improvements through governed review.

## **Next Recommended Files to Read**

* README.md (Repo Purpose and Operating Model)

* 00-policy-ai-resource-stewardship-and-model-routing.md

* 13-agent-authority-matrix.md

* 05-github-decision-tracking-policy.md

* role-specific workflows relevant to your machine/operator role
