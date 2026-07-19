# Mac Mini Phase 1 Setup — Inference Server

**Goal:** Bring Mac Mini back online as a remote inference server over Tailscale.  
No harness. No OpenClaw. No autonomous tasks yet. Just proven, stable, local inference.

**Reference:** ADR-0010 · Phase 1

---

## Prerequisites

**First: recover credentials from the Mac Mini before doing anything else.**  
Follow `scripts/recover-credentials.md` completely, then come back here.

- [ ] Credentials recovered and saved to `~/.ste-secrets/.env` (see `recover-credentials.md`)
- [ ] `.env.enc` committed to private GitHub secrets repo
- [ ] Tailscale running on Mac Mini (confirm with `tailscale status` — if it was already set up, it should reconnect automatically on power-on)
- [ ] LM Studio installed (if missing, download at https://lmstudio.ai)
- [ ] Qwen3.5 9B already downloaded in LM Studio (check `~/Library/Application Support/LM Studio/models/` — if it's there, skip re-downloading)

---

## Step 1 — Fix the system prompt in LM Studio

This is the root cause of the token bleeding. Without a system prompt, local models cannot handle tool calls, and OpenClaw falls back to cloud.

**Where the system prompt lives in LM Studio:**

LM Studio stores per-model presets. The system prompt is set in the **Chat** tab, not the model settings:

1. Open LM Studio on the Mac Mini
2. Click **Chat** in the left sidebar
3. Load `Qwen3.5 9B` using the model picker at the top
4. Click the **⚙ (gear)** icon next to the model name → **Edit Preset** (or "My Presets")
5. Find the **System Prompt** field
6. Paste this system prompt:

```
You are a helpful AI assistant with tool-use capability. When a task requires a tool, call it directly — do not ask permission. Follow all instructions precisely and completely. When writing structured output (JSON, markdown templates, file contents), match the exact format specified. Never skip required fields or sections. If you cannot complete a step, say so explicitly rather than skipping it silently.
```

7. **Save the preset** — name it `ste-default`
8. Make sure this preset is selected (shown in the chat header) before starting the server

**Verify it worked:**  
In the LM Studio chat, send: `List the tools you have available.`  
If it responds with a tool list (or says it has no tools but understands tool syntax), the system prompt is working.  
If it just says "I'm a helpful assistant" with no tool awareness, the preset is not loaded — check step 8.

---

## Step 2 — Enable LM Studio server mode

1. In LM Studio, go to **Local Server** (left sidebar, server icon)
2. Load `Qwen3.5 9B` into the server
3. Set port to `1234` (default)
4. Enable **CORS** (required for cross-machine API calls)
5. Click **Start Server**
6. Confirm it shows: `Server running on http://0.0.0.0:1234`

---

## Step 3 — Confirm reachability over Tailscale

On the Mac Mini, find the Tailscale IP:
```bash
tailscale ip -4
# e.g. 100.x.x.x
```

Update your `.env` on the laptop:
```
LMSTUDIO_API_BASE=http://100.104.149.107/v1
```

From your **M4 laptop**, test the connection:
```bash
source ~/.ste-secrets/.env
curl "$LMSTUDIO_API_BASE/models" | python3 -m json.tool
```

You should see `Qwen3.5 9B` listed in the models response.

---

## Step 4 — Test inference from laptop

Send a real completion request from the laptop to confirm the full path works.

**⚠️ qwen3.5-9b is a reasoning model** — it emits hidden `reasoning_content` tokens *before* the answer (~300 even for trivial prompts). A small `max_tokens` gets entirely consumed by reasoning, returning `finish_reason: "length"` with **empty content**. That's a token-budget failure, not a server failure. Always give it ≥2000. (`/no_think` does not disable reasoning in LM Studio 0.4.x.)

```bash
curl "$LMSTUDIO_API_BASE/chat/completions" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen/qwen3.5-9b",
    "messages": [{"role": "user", "content": "Reply with exactly: INFERENCE_OK"}],
    "max_tokens": 2000
  }' | python3 -m json.tool
```

(Model id is `qwen/qwen3.5-9b` — with the `qwen/` prefix — as reported by `$LMSTUDIO_API_BASE/models`.)

Expected: `"content"` contains `INFERENCE_OK` and `finish_reason` is `"stop"`. If so, Phase 1 is complete.

**Rule for all consumers of this endpoint (OpenCode, OpenClaw Phase 2):** set `max_tokens` ≥ 2000. An empty response with `finish_reason: "length"` means a starved token budget. For lightweight/tool-call traffic where reasoning overhead hurts, `google/gemma-3-4b` (non-reasoning) is also served.

---

## Step 5 — Configure OpenCode on laptop to use Mac Mini

In your OpenCode config (or VS Code settings), set the API base to the Mac Mini:

```json
{
  "opencode.apiBase": "${LMSTUDIO_API_BASE}",
  "opencode.model": "qwen3.5-9b"
}
```

During active coding sessions on the laptop, OpenCode will now send inference requests to the Mac Mini — freeing your laptop's RAM for video calls and other apps.

---

## Verification checklist

- [ ] LM Studio system prompt configured on Qwen3.5 9B
- [ ] LM Studio server running on port 1234
- [ ] `curl` test from laptop returns `INFERENCE_OK`
- [ ] Laptop RAM is noticeably freed when Mac Mini is handling inference
- [ ] No OpenRouter spend observed (check OpenRouter dashboard)
- [ ] Tailscale shows both machines as connected (`tailscale status`)

---

## If something breaks

| Symptom | Likely cause | Fix |
|---|---|---|
| Empty `content` + `finish_reason: "length"` | `max_tokens` too small — all budget eaten by reasoning tokens | Set `max_tokens` ≥ 2000 (see Step 4) |
| Connection refused from laptop | LM Studio server not started, wrong IP, or "Serve on Local Network" toggle off (binds localhost-only after restart) | Check `tailscale ip` on Mac Mini; verify server is running; enable the toggle in Local Server tab |
| Model not found error | Model name mismatch in API call | Use exact id from `/v1/models` (e.g. `qwen/qwen3.5-9b`, with prefix) |
| Tool calls still failing | System prompt not saved correctly | Re-open model config in LM Studio, re-save |
| Slow responses | Qwen3.5 9B using swap memory | Check Activity Monitor → Memory; close other apps on Mac Mini |

---

## Next: Phase 2

Once Phase 1 is stable for 48 hours with no issues, proceed to Phase 2:
- Re-enable OpenClaw on the Mac Mini
- Configure OpenClaw with the hard local block (no OpenRouter)
- Set up Mattermost `#transcripts` listener
- Write the transcript processing spec in OpenProjects

See `ADR-0010` for the full Phase 2 plan.
