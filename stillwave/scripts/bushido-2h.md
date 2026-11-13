# BUSHIDO — Japanese Samurai Music for Calm & Quiet Discipline (2 Hours)

## Meta

- **Slug:** bushido-2h
- **Concept:** bushido as everyday discipline: sincerity, restraint, doing the plain thing properly when no one is watching.
- **Playlist (add to in Studio):** Japanese Zen Music
- **Format:** 6 Musicful tracks (one prompt, 3 requests = 18 units) stitched into one cycle with `sevenlights/tools/make_long_track.py`, looped to 2:00:00. One-cycle copyright check on YouTube before the 2 hours (same routine as RONIN).
- **Working folder on the PC:** `Desktop\StillWaveZen\BUSHIDO\`
- **Status:** 📝 title/description (user), overlay, image, Flow, music prompt, tags and pinned ready. Frame, overlay and thumbnail done (§5). Waiting for: music check.

**🇺🇦 RU:** Бусидо как повседневная дисциплина: искренность, сдержанность, простые дела, сделанные как следует, даже когда никто не видит. Формат как у RONIN: 6 треков Musicful, круг, проверка на YouTube, затем 2 часа.

## §1 — Music (Musicful)

Prompt file: `stillwave/scripts/bushido-musicful-prompt.txt` (no percussion, same quiet brief as RONIN).

## §3 — Hero image (NanoBanana 16:9)
```
Photorealistic cinematic still, 16:9, 4K, muted and restrained like a frame from a Kurosawa film shot on location. Dawn inside an old samurai house in the mountains. A lone samurai in a plain dark grey kimono and hakama kneels in seiza on polished dark wooden floorboards, back to camera, face never visible, hands resting on his thighs, placed in the lower third of the frame. EXACTLY TWO sheathed swords, a katana and a shorter wakizashi (the daisho pair), rest on a low wooden sword rack beside him. NO third sword. NO drawn sword. NO sword in his hands. In front of him the wide shoji screens stand fully open onto a quiet garden and, beyond it, layers of misty mountains. Above the mountains, filling the upper part of the frame, hangs an enormous pale golden rising sun, softly diffused by the mist; its low warm light falls through the open doorway and lays a long golden stripe across the floor and up the back of his kimono. A single steaming cup of tea on the floor beside him. Muted cool grey and dark wood tones, with ONE warm accent: the gold of the sun and its light on the floor. Profound stillness, discipline, quiet sincerity. The air is calm and still. No text, no letters.
```

## §4 — Flow loop
```
Feed the clean hero (no text). Camera completely locked: no pan, no zoom, no dolly. Keep the samurai, his swords, the room, the garden and the mountains exactly as they are, as a frozen photograph. The samurai does not move. Animate ONLY: (1) thin steam rising slowly from the tea cup; (2) the morning mist drifting very slowly across the distant mountains; (3) the glow of the sun breathing almost imperceptibly in brightness; (4) the faintest shimmer of light on the polished floor. Everything is slow and calm. Perfectly seamless 8-second loop, last frame matches first frame exactly.
```

## §5 — Chosen frame, overlay, thumbnail (2026-11-13)

- Frame saved as `assets/bushido-2h-source.jpg` (1984x1116, cropped to 16:9). The sword rack sits in the lower-left, so the overlay is **upper-left** over the left shoji, with a heavy scrim that stops short of the sun (`make_overlay.py --dy -600 --scrim 215 --scrim-right 640`).
- Thumbnail `assets/bushido-2h-thumb.jpg` (`bushido-compose-thumb.py`): contrast and warmth lifted (thumbnail only), BUSHIDO bold white upper-left, 武士道 in black brush on the sun.
- For a stronger click, the frame itself could be regenerated warmer and with more contrast (see chat 2026-11-13).

**🇺🇦 RU:** Подставка с мечами слева внизу, поэтому оверлей слева вверху на сёдзи, с плотной подложкой, которая не заходит на солнце. Превью: контраст и тепло подняты только на превью, BUSHIDO белым слева вверху, 武士道 кистью на солнце.

## §6a — Wisdom Overlay

- **至誠一貫** / *Shisei ikkan* / Sincere all the way through
- File: `assets/bushido-shisei-ikkan-overlay.png` (brush font, upper-left on the chosen frame — see §5).

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

[TRACKLIST — one cycle, then "(the cycle repeats until 2:00:00)"]

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
