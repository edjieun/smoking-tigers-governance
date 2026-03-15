# SOP — YouTube Reaction Video Production (James Min Channel)

**Status:** Draft v1.0
**Owner:** Ed (Steward) / James Min (Creator)
**Applies To:** James Min creator partnership — Content Agent Pipeline pilot
**Last Updated:** 2026-03-15

---

## Purpose

Define the end-to-end standard operating procedure for producing YouTube reaction videos for the Jimmy Ren channel. This SOP covers capture through publish, integrating the ST Content Agent Pipeline where agents replace or assist manual steps.

---

## Scope

- Reaction videos for: period dramas, rom-coms (Gilded Age, Crown, Bridgerton, Downton Abbey, Stranger Things)
- Source files: two MP4 streams (face cam + screen capture) per session
- Output: YouTube-published, copyright-compliant reaction video

---

## Roles

| Role | Responsibility |
|---|---|
| James Min (Creator) | Recording, creative direction, final approval |
| Ingest Agent | Receive + validate source files from shared Drive |
| Edit Agent | Cut, layer, apply copyright compliance techniques |
| Compliance Agent | Flag and resolve copyright exposure before publish |
| Copy Agent | Generate title, description, tags, thumbnail brief |
| Publish Agent | Upload (private), monitor copyright scan, publish |
| Ed / Scout | Pipeline oversight, issue escalation |

---

## Phase 1 — Capture

**Owner:** James Min

1. Record reaction session via OBS — two scenes simultaneously:
   - **Face cam scene:** DSLR + audio input (primary audio source)
   - **Screen capture scene:** 1080p browser stream (Netflix / Amazon / etc.)
2. Export two MP4 files per session:
   - `[show-title]-[ep]-facecam.mp4` — 5–9 GB typical
   - `[show-title]-[ep]-stream.mp4` — 3–7 GB typical
3. Upload both files to the shared Google Drive folder (ST Content Pipeline).
4. Notify Scout or drop in #james-min channel when upload is complete.

**File naming convention:**
```
gilded-age-s01e01-facecam.mp4
gilded-age-s01e01-stream.mp4
```

---

## Phase 2 — Ingest

**Owner:** Ingest Agent

1. Monitor shared Drive folder for new uploads.
2. On detection: validate both files present, not corrupted, naming convention correct.
3. Log ingest event to project tracker (title, episode, file sizes, timestamp).
4. Move files to local processing queue.
5. Notify Edit Agent: ready for processing.

**Acceptance criteria:**
- Both MP4s present
- Files > 1 GB (sanity check — corrupt/incomplete uploads fail this)
- Duration delta ≤ 2 minutes (face cam ≈ stream runtime)

---

## Phase 3 — Edit

**Owner:** Edit Agent (with James Min approval on layout)

### Layout Layers (3 modes — alternate for engagement)
1. **Full screen show** + face circle overlay (lower left or right)
2. **Full face** + show inset (picture-in-picture, corner)
3. **Blurred background** + face centered, show inset

### Editing Standards
- **Cut reaction segments only** — do not include dead air, setup, or unrelated commentary
- Target runtime: **8–20 minutes** finished video
- **Copyright compliance cuts:** no single continuous clip > 5 seconds; total source content ≤ 10 minutes across the video
- Apply: zoom (1.05–1.1x), mirror flip alternation, speed ramp (1.01–1.02x) on source clips to disrupt audio/video fingerprinting
- Maintain audio sync between face cam and screen throughout
- Export: 1080p MP4, H.264, AAC audio

### Branded Assets (stored in CapCut branded media cloud)
- Intro bumper
- Outro bumper
- Logo watermark (lower right, 30% opacity)
- Meme clip library (insert at reaction moments)

### Output
- Edited MP4 (export-ready)
- CapCut project file (archived)
- Edit log: clip timestamps, compliance actions taken

---

## Phase 4 — Copyright Compliance Review

**Owner:** Compliance Agent

1. Analyze edited video against known fingerprinting patterns.
2. Flag any segment exceeding 5 continuous seconds of source content.
3. Flag total source content if approaching 10-minute threshold.
4. If issues found: return to Edit Agent with specific timestamps and correction brief.
5. When clean: approve and pass to Copy Agent.

**Compliance techniques used:**
- Hard cuts under 5 seconds per clip
- Zoom + mirror flip per clip
- Speed ramp (minimal, imperceptible to viewer)
- Audio fade or cut at source clip boundaries

**Do not use:** pitch-shifting, heavy color grading, or content that changes the expressive meaning of the source (risks fair use defense).

---

## Phase 5 — Copy & Creative

**Owner:** Copy Agent

Generate per video:
- **Title:** engaging, search-optimized, ≤ 70 characters
  - Example: `My First Time Watching The Crown S4 | Full Reaction`
- **Description:** 2–3 paragraph summary of reaction highlights; Patreon link; channel subscribe CTA; episode/show tags
- **Tags:** 10–15 (show name, season, "reaction", "first time watching", character names, genre)
- **Thumbnail brief:** key reaction frame, bold text overlay, thumbnail A/B variant

**Thumbnail specs:**
- 1280 × 720 px, JPG
- Text: max 4 words, high contrast
- Two variants for A/B test (YouTube thumbnail test or TubeBuddy)

Deliver copy doc + thumbnail brief to James for approval before upload.

---

## Phase 6 — Publish

**Owner:** Publish Agent / James Min (approval)

1. James reviews and approves copy + thumbnail.
2. Upload video to YouTube as **Private**.
3. Set: title, description, tags, thumbnail, playlist (if applicable), end screen + cards.
4. Wait for YouTube copyright scan (typically 1–24 hours post-upload).
5. Monitor copyright status via YouTube Studio:
   - ✅ No claims → make **Public**
   - ⚠️ Content ID claim (monetization only) → accept or dispute per revenue impact
   - 🔴 Block claim → escalate to Compliance Agent; re-edit flagged segments; re-upload
6. Notify James when public; share link to #james-min or via DM.

---

## Phase 7 — Repurpose (Optional / Phase 2)

- Extract 3–5 reaction highlights (15–60 sec clips) for Patreon
- Short-form clips for YouTube Shorts or social (pending channel decision)
- Archive edited MP4 + raw files for 90 days, then delete raw to manage storage

---

## Quality Checklist (before publish)

- [ ] Audio sync confirmed throughout
- [ ] No continuous source clip > 5 seconds
- [ ] Total source content ≤ 10 minutes
- [ ] All 3 layout layers used at least once (or agreed exception)
- [ ] Intro and outro bumpers present
- [ ] Logo watermark present
- [ ] Title ≤ 70 characters, no clickbait flags
- [ ] Description includes Patreon link
- [ ] Thumbnail uploaded (non-auto-generated)
- [ ] Private upload confirmed before making public
- [ ] Copyright scan passed before publish

---

## Escalation

| Issue | Who to Contact |
|---|---|
| Source files corrupted or missing | James Min |
| YouTube block claim (not just Content ID) | Ed / Scout |
| Pipeline agent failure | Scout |
| Copyright compliance edge case | Ed — legal escalation if needed |

---

## Notes

- James's primary edit tool is CapCut — branded media assets are in CapCut's cloud, not local. Scout/agents cannot directly access CapCut; agents produce CapCut-compatible project specs or export-ready files.
- Dropbox is James's current personal storage. Shared Drive is the ST-managed collaboration layer.
- Patreon uploads are raw (pre-edit) — Patreon members get early, unedited access. This is intentional and not covered by this SOP.
