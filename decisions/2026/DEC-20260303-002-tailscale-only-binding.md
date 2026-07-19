# DEC-20260303-002 — Restrict Mattermost and Cal.com Access to Tailscale Network Only

**Decision ID:** DEC-20260303-002
**Title:** Restrict Mattermost and Cal.com Access to Tailscale Network Only
**Status:** Approved
**Date:** 2026-03-03
**Owner / Approver:** Ed (Steward)

---

## Context

Both Mattermost (port 8065) and Cal.com (port 3000) currently bind to `0.0.0.0`, making them reachable on all network interfaces including the local LAN. The security posture for STM calls for restricting access to Tailscale-authenticated users only.

An initial approach (binding Docker ports directly to the Tailscale IP `100.122.103.40`) was attempted on 2026-03-03 but failed. Docker Desktop for macOS runs services inside a Linux VM and cannot bind to macOS host network interfaces (including Tailscale/utun interfaces). The Mattermost compose file has Tailscale IP configured but Docker silently falls back to `0.0.0.0`.

## Decision

Access to Mattermost and Cal.com will be restricted to Tailscale-authenticated users using **Tailscale Serve** as the access control mechanism, combined with macOS `pf` firewall rules to block direct LAN access to the service ports.

### Implementation approach:

1. **Tailscale Serve** — configure Tailscale to proxy Mattermost and Cal.com via the Tailscale network:
   - `tailscale serve https:443 / http://localhost:8065` (Mattermost)
   - `tailscale serve https:4430 / http://localhost:3000` (Cal.com, alternate port)

2. **macOS pf firewall** — block ports 8065 and 3000 from all non-loopback, non-Tailscale source addresses at the OS level so direct LAN access is rejected even while Docker binds to `0.0.0.0`

3. **No Docker changes required** — services continue to bind to `0.0.0.0` internally; access control is enforced at the OS/Tailscale layer

### Access after implementation:
- Mattermost: `https://edlicious-server.tailebe6d3.ts.net`
- Cal.com: `https://edlicious-server.tailebe6d3.ts.net/calcom`
- Direct LAN access (192.168.x.x:8065, :3000): blocked

## Rationale

- Direct Docker IP binding to Tailscale interface is not possible on Docker Desktop for macOS
- Tailscale Serve is the designed mechanism for exactly this use case — proxying local services onto the Tailscale network with authentication
- pf firewall rules provide defense-in-depth at the OS layer
- No service disruption during implementation — no container restart required for Tailscale Serve approach

## Tradeoffs / Risks

- **Tailscale dependency strengthened:** if Tailscale daemon is unhealthy, Mattermost and Cal.com are unreachable until resolved — intentional, but operationally significant
- **pf firewall rules persist across reboots** only if loaded via LaunchDaemon — sysops must ensure rules survive restarts
- Tailscale Serve HTTPS adds TLS termination — certificates managed by Tailscale automatically
- LAN-only access path eliminated — intentional

## Impacts

- Sysops: implements Tailscale Serve config + pf rules; responsible for reboot persistence
- Ed / STM users: access Mattermost and Cal.com via Tailscale hostname after change
- Network architecture docs: update to reflect Tailscale Serve as the access layer
- Monitoring: should alert if Tailscale daemon goes unhealthy

## Dependencies

- Tailscale daemon running and stable on Mac Mini
- Tailscale Serve feature available (standard in Tailscale v1.32+)
- macOS pf firewall (built-in)
- Sysops authorization to configure Tailscale Serve and pf rules
- Ed's explicit approval before execution

## References / Sources

- Infrastructure clarity session: 2026-03-03
- Failed attempt: Docker port binding to Tailscale IP not supported on Docker Desktop for macOS
- Tailscale Serve docs: https://tailscale.com/kb/1312/serve
- Related: DEC-20260303-001 (Cal.com installation)

## Change History

| Date | Change | Author |
|------|--------|--------|
| 2026-03-03 | Initial draft — Docker IP binding approach | Governance Ops |
| 2026-03-03 | Revised — Tailscale Serve + pf firewall approach after Docker binding failure | Scout |
| 2026-03-03 | Status set to Deferred — revisit when adding external collaborators or after Cal.com test/deploy cycle | Scout |
| 2026-03-04 | Approved by Ed (Steward) — execute Tailscale Serve + pf firewall | Ed |
