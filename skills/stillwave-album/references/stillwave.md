# StillWave (@stillwavezen) — album rules

Condensed from `stillwave/CLAUDE.md`. If that file says something different, it wins.

## Format
- Long-form album, **cap 2 hours** (`--cap 120`). Typical: 32–42 tracks, 1:55–2:00.
- Assembled by the user in CapCut from the renamed `<slug>-ALBUM` folder. CapCut sorts files by
  name, which is why the `NN - ` prefix matters.
- Playlist in Studio: **Japanese Zen Music**. Not for kids. First publish Scheduled or Unlisted.

## Wisdom overlay (every long-form)
- Real Japanese phrase, three lines: kanji (large), romaji, English gloss (2–6 words).
- Lower-left over a dark zone, cream `#F5EAD2`, kanji in the YujiBoku brush font, romaji and gloss
  in Liberation Serif Bold. Built by `scripts/make_overlay.py`.
- In CapCut: text layer on the top track, 0:03 → 0:14, fade in 2 s, fade out 2 s, no glow/box.
- Never reuse a phrase. Never name the album's own concept in it.
- Phrases used recently (grep the repo for the full list): 只管打坐 (ZAZEN), 深山幽谷 (NARA),
  啐啄同時 (SATORI), 坐忘心斎 (Shikantaza), 千年万年 (YAKUSHIMA), 寂然不動 (KARESANSUI),
  万理一空 (MUSASHI), 一葉知秋 (Autumn Leaves), 物我一如 (MUGA), 色即是空 (ENSO), 温故知新 (TENJIN),
  行雲流水 (BENZAITEN).

## Track names
- 3–6 words, a scene image or a small zen koan: temple, mist, moon, stone, bamboo, bell, breath.
- Never Hz numbers, BPM or technical music terms.
- Tie them to the album's world (MUSASHI used the five scrolls of the Book of Five Rings;
  KARESANSUI used sand, stone and the circle).

## Title and description
- Kanji-Concept format: `CONCEPT — 漢字 | Japanese Zen Music for …`, ≤ 90 characters.
- The word **Music** must appear in the first half of the title (otherwise YouTube can file the
  video under Lifestyle — it happened to Pomodoro 50/10).
- Description: keyword paragraph first, 3-line concept poem, scene in prose, tracklist, 2-line
  close, one subscribe line. No "Perfect for" lists, no hashtags in the body.
- Never claim the music was "recorded"; it is generated. Avoid BPM or "pulse" in copy for
  music sold as having no rhythm.

## Music generation notes (for new Lyria prompts)
- No percussion, no BPM numbers, flat dynamics, locked tail on every prompt.
- Vary the opening sound across variants (bell / shakuhachi / drone / koto) — Content ID.
- Rain, water and wind are never written into the music prompt; they go in as a separate CC0
  layer in CapCut.

## Visual notes
- Do not draw anything falling or flying in the still (leaves, petals, snow, birds): it freezes
  or jumps in the loop. Add that motion in Flow or as a separate CapCut layer.
- Thumbnails with baked-in text are fine as thumbnails; the video needs the clean frame.
