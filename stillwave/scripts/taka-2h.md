# TAKA — Samurai Meditation Music (2 Hours)

## Meta
- **Status (2026-11-22):** hero 16:9 approved, 9:16 chosen (file still to be sent by the user), 4K loop rendering, album built, one-cycle check video sent for Content ID.
- **Concept:** a colossal hawk on a pine, painted in ink on gold (the Kano school "pine and hawk" theme of the shoguns' castles; falconry was the shogun's privilege), staring straight at the viewer; a lone samurai kneels before it. Chosen over the karajishi lion after a skeptical review (the lion read as comical; the hawk keeps a stern mood, high contrast and a direct gaze). The mural is one seamless wall without door rails.
- **Frames:** `assets/taka-2h-source.jpg` (2602×1464, cropped from 2752×1536).
- **Playlist (add to in Studio):** Japanese Zen Music + Samurai Meditation Music — Japanese Zen for Focus & Sleep.

## §2 — Album
Music generated for SHISHI (branch `claude/shishi-musicful`, 46 → 22 units); the music does not depend on the animal. Dropped `1631208` (widest loudness range, 19 dB) and `1631209`.

| # | Track | Key | Start in loop |
|---|---|---|---|
| 1 | 1631206 | D minor | 0:00 |
| 2 | 1631203 | G minor | 2:47 |
| 3 | 1631207 | D minor | 4:56 |
| 4 | 1631205 | G minor | 7:41 |
| 5 | 1631210 | D minor | 10:34 |
| 6 | 1631204 | D minor | 13:28 |

Loop 16:26.4 × 7.3 = exactly 2:00:00, seams 3 s, same-request pairs never adjacent incl. the loop. Deliver as MP3 320 kbps parts (CapCut truncates big WAVs imported together).

## §4b — Animation without Flow
`assets/taka-animate.py` (adapted from `shogun-animate.py`): candles, light on gold and floor, glowing eyes, candle sheen, the hawk breathes, gold dust. Checked on a draft: samurai and rack change ≤ 5/255 (light only).
