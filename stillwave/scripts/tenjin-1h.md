# TENJIN — 天神 | Japanese Zen Music for Deep Focus, Study & Quiet Wisdom

## Meta

- **Series:** Kanji-Concept — **KAMI (神) "Gods of Japan" sub-series** — ninth entry (after TSUKUYOMI, AMATERASU, HACHIMAN, BENZAITEN, KANNON, FUJIN, RAIJIN, INARI).
- **Slug:** tenjin-1h
- **Concept:** 天神 (Tenjin) — the deified spirit of Sugawara no Michizane (845–903), a real Heian-era scholar, poet and statesman exiled on false charges and reduced to poverty and grief. After his death, decades of disasters in Kyoto were blamed on his vengeful spirit, and he was enshrined and pacified as Tenjin — over time settling into his enduring role as the god of scholarship, learning, and calligraphy. Today students across Japan visit Tenmangu shrines (Dazaifu Tenmangu, Kitano Tenmangu) to pray for exam success. Theme here: **quiet devotion to study and the long patience of learning**, not exam-day anxiety.
- **Playlist (add to in Studio):** Japanese Zen Music
- **Length target:** 1H (continues the KAMI 1H format).
- **Production note:** 🔒 **Built outside the usual package workflow** — the user generated the hero image independently (not via the channel's usual §3 NanoBanana prompt-drafting process). This script holds the SEO pack (title, description, tags, wisdom overlay, pinned, Community Post) and the §2/§8 tracklist — §0 documents the concept and visuals retroactively from the delivered hero image, same pattern as `inari-1h.md`.
- **Status:** 🟡 IN PROGRESS — ✅ hero image delivered, ✅ thumbnail composited, ✅ wisdom overlay built, ✅ music mastered (22 tracks, 1:00:37 → §8). **Next: rename files per §2 script, generate Flow loop + Shorts frames (not yet produced), CapCut laydown.**

---

## §0 — Positioning (documented retroactively from delivered hero image)

- **Hero image** (delivered by user, `tenjin-1h-source.jpg`): a luminous white-and-gold spirit of a Heian-court scholar — hair tied in a topknot with a kanzashi pin, seated cross-legged in glowing white robes — manifests in the misty air above a temple courtyard at dusk, holding a writing brush poised over an open book resting on his lap. Glowing white plum blossoms (ume) bloom on branches framing him on both sides, some blossoms themselves lit from within like small lanterns. Below, a lone dark-robed figure sits in seiza on a wooden veranda facing the courtyard — a stone pagoda lantern, garden lanterns, and a bare flowering plum tree stand in the misted courtyard between the figure and the spirit above.
- **Signature colour:** luminous white/gold — distinct from AMATERASU's warm dawn-amber and RAIJIN's violet by its cool, paper-white glow (ink-and-moonlight, not sunrise or storm).
- **Signature motif:** glowing plum blossoms (ume), standing in for the usual "sacred creature" — the ume is Tenjin's own iconographic flower, tied to a real poem Michizane wrote to a beloved plum tree before his exile ("When the east wind blows, send me your fragrance, plum blossoms — do not forget spring, even without your master"). Note for future Shorts/detail frames: Tenjin's traditional animal is the reclining ox (his funeral ox reportedly refused to move, marking his burial site — stone oxen recline at Tenmangu shrines today) — available as a detail-shot option if a companion creature is wanted later, but the delivered hero image centers plum blossoms instead.
- **Human anchor:** a lone figure in dark robes seated in seiza on a temple veranda, back to camera, face never visible, per series convention.
- **Wisdom phrase is NOT 天神 itself** (overlay ≠ title concept, series rule). Chosen: **温故知新** (onko chishin — "study the old to understand the new"), a classical scholarly idiom describing the pursuit of knowledge through studying the past — directly Tenjin's own domain without naming him. See §6a.
- **🇺🇦** Девятая запись серии KAMI, собрана иначе — пользователь сам сгенерировал герой-кадр, без обычного прогона через промт §3. Файл нужен для SEO-пакета и треклиста. Тэндзин — обожествлённый Сугавара-но Митидзанэ, учёный и поэт эпохи Хэйан, несправедливо сосланный; после смерти стал богом учёности и каллиграфии. Сигнатурный цвет — светящийся бело-золотой; вместо священного животного — светящиеся цветы сливы (уме), собственный поэтический символ Митидзанэ. Мудрость — 温故知新 (изучай старое, чтобы понять новое).

---

## §2 — Mastering

**✅ Done 2026-09-29.** 41 raw tracks generated (already titled by the user's own process — no §1 prompt list this time, see Meta note). `master-album.py` flagged 9 tracks for input clipping and 1 exact duplicate (`Bamboo Drift (8)` == `Bamboo Drift (7)`, dropped). `select-album.py --slug TENJIN --cap 60 --min-length 2.5` (the `--min-length` filter was added to the tool this session, to drop three short outlier tracks under 2:30 — `Bamboo Breath (1)` 1:56, `Bamboo Drift (3)` 2:18, `Quiet Pulse` 2:19) selected 21 tracks, 57:58 total. **User manually appended `Silk Echo.wav` (2:39) as track 22 from RESERVE, rounding the album to 1:00:37** — same "add one more from reserve to round out the hour" pattern as RAIJIN. Final tracklist + poetic names in §8; rename script below.

```powershell
cd "C:\Users\jdan1\OneDrive\Desktop\TENJIN-ALBUM"

$titles = @(
  "The Old Scholar's Breath", "Wind Through the Sutra Hall", "Plum Blossom Hush",
  "Ink Not Yet Dry", "The Brush Rests", "A Single Page Turns",
  "Lantern Over the Sutra", "Echo of the Study Hall", "Moonlight on the Inkstone",
  "The Scholar's Reverie", "A Bell Beyond the Grove", "Mist Over the Shrine Steps",
  "Kyoto at First Light", "The Quiet Between Words", "Silk Sleeves, Still Hands",
  "The Weight of a Single Word", "Robes at Rest", "The Last Candle of Study",
  "A Thought Takes Root", "Stillness Before Dawn", "What the Old Books Remember",
  "An Echo Before Sleep"
)

Get-ChildItem -Filter "*.wav" | ForEach-Object {
    if ($_.Name -match '^(\d{2}) - ') {
        $n = [int]$matches[1]
        $newName = "{0:D2} - {1}.wav" -f $n, $titles[$n - 1]
        Rename-Item $_.FullName $newName
        Write-Host "$($_.Name)  ->  $newName"
    }
}
```
**🇺🇦** Готово — 22 трека (добавлен Silk Echo вручную из резерва), 1:00:37, в `TENJIN-ALBUM/`. Если файл `Silk Echo.wav` ещё не переименован в `22 - Silk Echo.wav` (с префиксом номера), переименуй его вручную перед запуском скрипта, иначе он не попадёт под regex.

---

## §6a — Wisdom Overlay

- Line 1 (kanji): **温故知新**
- Line 2 (romaji): *Onko chishin*
- Line 3 (gloss): Study the old to understand the new
- Cream `#F5EAD2`, Liberation Serif Bold, LEFT-lower over the dark temple silhouette (measured mean brightness ~35 vs ~78 for the full frame). 0:00–0:03 scene only → fade-in 2s → hold ~5s → fade-out 2s (ends 0:14).
- **🇺🇦** Мудрость: **温故知新** / *Onko chishin* / «Изучай старое, чтобы понять новое» — классическая идиома об учёности, прямая область Тэндзина, без называния его по имени. Оверлей уже собран (`tenjin-onkochishin-overlay.png`).

---

## §7 — Title

```
TENJIN — 天神 | Japanese Zen Music for Deep Focus, Study & Quiet Wisdom
```
(`Music` well within the first 50% of chars ✅ · ≤90 ✅ · no hashtags)

**A/B:** `TENJIN — 天神 | Japanese Zen Music for Focus, Clarity & the Scholar's Mind`

---

## §8 — Description (Hikari 5-block)

```
japanese zen music, meditation music, zen music, focus music, study music, deep focus music, ambient music, calming music, relaxing music, tenjin, japanese god of scholarship, plum blossoms, koto music, shakuhachi flute music, music for studying, music for deep focus — a one-hour Japanese zen session for quiet study, deep focus, and the patience of learning.

🌀 TENJIN (天神) is the god of scholars —
not sudden brilliance,
but the long, quiet devotion of study.

Beneath a temple's plum trees, in bloom even in mist, a scholar's spirit sits with brush in hand above a lone figure seated in evening stillness. Breathy flute, sparse koto, the hush of an old study hall at dusk — one hour to sit with a single page a little longer, and let understanding come slowly.

Tracklist:
00:00 — The Old Scholar's Breath
02:49 — Wind Through the Sutra Hall
05:41 — Plum Blossom Hush
08:19 — Ink Not Yet Dry
11:00 — The Brush Rests
13:33 — A Single Page Turns
16:24 — Lantern Over the Sutra
19:15 — Echo of the Study Hall
21:48 — Moonlight on the Inkstone
24:36 — The Scholar's Reverie
27:27 — A Bell Beyond the Grove
30:11 — Mist Over the Shrine Steps
32:49 — Kyoto at First Light
35:36 — The Quiet Between Words
38:27 — Silk Sleeves, Still Hands
41:19 — The Weight of a Single Word
43:56 — Robes at Rest
46:36 — The Last Candle of Study
49:24 — A Thought Takes Root
52:19 — Stillness Before Dawn
55:06 — What the Old Books Remember
57:58 — An Echo Before Sleep

🌀 Study the old to understand the new.
🍃 Let one page be enough for tonight.

Subscribe for more Japanese ambient meditation journeys 🌿
```

---

## §9 — Tags (verify VidIQ scores; < 450 chars)

```
stillwave, japanese zen music, meditation music, zen music, focus music, study music, deep focus music, ambient music, calming music, relaxing music, tenjin, japanese god of scholarship, plum blossoms, koto music, shakuhachi flute music, japanese meditation music, zen meditation music, music for studying, a scholar spirit with a writing brush above glowing plum blossoms over a temple courtyard at dusk, joe hisaishi
```

---

## §10 — Thumbnail

- **Composited:** 天神 vertical white kanji upper-left (over the dark temple-roof silhouette), TENJIN white serif low-centre (over the dark courtyard stone beneath the seated figure) — same white-on-bright-background treatment as AMATERASU/HACHIMAN/BENZAITEN/KANNON/FUJIN/RAIJIN/INARI. Built via `tenjin-compose-thumb.py`, saved as `stillwave/assets/tenjin-1h-thumb.jpg`.

---

## §11 — Pinned Comment

```
🌀 天神 TENJIN — the god of scholars, and the long quiet patience of study. 🍃 What's one page you could sit with a little longer tonight? Subscribe for more Japanese ambient meditation journeys 🌿
```

---

## §12 — Community Post (day-of)

```
TENJIN (天神) in Japanese Culture: A Concise Overview

天神 (Tenjin) is the deified spirit of Sugawara no Michizane, a real Heian-era scholar, poet and statesman exiled on false charges in 901 CE. After a string of disasters struck Kyoto in the following decades, his aggrieved spirit was blamed — and pacified through enshrinement, eventually settling into his enduring role as the god of scholarship, learning, and calligraphy. Today students across Japan visit Tenmangu shrines, most famously Dazaifu Tenmangu and Kitano Tenmangu, to pray for exam success, leaving wooden ema plaques inscribed with their wishes. Plum blossoms (ume) are Tenjin's own flower, tied to a poem Michizane wrote to a beloved tree before his exile, asking it not to forget spring even without its master. Here his spirit appears above a temple courtyard in bloom, brush in hand, watching over a lone figure seated in quiet study.
```

---

## §14 — Shorts (not yet produced)

Teaser and Concept Short have not been generated for TENJIN yet. Once frames or a video exist, build both packs per the standard rules (§3c 10-candidate process if generating fresh frames, or a copy-paste pack matched to whatever the user delivers — same pattern as INARI's §14).

**🇺🇦** Shorts (тизер и обучающий Concept Short) для TENJIN ещё не сделаны. Когда появятся кадры или готовое видео — соберу оба пакета по стандартным правилам.
