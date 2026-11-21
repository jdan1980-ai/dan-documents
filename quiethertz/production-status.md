# Quiet Hertz — Production Status

New channel, launch batch of 10 videos replicating the "Healing Quiet Tonight" competitor format (see `../stillwave/competitor-tracker.md` for the teardown). Full content package for all 10 is in `scripts/batch-01.md`.

> Pipeline: 📝 script → 🎵 Lyria generated/mastered → 🎨 hero image generated → 🎬 Flow loop (optional) → 🎞️ ffmpeg assembled → ⏰ scheduled → 📤 published.

| # | Slug | Title | 📝 | 🎵 | 🎨 | 🎬 | 🎞️ | ⏰ | 📤 |
|---|------|-------|----|----|----|----|-----|-----|-----|
| 1 | `432hz-sleep-1` | 432Hz Deep Sleep Music — Fall Asleep in Minutes... #1 | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| 2 | `528hz-healing-1` | 528Hz Healing Music — Whole Body Regeneration & DNA Repair... #1 | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| 3 | `432-528hz-sleep-1` | 432Hz + 528Hz Sleep Music — Drift Into Deep Sleep... #1 | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| 4 | `741hz-sleep-1` | 741Hz Deep Sleep Music — Detox the Body... #1 | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| 5 | `963hz-healing-1` | 963Hz Healing Music — Pineal Gland Activation... #1 | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| 6 | `432hz-alpha-1` | 432Hz Alpha Waves Sleep Music — Whole Body Regeneration... #1 | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| 7 | `528-741hz-sleep-1` | 528Hz + 741Hz Sleep Music — Full Spine Healing... #1 | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| 8 | `432hz-melatonin-1` | 432Hz Deep Sleep Music — Melatonin Release... #1 | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| 9 | `396hz-healing-1` | 396Hz Healing Music — Release Fear & Guilt... #1 | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| 10 | `852hz-sleep-1` | 852Hz Deep Sleep Music — Awaken Intuition... #1 | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |

**Status (2026-10-08):** Full content package written for all 10 (titles, hero image prompts, Lyria music prompts, tags, descriptions, pinned comments — see `scripts/batch-01.md`). Visual template corrected same day from real competitor thumbnail screenshots: NOT a single reused background — consistent glowing wireframe-human character + a themed background that rotates per video's Hz/benefit (see `../CLAUDE.md`'s table). Channel itself not yet created on YouTube — still deciding final name/handle (working name "Quiet Hertz").

**Next steps, in order:**
1. Create the YouTube channel (Brand Account under the same Google account as StillWave) — pick final name/handle.
2. Generate the 10 hero images (NanoBanana, prompts in `scripts/batch-01.md`) — reuses only 6 background themes across the 10, so some images share a treatment.
3. Generate Lyria music per video (prompts in `scripts/batch-01.md`), master/select via `tools/master-album.py` + `tools/select-album.py` (cap ~180 min, adjust per video).
4. Build thumbnails via `assets/compose-thumb.py` (parameterize Hz text + tagline per video).
5. Assemble via ffmpeg (see `../CLAUDE.md` § Pipeline) — no CapCut needed.
6. Upload all 10, staggered (near-daily, matching the competitor cadence) rather than all at once — same "don't nuke your own impressions pool" logic as any new channel.
