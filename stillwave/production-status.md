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
| `tea-house-rain-2h` | Quiet Focus Music — Japanese Tea House Rain | 2H | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| `bonsai-desk-night-2h` | Deep Focus Music — Bonsai Desk Late Night | 2H | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| `lantern-glow-study-3h` | Quiet Hours Focus Music — Lantern Glow Study | 3H | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |

## Phase 1 batch — week of May 13–19

These are the first 3 hybrid-format videos for the gradual transition (Phase 1 = 1 of 4 / week, but we're running 3 as a test batch). Each script file under `scripts/` has the full 11-item `SW:` package: Suno A + Suno B + NanoBanana 16:9 + NanoBanana 9:16 + ffmpeg command + Title + Description + Tags + Hashtags + Pinned comment + A/B variant.

| Date | Slug | Aesthetic-lean | Why |
|------|------|----------------|-----|
| TBD | `tea-house-rain-2h` | Most Japanese (engawa + shoji + bamboo + tea) | Bridge — feels familiar to current audience, introduces new format softly |
| TBD | `bonsai-desk-night-2h` | Balanced (modern desk + bonsai + city night) | Tests new dark city aesthetic + Japanese accent |
| TBD | `lantern-glow-study-3h` | Modern-leaning (study room + lantern + mountain silhouette) | Tests Phase 2 direction — minimum Japanese accent, maximum focus on the productivity scene |

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