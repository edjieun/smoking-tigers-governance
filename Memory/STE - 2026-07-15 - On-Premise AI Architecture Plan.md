---
project: STE
date: 2026-07-15
participants: [Ed Hwang]
source: Transcripts/STE/On Premise AI.md
timestamp_start: "0:00"
timestamp_end: "end"
tags: [on-premise-ai, mac-mini, infrastructure, openclaw, lm-studio, openprojects, secrets, tailscale, transcript-pipeline]
---

# On-Premise AI Architecture Plan

## Summary
Ed's 3-machine home AI stack (M4 laptop + M4 Mac Mini + M1 MacBook) was shut down due to token bleeding — OpenClaw on the Mac Mini was silently falling back to OpenRouter/Sonnet 4.6 because LM Studio had no system prompt configured, preventing local models from handling tool calls. The rebuild plan assigns explicit non-overlapping roles to each machine: laptop = interactive power use + orchestration; Mac Mini = local inference executor (hard local block, no cloud fallback); M1 = OpenProjects transparency layer. Phase 0 is secrets management (encrypted `.env` in private GitHub repo). Phase 1 is Mac Mini as inference server only. Phase 2 adds OpenClaw back with the system prompt fix. Transcript processing via Mattermost `#transcripts` dump interface is the first real pipeline to build.

## Decisions
- Root cause of token bleeding: LM Studio missing system prompt → local models can't handle tool calls → silent cloud fallback.
- Secrets: encrypted `.env` in private GitHub repo; restore = `git pull` + decrypt + `source .env`.
- Mac Mini Phase 1: LM Studio server mode over Tailscale, inference only, no harness.
- Mac Mini Phase 2: OpenClaw re-enabled with system prompt fix; evaluate before replacing with OpenCode.
- Hard local block: Mac Mini never calls cloud; failures notify via Mattermost loudly.
- Primary model: Qwen3.5 9B for orchestration and card writing on Mac Mini.
- Hermes agent: stays on M4 laptop only until local inference is stable.
- OpenProjects on M1: spec (not prompt) is the unit of work; step-by-step status updates = audit trail.
- Dump interface: Mattermost `#transcripts` first → any-format input as target.
- No hardcoded source paths in the transcript pipeline.

## Action Items
- [ ] **Ed:** Create private GitHub repo; consolidate all credentials into encrypted `.env`; document restore procedure.
- [ ] **Ed:** Power on Mac Mini; restore credentials; configure LM Studio with system prompt; enable server mode; test over Tailscale.
- [ ] **Ed:** Write OpenProjects spec template for transcript processing (input → chunk → card writing → Google Drive + 1TB).
- [ ] **Ed:** Configure OpenClaw Mattermost `#transcripts` listener.
- [ ] **Ed:** Validate Qwen3.5 9B orchestration capability (Phase 3).
- [ ] **Ed:** Evaluate Hermes agent on laptop after inference is stable.

## Key Quotes
> "If qwen 3.5 9b can orchestrate, deploy subagents, complete jobs — we are golden." — Ed Hwang

> "One of the issues that I have had with deploying agents is the lack of transparency when work gets done. Often it hallucinates, and doesn't produce the desired result, and it's difficult to see what broke down." — Ed Hwang

> "I don't want to hardcode 'Transcripts' on my laptop as the source. I'd prefer a process where the transcript/meeting link can be 'dumped' into the system, and the agents do the work from there." — Ed Hwang

## Open Questions
- Can Qwen3.5 9B reliably orchestrate multi-step specs with subagents on 16GB M4 RAM?
- Should OpenClaw be replaced with OpenCode headless if it remains buggy after system prompt fix?
- What is the right git-crypt or encryption approach for the `.env` repo?
- When is the Mac Mini coming back online — what's blocking it beyond the plan?
- Should the 1TB storage be the primary output location or Google Drive?
