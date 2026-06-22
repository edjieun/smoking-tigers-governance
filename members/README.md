# Members Registry

This directory contains enrollment records for all machines participating in the
Smoking Tigers governance model.

## What Is a Member

A **member machine** is a local OpenClaw instance that has adopted this
governance repo as its shared operating layer. Each member:

- clones and syncs this governance repo locally
- runs its agents within the authority boundaries defined here
- contributes improvements through the governed PR process

## Enrollment Process

To enroll a new machine:

1. Copy `template.yaml` to `<your-device-id>.yaml`
2. Fill out all fields
3. Submit a Pull Request to this repository
4. After approval and merge, follow `ONBOARDING-LOCAL-MACHINE.md` to complete setup

## Trust Levels

| Level | Who | Access |
|-------|-----|--------|
| `owner` | Founding steward (Ed) | Full governance authority, approves all PRs |
| `contributor` | Executive council members | May propose policy changes, run full agent suite |
| `observer` | Authorized community operators | Read governance, run local agents within constraints |

## Active Members

| Device ID | Operator | Trust Level | Joined |
|-----------|----------|-------------|--------|
| eds-mac-mini | edjieun | owner | 2026-06-22 |
