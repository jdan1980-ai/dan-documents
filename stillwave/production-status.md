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
| `bonsai-desk-night-2h` | Deep Focus Music — Bonsai Desk Late Night | 2H | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| `lantern-glow-study-3h` | Quiet Hours Focus Music — Lantern Glow Study | 3H | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| `healing-hour-vol-1-528hz-kyoto-zen-garden` | 528 Hz Healing Frequency \| Kyoto Zen Garden Meditation to Stop Overthinking | 1H 02min | ✅ | ⏳ | ✅ 16:9 + thumb done | ⏳ | ⏳ | ⏳ |
| `power-hour-528hz-tokyo-sound-bath` | 528 Hz Deep Sleep Music \| Tokyo Sound Bath for Anxiety Relief & Healing | 1H | ✅ | n/a (existing audio) | ✅ bowl thumb | n/a | ✅ rebrand applied | ✅ **published/scheduled 21.5** (`-1RE1P98_u8`) |
| `power-hour-pomodoro-tokyo-rain-25-5` | Pomodoro Study With Me — Deep Focus Music \| Tokyo Rain 25/5 for Coding & Studying | 2H (25/5 ×4) | ✅ | ✅ | ✅ gold thumb | ✅ CapCut assembled | ✅ **scheduled Mon Jun 1, 07:00** | ⏳ |

### Power Hour Pomodoro 25/5 — scheduled Mon Jun 1, 07:00 (ID TBD)

First full Power Hour Pomodoro. Locked series look debuted: gold chroma-key live timer overlay (FOCUS 25:00 / BREAK 05:00) + music-breathing gong fades (50s taper into focus, 10s dip into breaks) + hourglass signature + gold thumbnail. Assembled as full Suno album in CapCut (no ffmpeg).

**Why Mon 07:00:** Pomodoro / study / coding = work-week demand. Monday morning catches the start-of-week work/study surge — stronger than a weekend slot for this content type.

Review schedule (don't judge before day 7 — algo push lands days 4–14):
- **48h** — Jun 3, 07:00 → log VPH + views/likes/comments; just log, don't conclude. **Get the video ID and fill it in here.**
- **7d** — Jun 8 → real read. Success = sustained VPH + functional repeat-use signals (saves, returning viewers) clearly beating a flat curve
- **30d** — Jul 1 → final snapshot; decide if the Pomodoro template (gold timer + gong fades) becomes the locked Power Hour focus format

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
| **1** | **2026-05-21** | **528 Hz Healing Frequency \| Stop Overthinking** (`po4jmYdX2_w`) | 528 | Ghibli Kyoto garden, QUIET MIND | ✅ **published 05-21** | D1=64 · D2=137 🔥 · D3=147 · D4=150 · D5=156 · **D6=157** · likes 4 · like-rate 2.5% · comments 1 | Strong D1-D2 burst (137 by D2 = best D2 on channel), then **HARD PLATEAU from D3** (+20 only across D3-D6). Algo push spent quickly. Like-rate below 3% threshold. Diagnosis: thumbnail/title pulled the click, follow-through/retention/recommend signals didn't sustain. Compare 852 Hz Monks' Secret: 4 → 268 by D5 (sustained climb). |
| **2** | **2026-05-26** | **963 Hz Frequency of God \| Pineal Gland Activation for Spiritual Awakening** (`pwnoQYJjgOo`) | 963 | Ghibli Mount Koya night, gold AWAKEN, stone lantern, intro 天地一如 | ✅ **published 05-26** | **D1 ≈ 400 views** (channel +432 on 05-26 vs ~+15-20 baseline) = **×6 stronger Day-1 than Kyoto** 🔥 | "Frequency of God" mystery framing + gold thumb + cosmic Ghibli HITTING harder than "Stop Overthinking" + cream. Validates the mystery-frame hypothesis. Shorts cross-promo 05-27. Watch D2-D3 (05-28 / 05-29) for sustain — if it doesn't plateau like Kyoto, lock the mystery template. |

### Channel-level signal (2026-05-19 → 2026-05-27)

- Subs: **38 → 48 (+10 in 6 days)** — channel was stuck at 38 for 11 consecutive days before Vol. 1 launched. Healing Hour relaunch broke the stall.
- Views: 4573 → 5302 (+729). Biggest single-day jump: **+432 on 05-26 (963 launch day)** — best day in channel history.
- Conclusion: the Healing Hour Ghibli + keyword-front-loaded titles are the validated growth lever.

### 🏆 Key lesson (2026-05-22) — fresh upload >> rebrand of a stalled video

Same frequency (528 Hz), same week, two approaches:
- **Sound Bath** = rebrand of the stalled `-1RE1P98_u8` (new title/tags/thumbnail on the existing video) → **56 views, still flat**
- **Healing Hour Vol. 1** = fresh upload `po4jmYdX2_w` → **118 in <24h, VPH 23 peak**

YouTube gives a new upload a clean algorithmic test; a stalled video stays suppressed even after a full rebrand. **Going forward: re-upload fresh rather than try to revive a dead video.**

### Tracking — Healing Hour Vol. 1 (`po4jmYdX2_w`)
- 48h (05-23): log VPH + views
- **7d (05-28): real read** — sustained VPH > 0, total clearly beating 852 Hz curve = locked template
- 30d (06-20): final snapshot

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