# PRD: Gemini Integration & Multi-Tier AI Ecosystem
**Project Name:** TigerClaw  
**Subproject/Workspace:** Discovery / Gemini Integration  
**Author:** Ed Hwang & Collaboration Team  
**Status:** Draft / Active  

---

## 1. Objective & Vision
TigerClaw establishes an integrated, multi-tier AI ecosystem designed to execute tasks autonomously and silently. By pairing high-reasoning orchestrators (Google Gemini) with local macOS automation, n8n workflows, and local LLM fallbacks, TigerClaw minimizes token costs while keeping operations fast, local-first, and secure.

---

## 2. Architectural Tiers

### Tier 1: On-Device Tier (Developer Workstation)
*   **Primary Engine:** OpenCode / VS Code Copilot powered by Google Gemini (Free Tier via Google AI Studio).
*   **Local Fallback:** Automatic or configured transition to on-device local models (e.g., via Ollama/LM Studio) when Gemini hits RPM/TPM rate limits or offline conditions.
*   **Data Security:** Strictly enforce strict privacy boundaries using `.gitignore`, `.opencodeignore`, and secrets management policies defined in OpenProject tasks.

### Tier 2: On-Premises Tier (Home Server & Mac Network)
*   **24/7 Workforce Engine:** OpenClaw running on dedicated macOS hardware acting as the background orchestration server.
*   **Escalation Pipeline (The 5-Step Escalation Contract):**
    1.  **Native macOS Level:** Execute system actions via AppleScript, macOS Shortcuts, CLI, or Automator actions.
    2.  **Automation Middleware Level:** Execute complex integrations via n8n (or Zapier/webhooks).
    3.  **Local Sub-Agent Level:** Use small, on-device models for low-reasoning background tasks.
    4.  **Gemini Cloud Orchestrator Level:** Escalate to Gemini Pro/Flash when high-reasoning, architectural strategy, or multi-step synthesis is required.
    5.  **Human-in-the-Loop (Premise Owner):** Final escalation point if all automation tiers fail or require manual validation.
*   **Shared Script Library:** A non-duplicative, global script repository made available to all local projects on the host device.

### Tier 3: On-Network Tier (Shared Co-Working)
*   **Permissions & Profiles:** Shared rules, profile specs, and device authorization contracts across local network machines to allow distributed agent collaboration.

---

## 3. Governance & Spec-Driven Development
*   **Spec-Coding with OpenProject:** Every agent task and permission boundary must be pre-authorized via OpenProject tasks before execution.
*   **Silent Background Execution:** Agents should run silently without interrupting the user unless a task escalates to Level 5 (Human Owner).