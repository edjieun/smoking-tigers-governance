---
title: SOP — Nerve (OpenClaw Web UI)
status: Active
last-updated: 2026-07-19
op_task: https://ste-business-server.tailebe6d3.ts.net:8080/projects/ste-ai-buildout/work_packages/249
tier: On Premise
source: edjieun/openclaw-nerve (fork of daggerhashimoto/openclaw-nerve)
---

# SOP: Nerve — OpenClaw Web UI

## Who / What / Where / Why / How

**Who:** Ed Hwang (primary user), future team members
**What:** Browser-based control plane for OpenClaw/TigerClaw agents — chat, voice, kanban, workspace browser, session management, agent monitoring
**Where:** Mac Mini, port 3080 — accessed from M4 Laptop at `http://100.104.149.107:3080` (Tailscale) or `http://192.168.1.253:3080` (LAN)
**Why:** Replaces raw Mattermost as the human-facing agent operating surface; provides visibility into agent state, task delegation, and kanban workflows without staying inside a chat thread
**How:** Node.js server (`~/nerve/`) connects to OpenClaw gateway via WebSocket; served to browser; communicates via OpenClaw gateway token

---

## What Nerve Can Do

| Feature | Description |
|---|---|
| **Chat** | Talk to agents; full streaming response UI |
| **Voice** | Push-to-talk, wake word, local Whisper transcription, TTS output |
| **Kanban** | Delegate work to agents as cards; review what came back |
| **Sessions** | Browse and inspect past agent sessions; watch cron runs |
| **Workspace browser** | Browse and edit agent workspace files live in browser |
| **Memory** | Inspect what agents remember |
| **Dashboard** | Token usage, costs, context pressure, agent activity |
| **Settings** | Model overrides, agent config, identity/soul/skills |
| **File browser** | Browse agent workspace files |

---

## What Nerve Is NOT

- Not a standalone app — it requires OpenClaw/TigerClaw gateway running on Mac Mini (:18789)
- Not a router between harnesses — Nerve connects to exactly one gateway
- Kanban is for delegating work to agents inside OpenClaw — not a general project management board

---

## Service Configuration

| Item | Value |
|---|---|
| Install path | `~/nerve/` |
| Port | `3080` |
| Process manager | launchctl (`com.nerve.server`) |
| Gateway URL | `http://127.0.0.1:18789` (OpenClaw, loopback) |
| Bind | `HOST=0.0.0.0` (all interfaces — Tailscale accessible) |
| Allowed WS hosts | `100.104.149.107, 192.168.1.253, localhost, 127.0.0.1` |
| Access URL (Tailscale) | `http://100.104.149.107:3080` |
| Health check | `curl http://100.104.149.107:3080/health` → `{"gateway":"ok"}` |

---

## How to Open Nerve in Browser

1. Navigate to `http://100.104.149.107:3080` in Chrome on M4 Laptop
2. If you see a blank page or stale connection error:
   - Open Chrome DevTools (Cmd+Option+J)
   - Run: `localStorage.removeItem('oc-config'); location.reload()`
   - Nerve will auto-connect to OpenClaw gateway
3. Confirm status bar shows `gateway: ok`

---

## How to Restart Nerve on Mac Mini

```bash
ssh edhwang@192.168.1.253
launchctl stop com.nerve.server
sleep 2
launchctl start com.nerve.server
curl -s http://127.0.0.1:3080/health
```

---

## Known Issues

| Issue | Status | Fix |
|---|---|---|
| Browser shows blank / won't connect | ⚠️ Common after config changes | `localStorage.removeItem('oc-config')` in DevTools |
| `gateway: error` in status bar | Config points to wrong gateway | Check `GATEWAY_URL` env var — must be `:18789`, not `:42617` (ZeroClaw) |
| Kanban capability scope | ⏳ Not yet fully tested | See [OP #256](https://ste-business-server.tailebe6d3.ts.net:8080/projects/ste-ai-buildout/work_packages/256) — blocked on browser access |

---

## Open Questions

- What kanban card schema does Nerve use? (see OP #256 — requires reading `~/nerve/src/features/kanban/` source)
- Does Nerve trigger agent execution, or only display state? (OP #257 — ADR-0004)
- Can Nerve connect to OpenProjects for cross-board visibility? (OP #257)
