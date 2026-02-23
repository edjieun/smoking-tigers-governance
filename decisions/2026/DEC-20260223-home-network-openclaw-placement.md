# DEC-20260223-home-network-openclaw-placement

**Decision ID:** DEC-20260223-010
**Title:** Document Home Network and OpenClaw Placement Architecture
**Status:** Approved
**Date:** 2026-02-23
**Owner / Approver:** Ed (Steward)

## Context
OpenClaw and related services run on consumer-grade home infrastructure. A documented architecture is needed to support secure remote access, travel use cases, and team collaboration.

## Decision
Adopt a home network architecture document defining private-by-default service placement, Tailscale-based remote access, tiered access controls, and phased upgrade path.

## Rationale
- Reduces attack surface by keeping services behind private network
- Supports digital nomad and travel use cases
- Creates a clear path to scale without redoing everything

## Tradeoffs / Risks
- Consumer hardware limitations vs enterprise controls
- Single point of failure with home internet connectivity

## Impacts
- OpenClaw and Mattermost accessed through Tailscale by default
- Mac Mini designated as primary internal services host

## Dependencies
- Tailscale deployment
- Mattermost access policy
- Backup strategy (separate)

## References / Sources
- Architecture: `architecture/home-network-openclaw-placement.md`
- Discussion: Mattermost #executive, 2026-02-23
