# GCP Environment Options for Smoking Tigers

> Draft for Ed's review. Purpose: email Esteban Montero with your choice so he can provision.

---

## What Needs to Run

| Service | Current Home | Notes |
|---------|-------------|-------|
| Mattermost | Mac Mini M4 (local) | Postgres, file storage, ~5 bots |
| Cal.com | Mac Mini M4 (local, Docker) | Postgres, Redis, Next.js app |

These are self-hosted, containerized (Docker Compose). They need persistent disk, always-on uptime, and outbound internet. No heavy GPU or ML workloads.

---

## Recommended Options

### Option 1 — e2-standard-2 (Recommended for now)
- **Machine:** e2-standard-2 (2 vCPU, 8 GB RAM)
- **Disk:** 50 GB SSD persistent disk
- **Region:** us-west1 (Oregon) — lowest latency for Santa Clara
- **Estimated cost:** ~$50–60/month
- **Fits:** Both services comfortably, with headroom for agents/bots
- **Good for:** Current team size (5–15 users), early operational phase

### Option 2 — e2-standard-4 (Growth headroom)
- **Machine:** e2-standard-4 (4 vCPU, 16 GB RAM)
- **Disk:** 100 GB SSD persistent disk
- **Region:** us-west1 (Oregon)
- **Estimated cost:** ~$110–130/month
- **Fits:** Full team onboarding, heavier Mattermost use, future services
- **Good for:** If you expect rapid user growth or want to run additional services (e.g., n8n, Fathom alternative, OpenClaw gateway)

---

## Recommendation

**Start with e2-standard-2 in us-west1.** It handles both services at current scale. Upgrade to e2-standard-4 when Mattermost user count exceeds ~20 active users or if you add more services.

---

## What to Tell Esteban

> "I'd like to run Mattermost and Cal.com on GCP. Recommend starting with **e2-standard-2, us-west1 (Oregon), 50GB SSD**. Can you provision that environment and give me access so we can deploy? Let me know if you prefer a different setup given what Q1 runs."

---

*Draft by Scout — 2026-03-09. Pending Ed review and send.*
