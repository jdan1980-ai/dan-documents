# StillWave — Production Status

Single source of truth for the StillWave pipeline. Update at every status change.

**Pipeline stages:** 📝 concept → 🎵 suno generated → 🎨 image generated → 🎬 video generated → 🎞️ assembled → ⏰ scheduled → 📤 published

---

## Published

See `published-videos.md` for the full table with metrics.

## In production / scheduled

> Pipeline для long-form статической картинки: 📝 script → 🎵 suno generated → 🎨 image generated → 🎬 ~~not needed~~ → 🎞️ ffmpeg encoded → ⏰ scheduled → 📤 published.

| Slug | Title | Length | 📝 | 🎵 | 🎨 | 🎞️ | ⏰ | 📤 |
|------|-------|--------|----|----|----|-----|-----|-----|
| `tokyo-apartment-rain-1h` | Power Hour Focus Music — Tokyo Apartment Rain | 1H 04min 48sec (24 tracks) | ✅ | ✅ | ✅ | ✅ | ✅ **scheduled May 10, 14:00** | ⏳ |

### Tokyo Apartment Rain — review schedule

After publish (May 10, 14:00):
- **48h review** — May 12, 14:00 → pull live API data, log views/likes/comments/CTR
- **7d review** — May 17, 14:00 → full retention analysis + comment mining + first lessons
- **30d review** — June 9, 14:00 → final perf snapshot, decide if pattern goes into Power Hour series template
| `bonsai-desk-night-2h` | Deep Focus Music — Bonsai Desk Late Night | 2H | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⚠️ predates locked Pomodoro look (hourglass + chroma timer + music-breathing). Reshape before producing. |
| ~~`lantern-glow-study-3h`~~ | ~~Quiet Hours Focus Music — Lantern Glow Study~~ | ~~3H~~ | ~~✅~~ | — | — | — | — | — | 🪦 **Dropped 2026-05-31** — 2H cap rule (CLAUDE.md). Length above 2H no longer in scope. |
| `healing-hour-vol-1-528hz-kyoto-zen-garden` | 528 Hz Healing Frequency \| Kyoto Zen Garden Meditation to Stop Overthinking | 1H 02min | ✅ | ⏳ | ✅ 16:9 + thumb done | ⏳ | ⏳ | ⏳ |
| `power-hour-528hz-tokyo-sound-bath` | 528 Hz Deep Sleep Music \| Tokyo Sound Bath for Anxiety Relief & Healing | 1H | ✅ | n/a (existing audio) | ✅ bowl thumb | n/a | ✅ rebrand applied | ✅ **published/scheduled 21.5** (`-1RE1P98_u8`) |
| `power-hour-pomodoro-tokyo-rain-25-5` | Pomodoro Study With Me — Deep Focus Music \| Tokyo Rain 25/5 for Coding & Studying | 2H (25/5 ×4) | ✅ | ✅ | ✅ gold thumb | ✅ CapCut assembled | ✅ | ✅ **published Tue Jun 2, 07:00 MSK** (`zjtGEZISKbg`) |

### Power Hour Pomodoro 25/5 — published Tue Jun 2, 07:00 MSK (`zjtGEZISKbg`)

First full Power Hour Pomodoro. Locked series look debuted: gold chroma-key live timer overlay (FOCUS 25:00 / BREAK 05:00) + music-breathing gong fades (50s taper into focus, 10s dip into breaks) + hourglass signature + gold thumbnail.

**SEO landed clean (verified 2026-06-02):** title 82c, full description with Pomodoro schedule + 36-track tracklist + 10 hashtags in body, 27 tags (Karena 20/20/40-50: brand `stillwave`/`stillwave pomodoro` + broad `pomodoro`/`study with me`/`focus music` + narrow `pomodoro 25 5`/`2 hour pomodoro`/`deep work pomodoro`/`pomodoro timer 2 hours`), topic categories = **Electronic Music + Music** (NOT Religion like 963 — landed in the right cluster 🎯), duration 2:00:12.

**Slipped from Mon Jun 1 to Tue Jun 2** — day later than planned. Tuesday morning still hits the work-week start surge for the pomodoro/study cluster, so timing remains valid.

Review schedule (don't judge before day 7 — algo push lands days 4–14):
- **48h** — Thu Jun 4, 07:00 → log VPH + views/likes/comments; just log, don't conclude
- **7d** — Tue Jun 9 → real read. Success = sustained VPH + functional repeat-use signals (saves, returning viewers) clearly beating a flat curve
- **30d** — Thu Jul 2 → final snapshot; decide if the Pomodoro template (gold timer + gong fades) becomes the locked Power Hour focus format

**Shorts cross-promo plan:** drop Pomodoro Shorts cover on D3 (Fri Jun 5) or D4 (Sat Jun 6) to re-ignite long-form after the initial algo test plateaus (per our Healing Hour pattern). Skip if D1 < 30 views — Shorts won't save a dead launch.

### Power Hour Tokyo Sound Bath — rebrand applied (2026-05-21)

Rebrand of `-1RE1P98_u8` went live 21.5 (title + tags + description + DEEP CALM thumbnail + Power Hour playlist all applied; hashtags last to add). Review schedule — **do not judge before day 7** (BrainCatAI Lesson 3: videos catch the algo push days 4–14):

- **48h** — May 23: pull VidIQ VPH + views/likes; just log, don't conclude
- **7d** — May 28: real read. Success = VPH > 0 sustained + clearly beating the old 53-view stall = rebrand moved it into a live cluster
- **30d** — Jun 20: final snapshot; decide if the penthouse-sound-bath pattern becomes a Power Hour template

## Series restructure (2026-05-20)

The original "528 Hz Japanese Zen Music Marathon Vol. 1" (`-1RE1P98_u8`) stalled at 53 views — its photoreal penthouse visual sat in the Deep Work cluster, not healing. Decision: **move it into Power Hour** (where that penthouse visual belongs) via a Studio-only rebrand, and **relaunch Healing Hour clean** in the validated Ghibli aesthetic.

- **Healing Hour Vol. 1** = the Ghibli Kyoto Zen Garden video (was "Vol. 2") — `healing-hour-vol-1-528hz-kyoto-zen-garden.md`
- **Power Hour 528 Hz Tokyo Sound Bath** = the rebranded old video — `power-hour-528hz-tokyo-sound-bath.md`
- De-dup: Healing Hour Vol. 1 owns **Stop Overthinking**; Power Hour Sound Bath owns **Deep Sleep & Anxiety Relief** (both 528 Hz, distinct outcomes, no cannibalization)

### Healing Hour series — running ledger

| Vol | Date | Title | Hz | Visual | Status | Early data | Notes |
|-----|------|-------|----|----|--------|-----------|-------|
| Sound Bath (moved out) | 2026-05-14, rebrand 05-21 | 528 Hz Deep Sleep Music \| Tokyo Sound Bath for Anxiety Relief & Healing (`-1RE1P98_u8`) | 528 | Photoreal penthouse → DEEP CALM | ✅ rebrand applied | **56, stalled** | Rebrand of a stalled video barely moved it. Lesson: reviving a stalled video ≈ doesn't work. |
| **1** | **2026-05-21** | **528 Hz Healing Frequency \| Stop Overthinking** (`po4jmYdX2_w`) | 528 | Ghibli Kyoto garden, QUIET MIND | ✅ **published 05-21** | D1=64 · D2=137 🔥 · D3=147 · D6=157 · **D10=157** · likes 4 · like-rate 2.5% · comments 1 | Strong D2 burst (137), then **HARD PLATEAU from D4** — D6 to D10 = ZERO new views, VPH=0 since D8. Algo gave it the test, dropped it cold. Like-rate below 3% threshold. Diagnosis: thumbnail/title pulled click, retention/recommend signals didn't carry. Compare 852 Hz Monks' Secret: 4 → 268 by D5 (sustained climb) — we DIDN'T match that pattern. |
| **2** | **2026-05-26** | **963 Hz Frequency of God \| Pineal Gland Activation for Spiritual Awakening** (`pwnoQYJjgOo`) | 963 | Ghibli Mount Koya night, gold AWAKEN, stone lantern, intro 天地一如 | ✅ **published 05-26** | **D1=12** · D2=29 · D3=31 · **D5=32, 0 likes, 1 comment** | 🔴 **FLOPPED.** Original log "D1≈400" was misattribution — channel +432 on 05-26 came from Shorts cross-promo + recommended-to-backlog wave, NOT this long-form (per-video VPH stats show real D1=12, D5=0.10). **Mystery-frame hypothesis BUSTED:** "Frequency of God" + gold thumb + cosmic Ghibli underperforms "Stop Overthinking" + cream cream. Worse than Kyoto on every metric. Don't lock the template — shelve. |

### Channel-level signal (2026-05-19 → 2026-05-31)

- Subs: **38 → 49 (+11 in 12 days)**, then **stalled at 49 since 05-28** (4 days flat). Initial bump was real, but momentum gone.
- Views growth crashed: 05-26 +432 → 05-29 +26 → 05-31 **+5**. Algo boost fully exhausted, channel back to ~5-15/day baseline.
- **Correction (2026-05-31):** the 05-26 +432 jump was earlier attributed to the 963 long-form. Per-video data shows that's wrong — 963 itself only got ~12 views D1. The +432 came from Shorts cross-promo and old-video recommendation surges. Healing Hour long-form is NOT the channel growth lever we thought.

### 🔴 Key lesson (2026-05-31) — Healing Hour pattern under question

Two-of-two Healing Hour videos hit D2 push and then plateaued. The Ghibli aesthetic + keyword-front title gets the **click**, but the **watch/retention/save signals** aren't sustaining the algorithmic push. Diagnosis options (need YouTube Studio retention data to confirm):
- Audio not compelling enough to keep viewers past 30s
- Title overpromises ("Frequency of God" → people expect more)
- Wrong audience segment from the click (curiosity, not intent)
- Saturated cluster — competitors do it better/longer

**Until diagnosed: pause more Healing Hour launches.** Pomodoro Mon 06-01 is the next test in a different cluster.

### 🏆 Key lesson (2026-05-22) — fresh upload >> rebrand of a stalled video

Same frequency (528 Hz), same week, two approaches:
- **Sound Bath** = rebrand of the stalled `-1RE1P98_u8` → **60 views by D17, still flat** (rebrand confirmed dead 05-31)
- **Healing Hour Vol. 1** = fresh upload `po4jmYdX2_w` → **157 by D10** (also plateaued, but ×2.6 better than rebrand)

YouTube gives a new upload a clean algorithmic test; a stalled video stays suppressed even after a full rebrand. **Going forward: re-upload fresh rather than try to revive a dead video.**

### Tracking — Healing Hour Vol. 1 (`po4jmYdX2_w`)
- ✅ 48h (05-23): D2=137 logged
- ✅ 7d (05-28): plateau confirmed at 157 — verdict: **template did NOT work, mystery-frame stays unvalidated**
- 30d (06-20): final snapshot

### Tracking — 963 Mount Koya (`pwnoQYJjgOo`)
- ✅ 48h (05-28): D2=29
- ✅ 7d-ish (05-31, D5): 32 — verdict: **flop, mystery-frame hypothesis BUSTED**
- 30d (06-25): final snapshot

## Phase 1 batch — week of May 13–19

These are the first 3 hybrid-format videos for the gradual transition (Phase 1 = 1 of 4 / week, but we're running 3 as a test batch). Each script file under `scripts/` has the full 11-item `SW:` package: Suno A + Suno B + NanoBanana 16:9 + NanoBanana 9:16 + ffmpeg command + Title + Description + Tags + Hashtags + Pinned comment + A/B variant.

| Date | Slug | Aesthetic-lean | Why |
|------|------|----------------|-----|
| TBD | `tokyo-apartment-rain-1h` | Tokyo apartment + heavy rain on glass + neon city + tea + bonsai. **Power Hour format (1H 04min, 24 Suno tracks, no loop)** | Catches "1 hour focus music" + "power hour" search demand. Lower production overhead than 2H. |
| TBD | `bonsai-desk-night-2h` | Tokyo apartment + open MacBook (warm screen glow) + bonsai + neon city | Most "coding/programming" hook, laptop is the hero |
| TBD | `lantern-glow-study-3h` | Tokyo apartment + paper andon lantern (warm vs neon contrast) + closed laptop + book | Most "scholarly/study" hook, lantern is the hero, longest at 3H |

Mix the 3 with current иероглиф / Hz format videos so the channel doesn't shift too fast.

## Workflow per video

1. Trigger `SW: [theme]` or `SWS: [theme]` in chat — get the 11-item package
2. Generate music in Suno (Prompts A + B)
3. Generate image in NanoBanana (16:9 + 9:16)
4. Generate video loop in Flow / Kling
5. Edit + master in CapCut + ffmpeg
6. Generate thumbnail via `THUMB: [theme]` → Canva
7. Schedule upload in YouTube Studio
8. After publish: update `published-videos.md` with views at 48h / 7d / 30d