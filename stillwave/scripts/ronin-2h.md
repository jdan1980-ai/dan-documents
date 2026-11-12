# RONIN — Samurai Zen Music for Deep Focus & Inner Stillness (2 Hours)

## Meta

- **Slug:** ronin-2h
- **Concept:** a ronin is a samurai with no master: no banner, no orders, only the work in front of you and the breath that carries it. Deep-focus album.
- **Playlist (add to in Studio):** Japanese Zen Music
- **Length target:** 2H, built from **8 Musicful tracks (~3:15 each) stitched into one cycle and looped to 2 hours** — the short-album format the user switched to on 2026-11-12 (see `CLAUDE.md`).
- **Status:** 📝 title + description drafted by the user, overlay built, image prompts and the Musicful music prompt written (§1, §3, §4). Waiting for: hero frame; track generation in the "dan-documents" environment.

**🇺🇦 RU:** Ронин — самурай без господина: ни знамени, ни приказов, только работа перед тобой и дыхание. Альбом для глубокой концентрации. Ждём папку с треками и кадр.

## §1 — Music (Musicful API, one prompt for the whole album)

Per the user's instruction of 2026-11-12: music comes from the **Musicful API** with the tools in `sevenlights/tools/` (`musicful_album.py`, `make_long_track.py`), the same way Seven Lights albums are built. One prompt for the whole album (similarity between tracks is intended), 1 request = 2 tracks (~3:15) = 6 units of the Starter plan shared by both channels.

- Prompt: `stillwave/scripts/ronin-musicful-prompt.txt`
- Plan: 4 requests = 8 tracks = 24 units. Check `--balance` first.
- **Must run in the cloud environment "dan-documents"** — the API key is injected there by the proxy. The session that wrote this file ran in "Default", where `api.musicful.ai` is blocked and the session could not be moved.

```bash
python sevenlights/tools/musicful_album.py --balance
python sevenlights/tools/musicful_album.py --prompt-file stillwave/scripts/ronin-musicful-prompt.txt --requests 4 --out <work>/ronin/
python sevenlights/tools/make_long_track.py --in <8 mp3> --trim-start 8 --trim-end 6 --check --out <work>/ronin_check_1cycle.wav
# one-cycle video with the hero image -> user uploads as Unlisted -> YouTube copyright check
# only after a clean check (StillWave cap is 2 hours, not 3):
python sevenlights/tools/make_long_track.py --in <8 mp3> --trim-start 8 --trim-end 6 --hours 2 --out <work>/ronin_2h.flac
```

**🇺🇦 RU:** Музыка — через Musicful API инструментами из `sevenlights/tools/`, один промт на весь альбом. 4 запроса = 8 треков = 24 единицы общего тарифа; сначала проверить остаток. Запускать только в облачной среде «dan-documents»: ключ подставляется там. Порядок: треки → один круг (`--check`) → видео с картинкой → проверка авторских прав на YouTube (ограниченный доступ) → только потом 2 часа (`--hours 2`, у StillWave кап 2 часа).

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

## §4 — Flow loop (for variant A)
```
Feed the clean hero (no text). Camera completely locked: no pan, no zoom, no dolly. Keep the ronin, his hat, cloak and swords, the path and the mountains exactly as they are, as a frozen photograph. The ronin does not move. Animate ONLY: (1) the valley mist drifting very slowly sideways, soft and continuous; (2) the pampas grass swaying gently in a light breeze; (3) the glow of the sun breathing almost imperceptibly in brightness; (4) the hem of the cloak stirring very slightly. Everything is slow and calm. Perfectly seamless 8-second loop, last frame matches first frame exactly.
```

## §6a — Wisdom Overlay

- Line 1 (kanji): **独立独歩**
- Line 2 (romaji): *Dokuritsu doppo*
- Line 3 (gloss): Stand alone, walk your own path
- File: `assets/ronin-dokuritsu-doppo-overlay.png` (YujiBoku brush font, cream, lower-left, own scrim). Built before the hero frame arrived; re-check placement on the frame.
- CapCut: text layer on the top track, 0:03 → 0:14, fade in 2 s, fade out 2 s, no glow/box.

**🇺🇦 RU:** 独立独歩 — «стоять самому, идти своим путём»: классический четырёхзнак про самостоятельность, точно про ронина, но само слово 浪人 не называет. Оверлей собран до получения кадра, расположение нужно проверить по кадру.

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
