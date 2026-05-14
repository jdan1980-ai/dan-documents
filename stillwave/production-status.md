# StillWave — Production Status

Single source of truth for the StillWave pipeline. Update at every status change.

**Pipeline stages:** 📝 concept → 🎵 suno generated → 🎨 image generated → 🎬 video generated → 🎞️ assembled → ⏰ scheduled → 📤 published

---

## Published

See `published-videos.md` for the full table with metrics.

## In production / scheduled

> Pipeline для long-form статической картинки: 📝 script → 🎵 suno generated → 🎨 image generated → 🎬 ~~not needed~~ → 🎞️ ffmpeg encoded → ⏰ scheduled → 📤 published.

| Slug | Title | Length | Series | 📝 | 🎵 | 🎨 | 🎞️ | ⏰ | 📤 |
|------|-------|--------|--------|----|----|----|-----|-----|-----|
| `tokyo-apartment-rain-1h` | Tokyo Rain Deep Work Marathon \| 1 Hour Uninterrupted Vol. 1 | 1H 04M 56S (24 tracks) | POWER HOUR | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ **published May 10, 10:20 UTC** ([aUujtRQZGaw](https://www.youtube.com/watch?v=aUujtRQZGaw)) — title VidIQ 93/100 |
| `healing-hour-528hz-1h` | 528 Hz Japanese Zen Music Marathon \| 1 Hour Healing Uninterrupted Vol. 1 *(VidIQ 91/100)* | 1H 01M 25S | HEALING HOUR | ❌ (no script file yet) | ✅ | ✅ | ✅ | ✅ **scheduled May 14, 18:00 МСК (15:00 UTC)** ([-1RE1P98_u8](https://www.youtube.com/watch?v=-1RE1P98_u8)) | ⏳ — ⚠️ rename in YouTube Studio before publish |
| `tokyo-snowfall-coding-1h` | Tokyo Snowfall Coding Marathon \| 1 Hour Uninterrupted Vol. 2 | **1H 06M 05S (3965 sec, 25 tracks)** — redo on May 14 after CapCut project loss | POWER HOUR | ✅ | ✅ (mixed kokyu/sho/shakuhachi rotation) | ⏳ | ⏳ | ⏳ | ⏳ |
| `bonsai-desk-night-2h` | Deep Focus Music — Bonsai Desk Late Night | 2H | POWER HOUR | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| `lantern-glow-study-3h` | Quiet Hours Focus Music — Lantern Glow Study | 3H | POWER HOUR | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |

### Healing Hour 528 Hz — review schedule

Publishes May 14, 18:00 МСК (15:00 UTC). First entry in new **HEALING HOUR** series, parallel to POWER HOUR. Hook: "Nervous System Reset" — leans into wellness / vagus-nerve / somatic-healing search demand. No `scripts/` file yet — created directly in YouTube Studio.

- **48h review** — May 16, 18:00 МСК → views, like-rate, comments. Compare pacing vs Tokyo Power Hour (which hit 131 views by 72h).
- **7d review** — May 21, 18:00 МСК → retention, full comment mining, decide whether healing-hook outperforms focus-hook
- **30d review** — June 13, 18:00 МСК → final perf snapshot, decide if HEALING HOUR becomes recurring series

### Tokyo Power Hour — review schedule

Published May 10, 10:20 UTC. Title history:

1. **Planned (pre-upload):** "Power Hour Focus Music — Tokyo Apartment Rain"
2. **Uploaded May 10:** "Best Focus Music Tokyo Rain Power Hour [1H Top Deep Work]" (keyword-stuffed)
3. **Final (May 13, after Vol. N rule + VidIQ testing):** "Tokyo Rain Deep Work Marathon | 1 Hour Uninterrupted Vol. 1" — **VidIQ score 93/100**

The final title drops "Power Hour" from the title body entirely — series brand is now carried only by thumbnail overlay + playlist + description. Lead keyword is the scene (Tokyo Rain), hook is "Deep Work Marathon", differentiator is "1 Hour Uninterrupted". This is now the canonical VidIQ-validated formula for the series (see CLAUDE.md §Title format).

- ✅ **72h check** — May 13: **131 views, 2 likes, 2 comments**. Pacing ~44 views/day — faster than KIRI (27/day) and 852 Hz (18/day). Like-rate (1.5%) is **below** top performers (KIRI 3.3%, 852 Hz 2.1%) — investigate at 7d.
- **7d review** — May 17 → full retention analysis + comment mining + first lessons
- **30d review** — June 9 → final perf snapshot, decide if Power Hour pattern goes into series template

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