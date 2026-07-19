---
name: grill-with-docs
description: A structured documentation workflow. Grills a topic with who/what/where/why/how questions, then creates an ADR, an SOP, an OpenProjects work package, and a glossary update — all in one session. Generic and reusable across any project or workspace.
---

# grill-with-docs — Skill Instructions

## Purpose
Turn a vague plan, component, or idea into concrete, linked documentation.
Works for any project. Reads configuration from the workspace `AGENTS.md`.

## When to use this skill
- Introducing a new component, system, or integration
- Clarifying an open architectural question
- Starting a new phase of work
- Any time "what is X and how does it work?" can't be answered by existing docs

---

## Step 1 — Read workspace configuration

Before doing anything else, read the workspace `AGENTS.md` to find:
- `openprojects.url` — the OP base URL
- `openprojects.project_id` — the default project ID for new work packages
- `governance_repo` — the GitHub repo for SOPs and canonical docs
- `workspace_docs` — the local `docs/adr/` path for ADRs

If these fields are missing, ask the user before proceeding.

---

## Step 2 — Grilling session (who/what/where/why/how)

Ask these questions in order. Do not skip any. Get specific answers before writing anything.

1. **What** is this? (one sentence description)
2. **Why** does it exist? (what problem does it solve — be concrete)
3. **Who** uses it or is accountable for it? (human name or agent name)
4. **Where** does it run? (which device, which port, which path)
5. **How** does it work? (inputs → process → outputs)
6. **How** does it connect to other components? (what calls it, what does it call)
7. **What tier** does it belong to? (Network / On Premise / On Device — or ask the user if not obvious)
8. **What is the definition of done?** (how do we know it's working correctly)
9. **What are the open questions?** (anything unresolved that needs a decision)

Push back on vague answers. "It processes data" is not an answer. "It receives raw transcript text via HTTP POST from Scout and returns a JSON object with extracted tasks" is an answer.

---

## Step 3 — Create the ADR

Write an Architecture Decision Record in `docs/adr/` using this format:

```markdown
---
id: ADR-XXXX
title: [Component/Decision Name]
status: Accepted
date: [YYYY-MM-DD]
tier: [Network | On Premise | On Device]
---

## Context
[Why this decision was needed — the problem being solved]

## Decision
[What was decided — the component, integration, or approach]

## Who / What / Where / Why / How
- **Who:** [owner/accountable party]
- **What:** [one sentence]
- **Where:** [device, port, path]
- **Why:** [problem solved]
- **How:** [inputs → process → outputs]

## Connections
[What calls this component, what it calls, what protocol]

## Definition of Done
[How to verify it's working]

## Open Questions
[Unresolved items — each becomes an OP task]

## Consequences
[What this decision enables or constrains]
```

---

## Step 4 — Create the SOP

Write a Standard Operating Procedure in the governance repo (`governance_repo/docs/`):

```markdown
---
title: SOP — [Component Name]
status: Active
last-updated: [date]
tier: [tier]
---

# SOP: [Component Name]

## Who / What / Where / Why / How
[Fill from grilling answers]

## How to use it
[Step-by-step]

## How to add / change it
[What to update when this component changes]

## Troubleshooting
[Common failure modes and fixes]
```

---

## Step 5 — Create OpenProjects work package

Follow the WP template standard in `docs/sop-work-package-template.md` for all fields.

POST a work package to OpenProjects using the workspace config:

```
POST {openprojects.url}/api/v3/projects/{openprojects.project_id}/work_packages
Authorization: Basic base64("apikey:{OPENPROJECTS_API_KEY}")
Content-Type: application/json

{
  "subject": "DOC: [Component/Decision Name]",
  "description": {
    "raw": "Assignee: Copilot\nDevice: M4 Laptop\nTier: [tier]\nDeadline: [date]\n\n[agent instructions or done criteria]\n\nOutput: [ADR path]\nADR: [path to ADR file]\nSOP: [path to SOP in gov repo]\nSession: [date]"
  },
  "_links": {
    "type": { "href": "{openprojects.url}/api/v3/types/1" }
  }
}
```

Return the work package ID and full URL to the user. Every output from this skill must include the OP link.

For each open question identified in Step 2, create a separate Task tagged "open-question".

Agent identity fields to include in description:
```
Agent: Copilot
Harness: VS Code Copilot
Model: claude-sonnet-4.6
Device: M4 Laptop
```

---

## Step 6 — Update glossary

Add any new canonical terms to `docs/glossary.md`:

```markdown
- **[Term]:** [Definition — one sentence, precise]
  _Avoid_: [synonyms to not use]
```

---

## Output checklist

At the end of the session, confirm all of these exist:

- [ ] ADR written at `docs/adr/XXXX-[name].md`
- [ ] SOP written at `{governance_repo}/docs/[name]-sop.md`
- [ ] OP work package created — link: `{openprojects.url}/work_packages/{id}`
- [ ] Open questions created as OP tasks
- [ ] Glossary updated (if new terms)
- [ ] Tier tag confirmed in all documents

---

## Sub-skills

- `/domain-modeling` — use when the grilling session needs to define entities, relationships, and lifecycle states (e.g., "what are the core objects in this system and how do they relate?"). See `domain-modeling/SKILL.md`.
