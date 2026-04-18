# HEARTBEAT.md

# This file defines explicit periodic tasks.
# If empty (or comments only), no heartbeat actions occur.

# The agent must:
# - Execute only tasks listed here
# - Not infer new tasks
# - Not modify this file without explicit instruction
# - Reply HEARTBEAT_OK if no listed task requires action

# Add tasks below when you want periodic checks.

## Task: Intake Directory Processing

1. List all .md files in /Users/edlicious/Desktop/intake/
   Do not include files inside the completed/ subfolder.

2. If no .md files found — reply "HEARTBEAT_OK — intake empty"

3. If .md files found — take the first file alphabetically:
   a. Read the full file content
   b. Spawn knowledge-ops with the file path and content as the task
   c. Wait for knowledge-ops to complete
   d. On success — run: mv [filepath] /Users/edlicious/Desktop/intake/completed/
   e. Append to ~/.openclaw/workspace/agents/update-log.md:
      ✅ [filename] complete — [one line summary]
   f. Reply with: "Processed: [filename] — [one line summary]"

4. Process one file per heartbeat cycle only.

If no files exist — reply HEARTBEAT_OK
