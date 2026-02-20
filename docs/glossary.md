> Source: Extracted from STE_Knowledge_Bible_v0.3.md, Section 1.1

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
