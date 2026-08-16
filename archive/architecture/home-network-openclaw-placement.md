# Architecture — Home Network and OpenClaw Placement (Consumer-Grade Infrastructure)
Status: Draft v1.0
Owner: Ed (Steward)
Applies To: Home server operations, OpenClaw deployment, remote access workflows
Last Updated: 2026-02-23

## Purpose
Document a practical, secure, consumer-grade home network architecture for running OpenClaw and related services (e.g., Mattermost, local AI workflows, file storage) while supporting:
\- remote work
\- travel use cases
\- a "security gap" between public internet and internal systems
\- reliable access for a small trusted team
\- future expansion (Mac Mini home server, private AI services, backups)

This architecture is designed for real-world constraints, not enterprise perfection.

## Known Hardware and Devices (Current / Expected)
### Core Infrastructure
\- T-Mobile 5G internet gateway / modem
\- Linksys router (consumer-grade)
\- SSD hub / external storage (with backup drive)
\- Cat5-wired condo (MPOE in master bedroom closet)
\- Mac Mini (home server role, planned/active)
\- Laptop (admin \+ local AI \+ operations work)

### Personal / Work Devices
\- iPad Mini
\- iPhone
\- Apple Watch
\- Apple TV (display/ops dashboard use case)

### Team / Collaborator Access (Remote)
\- Executive council members using phones and laptops
\- Mattermost mobile/desktop clients
\- Tailscale (already installed; used for private access path)

## Design Goals
1. **Keep internal services private by default**
2. **Make remote access easy for trusted users**
3. **Separate "communication access" from "admin access"**
4. **Preserve local-first workflows where possible**
5. **Support travel and remote operations**
6. **Avoid overcomplicating a consumer setup**
7. **Create a path to scale later without redoing everything**

## Core Architecture Principle
**OpenClaw should live behind the home network boundary and be reached through a private access layer (e.g., Tailscale), not exposed broadly to the public internet by default.**

This reduces attack surface and keeps the setup manageable.

## High-Level Topology (Recommended)
Internet (T-Mobile 5G Gateway)
→ Linksys Router (primary LAN control)
→ Home LAN devices (Mac Mini server, storage, admin devices)
→ Private access overlay (Tailscale)
→ Remote trusted users (exec council, operator devices)

### Functional Zones (Logical, not necessarily VLAN-based yet)
1. **Edge / Internet Zone**
   \- T-Mobile gateway
   \- WAN connectivity
   \- minimal configuration, avoid complexity if ISP device is limited

2. **Home LAN / Trusted Devices Zone**
   \- Mac Mini server
   \- admin laptop
   \- storage device
   \- personal devices (as needed)

3. **Services Zone (logical)**
   \- Mattermost
   \- OpenClaw
   \- local AI services
   \- file shares / backup services
   \- internal dashboards

4. **Remote Access Overlay**
   \- Tailscale for private connectivity to internal services

5. **Guest / Untrusted Access (recommended separation)**
   \- guest Wi-Fi or separate SSID if supported
   \- no access to internal services

## Role of OpenClaw in This Architecture
OpenClaw is not the network.
OpenClaw is an orchestration/agent layer that sits on top of the infrastructure and helps with:
\- knowledge workflows
\- summaries and drafting
\- operational coordination
\- (optionally) controlled automations

OpenClaw should **not** be treated as a substitute for:
\- router security
\- identity/access management
\- backup strategy
\- secrets management
\- system patching

## Recommended Placement of Key Components

### Mac Mini (Home Server)
Primary role:
\- internal services host (Mattermost/OpenClaw/supporting tools)
\- file processing jobs
\- local AI service endpoints (if configured)
\- backup/automation scripts
\- internal dashboards/status pages (optional)

Placement:
\- wired Ethernet to Linksys router preferred
\- stable power
\- UPS recommended if possible (future upgrade)
\- always-on location with ventilation

### Laptop (Admin / Local AI Workstation)
Primary role:
\- admin console
\- local testing (LM Studio, docs, scripts)
\- emergency operations fallback
\- remote management while traveling

Guidance:
\- do not make laptop the only source of truth for server config
\- keep scripts/configs versioned where practical
\- use laptop to manage, not to permanently host critical team services (unless temporary)

### SSD Hub / External Storage
Primary role:
\- backups
\- archives
\- working storage for media / transcripts / exports (if needed)

Guidance:
\- define what lives here vs on Mac Mini internal storage
\- use clear folder standards
\- do not assume attached storage \= backup unless backup process is defined and tested

## Network Access Model (Recommended)
### 1\) Private-by-Default Services
Services like Mattermost and OpenClaw should be reachable over Tailscale/private network first.

Benefits:
\- fewer public ports exposed
\- simpler small-team trust model
\- easier mobile access for known users
\- cleaner "security gap" story

### 2\) Public Exposure as Exception
If a service must be public (future website, public endpoint, etc.):
\- isolate it from internal admin services
\- use reverse proxy/TLS
\- document why it is public
\- monitor and patch it

Do not expose OpenClaw or admin panels publicly just for convenience.

## Access Tiers (Network \+ Service)
### Tier A — Admin (You / designated SysOps)
\- Tailscale access
\- server admin access
\- service admin panels
\- logs/configs/scripts
\- credential handling (restricted)

### Tier B — Executive Council (Trusted Collaborators)
\- Tailscale access (if required)
\- Mattermost access
\- specific collaboration tools only
\- no server admin by default

### Tier C — Contributors / Guests
\- no home network access unless explicitly needed
\- use public collaboration tools or scoped systems
\- no direct access to internal infrastructure

## Home Router / Consumer Hardware Realities
Because this is consumer-grade infrastructure:
\- expect fewer enterprise controls
\- avoid stacking too many complex features at once
\- prefer simple, documented configurations
\- prioritize stability over "perfect" segmentation initially

Start with:
\- strong Wi-Fi password
\- guest network enabled (if available)
\- firmware updates
\- minimal port forwarding
\- documented device inventory

Then add complexity only if it solves a real problem.

## Security Baseline (Minimum)
### Network / Router
\- change default admin password
\- update firmware
\- disable remote admin from WAN (unless truly needed and secured)
\- use WPA2/WPA3 strong Wi-Fi credentials
\- enable guest network for non-trusted devices (if supported)

### Server (Mac Mini)
\- OS updates on a schedule
\- strong local admin password
\- disk encryption enabled
\- firewall enabled
\- SSH access limited to trusted users/devices
\- no unnecessary services running

### Accounts / Identity
\- unique accounts for collaborators in Mattermost
\- no shared credentials
\- MFA where supported
\- quick offboarding process

### Secrets
\- never store secrets in chat
\- avoid plain-text secrets in random notes/docs
\- keep `.env` files restricted
\- document where secrets live (without exposing values)

## Remote Access for Travel (User \+ Admin)
This setup should support your digital nomad / travel use case.

Recommended pattern:
\- use Tailscale from laptop/phone/tablet to reach home services
\- use Mattermost mobile app for lightweight coordination
\- use laptop for admin tasks (not phone) when changing configs
\- keep a simple emergency runbook for reconnecting or troubleshooting

If using a pocket router while traveling:
\- route your devices through your personal travel network
\- still use Tailscale to reach home services
\- avoid doing sensitive admin work on unknown hotel networks without your usual protections

## Reliability and Backup Strategy (Practical)
### What to Protect First
1. governance/knowledge docs
2. configs/scripts (OpenClaw, Mattermost, automation)
3. exported databases / critical app data
4. media/transcripts (as capacity allows)

### Baseline Backup Pattern
\- primary data on Mac Mini / working systems
\- scheduled backup to external SSD
\- periodic off-device copy for critical docs/configs (manual or automated)

Important:
A drive connected to the same machine is not sufficient disaster recovery by itself.

## Logging and Monitoring (Minimal but Useful)
Track at least:
\- service status (up/down)
\- disk space
\- backup success/failure
\- major access/account changes
\- incidents/outages

This can start as a simple markdown log and grow later.

## Integration Boundaries (OpenClaw \+ Network)
OpenClaw may assist with:
\- generating runbooks
\- drafting config checklists
\- summarizing incidents
\- organizing logs/docs
\- producing maintenance reminders

OpenClaw should not automatically:
\- change router settings
\- expose services publicly
\- alter firewall/network config
\- rotate secrets
\- restart critical services in production
without explicit human authorization and logging.

## Suggested Initial Architecture (Phase 1\)
Use this before adding advanced segmentation:

\- T-Mobile gateway provides internet
\- Linksys router manages home LAN/Wi-Fi
\- Mac Mini on wired Ethernet
\- Mattermost \+ OpenClaw hosted internally
\- Tailscale used for private remote access
\- Exec council gets Mattermost access (not admin access)
\- Backups to SSD hub on scheduled basis
\- Governance docs / decisions promoted to GitHub per policy

This is enough to be useful and safer than ad hoc exposure.

## Future Upgrades (Phase 2+)
Only adopt as needed.

### Potential Improvements
\- UPS for Mac Mini \+ networking gear
\- dedicated backup strategy with restore testing
\- reverse proxy with internal TLS for cleaner service routing
\- VLANs / separate IoT and server segments (if router supports or upgraded)
\- monitoring dashboard
\- NAS or more structured storage
\- managed DNS / domain strategy for internal and public services
\- MDM/device posture for key collaborators (if team grows)

## Failure Modes to Avoid
\- exposing internal services publicly for convenience
\- no backup testing
\- one shared admin account
\- treating Tailscale access as equal to server admin authority
\- storing secrets in chat or broad-access docs
\- running critical services only on an intermittently available laptop
\- changing many network settings at once without documentation

## Operational Checklists (Recommended Companion Docs)
Create separate docs for:
\- `home-network-inventory.md`
\- `tailscale-onboarding-checklist.md`
\- `server-maintenance-checklist.md`
\- `backup-and-restore-checklist.md`
\- `incident-response-runbook.md`

## Review Cadence
Review this architecture after:
\- first 30 days of active use
\- first executive council remote onboarding
\- first outage / incident
\- addition of new major service (e.g., public endpoint, NAS, new AI stack)
\- major hardware change (router/server/storage)
