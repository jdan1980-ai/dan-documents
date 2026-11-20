# SHOGUN — Samurai Meditation Music (2 Hours)

## Meta
- **Status (2026-11-20):** hero 16:9 + 9:16 approved, 4K loop rendered, album built (awaiting the user's Content ID check of the 8 tracks), Short B rendered. Next: overlay, thumbnail, SEO.
- **Concept:** the shogun, ruler of all samurai, sits alone in his castle's audience hall, facing us, his face hidden behind a black iron mask, a slender golden crescent on his helmet. Behind him the gold-leaf doors carry a giant painted tiger (as in the shogun's Nijō Castle): the tiger is the shogun's power. First front-facing figure in the series (user's idea, for CTR).
- **Frames:** `assets/shogun-2h-source.jpg` (1984×1116, cropped), `assets/shogun-916-source.jpg` (1116×2000). Frames are free; only Flow video costs credits.

## §2 — Album
8 tracks on branch `claude/shogun-musicful` (Musicful 70 → 46 units). Check video: all 8 in id order (0:00 1627119, 4:09 1627120, 8:13 1627121, 11:52 1627122, 15:12 1627123, 19:25 1627124, 23:14 1627125, 26:34 1627126).
Dropped: `1627124` (A♯ minor, far from the rest) and `1627123` (G minor, widest loudness range 23 dB; used for the Short instead).

| # | Track | Key | Start in loop |
|---|---|---|---|
| 1 | 1627120 | D minor | 0:00 |
| 2 | 1627125 | D minor | 3:17 |
| 3 | 1627121 | D minor | 5:45 |
| 4 | 1627119 | G minor | 8:38 |
| 5 | 1627126 | D minor | 12:12 |
| 6 | 1627122 | B♭ major | 14:57 |

Loop 17:22.8, ×6.9 = exactly 2:00:00, seams 3 s. Same-request pairs (119/120, 121/122, 125/126) never adjacent, incl. across the loop. Master: alimiter 0.891, 16-bit WAV, −15.3 LUFS, four 30-min parts.

## §4b — Animation without Flow
`assets/shogun-animate.py` (4K: `... shogun-2h-source.jpg out.mp4 24 3840`; vertical: `VERT=1 ... shogun-916-source.jpg out.mp4 24 1080`). Candles flicker (light on gold + floor reflections), tiger eyes glow, a candle sheen crosses the stripes once per loop, the tiger breathes (frozen at the rails, around the shogun, crest and sword), a spark runs along the crescent, gold dust. The shogun never moves. Checked: rails and shogun ≤5/255 change (light only).

## Short (version B) — `assets/shogun-short-motion.py`, track 1627123
Cover 将軍 / SHOGUN · hook "He ruled every samurai. / Only the tiger watched him." on the blazing eyes · 虎 TORA brush-written · "True power / is perfect stillness." · soft, slow ink transitions (1.6 s).
