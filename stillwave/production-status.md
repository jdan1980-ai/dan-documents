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
| `tokyo-apartment-rain-1h` | Power Hour Focus Music — Tokyo Apartment Rain | 1H 04min 48sec (24 tracks) | ✅ | ✅ | ✅ | ✅ | ✅ published May 10, 14:00 | ✅ **published — 58 views in 24h** 🔥 |
| `nervous-system-reset-528hz-1h` | Best 528 Hz Japanese Zen Healing Music [1H Top Nervous System Reset] | 1H 01min (16 tracks) | ✅ | ✅ | ✅ | ✅ | ✅ **uploaded May 10, scheduled May 13 (Tue)** | ⏳ |

### Tokyo Apartment Rain — review schedule

After publish (May 10, 14:00):
- **24h (May 11) — DONE:** 58 views — ≈20× typical first-day rate on this channel. Format greenlit early.
- **48h review** — May 12, 14:00 → pull live API data, log views/likes/comments/CTR
- **7d review** — May 17, 14:00 → full retention analysis + comment mining + first lessons
- **30d review** — June 9, 14:00 → final perf snapshot, decide if pattern goes into Power Hour series template

### Nervous System Reset 528Hz — review schedule

After publish (May 13, time TBD):
- **48h review** — May 15 → pull live API data, log views/likes/comments/CTR, compare to Tokyo Apartment Rain at the same age
- **7d review** — May 20 → audience cluster check: did it lift on "1 hour focus" search (deep work cluster) or on "528 Hz / nervous system reset" search (healing cluster)? This decides playlist placement (see `playlists/power-hour.md` §3 candidates table)
- **30d review** — June 12 → final perf, decide if 528 Hz nervous-system framing becomes a recurring sub-format

### Power Hour 力 playlist

The Tokyo Apartment Rain video seeds the `Power Hour 力` series playlist. Asset (title / description / video list / API commands / manual steps) lives at `stillwave/playlists/power-hour.md`. Status: ⏳ awaiting manual creation in YouTube Studio (no OAuth creds for `playlists.insert`). After creation, paste the playlist URL into that file §7 and into the Tokyo video description.

The 528 Hz video sits in the candidates table (length-eligible, audience-cluster-borderline) — decision held until 7d review on May 20.
| `bonsai-desk-night-2h` | Deep Focus Music — Bonsai Desk Late Night | 2H | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| `lantern-glow-study-3h` | Quiet Hours Focus Music — Lantern Glow Study | 3H | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |

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