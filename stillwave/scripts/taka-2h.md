# TAKA — Samurai Meditation Music (2 Hours)

## Meta
- **Status (2026-11-22):** hero 16:9 approved, 9:16 chosen (file still to be sent by the user), 4K loop rendering, album rebuilt with 10 tracks (26-min loop), check video sent for Content ID.
- **Concept:** a colossal hawk on a pine, painted in ink on gold (the Kano school "pine and hawk" theme of the shoguns' castles; falconry was the shogun's privilege), staring straight at the viewer; a lone samurai kneels before it. Chosen over the karajishi lion after a skeptical review (the lion read as comical; the hawk keeps a stern mood, high contrast and a direct gaze). The mural is one seamless wall without door rails.
- **Frames:** `assets/taka-2h-source.jpg` (2602×1464, cropped from 2752×1536).
- **Playlist (add to in Studio):** Japanese Zen Music + Samurai Meditation Music — Japanese Zen for Focus & Sleep.

## §2 — Album (10 tracks, 2026-11-22)
Music generated for SHISHI (branch `claude/shishi-musicful`, 46 → 22 units) plus two unpublished spares in the same keys: `1622094` (KATANA batch) and `1622169` (OKAMI batch). The first build had 6 tracks and a 16:26 loop (7.3 repeats in 2 h); the user asked for a longer cycle. Not used: `1622097` (loudness swings up to 5.7 dB), off-key spares. Same-request pairs never adjacent, incl. across the loop.

| # | Track | Key | Start in loop |
|---|---|---|---|
| 1 | 1631206 | D minor | 0:00 |
| 2 | 1631203 | G minor | 2:47 |
| 3 | 1631208 | D minor | 5:06 |
| 4 | 1622094 | G minor | 7:21 |
| 5 | 1631205 | G minor | 10:00 |
| 6 | 1631209 | D minor | 12:50 |
| 7 | 1622169 | G minor | 15:12 |
| 8 | 1631207 | D minor | 18:02 |
| 9 | 1631210 | D minor | 20:43 |
| 10 | 1631204 | D minor | 23:23 |

Loop 26:20.9 × 4.6 = exactly 2:00:00, seams 3 s, −15.8 LUFS. Check video: the whole 10-track loop. Deliver as MP3 320 kbps parts.

## §4b — Animation without Flow
`assets/taka-animate.py` (adapted from `shogun-animate.py`): candles, light on gold and floor, glowing eyes, candle sheen, the hawk breathes, gold dust. Checked on a draft: samurai and rack change ≤ 5/255 (light only).
