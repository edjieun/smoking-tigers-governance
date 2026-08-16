# Incident: SonnetOps agent removal (gateway registry)

**Date:** 2026-02-24  
**Status:** Resolved  
**Owner:** Ed (Steward)  
**Component:** OpenClaw Gateway / Agent Registry  
**Severity:** Medium  

## Summary
Removal of `sonnetops` agent from gateway agent registry was required. Final resolution completed on macOS via launchctl restart.

## Change
**Registry file:** `/Users/edlicious/.openclaw/gateway/config/agents.yaml`  
**Action:** Removed the agent entry:
- `id: sonnetops`

## Runtime
**Detected:** macOS `launchctl`

## Restart
`launchctl kickstart -k gui/504/ai.openclaw.gateway`

## Verification
- `openclaw agent list` shows no `sonnetops`
- Gateway logs contain no references to `SonnetOps` / `sonnetops`

## Follow-ups
- Codify orchestrator behavior for Dashboard Main (see CHIEF_OF_STAFF_ORCHESTRATOR.md)
