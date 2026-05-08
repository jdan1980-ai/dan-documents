# StillWave — Production Status

Single source of truth for the StillWave pipeline. Update at every status change.

**Pipeline stages:** 📝 concept → 🎵 suno generated → 🎨 image generated → 🎬 video generated → 🎞️ assembled → ⏰ scheduled → 📤 published

---

## Published

See `published-videos.md` for the full table with metrics.

## In production / scheduled

| Slug | Title | Format | Length | 📝 | 🎵 | 🎨 | 🎬 | 🎞️ | ⏰ | 📤 |
|------|-------|--------|--------|----|----|----|----|-----|-----|-----|
| _none yet_ | | | | | | | | | | |

## Planned for next week (TBD — set via `SW:` triggers)

| Slot | Date | Format | Theme |
|------|------|--------|-------|
| 1 | TBD | Long video | TBD |
| 2 | TBD | Long video | TBD |
| 3 | TBD | Long video | TBD |

## Workflow per video

1. Trigger `SW: [theme]` or `SWS: [theme]` in chat — get the 11-item package
2. Generate music in Suno (Prompts A + B)
3. Generate image in NanoBanana (16:9 + 9:16)
4. Generate video loop in Flow / Kling
5. Edit + master in CapCut + ffmpeg
6. Generate thumbnail via `THUMB: [theme]` → Canva
7. Schedule upload in YouTube Studio
8. After publish: update `published-videos.md` with views at 48h / 7d / 30d