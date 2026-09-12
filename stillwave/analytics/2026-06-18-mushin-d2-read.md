# StillWave — 2026-06-18 D2 read (MUSHIN long + Shorts) + Pomodoro 50/10 audit

> Pulled via VidIQ `get_videos_by_ids` + `video_stats` (hourly) + `channel_stats`. Snapshot taken Jun 18 ~18:00 MSK.

## Channel snapshot

| Date | Subs | Total views | Videos |
|------|------|-------------|--------|
| 2026-06-11 | 49 | 5,756 | 43 |
| 2026-06-12 | 50 | 5,775 | 43 |
| 2026-06-13 | 50 | 5,784 | 43 |
| 2026-06-14 | 50 | 5,791 | 43 |
| 2026-06-15 | 50 | 5,794 | 43 |
| 2026-06-16 | 50 | 5,796 | 43 |
| 2026-06-17 | 50 | 5,802 | 45 |
| 2026-06-18 (est) | 50 | ~5,820 | 45 |

- **Subs:** flat at **50** for 7 days. MUSHIN brought zero new subs in first 48h.
- **Daily views:** baseline ~5-10 (channel drift), no MUSHIN spike beyond it.

---

## MUSHIN long-form (`CamT9sohYQM`) — D2 read

**Published:** Tue Jun 16, 15:00 UTC (18:00 MSK). Age at snapshot: **~51h**.

| Metric | Value |
|--------|-------|
| Views | **16** |
| Likes | **0** ❌ |
| Comments | 1 |
| Like-rate | 0% |
| Topic Categories | ✅ **Music** + Electronic music + Music of Asia |
| Duration | 2H 01m 13s |

**Hourly trajectory (Jun 16 publish → Jun 17 17:00):**

| Hours post-publish | Views | VPH (avg of window) |
|---|---|---|
| 12h (02:45) | 7 | 0.6 |
| 14h (04:40) | 8 | 0.5 |
| 21h (12:32) | 10 | 0.3 |
| 24h (15:35) | **15** | **4.8** ← brief D1 algo bump |
| 25h (16:32) | 14 | flat |
| 51h (now) | **16** | ~0 |

**Read:**
- ✅ **Topic fix WORKED** — landed cleanly in `Music` cluster (not Lifestyle like 50/10). Title front-loading `Japanese Zen Music` did its job.
- ❌ **Discovery is dead.** D1 = ~15, D2 = 16. At this trajectory D7 ≈ 30-40 — far below the 200-view success threshold and even below Kyoto's D2 = 137.
- ❌ **0 likes** at D2. Engagement signal absent. 1 comment is from a friendly viewer, not an algorithm-meaningful number.
- 🔍 **Hypothesis:** The Kanji-Concept template fix (photoreal + monk + ENSO + Hikari description) was the right move, but the channel itself has no authority to feed the algorithm enough early signal. Even a clean Topic + clean SEO + correct format doesn't break out below ~100 subs.

---

## MUSHIN Shorts (`Rrwb_BBDMuM`) — D1 read

**Published:** Wed Jun 17, 15:00 UTC. Age: **~27h**.

| Metric | Value |
|--------|-------|
| Views | **7** |
| Likes | **0** ❌ |
| Comments | 1 |
| Topic | ✅ Music |
| Duration | 46s |

**Read:**
- Same anaemic pattern as the long-form. A healthy Shorts on a small channel usually does 50-200 in first 24h; ours did 7.
- The D1-drop strategy (vs the Pomodoro D4 delayed strategy) did NOT save the Shorts — both formats are starving for distribution.
- Comment from the same friendly viewer (likely Konstantin Tsereteli).

---

## Pomodoro 50/10 (`V4xwN0RRdpw`) — D8 read

| Metric | Value |
|--------|-------|
| Views | **24** (plateaued from D2 = 22 → D8 = 24) |
| Likes | 2 (**like-rate 8.3% — channel record**) |
| Comments | 1 |
| Topic | ✅ **Music + Electronic music** (no longer Lifestyle 🎯) |

**Update:** Topic Categories now show **Music + Electronic music** — the earlier `Lifestyle (sociology)` is GONE. Either YouTube re-classified it (Topic can shift over time as more data comes in) OR our previous VidIQ snapshot was reading stale metadata. **Title is still `Pomodoro Study Timer 50/10 — 2H Deep Focus Music...`** (matches our locked spec — no rename needed in Studio after all).

**Implication:** the long-form 50/10 was NOT classified wrong at the cluster level. Its 24-view plateau is the same channel-authority bottleneck affecting every recent upload, not a topic mis-classification.

---

## Pomodoro 50/10 Shorts (`t_valshIMi4`) — D7 read

| Metric | Value |
|--------|-------|
| Views | **11** (plateaued) |
| Likes | 0 |
| Comments | 1 |
| Topic | ❌ **`Lifestyle (sociology)`** — wrong cluster |
| Description | ❌ Still the AI-boilerplate Lightroom/Premiere text |

**Action items still open:**
- 🔧 Fix Shorts description in Studio — replace AI boilerplate with proper Pomodoro 50/10 Shorts copy from script §SHORTS PACKAGE
- 🔧 After description fix, Topic may re-categorize within 48-72h to Music

---

## 🎯 Verdict — D2 MUSHIN read

**Format works mechanically, channel can't lift it.** Three signals converge:

1. **Topic = Music** — Kanji-Concept template + title rule fixed the cluster problem.
2. **No engagement** — 0 likes at D2 on long-form, 0 on Shorts.
3. **No discovery push** — D2 ≈ 16 views, same trajectory as Kyoto D2 of 137 would have been... but at 1/9 the rate.

The bet at D7 (Tue Jun 23): does the slow climb hit 100+ via long-tail meditation traffic? Even small daily drips of 3-5 views could land us at ~50-80 by D7. That's still under the success benchmark but it would prove the SEO is working without algorithmic push.

**Go/no-go on SATORI:** the user has decided to ship SATORI in parallel (don't wait for D7). Rationale: SATORI is built on the same template — if MUSHIN doesn't catch, SATORI's separate visual hook (mountain dawn vs temple interior) gives the format a second clean shot. Two videos in series = more surface area for the algorithm to find ONE that resonates.

---

## Production action items (next 7 days)

| When | What | Why |
|------|------|-----|
| **Today (Jun 18)** | Begin SATORI production — Suno album generation | Parallel ship strategy, no wait for MUSHIN D7 |
| Today | Fix Pomodoro 50/10 Shorts description in Studio | Open issue, easy fix |
| Jun 20 (Sat) | MUSHIN D4 read — channel + per-video | Watch for any push |
| Jun 23 (Tue) | MUSHIN D7 read | Pre-SATORI publish: lock or unlock the template |
| Jun 23-25 | SATORI publish window | After Suno album + Flow loop + thumb composite |
