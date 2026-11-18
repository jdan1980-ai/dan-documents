# MUSHIN II — Samurai Meditation Music for an Empty Mind & Deep Focus (2 Hours)

## Meta

- **Slug:** mushin-ii-2h
- **Concept:** the sequel to MUSHIN (`CamT9sohYQM`, 54% of channel views). Mushin's classic image: *a mind like still water reflecting the moon* (水月). A lone samurai sits by a still pond under a colossal full moon.
- **Playlist (add to in Studio):** Japanese Zen Music (+ "Samurai Zen Music")
- **Format:** 8 Musicful tracks (4 requests = 24 units), best 6 used, one cycle, YouTube copyright check, then 2 hours.
- **Working folder on the PC:** `Desktop\StillWaveZen\MUSHIN II\`
- **Status (2026-11-17):** VidIQ check done, frame approved (`stillwave/assets/mushin-ii-2h-source.jpg`, black bars cropped, 3840x2160), overlay placed lower-left (zone brightness 8 / 4), 2-hour track built 2026-11-18 (§2).

**🇺🇦 RU:** Продолжение MUSHIN — единственного видео канала, которое реально работает. Образ мусина — ум как тихая вода, в которой отражается луна. Одинокий самурай у неподвижного пруда под огромной луной.

## §0 — VidIQ check (2026-11-17)

| Keyword | Searches / month | Competition | Note |
|---|---|---|---|
| samurai music | 79.9K | 8 (low) | +50.9% trend — the main title keyword |
| samurai meditation music | 28.6K | 20 | second keyword |
| the unattached mind | 28.6K | — | description |
| mushin | 13K | — | concept word |
| empty mind | 9.5K | — | +66% trend — title outcome |
| samurai relaxing music | 9.4K | — | tags |
| mushin no mind | 4K | 9 | tags |
| shogun music | < 750 | — | **too small → SHOGUN postponed** |

Outliers (samurai meditation, last 6 months): the top breakout is "Samurai under the Moonlight" (YOZORA, 51 subscribers, **162x**, giant full moon + samurai silhouette). GAN (tiger mural, 5.7x), KATANA (2.7x), MUGA (2.6x) confirm the "one huge icon + lone samurai" pattern. → Hero icon for MUSHIN II = **a colossal full moon and its reflection**.

**🇺🇦 RU:** «samurai music» — 80 тыс. запросов при низкой конкуренции и рост +51%; «empty mind» растёт +66%. «shogun music» почти никто не ищет — SHOGUN откладываем. Самый сильный выброс в нише за полгода — самурай под огромной луной (162x у канала на 51 подписчика), поэтому главный образ — луна.

## §1 — Music (Musicful)

Prompt: `stillwave/scripts/mushin-ii-musicful-prompt.txt` (917 characters; quiet, no percussion, length cue).

## §2 — Album (2026-11-18)

8 tracks generated (branch `claude/mushin-ii-musicful`, 142 → 118 units). The 22-minute check video with all 8 tracks was cleared by the user. Dropped: `1621035` (F minor) and `1621040` (G minor); the other six sit in D minor / F major. Order keeps tracks from the same request apart, including across the loop point.

| # | Track | Starts in the cycle |
|---|---|---|
| 1 | 1621034 | 0:00 |
| 2 | 1621036 | 2:55 |
| 3 | 1621038 | 5:38 |
| 4 | 1621041 | 8:18 |
| 5 | 1621037 | 10:47 |
| 6 | 1621039 | 13:18 |

Cycle 15:56, 7.5 repeats, exactly 2:00:00, −15.6 LUFS, peak −1.0 dBFS. Delivered as WAV in four 30-minute parts (`MUSHIN_II_2h_part1..4.wav`), to be joined into one file before CapCut.

**🇺🇦 RU:** Убраны 1621035 (фа минор) и 1621040 (соль минор), остальные шесть в ре миноре / фа мажоре. Треки из одной пары рядом не стоят, в том числе на стыке круга. Круг 15:56, итог ровно 2 часа. Отдано WAV в 4 частях по 30 минут.

## §3 — Hero image (NanoBanana 16:9)
```
Photorealistic cinematic still, 16:9, 4K, like a frame from a Kurosawa film. Night in an old Japanese temple garden. A perfectly still black pond fills the lower half of the frame, its surface like a mirror. A colossal full moon, enormous and pale silver-white, rises above a distant line of dark pine trees and a temple roof silhouette, and the whole moon is reflected perfectly in the still water below. A lone samurai in a plain dark hakama and dark kimono kneels in seiza on a flat stone at the edge of the pond, back to camera, face never visible, placed slightly right of center, small against the moon. EXACTLY TWO sheathed swords, a katana and a shorter wakizashi, rest on the stone beside him. NO third sword. NO drawn sword. NO sword in his hands. His hands rest on his thighs. The left third of the frame is calm, dark night sky and dark water. Deep blue-black night palette with ONE strong accent: the cold silver light of the moon and its reflection. High contrast, emptiness, profound stillness. No text, no letters.
```

## §3b — Stars added to the frame (2026-11-17)

The left half was empty. A starfield (denser on the left, fading out near the moon, with a faint Milky Way band) and its reflection in the water were composited onto the approved frame by `stillwave/assets/mushin-ii-add-stars.py`. Main frame: `mushin-ii-2h-source.jpg`; the version without stars: `mushin-ii-2h-source-v1-nostars.jpg`.

**🇺🇦 RU:** Левую половину заполнили звёздным небом и его отражением в воде. Звёзды наложены скриптом на одобренный кадр, поэтому луна, самурай и мечи не изменились.

## §4 — Flow loop (8 s, camera locked) — v3, starry left half
```
Camera completely locked, no pan, no zoom, no movement of the frame. Keep the image exactly as it is, every star stays in its exact place. Subtle motion only: the stars in the night sky twinkle very softly and slowly, a few at a time; their reflections in the dark water on the left shimmer gently as slow, wide ripples pass across the pond and settle again; the moon's reflection shimmers softly as the ripples pass; a thin, low layer of silver mist drifts very slowly over the water from the left edge toward the island. The samurai stays perfectly still, the moon stays perfectly still, the swords and the stone do not move, no new objects appear. Calm, hypnotic, seamless loop: the last frame matches the first frame.
```

## §6a — Wisdom overlay

- **無念無想** · *Munen musō* · "No thought, no imagining" — the state of mushin: the mind empty of thoughts and images, like still water.
- File: `stillwave/assets/mushin-ii-munen-muso-overlay.png` (lower-left default; re-render with `--hero` once the frame is ready).
- CapCut: top track, 0:03 → 0:14, fade in 2 s / fade out 2 s.

**🇺🇦 RU:** 無念無想 — «ни мысли, ни образа»: состояние мусин, ум пустой, как тихая вода. Положение уточню по готовому кадру.
