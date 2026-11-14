# RONIN — Samurai Zen Music for Deep Focus & Inner Stillness (2 Hours)

## Meta

- **Slug:** ronin-2h
- **Concept:** a ronin is a samurai with no master: no banner, no orders, only the work in front of you and the breath that carries it. Deep-focus album.
- **Playlist (add to in Studio):** Japanese Zen Music
- **Length target:** 2H, built from **6 Musicful tracks (~3:15 each) stitched into one cycle and looped to 2 hours** — the short-album format the user switched to on 2026-11-12 (see `CLAUDE.md`).
- **Status:** 📝 title + description drafted by the user, overlay built, image prompts and the Musicful music prompt written (§1, §3, §4). Hero frame chosen, overlay placed, thumbnail built (§5). Album of 6 tracks stitched, one-cycle check video sent (§2). YouTube copyright check passed (user, 2026-11-12). **2-hour track built:** `RONIN_2h.mp3` (320 kbps, 7 cycles, exactly 2:00:00, −15.6 LUFS, LRA 5.5, peak −0.3 dBFS) sent to the user. Next: CapCut assembly with the Flow loop and overlay, upload in the "dan-documents" environment.

**🇺🇦 RU:** Ронин — самурай без господина: ни знамени, ни приказов, только работа перед тобой и дыхание. Альбом для глубокой концентрации. Ждём папку с треками и кадр.

## §1 — Music (Musicful API, one prompt for the whole album)

Per the user's instruction of 2026-11-12: music comes from the **Musicful API** with the tools in `sevenlights/tools/` (`musicful_album.py`, `make_long_track.py`), the same way Seven Lights albums are built. One prompt for the whole album (similarity between tracks is intended), 1 request = 2 tracks (~3:15) = 6 units of the Starter plan shared by both channels.

- Prompt: `stillwave/scripts/ronin-musicful-prompt.txt`
- Plan (updated 2026-11-12): **6 tracks = 3 requests = 18 units**, to save credits. First ONE test request (2 tracks, 6 units); if the user likes the sound, 2 more requests. Check `--balance` first.
- Sound brief from the user: very quiet, calm, meditative, no bursts, Japanese. The prompt therefore has **no percussion** (the earlier draft had soft wooden taps); if the test confirms this, change "soft wooden percussion" in the description to match.
- **Must run in the cloud environment "dan-documents"** — the API key is injected there by the proxy. The session that wrote this file ran in "Default", where `api.musicful.ai` is blocked and the session could not be moved.

```bash
python sevenlights/tools/musicful_album.py --balance
python sevenlights/tools/musicful_album.py --prompt-file stillwave/scripts/ronin-musicful-prompt.txt --requests 1 --out <work>/ronin/   # test; then --requests 2
python sevenlights/tools/make_long_track.py --in <6 mp3> --trim-start 8 --trim-end 6 --check --out <work>/ronin_check_1cycle.wav
# one-cycle video with the hero image -> user uploads as Unlisted -> YouTube copyright check
# only after a clean check (StillWave cap is 2 hours, not 3):
python sevenlights/tools/make_long_track.py --in <6 mp3> --trim-start 8 --trim-end 6 --hours 2 --out <work>/ronin_2h.flac
```

**🇺🇦 RU:** Музыка — через Musicful API инструментами из `sevenlights/tools/`, один промт на весь альбом. 6 треков = 3 запроса = 18 единиц общего тарифа; сначала один пробный запрос (2 трека, 6 единиц) и проверка остатка. По просьбе пользователя музыка очень тихая и медитативная, поэтому в промте нет перкуссии. Запускать только в облачной среде «dan-documents»: ключ подставляется там. Порядок: треки → один круг (`--check`) → видео с картинкой → проверка авторских прав на YouTube (ограниченный доступ) → только потом 2 часа (`--hours 2`, у StillWave кап 2 часа).

## §2 — Album and one-cycle check (2026-11-12)

6 Musicful tracks (branch `claude/ronin-musicful-test`, `stillwave/audio-test/ronin/`), 18 units in total (280 → 262). All are in G minor / D minor / F major on the same notes (chroma similarity 0.88–1.00), so the cycle stays in one harmonic world. Sub-bass below 60 Hz: none.

Cycle order (chosen for the closest-sounding neighbours; four of six seams got the shortest 0.5 s join):

| # | Track | Starts in the cycle |
|---|---|---|
| 1 | 1605188 | 0:00 |
| 2 | 1605193 | 2:30 |
| 3 | 1605195 | 5:28 |
| 4 | 1605192 | 8:40 |
| 5 | 1605194 | 11:29 |
| 6 | 1605189 | 14:09 |

Cycle length 17:04, −15.7 LUFS, LRA 5.7 LU, peak −0.3 dBFS. No clicks at any seam (sample jumps at seams below the track-wide 99.99th percentile). The largest level change in the cycle (+14 dB) is at 5:40, inside track 1605195 (its first loud note), not at a seam.

```bash
python3 sevenlights/tools/make_long_track.py --in 1605188.mp3,1605193.mp3,1605195.mp3,1605192.mp3,1605194.mp3,1605189.mp3 --trim-start 8 --trim-end 6 --check --out ronin_check_1cycle.wav
# after a clean YouTube check (2 hours = ~7 cycles):
python3 sevenlights/tools/make_long_track.py --in <same order> --trim-start 8 --trim-end 6 --hours 2 --out ronin_2h.flac
```

**Copyright check: clean (2026-11-12).** 2-hour track: 7 cycles, exactly 2:00:00.

**🇺🇦 RU:** Проверка авторских прав пройдена. Финальный трек 2:00:00 (7 кругов) отдан пользователю. 6 треков, круг 17:04, все в одной тональной группе. Стыки без щелчков. Самый громкий перепад (+14 дБ) на 5:40 — внутри трека, не на стыке. Проверочное видео отдано пользователю для проверки авторских прав.

## §3 — Hero image (NanoBanana 16:9)

### Variant A — dawn on the mountain pass (default)
```
Photorealistic cinematic still, 16:9, 4K, muted and restrained like a frame from a Kurosawa film shot on location. A lone ronin stands on a narrow mountain pass at dawn, back to camera, face never visible, placed in the lower third of the frame. He wears a wide woven straw travelling hat, a worn dark indigo kimono and a faded travelling cloak. EXACTLY TWO swords, a katana and a shorter wakizashi (the daisho pair), both fully sheathed inside the obi belt at his LEFT hip, hilts pointing forward. His hands hang empty and relaxed at his sides. Tall pale pampas grass lines both sides of the worn dirt path. Ahead of him the path drops away into a vast valley filled with thick morning mist, with layer after layer of dark mountain ridges fading into the distance. Low over the farthest ridge hangs an enormous pale golden rising sun, softly diffused by the mist, filling the upper part of the frame and rim-lighting the edge of his hat and shoulders. Muted cool grey-blue tones across the mountains and mist, with ONE warm accent: the gold of the sun and its glow on the grass tips. Profound stillness, solitude, quiet resolve. The air is calm and still. No text, no letters.
```

### Variant B — night road under a giant moon
```
Photorealistic cinematic still, 16:9, 4K, muted and restrained like a frame from a Kurosawa film shot on location. Night. A lone ronin stands on an old stone road at the edge of a cedar forest, back to camera, face never visible, placed in the lower third of the frame. He wears a wide woven straw travelling hat, a worn dark indigo kimono and a faded travelling cloak. EXACTLY TWO swords, a katana and a shorter wakizashi (the daisho pair), both fully sheathed inside the obi belt at his LEFT hip, hilts pointing forward. His hands hang empty and relaxed at his sides. The road runs straight ahead between tall dark cedars toward a distant mountain. Above the mountain hangs a colossal full moon, pale and detailed, filling the upper part of the frame and casting cold silver light on the wet stones of the road. Low mist lies between the trees. Beside the road, one weathered stone lantern holds a small warm flame. Muted deep blue and silver tones, with ONE warm accent: the lantern flame. Profound stillness, solitude, quiet resolve. The air is calm and still. No text, no letters.
```

> Save the chosen frame as `assets/ronin-2h-source.jpg`. Thumbnail text is added afterwards by script (large `RONIN` at the top in the user's current bold white style, small `浪人` or `SAMURAI ZEN` under it).

**🇺🇦 RU:** A — рассвет на горном перевале, огромное солнце в тумане (основной). B — ночная дорога под гигантской луной, тёплый акцент — огонь в каменном фонаре. Текст превью добавляется после, скриптом.

## §3c — Stronger hero for the thumbnail (2026-11-13, same analysis as BUSHIDO §3b)

The current frame has no big icon: the moon is the only large element and the figure is small. Breakout competitors put one huge icon next to the human. For a ronin the natural icon is the **lone wolf** — an idiom every American viewer knows.

```
Photorealistic cinematic still, 16:9, 4K, like a frame from a Kurosawa film. Night on an old stone road through a cedar forest. A lone ronin in a wide woven straw hat, worn dark indigo kimono and ragged travelling cloak stands on the road, back to camera, face never visible, placed right of center, filling the lower half of the frame. EXACTLY TWO swords, a katana and a shorter wakizashi, both fully sheathed inside the obi belt at his LEFT hip, hilts pointing forward. His hands hang empty at his sides. Beside him, walking with him on the road, is a colossal white wolf made of pale moonlit mist and soft light, its shoulder far taller than the man, its head turned slightly toward him, calm and protective, its fur dissolving into the fog at the edges. Behind them a huge full moon fills the top of the frame. The left third of the frame is dark cedar trunks and empty shadow. Deep black and cold silver-blue tones, with ONE warm accent: a single stone lantern with a small orange flame beside the road. High contrast, solitude, a lone wanderer and his silent guardian, profound stillness. No text, no letters.
```

Typography v2 on the current frame: `assets/ronin-compose-thumb-v2.py` → `ronin-2h-thumb-v2.jpg` (text above the figure).

**🇺🇦 RU:** В текущем кадре нет крупного образа: только луна и маленькая фигура. Для ронина естественный образ — «одинокий волк», это выражение понятно любому американцу. Промт: огромный белый волк из лунного тумана идёт рядом с ронином.

## §4 — Flow loop (for variant A)
```
Feed the clean hero (no text). Camera completely locked: no pan, no zoom, no dolly. Keep the ronin, his hat, cloak and swords, the path and the mountains exactly as they are, as a frozen photograph. The ronin does not move. Animate ONLY: (1) the valley mist drifting very slowly sideways, soft and continuous; (2) the pampas grass swaying gently in a light breeze; (3) the glow of the sun breathing almost imperceptibly in brightness; (4) the hem of the cloak stirring very slightly. Everything is slow and calm. Perfectly seamless 8-second loop, last frame matches first frame exactly.
```

## §4b — Flow loop (for variant B, the chosen frame)
```
Feed the clean hero (no text). Camera completely locked: no pan, no zoom, no dolly. Keep the ronin, his hat, cloak and swords, the cedars, the stone road, the mountain and the moon exactly as they are, as a frozen photograph. The ronin does not move. Animate ONLY: (1) the low mist between the trees drifting very slowly sideways, soft and continuous; (2) the small flame inside the stone lantern flickering gently, a calm candle-like glow; (3) the ragged hem of the cloak stirring very slightly; (4) the faintest shimmer of moonlight on the wet stones of the road. Everything is slow and calm. Perfectly seamless 8-second loop, last frame matches first frame exactly.
```

## §5 — Chosen frame, overlay placement, thumbnail (2026-11-12)

- **Frame:** the user generated variant B (night road, giant moon, stone lantern). Saved as `assets/ronin-2h-source.jpg`. Replaced the same day with the larger version: it reached the chat at 2000x1116 (chat compresses uploads), cropped to 1984x1116 for exact 16:9 — enough for 1080p. The true 4K original stays on the user's PC in `StillWaveZen\RONIN` for Flow and CapCut.
- **Hat:** a woven travelling kasa, closest to an ajirogasa / sandogasa type — historically plausible for a ronin on the road.
- **Overlay:** the figure stands in the lower-left, where the standard overlay would cover the swords, so the overlay sits in the **upper-left** over the dark cedars (`make_overlay.py --dy -600`).
- **Thumbnail:** `assets/ronin-2h-thumb.jpg` (`ronin-compose-thumb.py`): 浪人 in black brush on the moon, RONIN in bold white upper-left, small `SAMURAI ZEN MUSIC` under it.

**🇺🇦 RU:** Выбран вариант B (ночная дорога, луна, фонарь). Кадр заменён на версию побольше (в чат дошёл как 2000x1116, обрезан до 1984x1116 под 16:9), для 1080p хватает; настоящий 4K-оригинал лежит у пользователя в `StillWaveZen\RONIN`. Фигура стоит слева внизу, поэтому оверлей перенесён в левый верхний угол. Превью: 浪人 чёрной кистью на луне, RONIN белым слева вверху.

## §6a — Wisdom Overlay

- Line 1 (kanji): **独立独歩**
- Line 2 (romaji): *Dokuritsu doppo*
- Line 3 (gloss): Stand alone, walk your own path
- File: `assets/ronin-dokuritsu-doppo-overlay.png` (YujiBoku brush font, cream, lower-left, own scrim). Placed upper-left on the chosen frame (`--dy -600`), clear of the figure and the moon.
- CapCut: text layer on the top track, 0:03 → 0:14, fade in 2 s, fade out 2 s, no glow/box.

**🇺🇦 RU:** 独立独歩 — «стоять самому, идти своим путём»: классический четырёхзнак про самостоятельность, точно про ронина, но само слово 浪人 не называет. На выбранном кадре оверлей стоит слева вверху, не задевая фигуру и луну.

## §7 — Title

```
RONIN — Samurai Zen Music for Deep Focus & Inner Stillness (2 Hours)
```

## §8 — Description (user's draft, channel name spelling fixed; tracklist goes in after mastering)

```
A ronin is a samurai with no master. No banner, no orders, no one to report to, and nowhere left to hide from himself. What remains is the work in front of you and the breath that carries it.

Two hours of calm Japanese Zen music built on that idea: shakuhachi breath, low koto strings, soft wooden percussion. A slow, even tempo that never rises suddenly and never breaks.

Best with headphones or low speakers, one task, and no second screen.

Made for:
- deep work sessions that need to run long
- writing, studying, reading, coding
- anyone working alone who needs the room to stay quiet

[TRACKLIST — paste after mastering]

More from StillWave Zen:
Hachiman — Japanese Zen Music for Warrior Focus: https://youtu.be/jkKiSuRTmZE
Miyamoto Musashi — Samurai Meditation for Stress Relief: https://youtu.be/mJ3RMn3J4B8

If you use this to work, tell me in the comments what you are building. I read every one.

New Japanese Zen music every week. Subscribe if you want it in your feed.

#samuraizenmusic #japanesemusic #deepfocus #zenmusic #kotomusic
```

Both links verified via VidIQ on 2026-11-12 (they point to the right StillWave videos).


## §9 — Tags

```
stillwave, ronin, samurai zen music, japanese zen music, samurai meditation music, japanese music for focus, deep focus music, focus music, study music, deep work music, meditation music, zen music, ambient music, calming music, relaxing music, shakuhachi flute music, koto music, japanese meditation music, samurai music, japanese warrior music, ancient japan ambience, lone samurai under the full moon on a misty cedar forest road with a stone lantern, joe hisaishi
```

## §11 — Pinned comment

```
🌀 浪人 RONIN — a samurai with no master, only the work in front of him and the breath that carries it. 🍃 What are you working on today, alone and without distractions? Subscribe for more Japanese zen focus sessions every week 🌿
```

## §12 — Content ID claim on the published video (2026-11-14)

Claimant: Timberton Records. Six matched segments: 0:14:29–0:14:43, 0:31:33–0:31:48, 1:22:50–1:23:01, 1:39:49–1:40:03, 1:43:01–1:43:11, 1:56:51–1:57:31.

Mapped onto the 17:04.4 cycle, five of the six land on the **same spot of track `1605189`** (its own ~0:32–0:51; cycle position ~14:25–14:45). The sixth lands on `1605188` at its own ~0:55–1:05 — the sister track from the same Musicful request (chroma similarity 1.00 with 1605189). So the match is one musical phrase, repeated in every cycle; Content ID listed only some of the repeats.

The one-cycle check had come back clean, so a check on one cycle is **not** a guarantee: the final upload can still be claimed. Fix chosen: trim the claimed segments in Studio (ambient, gaps are inaudible). **Do not reuse 1605189 or 1605188** in any future album.

**🇺🇦 RU:** Заявка Timberton Records. Пять из шести совпадений — одно и то же место трека 1605189 (около 0:32–0:51), шестое — трек 1605188 из того же запроса. Это одна музыкальная фраза, повторяющаяся в каждом круге. Проверка одного круга была чистой, значит она не гарантирует, что заявки не будет на финальном видео. Решение — обрезать фрагменты в Studio. Эти два трека больше не использовать.
