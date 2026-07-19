# HEARTBEAT.md

# This file defines explicit periodic tasks.
# If empty (or comments only), no heartbeat actions occur.

# The agent must:
# - Execute only tasks listed here
# - Not infer new tasks
# - Not modify this file without explicit instruction
# - Reply HEARTBEAT_OK if no listed task requires action

# Add tasks below when you want periodic checks.

## Task: Governance Sync

Sync the local governance repo clone to stay current with upstream changes.

1. Run: `git -C {GOVERNANCE_ROOT}/smoking-tigers-governance pull --ff-only`
2. If new commits pulled — log to daily memory:
   `📥 Governance synced: [N] new commits — [date]`
3. If already up to date — no log needed
4. If sync fails (conflict/error) — log warning to daily memory and skip

## Task: Intake Directory Processing

Note: `{INTAKE_DIR}` is machine-local. Each operator sets their own path.
Default convention: `~/SmokingTigers/local-knowledge/staging/intake/`
Configure in your local openclaw workspace HEARTBEAT.md.

1. List all .md files in `{INTAKE_DIR}/`
   Do not include files inside the completed/ subfolder.

2. If no .md files found — reply "HEARTBEAT_OK — intake empty"

3. If .md files found — take the first file alphabetically:
   a. Read the full file content
   b. Spawn knowledge-ops with the file path and content as the task
   c. Wait for knowledge-ops to complete
   d. On success — run: mv [filepath] {INTAKE_DIR}/completed/
   e. Append to {LOCAL_OPENCLAW_WORKSPACE}/agents/update-log.md:
      ✅ [filename] complete — [one line summary]
   f. Reply with: "Processed: [filename] — [one line summary]"

4. Process one file per heartbeat cycle only.

If no files exist — reply HEARTBEAT_OK
