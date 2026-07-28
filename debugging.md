# Debugging Reference — TigerClaws

> Patterns and known issues for debugging the TigerClaw agent stack.
> This file is a living stub — add entries as issues are encountered and resolved.

---

## Common Failure Patterns

### OpenProjects API

| Symptom | Likely cause | Fix |
|---|---|---|
| `401 Unauthorized` | Wrong auth scheme | Use `Basic` not `Bearer` — see `.github/skills/openprojects/SKILL.md` |
| `409 Conflict` on PATCH | Stale `lockVersion` | Fetch WP again, get fresh `lockVersion`, retry |
| `403` on user delete | OP design limitation | Use `PATCH /users/{id}` with `{"status":"locked"}` instead |
| Empty WP list | Wrong project ID or filter | Check project ID in AGENTS.md; verify filter URL encoding |

### Tailscale / Network

| Symptom | Likely cause | Fix |
|---|---|---|
| Can't reach `ste-business-server.*` | Tailscale session expired | Open Tailscale app → re-auth (one click, 90-day rotation) |
| `ste-business-server` resolves but port times out | Service down on M1 | SSH to M1, check `docker ps` or service status |
| Mac Mini unreachable at `100.104.149.107` | Mini asleep or offline | Wake via WoL or ask Ed |

### LM Studio / Local Inference

| Symptom | Likely cause | Fix |
|---|---|---|
| `connection refused` at `:1234` | LM Studio not running | Launch LM Studio, load model, start server |
| Slow responses | Wrong model loaded | Check active model — should be Qwen3.5 9B for agents |
| Empty completions | Context overflow | Reduce input size; `defaultContextLength: 32768` |

### Mattermost

| Symptom | Likely cause | Fix |
|---|---|---|
| Agent not responding in `#tigerclaw` | Scout not running on Mac Mini | Check OpenClaw process on Mac Mini |
| Messages duplicating | Multiple agent instances | Kill duplicate OpenClaw processes |

---

## Credential Issues

See `scripts/recover-credentials.md` for step-by-step credential recovery procedures.
Secrets location: `~/.ste-secrets/.env`

---

## Log Locations

| System | Log location |
|---|---|
| OpenClaw / TigerClaw | `~/.openclaw/logs/` (Mac Mini) |
| ZeroClaw | Mac Mini, port 42617 — check service logs |
| GitHub Actions | `.github/workflows/` → Actions tab in `edjieun/smoking-tigers-governance` |

---

## Adding to This File

When you resolve a non-obvious issue, add it here:
```
| [symptom] | [cause] | [fix] |
```

*Last updated: 2026-07-28*
