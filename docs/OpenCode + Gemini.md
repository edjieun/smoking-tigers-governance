
## Part 1: Initial OpenCode Setup (Discovery Workspace)

To get OpenCode in your Discovery workspace running on Gemini (to replace the paid OpenRouter/Sonnet flow), follow these quick configuration steps:

1. **Grab your Free Key:** Get your Google AI Studio API key from [aistudio.google.com](https://aistudio.google.com/).
    
2. **Environment Export:** In your terminal inside the `Discovery` workspace directory, run:
    
    Bash
    
    ```
    export GEMINI_API_KEY="[your-key-from-aistudio.google.com]"
    ```
    
3. **Launch & Connect:** Run `opencode` in your terminal.
    
4. **Select Gemini Model:** Switch models in OpenCode to `gemini-2.5-pro` (for deep reasoning/planning) or `gemini-2.5-flash` (for fast edits and lightweight tasks).
    

_Note on Rate Limits:_ Because OpenCode agent loops send context back and forth rapidly, keep `gemini-2.5-flash` as your primary driver for routine code edits, and reserve `gemini-2.5-pro` for Plan mode.

## Part 2: TigerClaw Gemini Integration PRD — Grill Questions

Answer these questions so we can generate the formal **PRD** and the initial **Governance Repo Guides** (`OPENCODE_SETUP.md`, `ORCHESTRATION_RULES.md`, and `MACOS_LIBRARY_SPEC.md`).

### 1. On-Device Tier (OpenCode & Token Budgeting)

- **Fallback Behavior:** When OpenCode hits Gemini's Free Tier RPM/TPM limits during an active agent session, how should it handle it? Should it pause and retry with exponential backoff, automatically switch to a local/open-weight model, or notify you via terminal?
    
- **Code Privacy & Boundaries:** Since Google AI Studio's free tier permits data logging for model training, what repositories or file types in the `Discovery` workspace must be blacklisted/ignored by OpenCode `.gitignore` or `.opencodeignore` rules?
    

### 2. On-Premises Tier (Orchestration & macOS Native Tools)

- **Tool Invocation Contract:** How should Gemini decide whether to execute a task via a **macOS native script** (AppleScript/Shortcuts/Folder Actions) versus an **n8n workflow** or **OpenClaw skill**? Is there a strict rule (e.g., _UI/System level actions = macOS Shortcuts; API/Webhooks = n8n_)?
    
- **Shared Script Library Schema:** How do you want to structure the macOS Automation Library inside the repo? (e.g., a `/scripts` directory with standardized CLI wrappers so local agents can invoke them via bash commands?)
    
- **Human-in-the-Loop (HITL):** What destructive or high-privilege actions (e.g., deleting files, pushing commits, executing AppleScript with elevated privileges) require explicit human confirmation versus running silently in the background via OpenClaw?
    

### 3. On-Network Tier (Co-Working & Shared State)

- **Multi-Device State & Memory:** When on-device agents perform work across different machines on the same network, where should the shared state/context live? (e.g., committed directly to Git, synced via a local server/database, or managed via OpenClaw session state?)
    
- **Permission Profiles:** Do all devices on the network have equal privileges to execute scripts, or will there be role-based permissions (e.g., _Mac Studio = Host Server/Full Access; Laptop = Client/Restricted Execution_)?
    

Once you reply with your answers, I will draft the full **Gemini Integration PRD** and write the corresponding markdown guides ready to commit into your `governance` git repository.