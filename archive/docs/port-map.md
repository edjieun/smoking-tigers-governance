---
title: Port Map — TigerClaw Infrastructure
status: Active (living doc)
last-updated: 2026-07-19
op_task: https://ste-business-server.tailebe6d3.ts.net:8080/projects/ste-ai-buildout/work_packages/247
tier: On Premise
owner: Ed Hwang
---

# Port Map — TigerClaw Infrastructure

> Living document. Update this file before deploying any new service.
> Every service must appear here with its port, bind address, and Tailscale exposure.

---

## Mac Mini (edlicious-server)

**Tailscale IP:** `100.104.149.107`
**LAN IP:** `192.168.1.253` ⚠️ DHCP — reservation pending (see [OP #277](https://ste-business-server.tailebe6d3.ts.net:8080/projects/ste-ai-buildout/work_packages/277))
**Wi-Fi MAC (en1 — active):** `d6:a1:92:42:bb:ff`
**Ethernet MAC (en0 — unused):** `d0:11:e5:e6:89:05`
**Router:** Linksys MR5500 — admin at `http://192.168.1.1`

| Service | Port | Bind | Tailscale Exposed | Tier |
|---|---|---|---|---|
| LM Studio (inference) | 1234 | 0.0.0.0 | ✅ Yes | On Premise |
| OpenClaw / TigerClaw gateway | 18789 | 127.0.0.1 | ⚠️ Loopback only | On Premise |
| ZeroClaw memory backend | 42617 | 127.0.0.1 | ⚠️ Loopback only | On Premise |
| Nerve UI | 3080 | 0.0.0.0 | ✅ Yes | On Premise |
| mcp-searxng | TBD | 127.0.0.1 | ⚠️ Loopback only | On Premise |
| mcp-crawl4ai-ts | TBD | 127.0.0.1 | ⚠️ Loopback only | On Premise |

---

## M1 MacBook (ste-business-server)

**Hostname:** `ste-business-server.tailebe6d3.ts.net`

| Service | Port | Bind | Tailscale Exposed | Tier |
|---|---|---|---|---|
| OpenProjects | 8080 | 0.0.0.0 | ✅ Yes | On Premise |
| Mattermost | 8065 | 0.0.0.0 | ✅ Yes | On Premise |
| LedgerSMB | 5762 | 0.0.0.0 | ✅ Yes | On Premise |

No current conflicts. All three services share the hostname, differentiated by port.

---

## M4 Laptop (on-device)

| Service | Port | Notes |
|---|---|---|
| VS Code / Copilot / OpenCode | — | No exposed ports |
| Obsidian | — | Local only |

---

## Conflict Risk Register

| Risk | Status | Action |
|---|---|---|
| Mac Mini LAN IP drift (DHCP) | ⏳ [OP #277](https://ste-business-server.tailebe6d3.ts.net:8080/projects/ste-ai-buildout/work_packages/277) | Ed: open http://192.168.1.1 → DHCP Reservations → add MAC `d6:a1:92:42:bb:ff` → `192.168.1.253` |
| ZeroClaw loopback — Scout (OpenClaw) can't reach it | ⚠️ Open | Resolve in ADR-0003 |
| New service on ste-business-server near 8080/8065/5762 | ⚠️ Watch | Check this doc first |
| OpenClaw :18789 loopback — not directly browser-accessible | ✅ By design | Nerve connects via gateway token over WS |

---

## How to Add a New Service

1. Confirm the port is not already in the tables above
2. Add a row to the correct machine table
3. Specify bind address: `127.0.0.1` (loopback, no external access) or `0.0.0.0` (all interfaces, Tailscale-accessible)
4. Commit this file **before** deploying the service
5. Update the conflict risk register if any risk applies
