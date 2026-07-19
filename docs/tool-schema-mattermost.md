# Tool Schema: Mattermost
**Type:** Schema Document — Descriptive Only
**Created:** 2026-03-25
**Owner:** Ed (Steward)
**Status:** Draft

---

## Overview

Mattermost is the internal operational communication platform for the Smoking Tigers agent network and exec team. It is the primary surface for agent interaction, operational alerts, and internal coordination. All agents are accessible via Mattermost. It is not the community platform (that's Discord).

---

## Instance

- **URL:** `http://localhost:8065` (Tailscale-accessible at Mac Mini IP)
- **Deployment:** Docker (self-hosted, `~/mattermost/docker-compose.yml`)
- **Bind address:** `0.0.0.0:8065` — accessible on LAN + Tailscale
- **Database:** PostgreSQL (Docker-internal)
- **Public internet exposure:** None (no port forwarding from T-Mobile)

---

## Teams

| Team | Name | ID | Scope |
|------|----|----|----|
| smoking-tigers | Smoking Tigers | `m84jdyhe8iyb9y9wf1upxq4w4r` | Single team — all STM ops |

*No Q1-specific Mattermost team. Q1 does not use this instance.*

---

## Channels

| Channel | Display Name | ID | Purpose | Agent(s) Present |
|---------|-------------|----|---------|----|
| #executive | Executive | `krzyoit3gjgkuqqxenf6e7qscw` | Primary Scout interaction; Ed's main command channel | Scout (main) |
| #chief-of-staff | Chief Of Staff | `nhpxutoh5jf17fr71aa6jdp9co` | Scout operational channel | Scout (main) |
| #ea | EA | `z74q9ycpot8ebe8ncq7xpcammw` | EA agent coordination | EA |
| #governance | Governance | `th6m56e8r7dmimihhewog6nfbe` | Governance ops activity | Governance Ops |
| #knowledge | Knowledge | `kd5gz7fz3bgudx4o1norcmnsay` | Knowledge ops + Notion intake | Knowledge Ops, Notion Intake Bot |
| #sysops | Sysops | `7s5prot6jfdxjx7m9j75g55jjw` | System operations | Sysops |
| #router | Router | `ujpwrxw6n383xmxtei9jmui8bo` | Internal routing / orchestration | — |
| #svp-christine | SVP Christine | `onr9euqt3tyifjh8fb36d5se4e` | Christine's exec channel | Rosie (christine-ea) |
| #ai-test | AI Test | `okhn63zy63n73p19ha7d8u1koc` | Testing / sandbox | — |
| #off-topic | Off-Topic | `8z9s7qgqnjrqbei519zgma4gay` | General / casual | — |
| #town-square | Town Square | `szqm9frcsigemkkfttetr11pth` | Default Mattermost channel | — |

---

## Users & Bots

| Username | Display Name | Role | Type |
|----------|-------------|------|------|
| @edlicious | Ed H | System Admin | Human |
| @christinefrancis | Christine | User | Human |
| @st-build-cos-bot | ST Chief of Staff (Build) | User | Bot — Scout (main) |
| @st-build-ea-bot | ST Executive Assistant (Build) | User | Bot — EA |
| @st-build-governance-ops-bot | Governance Ops | User | Bot |
| @st-build-knowledge-ops-bot | Knowledge Ops | User | Bot |
| @st-build-saa-bot | Sergeant at Arms | User | Bot |
| @st-build-sysops-bot | ST Systems Operations (Build) | User | Bot — Sysops |
| @rosie | Rosie | User | Bot — christine-ea |
| @sonnetops-bot | SonnetOps | User | Bot |
| @st-notion-intake | Notion Intake Bot | User | Bot — Notion bridge |
| @calls | Calls | User | System plugin |
| @system-bot | System | User | System |

**DM policy:** `open` — any user can DM any bot directly.
**Chat mode:** `oncall` — agents respond when addressed or in their bound channels.

---

## Agent–Channel Bindings

| Agent | Primary Channel | Bot Username |
|-------|----------------|-------------|
| Scout (main) | #executive, #chief-of-staff | @st-build-cos-bot |
| EA | #ea | @st-build-ea-bot |
| Governance Ops | #governance | @st-build-governance-ops-bot |
| Knowledge Ops | #knowledge | @st-build-knowledge-ops-bot |
| Sergeant at Arms | — | @st-build-saa-bot |
| Sysops | #sysops | @st-build-sysops-bot |
| Rosie (christine-ea) | #svp-christine | @rosie |
| Notion Intake | #knowledge | @st-notion-intake |

---

## OpenClaw Configuration

- **Primary account token:** `ixx5fu8qdibczp3f9xnem7ahur` (Scout/main)
- **Streaming:** Enabled (`blockStreaming: false`)
- **Coalesce limit:** 6000 chars per chunk
- **Additional bot tokens:** Separate tokens per agent (`sys-ops`, `ea`, `governance-ops`, etc.)
- **Heartbeat:** Every 1 hour (Scout)

---

## How It Connects to Other Tools

| Tool | Connection | Direction |
|------|-----------|-----------|
| OpenClaw | All agents communicate via Mattermost | Bidirectional |
| Notion | Notion Intake Bot bridges #knowledge → Notion | Inbound to Notion |
| GitHub | No direct integration | — |
| Google Drive | No direct integration | — |
| Discord | No direct connection — separate platforms | — |

---

## STM vs. Q1 Distinction

| Dimension | STM | Q1 |
|-----------|-----|----|
| Instance | Self-hosted at Mac Mini | Q1 does not use this instance |
| Access | Ed + exec team via Tailscale | No Q1 access |
| Agents | All STM agents bound here | — |

*This is a fully STM-scoped tool. Q1 does not have presence or access.*

---

## Known Gaps / Open Items

- Mattermost binds to `0.0.0.0` — decision pending: lock to Tailscale IP only vs. keep on all interfaces
- Mac Mini DHCP — IP is not reserved; if lease renews with a new IP, Tailscale routing could break
- `#router` channel purpose not fully documented — unclear if active
- `@sonnetops-bot` purpose undocumented — not mapped to a known agent config
- No webhook integrations to GitHub, Notion, or Discord
- No formal onboarding checklist for adding new exec members to Mattermost
- Christine accesses via #svp-christine through Rosie — no direct human login confirmed

---

## Canonical Role

> Mattermost is the **internal operational backbone**. All agent interaction, operational alerts, and exec coordination happen here. It is the command layer for the AI agent network. Not a community platform — that's Discord.
