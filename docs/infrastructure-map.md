# Infrastructure Map — Smoking Tigers / Ed's Setup
> Last updated: 2026-03-03

---

## Network Topology

```
Internet
    │
    ▼
T-Mobile 5G Router (WAN / ISP)
    │
    ▼
Linksys Router (primary Wi-Fi / LAN gateway)
    │
    ├── Mac Mini M4 (192.168.1.x — DHCP, not reserved)
    ├── MacBook 13" M4 (192.168.1.192 — active)
    ├── iPhone 15 Pro (Tailscale peer)
    ├── iPad 161 (192.168.1.55 — active, Tailscale peer)
    └── [other devices]
```

**Tailscale overlay network (100.x.x.x):**

| Device | Tailscale IP | Status |
|--------|-------------|--------|
| Mac Mini (edlicious-server) | 100.122.103.40 | This machine |
| MacBook Air | 100.71.214.17 | Active, direct |
| iPad | 100.123.110.8 | Active, direct |
| iPhone 15 Pro | 100.126.231.111 | — |

**Key facts:**
- T-Mobile is the ISP; Linksys is the home router/Wi-Fi
- Mac Mini is on DHCP — no static/reserved IP (⚠️ risk: IP can change on reboot/lease renewal)
- Tailscale provides VPN overlay for cross-device access
- No direct port forwarding from T-Mobile to LAN confirmed

---

## Services Running on Mac Mini

| Service | Bind Address | Port | Exposure |
|---------|-------------|------|----------|
| OpenClaw gateway | 127.0.0.1 | 18789 | Loopback only |
| Mattermost | 0.0.0.0 | 8065 | ⚠️ All interfaces — accessible via Tailscale |
| Cal.com | 0.0.0.0 | 3000 | ⚠️ All interfaces — accessible via Tailscale |
| Ollama | 127.0.0.1 | 11434 | Loopback only |
| cal-postgres | internal | 5432 | Docker-internal only |
| cal-redis | internal | 6379 | Docker-internal only |
| mm-postgres | internal | 5432 | Docker-internal only |

**Current exposure posture:**
- Mattermost (8065) binds to `0.0.0.0` — reachable on Tailscale IP + local LAN
- Cal.com (3000) binds to `0.0.0.0` — same
- OpenClaw itself is loopback-only, but Mattermost is a partial surface for it
- No public internet exposure confirmed (no port forwarding from T-Mobile)

**Recommended action (Phase 1 output):**
- Reserve Mac Mini DHCP lease in Linksys router (prevent IP drift)
- Decision needed: Should Mattermost and Cal.com bind to Tailscale IP only vs. 0.0.0.0?

---

## Storage Layout

### Local (Mac Mini)

| Path | Purpose |
|------|---------|
| `~/.openclaw/workspace/` | Scout workspace — agents, memory, scripts, docs |
| `~/srv/q1/governance/smoking-tigers-governance/` | STM governance repo (private GitHub mirror) |
| `~/srv/q1/governance/q1-governance/` | Q1 governance repo (public) |
| `~/srv/q1/governance/_readonly/` | Read-only mirrors |
| `~/q1_knowledge/` | Local knowledge base (00_core, 10_smoking_tigers, 20_quorum1, 30_ops, 40_templates, 90_archive) |
| `~/Desktop/intake/` | Document drop zone for intake pipeline |
| `~/meetings/` | Meeting notes (at least one entry: 2025-12-XX-first-meeting) |
| `~/mattermost/` | Contains docker-compose.yml — Mattermost container config |

### Cloud

| Service | Path / Location | Purpose |
|---------|----------------|---------|
| Google Drive (Shared) | `Shared/q1 creative/smoking tigers` | Project artifacts — deliverables, IP |
| iCloud | Ed's iCloud | Apple ecosystem sync, doc handoff |
| GitHub | edjieun (private) | Governance repos, code |

**Artifact philosophy:**
- Notion as the tracking layer (projects, meetings, tasks, contributors, RevPoints)
- Folder structures kept flat; artifacts tracked by reference in Notion not deep nesting
- Google Drive is the artifact store; Notion is the index

**Gaps:**
- `~/meetings/` and `~/mattermost/` contents unclear — review needed
- No defined IP/deliverable folder structure yet (Phase 2 item)
- Google Drive index (`ste-index.md`) not built

---

## Security Boundaries

| Surface | Who Has Access | Sensitivity | Notes |
|---------|---------------|-------------|-------|
| Apple data (iCloud, iMessage, Keychain, Notes, Reminders) | Scout (main), EA only | 🔴 High | Both have FDA. No other agents. |
| GitHub (edjieun) | Scout only | 🟡 Medium | gh CLI authenticated; no push without explicit instruction |
| Governance repos | Scout, governance-ops (read-only by default) | 🟡 Medium | No policy writes without Steward approval |
| Mattermost | All bots, Ed | 🟡 Medium | dmPolicy=open on private server |
| OpenClaw config | Scout only | 🔴 High | No config changes without explicit instruction |
| Docker / services | Scout, sysops | 🟡 Medium | Sysops can manage; no destructive actions without confirmation |
| Mac Mini local filesystem | Scout (main) | 🔴 High | FDA granted |

**FDA holders confirmed:** Scout (main), EA

**Open security questions:**
1. Mattermost + Cal.com bind to `0.0.0.0` — is Tailscale-only access the intent, or should these be locked to Tailscale IP?
2. Tailscale ACLs — are they configured, or is the full Tailscale network trusted?
3. Mac Mini DHCP — reserve the IP to prevent service disruption

---

## Open Items from Phase 1

- [ ] Reserve Mac Mini IP in Linksys DHCP (prevent drift)
- [ ] Decision: Lock Mattermost + Cal.com to Tailscale IP binding vs. 0.0.0.0
- [ ] Review `~/meetings/` and `~/mattermost/` — determine if anything important lives there
- [ ] Build Google Drive index (`ste-index.md`)
- [ ] Define Tailscale ACL policy (who can reach what)
- [ ] Cal.com deployment window — schedule with Ed when ready
