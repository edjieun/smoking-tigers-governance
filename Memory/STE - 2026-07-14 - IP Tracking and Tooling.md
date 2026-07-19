---
project: STE
date: 2026-07-14
participants: [Ed Hwang, Christine Francis]
source: Transcripts/STE/STE - 2026-07-14.md
timestamp_start: "47:00"
timestamp_end: "1:07:00"
tags: [ip, tooling, entire-io, xprize, rev-tokens, hypha, agent-licensing, spec-coding]
---

# IP Tracking and Tooling

## Summary
Christine introduced Entire.io (from the creators of GitHub, ~$60M raised) as a key tool for capturing IP provenance — it records the process of how agents work, not just the output, making it a legitimate audit trail for collaborative AI-generated work. This connects to Christine's earlier XPRIZE concept: a browser-layer tool that logs all agent API calls and sessions, enabling a structured IP generation system. Ed linked this to spec coding vs. vibe coding as a community differentiator and to the need for decision logs / ADRs in AI project work. The idea board model was refined: contributors post lightweight ideas with implied joint-venture terms baked in (a % of future IP goes back to the original idea poster), with the Quorum1 Rev Token / Hypha smart contract stack as the enforcement layer. Current state: spreadsheets — path to app via AI-assisted conversion.

## Decisions
- Entire.io is the target platform for IP process capture once available; Claude recommended it as a legitimate tool to build alongside.
- The community idea board will have joint-venture terms built in by default: posting an idea means accepting that contributors get equity, and the original poster retains a creator's fee (suggested ~10% equity).
- Spec coding over vibe coding is the community's stated technical value — this is a video topic and a community positioning statement.
- The monetization model for agents is service-based (help you build it), not product-based (sell the agent file itself) — at least for now.
- Rev Tokens + Hypha smart contracts are the target stack for IP equity tracking, but not the immediate priority.
- Current IP tracking is in spreadsheets; the AI-to-app conversion path is viable but deferred.

## Action Items
- [ ] **Christine:** Don't lose track of the Entire.io / XPRIZE concept — flag for a dedicated session when bandwidth allows.
- [ ] **Ed:** Draft the joint-venture terms language for the idea board (simple version — before worrying about Rev Token enforcement).
- [ ] **Both:** Identify the first seed idea to post on the board (suggested: on-device research agent setup as a small, scoped project).

## Key Quotes
> "Instead of just committing the code, you're actually committing the process. So it stores how the agents do it rather than just what they've created." — Christine Francis (describing Entire.io)

> "Spec coding versus vibe coding — that's a topic. That's a great video." — Christine Francis

> "If you put it on the board, you're giving it to people to say, hey, if you create IP from this, you have permission, but I get a portion of that because I'm the original IP creator." — Ed Hwang

## Open Questions
- When is Entire.io available for integration? Is there a waitlist or beta?
- What are the exact joint-venture terms for the idea board? (Simple language version needed before launch.)
- How does the agent licensing model work in practice — rental (community server) vs. ownership (local copy)? Pricing TBD.
