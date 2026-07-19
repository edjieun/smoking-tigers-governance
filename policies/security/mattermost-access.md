# Policy — Secure Mattermost Access for Executive Council (Mobile-Friendly, Global Team)
Status: Draft v1.0
Owner: Ed (Steward)
Applies To: Executive Council, designated operators, OpenClaw-related collaboration channels
Last Updated: 2026-02-23

## Purpose
Enable a small, trusted executive council to use self-hosted Mattermost (including the mobile app) in a way that is:
\- simple enough for daily use
\- secure enough for governance/ops coordination
\- practical for a global team
\- compatible with a "security gap" approach around OpenClaw and related systems

This policy is designed to reduce friction without exposing the broader system unnecessarily.

## Core Principles
1. **Least privilege by default**
2. **Private access path first (Tailscale / private network)**
3. **Mobile-friendly setup with controlled onboarding**
4. **Separation of communication access from infrastructure admin access**
5. **Human trust \+ technical controls**
6. **Small group, high discipline**

## Policy Statement
Executive council members may access the self-hosted Mattermost instance using approved devices and approved onboarding steps, provided they are granted role-based access and follow the security requirements in this policy.

Mattermost access for executive council does **not** automatically grant:
\- server shell access
\- OpenClaw admin access
\- private repo access
\- credentials to external systems
\- infrastructure control rights

## Intended Use
Mattermost is the primary secure communication layer for:
\- executive coordination
\- governance discussions
\- meeting prep/follow-up
\- operational decision staging
\- communication with OpenClaw-facing operators/agents (where configured)

Mattermost is **not** the canonical record for approved governance decisions.
Approved decisions must be promoted to the governance repo / decision log per policy.

## Access Model (Recommended)
Use a tiered access model.

### Tier 1 — Executive Council (Core)
\- Access to executive channels
\- Mobile app access allowed
\- Can participate in governance/ops discussions
\- No infrastructure admin rights by default

### Tier 2 — Operators (Trusted)
\- Access to operational channels relevant to role
\- May assist with formatting, summaries, coordination
\- May interface with OpenClaw workflows
\- No server admin rights unless separately assigned

### Tier 3 — SysOps / Platform Admin (Restricted)
\- Platform configuration/admin access
\- Security and user provisioning responsibilities
\- Logs/maintenance access as needed
\- Smallest possible group

### Tier 4 — Guests / Temporary Participants (Optional, limited)
\- Time-bound access to specific channels
\- No executive channel visibility
\- No admin access

## Network Access Standard (Security Gap)
### Preferred Model
Mattermost should be reachable through a private access layer (e.g., Tailscale) rather than broad public exposure whenever practical.

This supports:
\- reduced attack surface
\- easier access control for a small trusted team
\- mobile access through approved VPN/private-network client setup

### If Public Exposure Is Used (Exception)
If Mattermost must be internet-accessible:
\- require TLS/HTTPS
\- require strong auth
\- restrict admin endpoints where possible
\- monitor logs
\- document the exception and why it exists

## Authentication and Account Security
### Required
\- unique individual accounts (no shared logins)
\- strong passwords
\- MFA enabled if supported in current deployment
\- immediate removal/disable when access is no longer needed
\- role-based permissions (no blanket admin)

### Prohibited
\- shared executive account
\- reusing one credential across multiple people
\- sending passwords in chat/email without a secure handoff process
\- granting admin to "make setup easier"

## Approved Device Use (Mobile \+ Desktop)
Executive council members may use:
\- Mattermost mobile app (iOS/Android)
\- desktop app or browser (optional)

Requirements:
\- device has screen lock enabled
\- OS updates reasonably current
\- user understands logout/report process if device is lost
\- no credential sharing with assistants/family/etc.

For mobile simplicity, onboarding should be a guided process with a short checklist.

## Executive Onboarding Standard (Recommended)
Use a repeatable onboarding flow for each exec.

### Step 1 — Identity Confirmation
Confirm:
\- legal/preferred name
\- email address for account
\- role (Executive Council / Operator / etc.)
\- channels needed

### Step 2 — Access Approval
SysOps or Steward approves:
\- account creation
\- role
\- channel membership
\- network access requirements (e.g., Tailscale)

### Step 3 — Private Network Setup (if used)
User installs and signs into approved private network tool (e.g., Tailscale).
Verify they can reach the Mattermost instance before app setup.

### Step 4 — Mattermost App Setup
Provide:
\- server URL (private or approved public URL)
\- login steps
\- password/MFA setup instructions
\- basic channel usage expectations

### Step 5 — Security Orientation (5 minutes minimum)
Cover:
\- what can/can’t be shared
\- no forwarding screenshots of sensitive channels
\- reporting suspicious login/device loss
\- where decisions become official (not in chat alone)

### Step 6 — Test Message and Confirmation
User sends a message in onboarding/test channel and confirms mobile notifications work.

## Channel Architecture (Recommended)
Keep channels intentionally scoped.

### Core Channels (example set)
\- `exec-council` — executive coordination and decisions-in-progress
\- `exec-meetings` — agendas, prep, recaps, action checks
\- `sysops` — platform operations and incidents
\- `governance-ops` — policy drafting and process coordination
\- `ai-ops` or `openclaw-ops` — OpenClaw workflow updates (operators/sysops)

### Optional
\- `announcements-exec` (low-noise updates)
\- `incident-private` (security/availability issues)
\- project-specific private channels as needed

Avoid using one giant channel for all topics.

## Data Handling Rules
### Suitable for Mattermost
\- coordination messages
\- agendas and meeting prep
\- action check-ins
\- draft discussions
\- links to docs/issues
\- operational status updates

### Use Caution / Restrict
\- sensitive legal/financial details
\- personally identifying information
\- credentials/secrets
\- private security architecture specifics
\- unredacted contract terms

### Never Post in Chat
\- passwords
\- API keys
\- private tokens
\- recovery codes
\- raw secrets from `.env` files

Use a secure secret-sharing process/tool instead.

## OpenClaw Interaction Boundary
Mattermost may be used to coordinate work involving OpenClaw, but this policy does not assume Mattermost bots/agents have unrestricted rights.

OpenClaw-connected automation (if enabled) must be explicitly defined:
\- what channels it can read
\- what channels it can post to
\- whether it can summarize
\- whether it can trigger downstream actions
\- what audit logs are kept

No agent should silently perform high-risk actions from a chat message without human approval.

## Notifications and Global Team Norms
Because the executive council is global:
\- use timezone-aware scheduling language
\- post dates explicitly (e.g., "Tue, Feb 24, 2026")
\- avoid urgent pings unless truly urgent
\- use threads when possible to reduce noise
\- reserve @channel/@all for operationally important messages

Recommended:
\- define "response expectations" by channel (e.g., same day vs 24–48h)

## Offboarding / Access Changes (Required)
When someone changes role or leaves:
\- remove from executive channels immediately (same day preferred)
\- disable account if no longer needed
\- rotate any shared secrets they may have known (if applicable)
\- review linked systems they had access to

Offboarding should be logged by SysOps / Steward.

## Incident Response (Minimum Standard)
If suspicious activity is detected (unexpected login, lost phone, credential exposure):
1. Disable or suspend affected account
2. Notify SysOps \+ Steward
3. Rotate impacted credentials if relevant
4. Review logs and affected channels
5. Document incident and remediation steps
6. Re-enable only after confirmation

## Logging and Audit (Practical)
SysOps should maintain a simple access log record (manual or automated) for:
\- account created
\- role assigned
\- admin granted/removed
\- account disabled
\- major channel permission changes

This can live in a restricted ops doc or repo.

## Cost Awareness (Operational Note)
Mattermost deployment costs may include:
\- server hosting / compute
\- storage (files/backups)
\- domain/DNS
\- TLS/cert setup (if applicable)
\- admin time (hidden but real)
\- optional integrations (future)

Track these separately from this access policy in a cost-center record.

## Failure Modes to Avoid
\- sharing one login across execs
\- public internet exposure with weak auth
\- giving admin rights to all execs
\- using Mattermost as the only decision record
\- storing secrets in chat
\- no offboarding process
\- unclear difference between "chat access" and "system authority"

## Review Cadence
Review this policy after:
\- onboarding first 3 executive council members
\- first mobile access support issues
\- any security incident
\- changes to network approach (Tailscale/private vs public)
\- enabling any OpenClaw/Mattermost automation
