# TAKA — Samurai Meditation Music (2 Hours)

## Meta
- **Status (2026-11-22):** hero 16:9 approved, 9:16 chosen (file still to be sent by the user), 4K loop rendering, album rebuilt with 10 tracks (26-min loop), Content ID clean, MP3 parts delivered, overlay + thumbnail + SEO done.
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

## Short (version B) — `assets/taka-short-motion.py`, track 1622097 (unused KATANA spare)
Vertical frame `assets/taka-916-source.jpg` (1116×2000, a separate generation: the hawk is larger and symmetric, its plumage differs from the 16:9 frame). Living loop: `VERT=1 python3 taka-animate.py taka-916-source.jpg loop.mp4 24 1080` (the first render showed a pale patch above the right candle, where the flame-removal zone reached the dark branch; fixed with a tighter flame zone).
Cover 鷹 / TAKA in the gap between the wings · hook "Only the shogun / could hunt with hawks." on the blazing eyes · 鷹 brush-written (24 strokes) · "Calm eyes / see everything." · soft 1.6 s ink transitions.

## §6a — Wisdom overlay
- **能ある鷹は爪を隠す** · *Nō aru taka wa tsume o kakusu* · "The skilled hawk hides its talons": true strength does not show off.
- File: `stillwave/assets/taka-noaru-taka-overlay.png`, lower-left (zone brightness 62 / 35), checked on a 4K-loop frame. A 9-glyph proverb, so smaller glyphs (`make_overlay.py --kanji-size 80 --pitch 84`, options added for long proverbs); the text ends at x 832, just left of the samurai.
- CapCut: top track, 0:03 → 0:14, fade in 2 s / fade out 2 s.

**🇺🇦 RU:** «Умелый ястреб прячет когти» — настоящая сила не выставляет себя напоказ. Оверлей внизу слева, текст заканчивается у самурая, но его не задевает.

## §5 — Thumbnail v2
`assets/taka-compose-thumb-v2.py` → `assets/taka-2h-thumb-v2.jpg`: the series layout (white 鷹, tracked TAKA, rules + circle, SAMURAI MEDITATION MUSIC) on the left; the hawk's eyes glow. Checked at 320×180: 鷹, TAKA and the hawk's eyes stay readable; the small subtitle does not (as on every v2 thumbnail).

## §7 — Title
```
TAKA — 鷹 | Samurai Meditation Music for Deep Focus, Calm Vigilance & Inner Strength
```

## §8 — Description
```
Taka (鷹), the hawk. In the castles of the shoguns, giant hawks were painted in ink on gold, perched on ancient pines, and hunting with hawks was a privilege kept for the shogun himself. The hawk is the image of calm vigilance: it waits on the branch without a single wasted movement, and sees everything.

Two hours of samurai meditation music in a golden castle hall at night, before a giant hawk painted in ink and gold. A low shakuhachi flute, warm koto plucked one note at a time, a deep dark drone underneath like slow breathing, and long silences between the phrases. Candlelight on the gold. No drums, no beats, nothing that rises or builds. One quiet level from the first minute to the last.

Use it for:
- deep focus, study and long work sessions
- seated meditation and breathwork
- calm, clear attention before an important task
- falling asleep with a quiet, steady mind

0:00 Candlelight on the Golden Wall
2:47 The Hawk Opens Its Wings
5:06 An Old Pine in the Night
7:21 Eyes That Miss Nothing
10:00 Talons Hidden in Stillness
12:50 Waiting on the Branch
15:12 Gold Leaf and Ink
18:02 One Breath Before Flight
20:43 The Watchful Calm
23:23 Wings Folded at Rest
(the cycle repeats until 2:00:00)

More from StillWave Zen:
SHOGUN — Samurai Meditation Music: https://youtu.be/zH_eo09q7EA
OKAMI — Samurai Meditation Music, the Wolf Guardian: https://youtu.be/ujYOkplvF-k
KATANA — Samurai Meditation Music: https://youtu.be/_fDIyyxtpWQ
MUSHIN — Japanese Zen Music for Deep Focus: https://youtu.be/CamT9sohYQM

能ある鷹は爪を隠す — nō aru taka wa tsume o kakusu: the skilled hawk hides its talons.

New Japanese Zen music every week. Subscribe if you want it in your feed.

#samuraimusic #taka #hawk #samuraimeditation #zenmusic
```

## §9 — Tags (23 tags, 438 characters)
```
stillwave, taka, hawk, hawk music, samurai music, samurai meditation music, samurai relaxing music, japanese zen music, zen music, meditation music, focus music, deep focus music, sleep music, study music, relaxing music, shakuhachi flute music, koto music, japanese meditation music, ancient japan ambience, japanese hawk painting, kano school, candlelight meditation, samurai kneeling before a giant hawk painted in ink on a golden wall
```

## §11 — Pinned comment
```
🌀 鷹 TAKA — the skilled hawk hides its talons: real strength stays calm and quiet. 🍃 Where do you need calm, clear attention this week? Subscribe for more Japanese zen focus sessions every week 🌿
```

**Upload settings:** Not for kids · Playlists "Japanese Zen Music" + "Samurai Meditation Music — Japanese Zen for Focus & Sleep" · first publish Scheduled/Unlisted · end screen → MUSHIN. Album delivered as MP3 320 kbps, 4 × 30:00. Content ID check of the 10-track loop: clean (2026-11-23).

## Short copy
Title:
```
Only the Shogun Could Hunt With Hawks
```
Description (add the long-form link):
```
Taka (鷹), the hawk. In old Japan, hunting with hawks was a privilege of the shogun, and giant hawks painted in ink on gold watched over his castle halls. A hawk waits on the branch in perfect calm, and sees everything.

Full 2-hour samurai meditation music on the channel: [TAKA link]

#shorts #taka #hawk #samurai #samuraimusic #zenmusic
```
Tags:
```
taka, hawk, japanese hawk, falconry, shogun, samurai, samurai music, samurai meditation music, japanese zen music, meditation music, zen, shorts
```
Pinned:
```
🌀 Calm eyes see everything. What do you notice when you slow down? Full 2 hours of TAKA on the channel 🌿
```
