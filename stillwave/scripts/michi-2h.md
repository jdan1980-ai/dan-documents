# MICHI 道 — the samurai's path through the snow (2 Hours)

## Meta
- **Status (2026-11-25):** Flow tracking-shot clip approved by review; loop = Veo's own clip (it already matches step for step; my 16-frame crossfade version was worse and was dropped; ~10% slower walk in the first 0.5 s, user keeps it). Music: `music-bank/yuki` (or any bank theme) after the Content ID check.
- **Concept (user's idea):** a lone samurai walks endlessly across a snowfield toward a distant temple, leaving footprints — the "endless walk" format of the biggest hit in the niche (KUMAMICHI, 1.67M), done with a samurai. The camera follows at a constant distance, so the clip can loop.
- **Frame:** `assets/michi-2h-source.jpg` (first frame of the Flow clip).

**🇺🇦 RU:** Самурай бесконечно идёт по снегу к далёкому храму и оставляет следы. Камера идёт следом, поэтому петля склеивается без рывка.

## Workflow rule
The Flow prompt is written only after the final image is chosen (user, 2026-11-25).

## Short (version B) — `assets/michi-short-motion.py`, track yuki 1635764
Built on a vertical crop of the Veo clip (no new frame, no Flow credits): `ffmpeg -i flow.mp4 -vf "crop=608:1080:656:0,scale=1080:1920:flags=lanczos,unsharp=5:5:0.5"` → `MICHI_loop_916.mp4` (the user kept Veo's own loop: it matches step for step; my crossfade version was dropped). Softer than native 9:16 (1.8× upscale). Cover 道 / MICHI over the samurai's dark robe (user-approved; the bottom is the Shorts UI zone, the top is temple and moon). Hook from the temple light to the walking samurai, "He walks toward the temple. / He never arrives." · 道 emerges · "The path itself / is the destination." No gold dust (the clip has blowing snow).

Title:
```
He Walks Toward the Temple and Never Arrives
```
Description (add the long-form link):
```
Michi (道), the path. For the samurai, the way was never about reaching the end: every step through the snow is the practice itself. The temple stays on the horizon, and that is the point.

Full 2-hour samurai meditation music on the channel: [MICHI link]

#shorts #michi #samurai #samuraimusic #zenmusic #winter
```
Tags:
```
michi, the way, samurai path, samurai walking, samurai in snow, winter samurai, japanese temple, samurai music, samurai meditation music, japanese zen music, meditation music, shorts
```
Pinned:
```
🌀 The path itself is the destination. Which step are you taking today? Full 2 hours of MICHI on the channel 🌿
```

## §2 — Album (music bank: tsuru, all 10 tracks passed)
Order keeps same-request pairs apart, incl. across the loop. Loop 27:51.6 × 4.3 = exactly 2:00:00, seams 3 s, −15.8 LUFS, MP3 320 kbps 4 × 30:00.

| # | Track | Start |
|---|---|---|
| 1 | 1635846 | 0:00 |
| 2 | 1635848 | 2:32 |
| 3 | 1635850 | 5:29 |
| 4 | 1635852 | 8:37 |
| 5 | 1635854 | 11:44 |
| 6 | 1635847 | 14:37 |
| 7 | 1635849 | 16:46 |
| 8 | 1635851 | 19:35 |
| 9 | 1635853 | 22:11 |
| 10 | 1635855 | 25:08 |

## §6a — Wisdom overlay
- **千里の道も一歩から** · *Senri no michi mo ippo kara* · "A thousand miles begin with one step".
- File: `assets/michi-senri-no-michi-overlay.png`, UPPER-LEFT over the dark sky (`make_overlay.py --kanji-size 80 --pitch 84 --dy -600 --scrim 150`), the kanji row ends just left of the pagoda; the lower-left is bright snow.
- CapCut: top track, 0:03 → 0:14, fade 2 s / 2 s.

**🇺🇦 RU:** «Путь в тысячу ри начинается с одного шага». Вверху слева над тёмным небом, строка иероглифов заканчивается чуть левее пагоды.

## §5 — Thumbnail v2
`assets/michi-compose-thumb-v2.py` → `assets/michi-2h-thumb-v2.jpg`: 道 / MICHI on the left over the dark sky and the shadowed snow; the samurai, the trail and the pagoda under the moon on the right.

## Sound bed
User's plan: a CC0 snowstorm bed under the music, maybe the Veo footsteps. Measured on the Veo clip: −37.5 LUFS, mostly wind; footstep transients only 3 times per 7.9 s loop and not in sync with the visible steps; a fixed 8-s repeat is easy to hear. Advice: footsteps in the Short yes; in the long-form only very low or none (rhythmic sound vs sleep).

## §7 — Title
```
MICHI — 道 | Samurai Meditation Music for the Long Path — Deep Focus, Calm & Sleep
```

## §8 — Description
```
Michi (道), the path. A lone samurai walks across an endless snowfield toward a distant temple, leaving a line of footprints behind him. The temple stays on the horizon, and that is the point: for the samurai, the way was never about arriving. Every step through the snow is the practice itself.

Two hours of samurai meditation music for the long walk, with the soft sound of wind and snow underneath. A low shakuhachi flute, warm koto plucked one note at a time, a deep dark drone like slow breathing, and long silences between the phrases. No drums, no beats, nothing that rises or builds. One quiet level from the first minute to the last.

Use it for:
- deep focus, study and long work sessions
- walking meditation and breathwork
- patience on a long project
- falling asleep on a cold winter night

0:00 The First Step Into the Snow
2:32 A Temple on the Horizon
5:29 Footprints Behind Him
8:37 The Wind Across the Field
11:44 One Step, Then the Next
14:37 The Moon Walks With Him
16:46 No Hurry on the White Road
19:35 The Path Is the Practice
22:11 Snow Fills the Old Tracks
25:08 Still Walking at Dawn
(the cycle repeats until 2:00:00)

More from StillWave Zen:
YUKI — Samurai Meditation Music with Snowstorm Sounds: [YUKI link]
TAKA — Samurai Meditation Music: https://youtu.be/WxqidZzyv4M
SHOGUN — Samurai Meditation Music: https://youtu.be/zH_eo09q7EA
MUSHIN — Japanese Zen Music for Deep Focus: https://youtu.be/CamT9sohYQM

千里の道も一歩から — senri no michi mo ippo kara: a thousand miles begin with one step.

New Japanese Zen music every week. Subscribe if you want it in your feed.

#samuraimusic #michi #samuraipath #samuraimeditation #zenmusic
```

## §9 — Tags (22 tags, 448 characters)
```
stillwave, michi, the way, samurai path, samurai walking in snow, samurai music, samurai meditation music, samurai relaxing music, japanese zen music, zen music, meditation music, focus music, deep focus music, sleep music, study music, relaxing music, shakuhachi flute music, koto music, japanese meditation music, snowstorm sounds, footsteps in snow, lone samurai walking across an endless snowfield toward a distant temple
```

## §11 — Pinned comment
```
🌀 道 MICHI — a thousand miles begin with one step, and the path itself is the destination. 🍃 What is the one step you are taking today? Subscribe for more Japanese zen focus sessions every week 🌿
```

**Upload settings:** Not for kids · Playlists "Japanese Zen Music" + "Samurai Meditation Music — Japanese Zen for Focus & Sleep" · first publish Scheduled/Unlisted · end screen → MUSHIN. Publish after YUKI (the description links to it); insert the YUKI link before publishing.
