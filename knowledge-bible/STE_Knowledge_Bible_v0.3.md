# SMOKING TIGERS ENTERPRISES â€” KNOWLEDGE BIBLE

**Version:** 0.3 | February 19, 2026 | Canonical Reference Document
**Changelog v0.3:** Added OpenClaw agent architecture (Section 2.1), knowledge pipeline, DACI process, agent glossary terms (1.1), ST:AI thin spots (Part 4), updated document index (Part 5)

**Purpose:** This document is the master knowledge base for Smoking Tigers Enterprises. It serves as the primary RAG source for AI agents operating across contributor, investor, operations, governance, and creative contexts. Every section is written to be retrievable by role-specific agents and readable by humans.

**Document Status Legend:**
- ðŸŸ¢ LOCKED â€” Canonical, governance-grade, usable in agreements
- ðŸŸ¡ SPECIFIED â€” Well-defined, operational, may evolve through practice  
- ðŸ”´ THIN â€” Needs work; represents an atomic job opportunity

---

# PART 1: THE SYSTEM

## 1.1 Entity Map & Glossary

ðŸŸ¢ LOCKED

**Quorum1 (Q1)** â€” The network and governance layer. Q1 provides the ledger system that tracks Rev Point issuance, IP contributions, and revenue attribution across all enterprises. Governance framework documented at github.com/quorum1/governance. Q1 governance is supreme â€” where conflicts arise between Q1 and any downstream entity, Q1 controls.

**Smoking Tigers Enterprises (STE)** â€” A for-profit cooperative Line of Business (LOB) operating within the Q1 network. STE is a venture studio that launches, supports, and scales creator-led businesses through project-based partnerships, collective contribution agreements, and a dual-currency model centered on IP creation and revenue generation. STE is not a DAO, not a talent agency, not an MCN, not a holding company.

**Smoking Tigers Media (STM)** â€” The original entity name, now used interchangeably with STE. Legal entity: Quorum1, LLC d/b/a Smoking Tigers Media Group.

**Founding Stewards** â€” Ed Hwang, Basil Childers, Van Nguyen, Christine Francis. Initial custodians of the Governance Charter. Founding Stewardship conveys responsibility, not permanent control. May evolve through charter amendment.

**Enterprise** â€” A distinct project or line of business within STE. Each enterprise has its own vision, market analysis, BMC, RevPoints budget, job board, and contributor activation. Examples: Smoking Tigers AI, AXIOM, the Studio Model.

**Rev Points (RP)** â€” Internal trust currency. Not money, not equity, not wages, not securities. Face value: $1 per RP. Used to track contributions to IP, quantify sweat equity, and coordinate participation. RP remain disconnected from revenue until the moment of currency exchange (RP â†’ USD). All RP originate exclusively from the Steward and Q1-aligned investors who have executed a Rev Token Purchase Agreement.

**Rev Tokens** â€” Security instrument that secures the RP obligation. Governs the mechanics of the exchange process. Held per the Q1 governance framework. Rev Tokens are the investment and governance layer; RP is the operational layer.

**RPM (Rev Point Multiplier)** â€” A base-10 multiplier applied to Rev Points issued for work. Compensates contributors for the risk of accepting deferred compensation. Higher RPM = higher risk offset. Set per engagement. Each enterprise has a cap (e.g., STM AI: 4.1Ã—, RMA: 5Ã— ceiling).

**RP Ledger** â€” Records which contributor performed what work, how many RP were issued, and which IP the work contributed to. One ledger per discrete body of work. This is how attribution works: each issuance is tied to a specific ledger documenting the IP contribution.

**Income Ledger** â€” Maps IP to the revenue it generates. Creates the bridge: RP Ledger shows who contributed â†’ Income Ledger shows what that IP earns â†’ combined: who gets paid, and why.

**Recovery Pool** â€” A defined percentage of enterprise revenue allocated to RP redemption. Recovery is capped, time-bounded, and throttled (e.g., â‰¤20% of annual EBITDA for STM AI; 15% of gross revenue for AXIOM).

**Recovery Cap** â€” The absolute lifetime ceiling for all RP recovery within an enterprise. STM AI: $2.4M. AXIOM: $2M RP budget.

**Atomic Job** â€” The smallest executable, independently completable unit of work. The fundamental coordination mechanism replacing teams with scoped deliverables. Every job must include: clear deliverable, file format + submission location, deadline, reward (RP and/or cash), role badge requirement, and quality standard (definition of done). If a job cannot be completed independently, it is too large and must be broken down.

**Role Badge** â€” Permission-based access to job tiers. Not employment assignments. Roles function as quality gating mechanisms. Examples: Researcher, Writer, Editor, Producer, Reviewer, Steward.

**Project Assembly** â€” The governance body for each STM project. May include creators, contributors, RevPoint investors, and STM stewards. First forum for internal conflict resolution.

**DACI** â€” Decision framework used across STE: Driver (owns execution), Approver (final authority), Contributors (provide input), Informed (kept aware).

**CCA (Collective Contribution Agreement)** â€” The root agreement for all STM participants. Establishes shared rules of participation. Not an employment agreement. Not an equity agreement. All other agreements reference or inherit from the CCA.

**OpenClaw** — The local AI agent orchestration platform used by STE. Runs on STE-controlled hardware (Mac Mini). Hosts all AI agents via Ollama. OpenClaw is the execution environment; the Knowledge Bible and Notion exports are its knowledge sources. Not a cloud service. Not a SaaS dependency.

**Ollama** — Local AI model runtime. Runs open-weight language models (e.g., qwen2.5:14b-instruct) on STE hardware. Enables private inference with zero data leakage. The engine beneath all STE AI agents.

**Agent** — A purpose-built AI role operating within OpenClaw. Each agent has defined authority boundaries, access scope, and governance constraints. Agents propose; humans decide. No agent can promote decisions or modify canonical knowledge without human approval.

**Agent Tiers** — STE agents are organized in three tiers: Command (Chief of Staff, Executive Assistant, Router), Operations (SysOps, Knowledge Curator, DACI Logger), and Specialist (spawnable on-demand for domain-specific tasks: FinOps, Legal Analyst, Project Analyst, Meeting Processor, Content Strategist, Research Agent).

**Router** — The traffic controller agent. Receives all inbound requests, classifies task type, determines which agent(s) handle them, tracks token usage per agent per task, and logs all routing decisions. The Router distributes but does not decide.

**Knowledge Pipeline** — The governed process for ingesting external data (Notion exports, documents) into the OpenClaw knowledge base. Eight stages: Export → Upload → Unpack → Classify → Normalize → Index → Validate → Promote. Human gates at export, classification review, conflict resolution, and final promotion.

**Decision Promotion** — The lifecycle of a decision through governance: DRAFT → CANDIDATE → APPROVED → COMMITTED → ARCHIVED. Draft thinking must never leak into committed truth.

**Knowledge Taxonomy** — The layered structure of the OpenClaw knowledge base: L0 Constitution (Bible, Charter, CCA), L1 Strategy (ExecDB, project profiles), L2 Operations (SOPs, guidelines), L3 Projects (per-project scoped data), L4 People (team directory, PII-scrubbed), L5 Meetings (records, transcripts, actions), L6 DACI Log (decision audit trail), L7 Media & Brand (guidelines, press). EXCLUDED layer for credentials and sensitive PII.

**Token Budget** — The tracking of AI inference cost across the agent system. Tokens are the AI equivalent of labor cost. Tracked per request, per agent, per day. The Router maintains the token ledger. Steward decides if spend is justified.


---

## 1.2 The STE Operating Pattern

ðŸŸ¢ LOCKED

Every STE enterprise follows the same lifecycle. This is the repeatable pattern that makes the cooperative scalable:

**Step 1 â€” Vision Document.** Creates gravitational pull. Answers: What is this and why does it matter? What are the economic principles? Who is it for? The vision document is the seed â€” the right people read it and feel it pull them toward the project.

**Step 2 â€” Market Analysis.** Validates the opportunity. Sizes the market, maps competitors, identifies target segments, and surfaces the strategic white space.

**Step 3 â€” SWOT â†’ SOAR.** SWOT provides situational awareness. SOAR shifts the lens to what's feasible, actionable, and aspirational. Together they stress-test whether the enterprise is buildable given actual constraints.

**Step 4 â€” Business Model Canvas.** Maps how value flows: customer segments, value propositions, channels, relationships, revenue streams, key activities, key resources, key partnerships, cost structure. Each block must be consistent with Q1 governance and the RevPoints model.

**Step 5 â€” Feasibility & Financial Model.** Revenue projections, cost structure (cash vs. deferred via RP), recovery schedule, RPM calculation, cap validation. This is where the math proves the economics work.

**Step 6 â€” RevPoints Budget Framework.** Defines the total RP allocation for the enterprise, recommended configuration by tier, RPM bands, progressive milestone vesting, recovery timeline, and safeguards.

**Step 7 â€” Job Board & Contributor Activation.** Decomposes the work into atomic jobs. Each job has scope, deliverables, RP allocation, RPM band, and role requirements. The job board is the primary coordination mechanism.

**Step 8 â€” Governance & Reputation.** Role badges, reputation tiers, quality gates, review standards, and the governance rules that keep the marketplace from racing to the bottom. Steward authority, human-in-the-loop, right to exit.

**Critical principle:** Decisions precede labor, capital, and structure. No work begins before the enterprise has passed through Steps 1â€“4 at minimum.

---

## 1.3 Governance Architecture

ðŸŸ¢ LOCKED

### Hierarchy of Authority

1. Q1 Governance (supreme)
2. Collective Contribution Agreement (CCA)
3. Rev Token Purchase Agreement (capital matters only)
4. Project Activation Agreement
5. Project-specific agreements
6. Policies and appendices

### Core Governance Principles (Inherited from Q1)

- Contribution â‰  Employment. Participation is voluntary, scoped, opt-in.
- Stewardship â‰  Ownership. Authority exists to protect the system, not to control IP or people.
- Projects are the unit of action. Risk, work, and reward are organized around projects, not individuals.
- IP is explicit, not implied. No IP rights arise from contribution, funding, or governance unless written.
- Bounded recovery, no perpetual claims. All economic participation is capped and time-limited.
- Right to exit without penalty. No one is trapped by labor, capital, or IP structures.

### Decision Domains

| Domain | Proposer | Decider | Veto |
|--------|----------|---------|------|
| Creative Direction | Creator | Creator | STM (Brand Risk) |
| Budget Allocation | STM | Assembly | STM |
| Revenue Allocation Changes | Assembly | Assembly | â€” (requires quorum) |
| Multiplier Framework | STM / Assembly | Assembly | â€” |
| Scope Expansion | Any | Assembly | STM |
| Pause / Termination | STM / Creator | Assembly | STM |
| Charter Amendments | Any | Assembly | â€” |

Silence does not equal consent. Decisions require explicit approval.

### Voting Mechanics

- Eligibility: Active participants with economic exposure
- Weighting: One participant, one vote
- Quorum: >50% of eligible voters
- Approval: Simple majority
- Tie-breaker: Operating Steward (STM)

---

## 1.4 Role Definitions

ðŸŸ¢ LOCKED

**Steward** â€” Governance + capital allocator. Maintains Q1 alignment. Oversees project intake, feasibility, recovery caps, RPM guardrails. Primary source of RevPoints via Rev Token Purchase Agreement. Does not gain IP, equity, or control through RP. Not an employer, not a project manager of creators, not an IP owner by default.

**Q1 Investor (Rev Token Holder)** â€” Upstream capital provider. Supplies RP into the system via Rev Token Purchase Agreement. Accepts capped, time-bounded recovery. Does not participate in daily operations. Not a creator, contributor, decision-maker, or IP owner.

**Executive Contributor (Council Member)** â€” Governance and strategic labor. Contributes to governance refinement, intake review, system design. Compensated via cash and/or RP (allocated, not originated). Participation tied to active service. No automatic RP origination rights, no project IP claims.

**Creator (Partner)** â€” IP originator and business lead. Defines creative and business vision. Retains primary ownership of IP. Does not originate RevPoints. May be allocated RP to fund work and activate contributors. Use of RP does not change IP ownership, create debt, or create control obligations.

**Project Contributor** â€” Scoped labor and execution. Performs defined work under scope-bound agreements. May receive RP as compensation. RP are participation credit, recovery-capped, no ownership or control implied. No IP ownership unless explicitly granted.

**Internal Builder** â€” System and infrastructure contributor. Works on STE infrastructure (ops, AI, tooling, documentation) rather than creator IP. No IP claims on creator projects.

**Supporter** â€” Strategic leverage without labor. Provides access, distribution, relationships. Does not originate RP. Does not govern, manage projects, or gain IP rights.

### Role Multiplicity (The "Double Dip")

Individuals may simultaneously act as Steward, Contributor, and Investor. Explicitly allowed. All roles must be declared per project to avoid conflicts of interest.

### Scope Hierarchy (Not Power Hierarchy)

1. Q1 Governance â€” parent constraints
2. Steward â€” system integrity & allocation
3. Executive Contributors â€” governance labor
4. Creators â€” IP ownership & vision
5. Contributors / Builders â€” execution
6. Supporters â€” leverage without control

Capital never overrides IP. RevPoints never override governance.

---

## 1.5 Economic Model â€” The Dual Currency System

ðŸŸ¢ LOCKED

### Two Currencies

**Cash** â€” Finite, scarce, transactional. Used for hard costs, external vendors, campaign expenses.

**RevPoints** â€” Trust currency. Used for tracking participation, recognizing contribution, coordinating collaboration, and modeling bounded recovery. Non-cash, non-equity, non-guaranteed.

### RevPoint Flow (Governance-Safe)

**Step 1 â€” Capitalization (Upstream).** Steward + Q1 investors contribute capital. RP issued internally under Rev Token Purchase Agreements.

**Step 2 â€” Allocation.** Steward allocates RP to projects, creators, and specific scopes of work.

**Step 3 â€” Deployment.** RP funds contributor labor, production, ops, and infrastructure.

**Step 4 â€” Recovery (Conditional).** RP recover value from project revenue, up to explicit caps. Recovery flows back to original RP holders.

**Step 5 â€” Expiration / Retirement.** Unrecovered RP expire or are retired. No debt. No clawbacks. No leverage over creators.

### The Regenerative Trust Loop

This is not capital flowing downhill. It is:

Trust â†’ Work â†’ Value â†’ Regeneration

- Recovery is capped
- Trust can be renewed
- Failed projects do not poison the system
- Value increases system capacity, not dependency
- No participant is weakened by participation

### What RevPoints Are NOT

- âŒ Not wages
- âŒ Not equity
- âŒ Not profit-sharing instruments
- âŒ Not a claim on IP ownership
- âŒ Do not automatically convert into cash or revenue
- âŒ Do not transfer IP, grant equity, or create governance authority

### RPM Mechanics

When a project lead offers work to a contributor, the offer includes an RPM. Example: A task worth $5,000 at market rate with RPM 3Ã— = 15,000 RP issued.

| Market Rate | RPM | RP Issued | Risk Level | Typical Stage |
|-------------|-----|-----------|------------|---------------|
| $5,000 | 1Ã— | 5,000 | Low | Post-revenue, proven IP |
| $5,000 | 2Ã— | 10,000 | Moderate | Pre-launch, defined product |
| $5,000 | 3Ã— | 15,000 | High | Early stage, concept phase |
| $5,000 | 5Ã— | 25,000 | Very High | Pre-concept, foundational |

### Progressive Vesting â€” Milestone-Based, Not Time-Based

| Milestone | Trigger | What Vests | Significance |
|-----------|---------|------------|--------------|
| 1: Break-Even | Revenue covers contributor's market-rate value | Base RP (1Ã— equivalent) | Contributor made whole; risk validated |
| 2: Growth | Revenue exceeds break-even by defined multiplier | RPM-multiplied RP begin vesting | Risk premium begins paying off |
| 3: Scale | Sustained revenue / operational maturity | Remaining RPM RP fully vest | Full reward for early-stage risk |

---

## 1.6 Agreement Architecture

ðŸŸ¢ LOCKED

### System-Level Agreements

- **Collective Contribution Agreement (CCA)** â€” Root agreement for all participants. Constitutional layer.
- **Q1 Governance Incorporation** â€” Q1 docs incorporated by reference. Q1 controls where conflicts arise.

### Capital Agreements (Upstream Only)

- **Rev Token Purchase Agreement** â€” Defines capital contribution terms, recovery caps, time bounds, non-ownership and non-control clauses. Only Steward and Q1 investors sign this.
- **RevPoint Allocation Policy** â€” Internal governance policy for who may allocate, under what conditions, with what limits.

### Project-Level Agreements

- **Project Activation Agreement** â€” Cover sheet tying all project agreements together. Records activation decision, scope, ledgers, roles, caps.
- **Creator Partnership Agreement** â€” IP ownership (creator-owned by default), licenses granted to STM, revenue participation, exit terms.
- **Project Contribution Agreement** â€” Scope of work, compensation (cash/RP/hybrid), RPM, recovery constraints, IP treatment.

### Enterprise & Governance Agreements

- **Executive Contribution Agreement** â€” Governance and strategic labor terms.
- **Internal Builder Agreement** â€” Infrastructure scope, IP treatment of system outputs.

### Support & External Agreements

- **Supporter Agreement** â€” Access/distribution/strategic support, non-control clauses.
- **Sponsorship / Brand Agreement** â€” Campaign scope, deliverables, payment, usage rights.

### IP Agreements (Conditional)

- **IP License Agreement** â€” Cross-project reuse, distribution, derivatives. Always explicit, never implied.
- **Knowledge / Artifact License** â€” Decks, frameworks, playbooks, AI outputs.

---

## 1.7 The Atomic Job â€” Cold Start Mechanics

ðŸŸ¡ SPECIFIED

The atomic job is the fundamental unit that solves Andrew Chen's cold start problem for the STE cooperative. It must be:

- **Small enough** to complete independently
- **Valuable enough** to attract the first contributor
- **Composable enough** that many jobs build something greater than their sum
- **Compensable** through RP with clear RPM band
- **Quality-gated** through role badges and review standards

### Job Definition Requirements

Every job must include:
- Clear deliverable description
- Required file format + submission location
- Deadline
- Reward (RP allocation + RPM band)
- Role badge requirement
- Quality standard ("definition of done")

If a job cannot be completed independently, it is too large and must be broken down.

### How to Claim a Job

1. Claim one gig at a time
2. Agree on scope, RP allocation, RPM band
3. Deliver in milestones
4. RP issued only on accepted deliverables

No open-ended commitments. No silent scope creep.

### Reputation Tiers

**Tier 1 â€” Open Contributors.** Low-risk jobs (clips, captions, basic research).

**Tier 2 â€” Verified Contributors.** Medium/high-impact jobs (scripts, thumbnails, edits, structured output).

**Tier 3 â€” Trusted Point.** Producer-level jobs (episode assembly, publishing coordination, technical architecture).

**Tier 4 â€” Stewards.** Post jobs, approve deliverables, issue RevPoints, accountable for governance and recovery cap integrity.

### Governance Controls

- Quality gate: deliverables reviewed and approved before RP issued
- Rejection + rework policy: returned with notes, job reopens if uncorrected
- Standardization: templates, naming conventions, formatting standards mandatory
- Competition mechanisms: first-claim wins, rush multipliers, quality bonuses, repeat preference

---

## 1.8 The Four Pillars — A Framework for Building What Lasts

🟡 SPECIFIED

**Source:** Smoking Tigers – The Four Pillars (Francis & Hwang, February 2026)
**Status:** Active strategic framework; co-developed by Christine Francis and Ed Hwang

Every serious business — whether a startup entering a new market, a creator building a community, or a consortium activating around shared resources — needs the same four things to work. The order shifts depending on where you are. The timing shifts depending on what you are building. The four things stay constant.

The Four Pillars are a model for how any organization creates durable, compounding value. They work individually. They amplify each other. When one is missing, the others quietly fail to hold. STE operates as a for-profit business cooperative — clients and collaborators are one and the same. True partnership.

### Pillar One — Strategy & Structure

*The foundation before anything else can hold.*

The discipline of getting clear — on numbers, structure, legal foundation, and the story the data tells — before resources are spent on anything else. Strategy is about assumptions; Pillar One makes unknowns visible and separates what is known from what must still be proven.

**What this covers:**
- Business structure legible to investors, partners, regulators, collaborators
- Financial projections separating assumptions from facts
- Data room built for precision — structured to eliminate red flags
- Investment tracking and cap table management
- Go / No-Go decision frameworks
- Strategic documents holding vision and executable plan in correct relationship

**The Deeper Layer: Data & Technology.** Unstructured data is the most common source of organizational drag. Pillar One includes the AI-assisted tooling (ST:AI) that allows data to be organized, searchable, and actionable. Well-structured organizational data carries real value — clean, well-oriented data at scale represents IP worth millions. Organizations that treat their information as infrastructure gain compounding advantages that are difficult to replicate.

### Pillar Two — Network & Access

*The connections that take years to build — available from day one.*

Business runs on people and agreements. The network is not a nice-to-have layer on top of the real work — it is the real work. At its core, it's trust. Building networks of trust.

**The Atomic Network (Andrew Chen / Cold Start Problem).** The atomic unit of the STE network is measured by job — not users, signups, or followers. A defined job role that creates value and gets compensated. Jobs have boundaries, inputs, outputs, compensation (RP), XP tracking, and can be replicated and measured. This maps to Chen's lifecycle stages: Cold Start → identify the first job loop that executes. Escape Velocity → replicate reliably. Growth → reduce friction between job units. Defensibility → increase switching costs via role reputation, XP, and credentialing. Most communities grow by vibes. STE proposes growth by job completion density. This is venture architecture.

**What access means:**
- Relationships with key industry operators, ready before needed
- Regulatory navigation from people with direct system experience
- Grant and funding networks operating through existing credibility
- Capital sources beyond standard VC — agricultural capital, asset-backed financing, community funding models
- Introductions that compress months of relationship-building into days

**The Golden Ticket Logic.** The most expensive mistakes happen in the first 90 days — almost always traceable to landscape knowledge. Having that knowledge from Day 1 is a cost-reduction strategy. Building it from scratch takes 12–24 months. This logic extends beyond teams to franchises (the sports metaphor).

### Pillar Three — Storytelling & Media

*Story that earns trust before you ask for anything.*

Telling a story that builds trust, scales with integrity, and lands with the right people at the right time is a distinct discipline — closer to architecture than to marketing. Story is what makes the other pillars legible to the outside world. A data room without a narrative stays unread. A network without a story has nothing to carry through it.

**What this includes:**
- Brand architecture: durable creative posture built to hold over years, across markets
- Narrative guardrails: editorial framework keeping story consistent as it scales
- Content formats that are repeatable, credible, trust-building
- Greenwashing risk reduction: critical in values-aligned markets
- Media strategy aligned to real business goals and measurable outcomes

**The Media Layer.** Smoking Tigers Media operates as the creative and media production arm — building the evidence layer (interviews, documentary footage, community conversations) that makes a story feel real because it is real. The vision extends to a full media cluster model where creators, practitioners, and organizations with aligned values contribute to shared media infrastructure.

### Pillar Four — Execution & Orchestration

*The weave. The part people neglect until it breaks.*

Strategy, network, story, and a team of people become executable only when something weaves them together — the coordination of roles, rhythms, agreements, and decision logic that allows an organization to function at scale. Orchestration. Culture. The living system that makes the other three pillars run. This is about inventing a professional business that is unconventional — a change of the status quo, driven by the mutual obligations of human nature, capitalism, and democracy.

Coordination is a cultural act as much as a systemic one. A network without Pillar Four is a knitting club. A business plan without execution structure stays hypothetical.

**What this covers:**
- Legal & entity structure: making newer, better structures — non-extractive, regenerative
- Democratic decision-making: decision gates are a requirement — who makes the decisions, and how, matters
- Contracts as fundamental trust mechanics: offer, acceptance, consideration — now made smart, auto-deploying, keeping parties playing fair
- Operational rhythms: cadences, check-ins, accountability structures
- Supply chain and fulfillment design
- Onboarding systems: new people join a structure with clear context, roles, direction

### How the Pillars Work Together — The Compounding Effect

The Four Pillars form a system. Each one makes the others more valuable. Understanding how they interact is as important as understanding what each one does on its own.

**Pillars One & Three (Money and Story) — Narrative Partners.** Pillar One builds the data room; Pillar Three builds the story those numbers prove. Evidence-backed narrative earns a fundamentally different quality of engagement than narrative alone. When Pillar One comes first, the math and the message become the same argument, delivered in two registers.

**Pillars Two & Four (Network and Execution) — Operational Partners.** Pillar Two surfaces what is needed; Pillar Four builds the workflow that converts what the network reveals into action. Network intelligence requires operational structure to act on. The most elegant workflow produces results proportional to the quality of people and resources flowing through it.

**Breath In, Breath Out — The System's Rhythm.** Pillars One and Two move in opposite directions. Pillar One is centripetal — pulling things inward, giving raw material order and structure. Pillar Two is centrifugal — moving outward into the world, building the network. Pillars Three and Four repeat this rhythm at a different level. Three pulls inward (shaping complexity into coherent story). Four pushes outward (execution into the world). The organization contracts to get clear and expands to act on that clarity.

### Data as the Connective Tissue

Each pillar generates data: financial records and projections (One), relationship and market intelligence (Two), audience and content performance (Three), operational patterns and contributor records (Four). Connected data streams produce a fundamentally different organizational reality — the data room becomes a living document, network intelligence flows into projections, operational patterns improve storytelling, the organization learns from itself continuously and at scale.

Well-structured, well-curated organizational data is the asset beneath all the other assets.

### The AI Layer — Story as Sensemaking

AI plays two roles in this model: operational (automating data organization, workflow, administrative process) and sensemaking (surfacing what is relevant, timely, changing, and what it means for decisions). The question "Given everything we know, what should we do next?" benefits enormously from a system that has ingested the full context. That historically required a very expensive, very senior person. AI changes that equation.

The custodial dimension works like mise en place — continuously organizing data as it is created, managing entropy before it becomes crisis. The vision: joining the organization means being guided immediately by an intelligent layer that already knows the context, agreements, history, and current priorities.

This is a direct bridge to Smoking Tigers AI (Section 2.1) and its role as the operational intelligence layer across STE.

### What Happens When Pillars Are Missing

**Missing Pillar One:** Assumptions go unverified. Investor conversations stall. Due diligence impossible. Foundation never stress-tested.

**Missing Pillar Two:** Data room solid, story told, but resources inaccessible. The right supplier, regulatory pathway, distribution partner all require relationships that take months to build from scratch.

**Missing Pillar Three:** Business structured and alive, but the outside world has no way to find or understand it. Value accumulates internally and stays invisible.

**Missing Pillar Four:** Strategy, network, and story all present, but nothing converts into durable execution. Interest cycles without compounding. Good conversations produce no lasting structure.

**The Most Common Failure Mode.** Values-aligned organizations frequently develop strong Pillars Two and Three (genuine relationships, compelling narrative) alongside underdeveloped Pillars One and Four. Doors open, conversations go well, people are interested — then nothing converts. The network becomes a knitting club: warm, well-intentioned, and largely static. The four pillars compound, but only when they are in balance.

---

# PART 2: THE ENTERPRISES

## 2.1 Smoking Tigers AI

ðŸŸ¡ SPECIFIED

**Type:** Internal Platform â†’ Productized Service
**Status:** Active (Internal v1)
**RP Budget:** $2.4M recovery cap, 4.1Ã— RPM max
**Steward:** Ed Hwang

### What It Is

A private, governance-aware executive intelligence system. Operates as a Chief-of-Staffâ€“style intelligence layer that turns messy human work into clear decisions, coordinated action, and durable institutional memory. Local-first, human-in-the-loop, governance-aware.

### What It Is Not

Not a SaaS chatbot. Not an automation free-for-all. Not an "AI runs your business" fantasy. Not dependent on third-party AI clouds. Not a replacement for human judgment.

### Core Functions

1. Executive thinking & briefings
2. Meetings â†’ Decisions â†’ Actions (transcript â†’ candidate decisions â†’ DACI â†’ human promotion)
3. Project coordination (canonical profiles, ownership, milestones, drift detection)
4. Governance & memory (draft vs. committed truth, institutional memory in Markdown)
5. Creator & client operations (intake, proposals, RevPoints logic, cross-project visibility)

### System Principles (Non-Negotiable)

- Local-first (runs on STM-controlled hardware)
- Human-in-the-loop (no silent writes, no auto-execution)
- Governance-aware (authority, promotion, ownership matter)
- Explainable (why something exists is as important as what exists)
- Composable (fits into existing tools)
- Reversible (no changes without rollback paths)

### Market Position

Competes in the underserved Ops / Chief-of-Staff Augmentation category. Not competing with ChatGPT, Notion AI, or meeting bots. Selling operational clarity and governance-preserving coordination, not AI productivity.

### Primary ICP

Creator studios, founder-led media companies (5â€“50 people), small professional firms with complex coordination needs, communities/collectives with real governance.

### Revenue Model

- Setup/implementation: $7.5Kâ€“$15K per client
- Ongoing stewardship: $6Kâ€“$12K per client per year
- Early contributors compensated partially via RP; recovery capped at $2.4M, RPM max 4.1Ã—

### Financial Projection (Base Case, 10-Year)

Recovery completes in Year 8. Uses 24% of cap. Leaves $1.8M unused headroom. Post-recovery: $6M+/year revenue, high margins, zero extraction risk.

### Current Phase

Phase 1: Internal Productization. Use daily, tighten the human loop, prove trustworthiness, document patterns, resist premature automation. External offering explicitly deferred until internal value is undeniable.

### OpenClaw Agent Architecture

🟡 SPECIFIED

STM AI operates through OpenClaw, a local agent orchestration platform running on STE-controlled hardware (Mac Mini) via Ollama. The system uses open-weight models (qwen2.5:14b-instruct primary, qwen2.5:7b-instruct for lightweight tasks) with zero cloud dependency for inference.

Agents are organized in three tiers with explicit authority boundaries:

**Tier 1 — Command Layer**

| Agent | Role | Authority |
|-------|------|-----------|
| Chief of Staff (CoS) | Strategic coordination, priority management, governance enforcement. Owns the DACI log. | Can promote draft → candidate. Cannot promote candidate → committed without human approval. |
| Executive Assistant (EA) | Tactical support, scheduling, meeting prep, briefing drafts, follow-up tracking. | Can draft. Cannot promote. Surfaces recommendations to CoS. |
| Router | Task classification, agent selection, workload distribution, token tracking. | Can assign tasks to Tier 2/3 agents. Cannot make decisions. Logs all routing decisions. |

**Tier 2 — Operations Layer**

| Agent | Role | Authority |
|-------|------|-----------|
| SysOps | Infrastructure monitoring, system health, backup verification, pipeline status. | Can execute maintenance within defined runbooks. Escalates anomalies to CoS. |
| Knowledge Curator | Ingests Notion exports, normalizes markdown, maintains canonical knowledge base, enforces naming/versioning, detects drift. | Can transform and organize. Cannot delete or promote without CoS approval. |
| DACI Logger | Records all decisions, routes DACI entries through approval flow, maintains the decision audit trail. | Write-only to DACI log. Append-only. Cannot modify existing entries. |

**Tier 3 — Specialist Layer (Spawnable)**

Specialist agents are activated on-demand by the Router. They receive scoped context, execute, return results, and terminate. Not persistent.

| Specialist | Domain | Trigger |
|-----------|--------|---------|
| FinOps | Token tracking, RevPoints accounting, cost analysis | Token/cost queries, RPM calculations |
| Legal Analyst | Agreement review, CCA compliance, governance checks | Contract review, governance conflict flags |
| Project Analyst | Deep-dive on specific project health | Project status requests |
| Meeting Processor | Transcript → summary → actions → candidate DACI entries | New transcript uploaded |
| Content Strategist | Brand alignment, messaging review | Content review against guidelines |
| Research Agent | Market research, competitive analysis | Research queries requiring external context |

**Operating Principle:** Agents propose. Humans decide. No agent writes to the canonical knowledge base without human approval. The DACI log is the proof.

### Knowledge Pipeline (Notion → OpenClaw)

🟡 SPECIFIED

The knowledge pipeline governs how Notion exports enter the OpenClaw knowledge base. Manual-first by design — human decision-making at every promotion boundary.

**Pipeline Stages:**

1. **Export** — Human exports Notion team space as ZIP (Steward initiates)
2. **Upload** — Human uploads ZIP to OpenClaw ingestion directory (Steward decides what to upload)
3. **Unpack & Inventory** — Knowledge Curator extracts and catalogs all files (automated)
4. **Classify** — Knowledge Curator classifies each file: INGEST / SENSITIVE / ARCHIVE / SKIP (human reviews classification before proceeding)
5. **Normalize** — Approved files converted to clean Markdown, Notion UUIDs stripped, CSVs converted to structured records (automated per approved list)
6. **Index** — Normalized files indexed into RAG knowledge base with metadata tags (automated)
7. **Validate** — CoS runs validation queries, checks for contradictions with Knowledge Bible (human resolves conflicts)
8. **Promote** — Validated knowledge marked ACTIVE, DACI entry logged (Steward signs off)

**File Classification Rules:**
- INGEST: Active content with operational, strategic, or governance value
- SENSITIVE: Credentials, PII, financial details — never enters RAG
- ARCHIVE: Historical content, preserved but low-priority for agents
- SKIP: Empty placeholders, broken links, no-content pages

**Naming Convention (Post-Normalization):** All Notion UUIDs stripped. Files follow: `[section]/[subsection]/[descriptive-name].md`. Examples: `core/mission.md`, `projects/tln/feasibility-valuation.md`, `meetings/2026-02-18-exec-weekly.md`.

### Knowledge Base Taxonomy

🟡 SPECIFIED

The canonical knowledge base is organized in layers that map to how agents access information:

| Layer | Contents | Agent Access |
|-------|----------|-------------|
| L0: Constitution | Knowledge Bible, Governance Charter, CCA, Q1 principles | All agents (read-only) |
| L1: Strategy | ExecDB, Project Profiles, BMCs, SWOT/SOAR, Financial Models | CoS, EA, Project Analyst |
| L2: Operations | SOPs, Guidelines, Slack org, Notion operating guide, workflows | All agents |
| L3: Projects | Per-project data (TLN, Jajan, RiceSilk, AXIOM, RMA, DSP) | Scoped by Router |
| L4: People | Team directory, contact info, roles, bios (PII-scrubbed) | EA, CoS only |
| L5: Meetings | Meeting records, transcripts, extracted actions, candidate decisions | Meeting Processor, CoS, EA |
| L6: DACI Log | All decision records across the system | All agents (read), DACI Logger (write) |
| L7: Media & Brand | Brand guidelines, messaging, press materials | Content Strategist, EA |
| EXCLUDED | Credentials, financial PII, raw unclassified data | No agent access |

### DACI Process for Agent Operations

🟡 SPECIFIED

Every significant agent action generates a DACI log entry. The DACI log is the institutional memory of decisions made through the agent system.

**DACI Log Schema:** decision_id (auto-increment), timestamp, title, driver (agent or human), approver (always human), contributors, informed, status (DRAFT → CANDIDATE → APPROVED → COMMITTED → ARCHIVED), context, outcome, source_task, token_cost.

**What requires a DACI entry:**
- Knowledge ingestion (new Notion export)
- File classified as SENSITIVE or excluded
- New agent role activated
- Knowledge promoted from draft to committed
- Meeting transcript processed (for extracted decisions)
- Conflict detected between knowledge sources
- Token budget exceeded threshold
- RevPoints calculation or issuance

**What does NOT require a DACI entry:**
- Agent routing a task to a specialist (logged by Router)
- Informational query answered
- Draft outputs not promoted

### Operational Tool Stack

🟡 SPECIFIED

STE operates with a layered tool stack, each layer with a defined role:

| Tool | Role in System | Data Flow |
|------|---------------|-----------|
| Google Docs | Messy working space — brainstorms, drafts, raw notes, transcripts | Messy → Structured |
| Google Drive | File storage, shared assets | Reference layer |
| Notion | System of record — project state, finalized summaries, actions, decisions, SOPs | Structured → Canonical |
| Slack | Real-time communication, coordination | Ephemeral (decisions must move to Notion) |
| Fathom | Meeting recording and transcript generation | Transcripts → Meeting Processor agent |
| OpenClaw + Ollama | AI agent orchestration, knowledge base, decision processing | All structured data → agent context |
| Knowledge Bible (Markdown) | Constitutional layer — governance, economics, principles | L0 source of truth for all agents |

**Critical principle:** Notion is the shielded layer. It faces the team, not the public. Nothing from Notion enters public-facing systems without an explicit promotion decision and DACI entry. The manual export/import cycle between Notion and OpenClaw IS the governance — each import is a conscious act of knowledge promotion.

---

## 2.2 AXIOM â€” A Living Universe Game

ðŸŸ¡ SPECIFIED

**Type:** Open-universe action RPG with regenerative economics
**Status:** Concept stage on the STE idea board
**RP Budget:** $2M allocation from STE pool
**Steward:** Ed Hwang

### Vision

An open-universe action RPG that refuses to choose between scale and intimacy. A 4X grand strategy game, space combat simulator, FPS, fighting game, ship builder, and crew management RPG â€” all at once, all feeding each other, all telling the same story from different angles. The integration itself is the product.

### The Six Gameplay Layers

**Layer 1 â€” The 4X Galaxy.** Living system of factions, economies, trade routes, conflicts. The world you live in.

**Layer 2 â€” Ship Building.** Every component choice has mechanical consequences across all layers. Parts found, salvaged, stolen, earned â€” never just purchased.

**Layer 3 â€” Colony Wars (Space Combat).** Real-time flight combat. Your build, flying, and decisions determine outcomes.

**Layer 4 â€” FPS (Boarding and Raiding).** First-person corridor-by-corridor combat. Environments tell stories.

**Layer 5 â€” Crew (Your Roster).** Distinct fighters with unique roles, playstyles, personal stories. Permanent loss. Irreplaceable.

**Layer 6 â€” Hand-to-Hand Combat (Fighting Game).** Skill-based. Moves unlocked through experience and specific events. Mastery earned, never purchased.

### Six Design Principles

1. Story lives in the gameplay â€” not between missions
2. Every layer feeds every other layer â€” the galaxy remembers everything
3. Loss has meaning â€” losing a crew member should feel like losing someone
4. Your galaxy is yours alone â€” no two playthroughs are the same story
5. Development is proof of concept â€” how we build Axiom demonstrates what Axiom is
6. Value returns to its origin â€” contributors own what they build

### Development Model â€” Community as Studio

Gravity-based recruitment: contributors pulled by passion for the specific layer matching their expertise. Core team of 10â€“15 holds integration vision. Crowdfund maps directly to layers. Playable episodic releases.

### Regenerative Economics (In-Game)

Creator ownership of contributed content. Quality as economic incentive (content that players love keeps paying its creator). Porous line between player and developer. Early contributor risk weighted accordingly. Community governance of economic policy.

### Market Position

Triple-market convergence: gaming ($189B+), Web3 gaming ($32-40B, 18-22% CAGR), creator economy ($200-254B, 20-23% CAGR). No competitor unifies all three with regenerative principles. Post-shakeout timing: 300+ Web3 games shut down, market actively seeking sustainable successors.

### RevPoints Framework (Dual Currency: RP + Rev Tokens)

$2M RP budget. 15% Recovery Pool allocation. Progressive milestone vesting (break-even â†’ growth â†’ scale). Pro-rata distribution within milestone tiers. Hard cap: no additional RP beyond $2M without governance approval. Revenue threshold: no payouts until annual revenue exceeds $500K. Projected full redemption by Year 3 at moderate scenario.

### ðŸ”´ THIN SPOTS (Atomic Job Opportunities)

- **Tokenomics model & simulation** â€” In-game token economy, health metrics, emission constraints. HIGH RP, HIGH RPM.
- **Integration API specification** â€” How layers communicate state. Event model, propagation rules, data contracts. HIGH RP, HIGH RPM.
- **Creator tool specification** â€” What creators can build, publishing flow, approval mechanics. MEDIUM-HIGH RP.
- **Galaxy bible v0.1** â€” 3â€“5 factions, agendas, histories, political systems. MEDIUM RP.
- **Prototype scope definition** â€” Minimum viable integration, which layers first. MEDIUM RP.

---

## 2.3 The Studio Model (YouTube)

ðŸŸ¡ SPECIFIED

**Type:** Collaborator-driven media studio / multi-sided marketplace
**Status:** Active development with RMA
**Steward:** STE / Q1 Network

### Core Thesis

Not a traditional creator channel. A collaboration hub â€” a guild-powered media alliance functioning as a multi-sided marketplace where the organization posts atomic jobs (demand), contributors claim and complete jobs (supply), work is rewarded through cash and/or RevPoints, and contributors build proof-of-work and reputation over time.

### Why Collaboration Is the Growth Engine

A normal channel grows by beating the algorithm with better content. A collaboration hub grows by turning every episode into a multi-node network event where each collaborator becomes a broadcast tower. This creates signal density â€” YouTube rewards events, not uploads.

### The Regenerative Flywheel

More collaborators â†’ more distribution â†’ more viewers â†’ more credibility â†’ better guests â†’ more collaborators

### Content Taxonomy

- **Anchor Content** â€” High effort, high brand value. Creates cultural weight and credibility.
- **Core Series Content** â€” Medium effort, scalable, repeatable. Establishes rhythm and identity.
- **Derivative / Micro Content** â€” Low effort, high volume. Extends reach through clips, shorts, repackaged assets.

### Three Levels of Contributor Participation

1. **Participation** â€” Watch the video. Creates shared context and culture.
2. **Interaction** â€” Like, comment, share, cross-post. Creates the engagement surge that triggers algorithmic amplification.
3. **Contribution** â€” Host, guest, contribute briefs. The content supply layer.

### Twin Publish Model

Each collaboration produces two uploads â€” flagship on your channel, companion on theirs. Avoids the failure mode where collaborators feel they "gave you their audience." Both receive a real asset.

### Clip Commons System

Every collaboration produces a standardized clip package: 10â€“30 clips, captions + hook variants, platform-ready exports. Each piece produced via atomic jobs. Clips link back to flagship, collaborators tag the network, shared hashtags required.

---

## 2.4 Regenerative Media Alliance (RMA)

ðŸŸ¡ SPECIFIED

**Type:** Coordination institution / digital guild
**Status:** Active partnership with STE
**RP Exchange Rate:** $0.20 per RP, minimum allocation $10K

### What It Is

A stewarded ecosystem for regenerative media â€” functioning as a Digital Guild that provides durable structure, shared standards, apprenticeship, reputation, and governance, with acceleration and incubation as programs rather than defining identity.

### Rev Point Exchange Agreement (RMA Ã— STM)

- RP allocated at $0.20 USD per RP
- Minimum: $10,000 ($50,000 RP per allocation)
- RP are allocated, not sold as securities
- RP record contribution to IP creation, not ownership of IP
- Dual-currency: cash for costs, RP for contribution
- RP do not represent revenue, profit, or ownership
- Any future conversion requires separate, explicit agreement per specific project/revenue event

### RPM Policy for RMA

- 5Ã— hard ceiling (6Ã— rejected as debt-like)
- Annual revenue participation throttle: max 15% of gross annual revenue
- No RPM conversion before project sustainability
- System caps: 4,000,000 RP total, $800K maximum cash deployment to sponsors

### Sponsor Framework

- Sponsors provide RP at $0.20
- 8Ã— gross multiple potential based on original mint price ($0.025/RP)
- Total dollars available to sponsors: $800K max
- Finite, governed, transparent

### Hwang Reviewer Commentary (Key Insights for AI Agents)

Ed Hwang's reviewer commentary on the RMA whitepaper contains critical operating philosophy:

- **People â‰  value representations.** Stakeholders are people. Stewards, Nature, Members, Staff are currencies or value classes, not stakeholders themselves. Framing them as such makes the system legible as a multi-currency model.
- **Roles are jobs.** Real people occupy positions, span multiple roles, need to get paid. Short-term livelihood and long-term stewardship must coexist.
- **Collective intelligence comes from doing, not designing.** The answers emerge stigmergically â€” through signals left by real work in motion. The risk is mistaking contemplation for progress.
- **Culture should be expressed as network effects, not personal virtues.** Alignment through incentives, trust as network effect, risk-tolerant experimentation, reputation over integrity-as-virtue.
- **Ecomimetic design.** A YouTube channel behaves like a beaver pond: durable structure outliving any single content piece, value drawn from external flow (ads, sponsorships), community participation increases carrying capacity. Humans â†’ IP â†’ Value Generation â†’ Distribution.

---

# PART 3: HOW THE PIECES CONNECT

## 3.1 Cross-Enterprise Relationships

ðŸŸ¡ SPECIFIED

**Smoking Tigers AI â†” AXIOM:** Both STE enterprises. STM AI is operational intelligence; AXIOM is game product. Both use RevPoints under Q1 governance. STM AI could serve as internal coordination tooling for AXIOM's distributed development team.

**Smoking Tigers AI â†” Studio Model:** STM AI processes meetings â†’ decisions â†’ actions for the studio's production operations. The Studio Model generates the content workflows that STM AI coordinates.

**AXIOM â†” Studio Model:** AXIOM's development story, community building, and gameplay are content engines. The Studio Model's collaboration-as-distribution framework applies to AXIOM's community-building phase. AXIOM content becomes the Studio Model's anchor content.

**AXIOM â†” RMA:** The RMA provides the coordination institution framework. AXIOM is a concrete instantiation of regenerative economics applied to gaming. AXIOM development documentation becomes RMA learning content.

**Studio Model â†” RMA:** The RMA organizes the demand side economics. The Q1 Creative Guild provides the supply side. The Studio Model's atomic job board is the coordination mechanism connecting them.

### RevPoints Flow Across Enterprises

Ed Hwang holds ~13M RP available across Q1. $500K+ distributed to date. Allocations by enterprise:
- AXIOM: $2M RP budget
- STM AI: $2.4M recovery cap
- RMA: 4,000,000 RP system cap at $0.20/RP ($800K max)

Each enterprise maintains its own ledgers. Cross-enterprise RP flow governed by Q1.

---

## 3.2 The STE Portfolio Logic

ðŸŸ¡ SPECIFIED

STE operates as a portfolio, not a single bet. The "NBA of Media" analogy is structural:

| NBA | Smoking Tigers |
|-----|----------------|
| League | Smoking Tigers Enterprises |
| Teams | Creator-led businesses / enterprises |
| Players | Creators & contributors |
| Front Office | STE Ops + Q1 Infrastructure |
| CBA | Collective Contribution Agreement (CCA) |
| Revenue Sharing | Dual-currency (Cash + RevPoints) |
| IP Rights | Creator-owned, partnership-supported |
| Salary Cap | Risk-bounded contribution & recovery caps |

Portfolio effects: learning compounds, risk diversifies, operational costs amortize, tooling reuses, contributor reputation carries across projects.

---

# PART 4: THIN SPOTS â€” THE JOB BOARD FOR THE BIBLE ITSELF

Every thin spot below is an atomic job that, once completed, strengthens this bible AND creates proof-of-work for the contributor who did it. This is the cold start flywheel: bible thickens â†’ agents get smarter â†’ more contributors activate â†’ more jobs complete â†’ bible thickens.

## Tier 1 â€” Unlocks Everything Else

### ðŸ”´ JOB: STE Enterprise Playbook Template
**What's thin:** The eight-step operating pattern (1.2) is described but not templated. A new enterprise joining STE has no blank-canvas starter kit.
**Deliverable:** Markdown template with sections for each step, fill-in guidance, and examples drawn from AXIOM and STM AI as specimens.
**RP Band:** Medium RP, medium RPM.

### ðŸ”´ JOB: Ledger Flow Diagram
**What's thin:** The RP flow (1.5) is described in prose but has no canonical visual. The Miro board spec exists (in the STE doc) but hasn't been produced.
**Deliverable:** Production-ready diagram showing Trust Capitalization â†’ RP Issuance â†’ Project Activation â†’ Revenue â†’ Bounded Recovery â†’ Regeneration.
**RP Band:** Low RP, low RPM. Clear scope.

### 🔴 JOB: STM AI — Router Agent Modelfile
**What's thin:** The Router agent is specified in Section 2.1 but has no working Modelfile. Without it, task distribution is manual and token tracking doesn't exist.
**Deliverable:** Working Ollama Modelfile for the Router agent with task classification prompts, token logging format, and authority boundary enforcement. Tested against 10+ real request types.
**RP Band:** High RP, high RPM. Core infrastructure.

### 🔴 JOB: STM AI — Knowledge Curator Agent Modelfile
**What's thin:** The Knowledge Pipeline (Section 2.1) is specified but the agent that runs it has no Modelfile. Without it, Notion imports require fully manual processing.
**Deliverable:** Working Ollama Modelfile for the Knowledge Curator with file classification prompts, normalization rules, naming convention enforcement, and conflict detection logic.
**RP Band:** High RP, high RPM. Core infrastructure.

### 🔴 JOB: STM AI — DACI Log System Initialization
**What's thin:** The DACI schema is defined but no log file or system exists. The first DACI entry has never been written.
**Deliverable:** DACI log markdown file with schema header, the first entry (documenting the DACI system's own creation), and a template for future entries. Stored in L6 of the knowledge taxonomy.
**RP Band:** Low RP, low RPM. Clear scope, high governance value.

### 🔴 JOB: STM AI — Notion Export First Full Ingestion
**What's thin:** The pipeline script and pre-classified manifest exist but the first complete Notion → OpenClaw ingestion cycle has not been executed.
**Deliverable:** Completed ingestion with classification report, normalized file tree, validation results, and DACI entry documenting the import. Proof that the pipeline works end-to-end.
**RP Band:** Medium RP, medium RPM.

### 🔴 JOB: STM AI — Token Budget Baseline
**What's thin:** Token tracking is specified but no baseline exists. Unknown: how many tokens per typical request, per agent, per day. Cost model undefined.
**Deliverable:** 1-week token usage log from real operations. Baseline metrics: tokens/request by type, tokens/agent/day, context window utilization. Recommended budget thresholds.
**RP Band:** Low RP, low RPM. Measurement work.


## Tier 2 â€” Unlocks Contributor Activation

### ðŸ”´ JOB: AXIOM â€” Tokenomics Requirements Document
**What's thin:** In-game token economy unspecified. Health metrics, emission constraints, player-facing currency mechanics, bridge between contributor economy (RP) and player economy all undefined.
**Deliverable:** Requirements spec a mechanism designer can build against.
**RP Band:** High RP, high RPM. Foundational IP.

### ðŸ”´ JOB: AXIOM â€” Integration API Draft
**What's thin:** The vision says integration is the product, but no technical spec for how layers communicate state.
**Deliverable:** Event model, state propagation rules, data contracts between all six layers.
**RP Band:** High RP, high RPM. Core architecture.

### ðŸ”´ JOB: AXIOM â€” Galaxy Bible v0.1
**What's thin:** Faction lore, political systems, and history needed for narrative contributors to write within.
**Deliverable:** 3â€“5 factions, agendas, relationships. Enough canon for mission chain writing.
**RP Band:** Medium RP, medium RPM. Creative work.

### ðŸ”´ JOB: AXIOM â€” Prototype Scope Document
**What's thin:** No formal definition of what the prototype demonstrates and which layers are included first.
**Deliverable:** MVP integration spec, layer selection rationale, backer-facing proof of thesis.
**RP Band:** Medium RP, medium RPM.

## Tier 3 â€” Unlocks Investor and Partner Conversations

### ðŸ”´ JOB: Legal Structure Memo
**What's thin:** The OtoCo/Aragon/Series LLC relationships are referenced but unexplained. Contributor agreement templates not drafted.
**Deliverable:** Entity map, legal-entity-to-governance mapping, contributor agreement template.
**RP Band:** High RP, high RPM. Specialized work.

### ðŸ”´ JOB: AXIOM â€” Creator Tool Specification
**What's thin:** The "10K creators earning income" aspiration has no tool spec behind it.
**Deliverable:** User stories, capability scope, publishing flow, approval mechanics, revenue attribution.
**RP Band:** Medium-high RP, medium-high RPM.

### ðŸ”´ JOB: CCA Final Draft
**What's thin:** CCA v1.3 exists in the STE doc but references artifacts (Rev Token Purchase Agreement, RevPoint Allocation Policy) that haven't been finalized.
**Deliverable:** CCA with all cross-references resolved and companion policy documents complete.
**RP Band:** High RP, medium RPM. Governance-critical.

---

# PART 5: DOCUMENT INDEX

This bible synthesizes knowledge from the following source documents:

1. **Smoking_Tigers_Enterprises.md** â€” Governance charter (v1.1, v1.2), business plan, operating model (v1.3), role definitions, agreements framework, CCA, SOAR analysis, BMC, operating diagrams, financial projections, founder questionnaire
2. **Project__Smoking_Tigers_AI.md** â€” Project profile, market analysis, competitive landscape, SWOT, SOAR, BMC, financial model (10-year traditional + lean architecture), RPM calculation, roles, job board
3. **Project__AXIOM_-_A_Living_Universe_Game.docx** â€” Game vision, six layers, design principles, development model, regenerative economics, market analysis, SOAR, BMC, RevPoints budget framework (Revision 2)
4. **Smoking_Tigers_Studio_Model.docx** â€” Studio model, collaboration strategy, atomic job board, role badges, reputation tiers, content taxonomy, clip commons, launch campaign
5. **Regenerative_Media_Alliance.md** â€” RMA whitepaper with Hwang reviewer commentary, collaboration offer, Rev Point exchange agreement, sponsor framework, RPM policy, feasibility analysis

---

6. **OpenClaw_Agent_Architecture_v0.1.docx** — Agent tier architecture (Command, Operations, Specialist), Router specification, Knowledge Pipeline (8-stage Notion → OpenClaw), DACI log schema, knowledge taxonomy (L0–L7), Notion export audit and classification manifest, implementation roadmap

---

*This document is the seed of the STE knowledge system. Every thin spot is a job. Every job that gets completed makes the bible thicker, the agents smarter, and the next contributor easier to activate. The people building the knowledge base are the first users of the system they are describing.*
