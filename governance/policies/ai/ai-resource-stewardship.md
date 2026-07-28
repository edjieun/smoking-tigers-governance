# Policy — AI Resource Stewardship and Model Routing (Local-First, Escalation by Value)

Status: Draft v1.0
Owner: Ed (Steward)
Applies To: All agents, operators, and humans using the Smoking Tigers governance model
Last Updated: 2026-02-23

## Purpose

Establish a default set of operating policies for how humans and machines select AI models and spend limited AI resources using https://github.com/edjieun/smoking-tigers-governance

This policy affects all other work that an instance of openclaw does:
- how documents are reviewed
- how agent jobs are assigned
- how credits/quotas are consumed
- how local vs paid models are used
- how governance workflows avoid waste

The goal is to preserve scarce high-value model usage (e.g., premium hosted models) for tasks that truly require it, while using local models and human review for most preparation work.

## Core Principle

**Use the cheapest capable path first. Escalate only when the value or risk justifies it.**

This is a stewardship policy, not just a cost policy.

## Why This Policy Comes First

Without model-routing discipline:
- premium credits are wasted on low-value formatting/cleanup
- agents overuse expensive APIs for tasks local models can do
- humans become dependent on premium models for routine work
- governance processing becomes financially fragile
- review and ingestion pipelines become harder to sustain

With model-routing discipline:
- local agents do the bulk prep work
- premium models are reserved for judgment and edge cases
- throughput improves under budget constraints
- governance operations remain durable

## Policy Statement

All Smoking Tigers / OpenClaw workflows must follow a **Local-First AI Routing Standard** unless an exception is explicitly approved.

### Default Rule

1. **Human skim / triage first**
2. **Local model or local agent first pass**
3. **Human review**
4. **Escalate to premium hosted model only if needed**
5. **Promote outputs to canonical systems only with human approval**

If a task can be completed adequately by a local model, it should not consume premium hosted credits.

## Scope

This policy applies to:
- governance document review
- meeting summaries and action extraction
- policy drafting and formatting
- knowledge intake processing
- agent-generated summaries
- OpenClaw job design
- prompt workflows that can trigger paid usage

This policy applies to both:
- human-initiated AI use
- agent-initiated AI use (automations, jobs, workflows)

## Definitions

### Local Model / Local Agent

A model running on owned/controlled hardware (e.g., LM Studio, Ollama, local OpenClaw agent runtime) with no per-request hosted model charge.

### Premium Hosted Model

A cloud-hosted model with plan limits, per-use costs, quotas, or constrained usage (e.g., Claude Opus or similar high-value model access).

### Escalation

Routing a task from local processing to a higher-cost or higher-capability model because the task requires stronger reasoning, nuance, accuracy, or synthesis.

### AI Diet

A deliberate resource discipline approach where high-cost model usage is limited to high-value tasks and local systems handle routine processing.

## Routing Standard (Required)

All tasks should be classified before model selection.

### Class L — Local-First (Default)

Use local agents/models first. Premium model use is not required unless the local pass fails or risk is high.

Typical tasks:
- structure checks
- formatting cleanup
- markdown normalization
- extraction of bullets/actions
- duplicate detection
- naming/versioning cleanup
- draft summaries
- consistency checks across docs
- ingestion prep notes

### Class H — Human-Review + Local

Local model drafts, human reviews and edits before any escalation.

Typical tasks:
- policy wording cleanup
- ambiguity checks
- authority/risk wording scans
- cross-file linking suggestions
- draft indexes
- classification/tagging of documents

### Class E — Escalation Candidate (Premium If Needed)

Use local first if practical, then escalate only if there is a clear gap.

Typical tasks:
- complex synthesis across many docs
- conflict resolution between sources
- nuanced policy language
- strategic tradeoff analysis
- executive-facing summaries where wording matters
- high-ambiguity governance interpretation

### Class P — Premium Preferred (High-Leverage / High-Risk)

Premium hosted model use may be justified earlier due to stakes, nuance, or consequences.

Typical tasks:
- legal/compliance-sensitive drafting (human review still required)
- final strategic recommendations to executives
- resolving contradictory directives with governance impact
- major architectural decisions with multiple dependencies
- high-stakes external messaging drafts

**Note:** Premium Preferred does not remove human approval requirements.

## Human Roles in the Routing Loop

### Steward / Executive / Decision Owner

- sets priorities
- decides where premium usage is worth it
- approves final governance outcomes

### Operator (Human)

- classifies task (L/H/E/P)
- runs local-first workflow
- escalates only when justified
- documents why escalation happened (for repeat learning)

### Agent (Machine)

- follows routing rules
- does not self-escalate to paid tools/models unless authorized by workflow
- logs usage events if integrated into automation

## Required Workflow Pattern for Governance Documents

For any governance/policy markdown file:

1. **Human skim (triage)**
   - confirm intent and scope
   - identify obvious errors/sensitive content

2. **Local review pass**
   - structure check
   - ambiguity check
   - authority/risk wording scan
   - formatting consistency

3. **Human edits**
   - accept/reject local suggestions
   - mark status (`Draft`, `Review`, `Ready for OpenClaw`)

4. **Optional premium escalation**
   - only if there is unresolved ambiguity, strategy complexity, or high-stakes wording need

5. **OpenClaw processing**
   - selective ingestion by theme
   - not all files at once
   - preserve draft/canonical boundaries

## Premium Model Usage Rules (Budget Protection)

### Premium hosted models should be reserved for:

- judgment, not clerical work
- synthesis, not raw formatting
- conflict resolution, not first-pass extraction
- final wording, not draft cleanup

### Premium hosted models should not be used for:

- bulk markdown formatting
- repeated file-by-file structural checks
- simple summaries local models can handle
- duplicate conversions
- mechanical extraction tasks

## Escalation Criteria (When Premium Use Is Justified)

Escalate when one or more of the following is true:
- local model output is materially wrong or unstable
- task involves multi-document reasoning beyond local model reliability
- wording has governance, legal, security, or authority consequences
- ambiguity remains after local + human review
- the cost of a mistake is higher than the premium usage cost
- the result is executive-critical and time-sensitive

If none apply, stay local-first.

## "No Waste" Rules for Agent Workflows

Agents operating under this governance model must follow:

1. **No automatic premium escalation by default**
2. **No repeated retries on premium models without human approval**
3. **No parallel premium calls for the same task unless explicitly authorized**
4. **No premium usage for tasks classified as Class L**
5. **No premium usage when the input is clearly not ready (garbage-in stage)**

Agents should prefer to:
- ask for a local preprocessing step
- produce a draft for human review
- identify missing context before escalation

## Processing Tiers (Recommended Metadata Label)

To reduce accidental credit burn, files may include a temporary processing label near the top:

- `AI Processing Tier: Local Only`
- `AI Processing Tier: Local First, Escalate If Needed`
- `AI Processing Tier: Premium Review Required`

This label is guidance for humans and machines and can be removed before publication if not needed.

## Logging and Accountability (Practical Minimum)

For workflows that use premium hosted models, track:
- task name / file
- reason for escalation
- model used
- outcome quality (useful / partial / failed)
- whether escalation could have been avoided next time

This can be tracked in:
- a markdown log
- a Notion table
- an OpenClaw job log
- a governance issue/comment thread

Purpose: improve routing decisions over time, not micromanage people.

## Resource Stewardship as Governance Behavior

This policy is not only about money. It reflects organizational values:
- respect for constraints
- durable systems over convenience
- thoughtful escalation
- human judgment where it matters
- machine assistance where it saves effort

A team that cannot steward model usage will struggle to steward larger operational resources.

## Required Machine Behavior Under This Governance Model

Any machine/agent implementing this governance model as operating procedure must:

- default to local-first processing when capable
- classify tasks by risk/value before escalating
- avoid premium model use for clerical tasks
- preserve human approval gates for decisions/canonical changes
- clearly label outputs as draft/proposed when not approved
- avoid repeated expensive retries without authorization
- prefer smaller, staged processing over large unfocused runs
- log premium escalation events when technically possible

If the machine cannot determine the correct route, it must choose the safer and lower-cost path (local/propose-only) and flag for human review.

## Integration Guidance (OpenClaw / LM Studio / Hosted Models)

### LM Studio / Local Model Layer

Best for:
- first-pass review
- extraction
- structure/format checks
- lightweight synthesis
- corpus prep

### OpenClaw Agent Layer

Best for:
- workflow orchestration
- job sequencing
- policy-aware routing
- structured drafts
- selective ingestion and packaging

### Premium Hosted Model Layer

Best for:
- strategic synthesis
- nuanced final wording
- edge-case reasoning
- high-stakes review

These layers should complement each other, not compete.

## Failure Modes to Avoid

- using premium models as the default for every task
- escalating before the document is even reviewed by a human
- asking premium models to clean bad formatting repeatedly
- agents silently burning credits in loops
- no record of why premium usage happened
- treating premium output as automatically better or approved
- confusing "faster right now" with "sustainable operating procedure"

## Enforcement and Exceptions

### Enforcement (Practical)

- route tasks through local-first prompts/templates
- maintain simple review status on files
- review premium usage patterns monthly during active experimentation

### Exceptions

Exceptions are allowed when:
- deadlines are urgent and premium use materially reduces risk
- local infrastructure is unavailable
- the task is clearly Class P (high-stakes/high-value)
- a steward or designated operator approves the exception

Exceptions should be noted briefly so the organization learns from them.

## Review Cadence

Review this policy:
- after first month of active use
- after any premium-usage spike or quota problem
- when adding new local models/agents
- when changing hosted model plans or limits
- after major workflow automation changes
