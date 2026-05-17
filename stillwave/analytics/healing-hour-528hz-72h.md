# Healing Hour 528 Hz — 72h-fact review

**Video:** `528 Hz Japanese Zen Music Marathon | 1 Hour Healing Uninterrupted Vol. 1`
**Video ID:** [`-1RE1P98_u8`](https://www.youtube.com/watch?v=-1RE1P98_u8)
**Series:** HEALING HOUR (Vol. 1, first entry)
**Published:** 2026-05-14, 18:00 IDT (15:00 UTC)
**Snapshot taken:** 2026-05-17, 11:24 IDT (08:24 UTC) — actual T+65h (not full 72h; the 48h checkpoint at May 16 was missed, so this is the first formal review)

---

## Headline numbers

| Metric | Value | Notes |
|--------|-------|-------|
| Views (T+65h) | **49** | |
| Likes | 1 | |
| Like-rate | 2.04% | small sample |
| Comments (audience) | **0** | only the own pinned comment exists |
| Comments (own pinned) | 1 | posted May 15, 18:42 UTC (24h after publish) |
| Current VPH | 0.2–0.6 | down from 3.75 overnight peak |
| Days since publish | 2.7 | |

## Hourly view trajectory (VidIQ data)

| Hours since publish | Views | VPH | Note |
|---------------------|-------|-----|------|
| 0.4 | 2 | 5.4 | publish moment |
| 1.5 | 2 | 0 | flat |
| 2.6 | 4 | 1.7 | |
| 6.7 | 10 | 1.5 | |
| **11.8** | **29** | **3.8** | overnight algorithmic spike (Israel night = US/EU daytime) |
| 18.9 | 30 | 0.1 | spike ended |
| 23.0 | 31 | 0.2 | |
| 36.9 | 42 | 0.8 | |
| 60.1 | 46 | 0.2 | first like appears |
| 65.4 | 49 | 0.6 | latest data point |

## Comparison vs Tokyo Rain Vol. 1 (Power Hour)

| Metric | Healing Hour @ 65h | Tokyo Rain @ 72h | Δ |
|--------|--------------------|-------------------|---|
| Views | 49 | 131 | **−63%** |
| Likes | 1 | 2 | −50% |
| Audience comments | 0 | 2 | −100% |
| Pace (views/day) | ~18 | ~44 | **−59%** |

**Healing Hour is performing at roughly 1/3 the velocity of Power Hour** despite being a similar 1-hour static-image video with the same release time slot, channel, and overlay-brand formula.

## Hypotheses for under-performance

1. **Title / SEO did not get the VidIQ-validated rename before publish.** `production-status.md` had a ⚠️ flag: "rename in YouTube Studio before publish". Need to verify the title actually went out as `528 Hz Japanese Zen Music Marathon | 1 Hour Healing Uninterrupted Vol. 1` (VidIQ 91/100) and not the original draft.
2. **No `scripts/` file = no Description / Tags / Pinned-comment pre-write.** The video was uploaded with whatever was typed directly into YouTube Studio. Likely missing the 22-tag base set, lower-quality description, weaker pinned CTA.
3. **No 9:16 / Short companion** to drive cross-format discovery (Tokyo Rain didn't have one either at this stage — not a clean diff).
4. **Wellness audience is harder to reach cold on a young channel** (~50 subs). Wellness keywords are dominated by 100k+ sub channels; algorithm doesn't surface tiny channels into that pool easily.
5. **528 Hz claim invites skepticism** — viewers who click expecting "real" 528 Hz may bounce if the music doesn't feel medically credible. Retention data (not in this snapshot) needed to confirm.
6. **Pinned comment delay (24h after publish)** = first 24h had zero CTA pin to anchor the comment section.

## Recommendations

### Immediate (today, before 7d review) — ⚠️ LIVE METADATA AUDIT CONFIRMED 2 DEFECTS

Pulled live metadata via YouTube Data API on 2026-05-17 (T+65h):

**Defect 1: Title is wrong.** The VidIQ-validated draft was `528 Hz Japanese Zen Music Marathon | 1 Hour Healing Uninterrupted Vol. 1` (91/100). What actually went live is `528 Hz Japanese Zen Healing Marathon | 1 Hour Uninterrupted Vol. 1` — the word **"Music" is missing** and "Healing" is in a different position. "japanese zen music" is a high-demand search phrase; losing it is significant SEO damage. Live VidIQ score is likely ~75–80, not 91.

**Defect 2: Description violates the `every week` locked rule.** Para 1 says "...every week" ✅ but Para 2 says "New Nervous System Reset and Power Hour sessions **every Tuesday and Friday**" — a hard rule violation per `stillwave/CLAUDE.md` Description rules section. Also mixes Healing + Power Hour CTAs in a healing-themed video, fragmenting subscriber intent.

**Required fixes (do today, before 7d window closes):**

```
Title:       528 Hz Japanese Zen Music Marathon | 1 Hour Healing Uninterrupted Vol. 1
Description: Replace "every Tuesday and Friday" → "every week"
             Remove "Power Hour" mention from the bell-CTA paragraph
```

Tags (23, 448 chars) and pinned comment audit-clean. No changes needed there.

### Hold decisions until 7d review (May 21, 18:00 IDT)

- **Do not produce HEALING HOUR Vol. 2 yet.** Until 7d shows retention + ranking signals, we don't know if this hook can support a series.
- Tokyo Snowfall Vol. 2 (POWER HOUR) goes out today (May 17, 18:00 IDT) on its own merit — leans into the proven hook.

### Strategic decision points at 7d

- **If views ≥ 120 and at least 2 audience comments by May 21** → Healing Hour viable, queue Vol. 2 for late May.
- **If views < 100 and still 0 audience comments** → kill HEALING HOUR brand, redirect slot to second POWER HOUR or a new experimental hook (Sleep Music, Rain ASMR, Lo-fi).
- **If 100–120 views and 1 comment** → ambiguous, run one more cheap variant (Vol. 2 with different title hook like "Vagus Nerve Reset") and decide at 14d.

## Open data gaps

- No average view duration / retention curve (vidiq_video_stats doesn't expose it; would need YouTube Analytics API directly).
- No traffic source breakdown (search vs browse vs suggested).
- No CTR / impression count (also requires YouTube Analytics API).

These should be pulled at the 7d checkpoint via YouTube Studio Analytics by the channel owner.
