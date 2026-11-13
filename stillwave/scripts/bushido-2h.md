# BUSHIDO — Japanese Samurai Music for Calm & Quiet Discipline (2 Hours)

## Meta

- **Slug:** bushido-2h
- **Concept:** bushido as everyday discipline: sincerity, restraint, doing the plain thing properly when no one is watching.
- **Playlist (add to in Studio):** Japanese Zen Music
- **Format:** 6 Musicful tracks (one prompt, 3 requests = 18 units) stitched into one cycle with `sevenlights/tools/make_long_track.py`, looped to 2:00:00. One-cycle copyright check on YouTube before the 2 hours (same routine as RONIN).
- **Working folder on the PC:** `Desktop\StillWaveZen\BUSHIDO\`
- **Status:** 📝 title/description (user), overlay, image, Flow, music prompt, tags and pinned ready. Frame, overlay and thumbnail done (§5). **2-hour track built** (2026-11-13): `BUSHIDO_2h.mp3`, 320 kbps, exactly 2:00:00, −15.5 LUFS, peak −0.9 dBFS after a −1 dB limiter. Next: CapCut, upload.

**🇺🇦 RU:** Бусидо как повседневная дисциплина: искренность, сдержанность, простые дела, сделанные как следует, даже когда никто не видит. Формат как у RONIN: 6 треков Musicful, круг, проверка на YouTube, затем 2 часа.

## §1 — Music (Musicful)

Prompt file: `stillwave/scripts/bushido-musicful-prompt.txt` (no percussion, same quiet brief as RONIN).

## §2 — Album and one-cycle check (2026-11-13)

6 Musicful tracks (branch `claude/bushido-musicful`), 18 units (262 → 244). Musicful has no length parameter (docs checked): MFV3.0 caps at 8 min but sets no target, so the prompt's length cue is the only lever; tracks came out 3:13–3:45.

Track `1606611` is in **G major** while the other five sit in D minor / G minor (chroma similarity 0.50 vs 0.96–0.99), and it has the album's biggest jump (+19.5 dB at 0:18). It is **left out** of the cycle so the album stays in one key.

| # | Track | Starts in the cycle |
|---|---|---|
| 1 | 1606610 | 0:00 |
| 2 | 1606614 | 2:54 |
| 3 | 1606612 | 5:16 |
| 4 | 1606613 | 7:56 |
| 5 | 1606615 | 10:43 |

Cycle 13:42 (≈ 9 repeats in 2 hours), −15.5 LUFS, LRA 6.2. Peak reaches 0.0 dBFS, so the 2-hour build gets a −1 dB true-peak limit.

**🇺🇦 RU:** Трек 1606611 в другой тональности (соль мажор) и с самым резким скачком, поэтому в круг не взят: 5 треков, круг 13:42. В документации Musicful параметра длины нет, только подсказка в промте.

## §3 — Hero image (NanoBanana 16:9)
```
Photorealistic cinematic still, 16:9, 4K, muted and restrained like a frame from a Kurosawa film shot on location. Dawn inside an old samurai house in the mountains. A lone samurai in a plain dark grey kimono and hakama kneels in seiza on polished dark wooden floorboards, back to camera, face never visible, hands resting on his thighs, placed in the lower third of the frame. EXACTLY TWO sheathed swords, a katana and a shorter wakizashi (the daisho pair), rest on a low wooden sword rack beside him. NO third sword. NO drawn sword. NO sword in his hands. In front of him the wide shoji screens stand fully open onto a quiet garden and, beyond it, layers of misty mountains. Above the mountains, filling the upper part of the frame, hangs an enormous pale golden rising sun, softly diffused by the mist; its low warm light falls through the open doorway and lays a long golden stripe across the floor and up the back of his kimono. A single steaming cup of tea on the floor beside him. Muted cool grey and dark wood tones, with ONE warm accent: the gold of the sun and its light on the floor. Profound stillness, discipline, quiet sincerity. The air is calm and still. No text, no letters.
```

## §3b — Stronger hero for the thumbnail (2026-11-13, after a low VidIQ thumbnail score)

Competitor thumbnails that break out (GAN tiger mural 9.1K, ŌKAMIMICHI wolf 13.8K, KUMAMICHI bear 2.2M, JAKU armor + red lilies, TAO tiger mural 1.7M) share four things ours lack: **one huge icon** (tiger, wolf, bear, armor) larger than the human; **high contrast** with one strong colour (red or gold); **few elements and empty space** for the text; and **light elegant typography** (white brush kanji + spaced serif romaji + a thin rule + "JAPANESE ZEN MUSIC"), not bold sans block letters.

```
Photorealistic cinematic still, 16:9, 4K, like a frame from a Kurosawa film. A lone samurai in full dark lacquered armor with a horned kabuto helmet kneels in seiza on the polished wooden floor of a vast old temple hall at dawn, back to camera, face never visible, placed slightly right of center and filling the lower half of the frame. EXACTLY TWO sheathed swords, a katana and a shorter wakizashi, rest on the floor beside him. NO third sword. NO drawn sword. NO sword in his hands. The entire back wall in front of him is a colossal ancient ink-and-gold mural of a tiger emerging from swirling clouds, the tiger's head and eyes larger than the samurai, staring down calmly. A single beam of warm golden morning light falls through a high window across the floor and the mural. A thin ribbon of incense smoke rises beside him. The left third of the frame is calm, dark and empty wooden wall. Deep charcoal blacks and aged wood browns, with ONE strong accent: the deep red of the samurai's armor cords and the gold of the light beam. High contrast, profound stillness, discipline, power at rest. No text, no letters.
```

Typography v2 on the current frame: `assets/bushido-compose-thumb-v2.py` → `bushido-2h-thumb-v2.jpg`.

**🇺🇦 RU:** У превью конкурентов, которые выстреливают, есть четыре вещи, которых нет у нас: один огромный образ (тигр, волк, медведь, доспех) крупнее человека; высокий контраст с одним сильным цветом; мало деталей и пустое место под текст; лёгкая элегантная типографика вместо жирных блоковых букв.

## §4 — Flow loop
```
Feed the clean hero (no text). Camera completely locked: no pan, no zoom, no dolly. Keep the samurai, his swords, the room, the garden and the mountains exactly as they are, as a frozen photograph. The samurai does not move. Animate ONLY: (1) thin steam rising slowly from the tea cup; (2) the morning mist drifting very slowly across the distant mountains; (3) the glow of the sun breathing almost imperceptibly in brightness; (4) the faintest shimmer of light on the polished floor. Everything is slow and calm. Perfectly seamless 8-second loop, last frame matches first frame exactly.
```

## §5 — Chosen frame, overlay, thumbnail (2026-11-13)

- Frame saved as `assets/bushido-2h-source.jpg` (1984x1116, cropped to 16:9). The sword rack sits in the lower-left, so the overlay is **upper-left** over the left shoji, with a heavy scrim that stops short of the sun (`make_overlay.py --dy -600 --scrim 215 --scrim-right 640`).
- Thumbnail `assets/bushido-2h-thumb.jpg` (`bushido-compose-thumb.py`): contrast and warmth lifted (thumbnail only), BUSHIDO bold white upper-left, 武士道 in larger black brush running top to bottom on the left shoji (moved off the sun at the user's request).
- For a stronger click, the frame itself could be regenerated warmer and with more contrast (see chat 2026-11-13).

**🇺🇦 RU:** Подставка с мечами слева внизу, поэтому оверлей слева вверху на сёдзи, с плотной подложкой, которая не заходит на солнце. Превью: контраст и тепло подняты только на превью, BUSHIDO белым слева вверху, 武士道 крупнее, сверху вниз на левой сёдзи (по просьбе пользователя).

## §5b — Final frame: armored samurai before the tiger mural (2026-11-13)

The user generated the §3b prompt. It replaces the shoji frame (kept as `assets/bushido-2h-source-v1-shoji.jpg`): `assets/bushido-2h-source.jpg`, 1984x1116. Huge tiger, red armor cords, gold light beam, dark empty left third. Two swords on the floor, both sheathed. The standard lower-left overlay sits on the dark floor and wall (brightness 18–24), clear of the swords. Thumbnail: `bushido-2h-thumb-v2.jpg` (white brush 武士道, serif BUSHIDO, rule, JAPANESE ZEN MUSIC).

### Flow loop for this frame
```
Feed the clean hero (no text). Camera completely locked: no pan, no zoom, no dolly. Keep the armored samurai, his helmet, the two swords on the floor, the hall and the tiger mural exactly as they are, as a frozen photograph. The samurai and the tiger do not move. Animate ONLY: (1) the thin ribbon of incense smoke rising and curling slowly; (2) fine dust drifting very slowly inside the beam of light from the high window; (3) the beam's brightness breathing almost imperceptibly; (4) the faintest shimmer of light on the polished floor. Everything is slow and calm. Perfectly seamless 8-second loop, last frame matches first frame exactly.
```

**🇺🇦 RU:** Новый кадр (самурай в доспехах перед огромным тигром) заменил кадр с сёдзи. Оверлей стоит в стандартном месте слева внизу на тёмном полу, мечей не касается. Превью — v2 на новом кадре.

## §6a — Wisdom Overlay

- **至誠一貫** / *Shisei ikkan* / Sincere all the way through
- File: `assets/bushido-shisei-ikkan-overlay.png` (brush font, standard lower-left on the final tiger frame — see §5b).

**🇺🇦 RU:** 至誠一貫 — «искренность от начала до конца». Прямо о сути бусидо (честность и постоянство), но само слово 武士道 не называет. На канале не использовалось.

## §7 — Title
```
BUSHIDO — Japanese Samurai Music for Calm & Quiet Discipline (2 Hours)
```

## §8 — Description
```
Bushido is not a code about winning. It is a code about how you behave when no one is watching: sincerity, restraint, and doing the plain thing properly, again and again.

Two hours of calm Japanese samurai music for that kind of discipline. Koto and shakuhachi over a warm, steady drone, slow and unhurried, with no dramatic swells. Discipline does not need drama.

Best for:
- morning routines and slow starts
- long focus sessions
- reading and study
- quiet evenings when the mind is still moving

0:00 Dawn in the Hall of the Tiger
2:54 The Armor Rests
5:16 Incense Before the First Lesson
7:56 A Plain Thing, Done Properly
10:43 Light Across the Wooden Floor
(the cycle repeats until 2:00:00)

More from StillWave Zen:
Miyamoto Musashi — Samurai Meditation for Stress Relief: https://youtu.be/mJ3RMn3J4B8
Hachiman — The God of War's Silence: https://youtu.be/jkKiSuRTmZE

What is your own version of bushido, the one rule you keep even when nobody checks? Tell me in the comments.

New Japanese Zen music every week. Subscribe if you want it in your feed.

#samuraimusic #japanesezenmusic #calmmusic #bushido #kotomusic
```

## §9 — Tags
```
stillwave, bushido, samurai music, japanese samurai music, samurai meditation music, japanese zen music, calm music, focus music, deep focus music, study music, morning routine music, meditation music, zen music, relaxing music, calming music, shakuhachi flute music, koto music, japanese meditation music, japanese warrior music, ancient japan ambience, samurai kneeling in a dawn-lit japanese house with open shoji and a golden sun over misty mountains, joe hisaishi
```

## §11 — Pinned comment
```
🌀 武士道 BUSHIDO — not a code about winning, but about how you act when no one is watching. 🍃 What is the one rule you keep even when nobody checks? Subscribe for more Japanese zen focus sessions every week 🌿
```
