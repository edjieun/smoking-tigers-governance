# SOP — YouTube Content Performance Review (James Min Channel)

**Status:** Draft v1.0
**Owner:** Ed (Steward) / James Min (Creator)
**Applies To:** James Min creator partnership — Content Agent Pipeline pilot
**Last Updated:** 2026-03-15

---

## Purpose

Define the standard process for monitoring, analyzing, and acting on YouTube performance data for the Jimmy Ren channel. This SOP ensures the Content Agent Pipeline improves over time and that James's channel growth is tracked against measurable goals.

---

## Scope

- YouTube analytics (views, CTR, watch time, subscribers, revenue)
- Content performance per video and per series
- Pipeline effectiveness (time-to-publish, copyright incidents, edit quality)
- Audience growth and retention trends

---

## Roles

| Role | Responsibility |
|---|---|
| James Min (Creator) | YouTube Studio access; final call on strategy |
| Copy Agent | Pull analytics data; generate performance reports |
| Ed / Scout | Pipeline performance review; surface recommendations |

---

## Review Cadence

| Cadence | What |
|---|---|
| **Per video** (72h post-publish) | Initial performance check |
| **Weekly** | Active series + pipeline health |
| **Monthly** | Channel-level trends; strategic review |
| **Per pilot milestone** | Pipeline quality + business case assessment |

---

## Phase 1 — Per-Video Review (72 Hours Post-Publish)

**Trigger:** 72 hours after a video goes public.
**Owner:** Copy Agent → report to James + Scout

### Metrics to Pull

| Metric | Source | Target Threshold |
|---|---|---|
| Views (72h) | YouTube Studio | Baseline from prior 3 videos |
| Click-through rate (CTR) | YouTube Studio | ≥ 4% |
| Average view duration | YouTube Studio | ≥ 40% of video length |
| Impressions | YouTube Studio | Track for trend |
| Comments | YouTube Studio | Note top themes |
| Copyright claims | YouTube Studio | 0 block claims |

### Actions

- CTR < 4%: flag thumbnail for A/B swap (if YouTube Thumbnail Test available) or manual swap
- Avg view duration < 35%: flag edit pacing — review drop-off timestamps
- Block copyright claim: escalate immediately to Edit Agent + Compliance Agent for re-edit
- Unusual spike or viral signal: notify James same day

### Output

Short performance note logged to project tracker:
```
[Video Title] — 72h check
Views: X | CTR: X% | Avg duration: X% | Claims: none/flagged
Action: [none / thumbnail swap / re-edit / escalate]
```

---

## Phase 2 — Weekly Pipeline Health Review

**Cadence:** Every Monday (or end of active week)
**Owner:** Scout

### Pipeline Metrics

| Metric | What We're Tracking |
|---|---|
| Videos published (week) | Pipeline throughput |
| Avg time from ingest to publish | Pipeline speed |
| Copyright incidents | Compliance agent effectiveness |
| Edit revisions required | Edit agent quality |
| Backlog size | Remaining unprocessed assets |

### Target Pipeline SLAs

| Stage | Target Time |
|---|---|
| Ingest → Edit start | ≤ 24 hours |
| Edit complete | ≤ 48 hours |
| Compliance review | ≤ 4 hours |
| Copyright scan (YouTube) | ≤ 24 hours |
| Total: ingest → public | ≤ 5 days |

### Output

Weekly pipeline note to #james-min or project tracker:
```
Week of [date]
Published: X videos
Avg time to publish: X days
Copyright incidents: X (0 blocks)
Backlog: X videos remaining
Blockers: [none / list]
```

---

## Phase 3 — Monthly Channel Performance Review

**Cadence:** First week of each month
**Owner:** Copy Agent (data) + Scout (synthesis)

### Channel Metrics

| Metric | Source |
|---|---|
| Monthly views | YouTube Studio |
| Watch time (hours) | YouTube Studio |
| Subscriber growth (net) | YouTube Studio |
| Revenue (YouTube + Patreon) | YouTube Studio + Patreon dashboard |
| Top performing videos | YouTube Studio |
| Audience retention curves | YouTube Studio |
| Traffic sources (search vs. browse vs. external) | YouTube Studio |

### Analysis Questions

1. Which series is driving the most growth? (Gilded Age vs. Crown vs. other)
2. Are newer videos outperforming older ones? (Content quality trend)
3. What is the subscriber conversion rate? (Views → subscribers)
4. Is Patreon revenue tracking with YouTube growth?
5. Are there content gaps the audience is requesting? (Comments analysis)

### Strategic Outputs

- **Series prioritization recommendation** — which show to prioritize next based on audience signal
- **Format recommendation** — layout preferences, video length, thumbnail style
- **Backlog prioritization** — order remaining assets based on audience demand

Deliver as a brief written report to James via DM or shared doc (not a raw analytics dump).

---

## Phase 4 — Pilot Milestone Review

**Trigger:** After first 5 videos published through the ST Content Agent Pipeline
**Owner:** Ed + James Min joint review

### Assessment Areas

1. **Pipeline quality** — Does the edited output meet James's creative standards?
2. **Time savings** — How many hours has the pipeline saved James per video?
3. **Copyright safety** — Zero block claims in pilot?
4. **Audience response** — Performance vs. pre-pipeline baseline?
5. **Commercial case** — Is the pipeline worth ongoing investment?

### Outputs

- Written pilot assessment (stored in governance repo under `projects/james-min/`)
- Decision: continue, expand, or adjust pipeline
- If expand: scope commercial terms (RP allocation, revenue share, or retainer)

---

## Thumbnail A/B Testing Protocol

YouTube Studio offers native thumbnail testing (A/B) for eligible channels.

1. Upload two thumbnail variants on publish.
2. After 72 hours, check CTR by variant in YouTube Studio (if test is live).
3. Lock in winner; archive loser.
4. If not eligible: manually swap thumbnail at 72h if CTR < 4%, track result.

---

## Copyright Incident Log

Maintained in project tracker. Per incident, log:

| Field | Value |
|---|---|
| Video | Title / upload date |
| Claim type | Content ID (monetization) / Block |
| Claimant | Rights holder name |
| Segment flagged | Timestamp range |
| Resolution | Accepted / Disputed / Re-edited |
| Re-upload required | Yes / No |
| Outcome | Resolved / Pending |

Target: **zero block claims**. Monetization-only Content ID claims are acceptable if revenue share is not materially damaging.

---

## Escalation

| Issue | Action |
|---|---|
| Block claim (video taken down) | Immediate re-edit + re-upload; notify James |
| CTR persistently < 3% across 3+ videos | Strategic review — thumbnail strategy, title strategy |
| Subscriber loss (negative week) | Investigate top drop-off reasons; review recent content |
| Patreon-YouTube revenue misalignment | James-led review; pricing/tier assessment |

---

## Notes

- YouTube Studio access required for full metrics. James controls channel credentials. Scout pulls reports via copy agent where API access is available.
- Patreon analytics are James-controlled; share monthly numbers via DM or shared doc.
- Do not publish performance data publicly. Treat as creator business-sensitive.
