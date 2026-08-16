# Tool Schema: GitHub
**Type:** Schema Document — Descriptive Only
**Created:** 2026-03-25
**Owner:** Ed (Steward)
**Status:** Draft

---

## Overview

GitHub is used as the canonical source of truth for governance decisions, policies, architecture documents, and formal agreements. It is the authoritative layer for anything that requires version history, auditability, or immutable record.

---

## Repositories

### STM Scope

| Repo | Visibility | Path (Local Mirror) | Purpose |
|------|-----------|---------------------|---------|
| `edjieun/smoking-tigers-governance` | Private | `~/srv/q1/governance/smoking-tigers-governance/` | STM governance decisions, policies, architecture, agreements, charters |

### Q1 Scope

| Repo | Visibility | Path (Local Mirror) | Purpose |
|------|-----------|---------------------|---------|
| `edjieun/governance` | Public (fork) | `~/srv/q1/governance/q1-governance/` | Q1 parent governance — operating agreement, financial model, community standards |

### Not in Scope
- No application code repositories currently active under this account for STM operations
- No CI/CD pipelines connected to OpenClaw or agent infrastructure

---

## STM Governance Repo Structure (`smoking-tigers-governance`)

```
smoking-tigers-governance/
├── README.md
├── DECISIONS_INDEX.md          — Master index of all formal decisions
├── ONBOARDING-LOCAL-MACHINE.md
├── LICENSE
├── _incoming/                  — Staged documents pending processing
├── agreements/                 — Formal agreements (RTPA, contributor, invoices)
├── analysis/                   — Ad hoc research and cost analysis docs
├── architecture/               — System architecture documents
│   └── home-network-openclaw-placement.md
├── charters/
│   └── smoking-tigers-charter.md
├── decisions/                  — Individual decision records (DEC-YYYYMMDD-NNN)
├── docs/                       — Reference documents
│   ├── index.md
│   ├── glossary.md
│   ├── governance-overview.md
│   ├── knowledge-sources.md
│   ├── knowledge-channel-sop.md
│   ├── scout-interaction-surface.md
│   ├── exec-mattermost-onboarding.md
│   └── smoking-tigers-enterprises.md
├── governance/
│   └── directory.md
├── knowledge-bible/
│   ├── STE_Knowledge_Bible_v0.3.md
│   └── trade-like-nick-bible-v1.0.md
├── policies/                   — Formal policy documents
├── projects/                   — Project-specific governance artifacts
└── workflows/                  — Agent and operational workflows
```

### Q1 Governance Repo Structure (`q1-governance`)

```
q1-governance/
├── readme.md
├── standards.md
├── docs/
│   ├── operating-agreement.md
│   ├── financial-model.md
│   ├── community-agreement.md
│   ├── ic-agreement.md
│   ├── igs-roles.md
│   ├── code-of-conduct.md
│   ├── rules-and-regs.md
│   ├── glossary.md
│   ├── privacy-policy.md
│   └── terms-of-service.md
└── flows/
    ├── fm-changes.md
    ├── org-investment-ledger-governance.md
    └── q-git.md
```

---

## Access & Authentication

| Actor | Access Level | Method |
|-------|-------------|--------|
| Ed (@edlicious) | Owner / Admin | `gh` CLI (authenticated) |
| Scout (main agent) | Read + write (with instruction) | `gh` CLI via host shell |
| Other agents | None (no token configured) | — |
| christine-ea | Read-only intent, no token configured | Blocked — pending GitHub token from Ed |

**Note:** No organization-level GitHub account configured. Repos live under personal account `edjieun`.

---

## How It Connects to Other Tools

| Tool | Connection | Direction |
|------|-----------|-----------|
| OpenClaw workspace | Local mirror of repos at `~/srv/q1/` | Pull (on-demand, manual sync) |
| Notion | Governance decisions linked by URL in Notion records | Reference only |
| Google Drive | No direct connection | — |
| Mattermost | No direct integration | — |
| Discord | No direct integration | — |

---

## STM vs. Q1 Distinction

| Dimension | STM (`smoking-tigers-governance`) | Q1 (`q1-governance`) |
|-----------|----------------------------------|----------------------|
| Scope | STM entity — projects, decisions, operations | Parent governance — Q1 framework |
| Visibility | Private | Public (fork of Q1 canonical) |
| Authority | STM Steward (Ed) | Q1 parent org |
| Agents with access | Scout (read/write), others none | Scout (read), others none |
| Change process | Steward approval → commit | Q1 process |

---

## Known Gaps / Open Items

- No CI/CD or branch protection rules configured
- No organization-level account (all repos under personal `edjieun`)
- GitHub tokens not provisioned for EA or governance-ops agents — Phase 2 item
- `DECISIONS_INDEX.md` and individual decision files not yet indexed by knowledge-ops nightly run (planned Phase 2)
- No webhook integration with Mattermost or Notion
- `_incoming/` folder used as staging area but no automated processing

---

## Canonical Role

> GitHub is the **policy and decisions layer**. If a governance document exists only in Notion or Google Drive, it is not authoritative. The canonical copy must be committed to the governance repo.
