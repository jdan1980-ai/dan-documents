# INARI — 稲荷 | Japanese Zen Music for Abundance, Gratitude & Inner Prosperity

## Meta

- **Series:** Kanji-Concept — **KAMI (神) "Gods of Japan" sub-series** — eighth entry (after TSUKUYOMI, AMATERASU, HACHIMAN, BENZAITEN, KANNON, FUJIN, RAIJIN).
- **Slug:** inari-1h
- **Concept:** 稲荷 (Inari Ōkami), one of Japan's most widely worshipped kami — deity of rice, agriculture, foxes (kitsune), industry and prosperity. Head shrine at Fushimi Inari Taisha in Kyoto, famous for its thousands of vermillion torii gates. Kitsune (foxes) are Inari's sacred messengers, often carved as stone guardian statues at Inari shrines. Theme here: **abundance and gratitude** — quiet prosperity, not loud wealth.
- **Playlist (add to in Studio):** Japanese Zen Music
- **Length target:** 1H (continues the Lyria-pilot format).
- **Production note:** 🔒 **Built outside the usual package workflow** — the user generated hero image, thumbnail, long-form animated loop, and Shorts independently this time (not via the channel's usual §1–§4 NanoBanana/Lyria/Flow prompt-drafting process). This script exists to hold the SEO pack (title, description, tags, wisdom overlay, pinned, Community Post) and the §8 tracklist once mastering is done — §0 documents the concept retroactively from the delivered assets rather than prescribing it.
- **Status:** 🟡 IN PROGRESS — ✅ hero/thumbnail/loop/Shorts already made by user, ✅ music mastered/selected (21 tracks, 58:47 → §8). **Next: rename files per §2 script, confirm Concept Short vs teaser Short (§14), CapCut laydown.**

---

## §0 — Positioning (documented retroactively from delivered assets)

- **Thumbnail** (delivered, already composited): a dramatic, colossal fire-gold kitsune spirit with red facial markings rises behind a tunnel of vermillion torii gates (Fushimi Inari's senbon torii), a lone dark-robed figure kneels in a misted rice paddy before it, a small stone Inari fox guardian statue with a red bib sits at the right edge, full moon upper-right. 稲荷 kanji vertical white upper-left, INARI white serif low-centre — already built, matches the KAMI series thumbnail treatment (white text on a warm/bright background, same lesson as AMATERASU/HACHIMAN/BENZAITEN/KANNON/FUJIN/RAIJIN).
- **The actual long-form animated scene is calmer and smaller-scale than the thumbnail's dramatic staging**: a normal-sized, softly glowing nine-tailed kitsune sits calm in a misty rice field at night; a lone silhouetted figure sits in seiza meditation in the foreground; a distant torii gate stands silhouetted directly against a huge rising moon; mist drifts low over the rice paddies. Quiet, intimate, devotional — not a colossal deity-manifestation moment like the rest of the KAMI series' hero shots. **Copy below is written to match this actual video scene** (thumbnail is allowed to be more dramatic than the content, per normal packaging practice, but the description itself stays honest to what plays).
- **Signature color:** warm fire-gold with red accents (fox's markings, torii, shrine bib) on the thumbnail; the long-form scene itself reads cooler and softer — warm amber fox-glow against a cool moonlit-blue night. Distinct from AMATERASU's dawn-amber by the night/moonlit setting and the fox-glow source (not a sunrise wash).
- **Sacred creature:** the kitsune (fox) itself — Inari's own sacred messenger — appears as the companion, calm and seated/still (not leaping), consistent with the series' "creature always resting" rule.
- **Human anchor:** a lone silhouetted figure in seated meditation (seiza), no visible detail beyond silhouette — devotional stillness rather than a named role (monk/musician/pilgrim).
- **Wisdom phrase is NOT 稲荷 itself** (overlay ≠ title concept, series rule). Chosen: **五穀豊穣** (gokoku hōjō — "abundant harvest of the five grains"), the classical shrine-blessing phrase for agricultural abundance and prosperity — directly Inari's own domain without naming him, in the same spirit as the other KAMI overlays. See §6a.
- **🇺🇦** Восьмая запись серии KAMI, но собрана по-другому: пользователь сам сделал герой-кадр, тумбу, анимированный луп и Shorts — без обычного процесса прогонки через промты §1-§4. Этот файл нужен для SEO-пакета (тайтл, описание, теги, оверлей, закреп, Community Post) и треклиста §8. Тумба — драматичная (колоссальный огненно-золотой лис за тоннелем тории), а сам ролик спокойнее — обычный светящийся лис-кицунэ рядом с медитирующей фигурой на фоне тории и полной луны в тумане рисового поля. Мудрость — 五穀豊穣 (обильный урожай пяти злаков) — прямая связь с темой Инари без называния его по имени.

---

## §2 — Mastering

**✅ Done 2026-09-23.** 29 raw tracks generated (already titled by the user's own process — no §1 prompt list this time, see Meta note), all 29 mastered cleanly. 4 tracks flagged for input clipping (`Fox Under the Moon (1)`, `Fox Under the Moon`, `Red Torii in Fog (1)`, `The Fox Watches the Fields (1)`) — mastered versions are safe per the tool's note. `select-album.py --slug INARI --cap 60` selected **21 tracks, 58:47 total** → `INARI-ALBUM/`, 8 in `INARI-RESERVE/`. Two clipped tracks (`Fox Under the Moon` #7, `Red Torii in Fog (1)` #13, `The Fox Watches the Fields (1)` #16) landed in the final selection on calmness score — swap from RESERVE if audible. Final tracklist + poetic names in §8; rename script below.

```powershell
cd "C:\Users\jdan1\OneDrive\Desktop\INARI-ALBUM"
$names = @(
  "A Bell for the Harvest",
  "The Bell Rings Once More",
  "A Fox Sits in the Moonlight",
  "Moonlight Settles on the Fox",
  "Evening Incense",
  "The Last Curl of Incense",
  "Fox Under the Moon",
  "Hushed Rice Fields",
  "The Fields Grow Quiet",
  "Lantern Field",
  "Nine Tails, One Breath",
  "One Breath, Nine Tails Still",
  "Red Torii in Fog",
  "Stone Path at Dusk",
  "The Path Remembers Dusk",
  "The Fox Watches the Fields",
  "The Gate at the Edge",
  "The Quiet Abundance",
  "Abundance Without Asking",
  "Water Over Stones",
  "Wisteria Wind"
)
Get-ChildItem -File | Sort-Object Name | ForEach-Object {
    if ($_.Name -match '^(\d{2}) - ') {
        $idx = [int]$matches[1] - 1
        Rename-Item $_.FullName -NewName "$($matches[1]) - $($names[$idx]).wav"
    }
}
```
**🇺🇦** Готово — 21 трек, 58:47, в `INARI-ALBUM/`, 8 в резерве. Часть треков с клиппингом на входе всё же попала в финал по баллу спокойствия — если на слух заметно, замени на трек из RESERVE. Названия у части треков совпадали (генератор дублировал имя) — дал вторым версиям отдельные поэтичные варианты, чтобы в треклисте не было повторов.

---

## §6a — Wisdom Overlay

- Line 1 (kanji): **五穀豊穣**
- Line 2 (romaji): *Gokoku hōjō*
- Line 3 (gloss): A bountiful harvest for all
- Cream `#F5EAD2`, Liberation Serif Bold, LEFT-lower over a calm dark zone in the scene (misty foreground rice field works well). 0:00–0:03 scene only → fade-in 2s → hold ~5s → fade-out 2s (ends 0:14).
- **🇺🇦** Мудрость: **五穀豊穣** / *Gokoku hōjō* / «Обильный урожай пяти злаков» — классическая синтоистская благословляющая формула изобилия, прямая область Инари, без называния его по имени.

---

## §7 — Title

```
INARI — 稲荷 | Japanese Zen Music for Abundance, Gratitude & Inner Prosperity
```
(`Music` well within the first 50% of chars ✅ · ≤90 ✅ · no hashtags)

**A/B:** `INARI — 稲荷 | Japanese Zen Music for Prosperity, Gratitude & Deep Calm`

---

## §8 — Description (Hikari 5-block; tracklist after mastering)

```
japanese zen music, meditation music, zen music, ambient music, calming music, relaxing music, healing music, inari, japanese god of rice and prosperity, kitsune, koto music, shakuhachi flute music, music for abundance, music for gratitude — a one-hour Japanese zen session for abundance, gratitude and quiet prosperity.

🌀 INARI (稲荷) is the quiet god of the full harvest —
not wealth that is taken,
but abundance that is given and returned.

Beneath a rising moon, a lone figure sits in silent meditation at the edge of a misted rice paddy, a fox spirit — Inari's own sacred messenger — resting calm in the grass beside a distant torii gate. Soft strings, a breathy flute, the hush of mist over still water — one hour to sit with gratitude for what is already enough.

Tracklist:
00:00 — A Bell for the Harvest
02:58 — The Bell Rings Once More
04:54 — A Fox Sits in the Moonlight
07:46 — Moonlight Settles on the Fox
10:44 — Evening Incense
13:18 — The Last Curl of Incense
16:04 — Fox Under the Moon
18:56 — Hushed Rice Fields
21:52 — The Fields Grow Quiet
24:26 — Lantern Field
27:14 — Nine Tails, One Breath
30:11 — One Breath, Nine Tails Still
32:53 — Red Torii in Fog
35:39 — Stone Path at Dusk
38:28 — The Path Remembers Dusk
41:21 — The Fox Watches the Fields
44:18 — The Gate at the Edge
47:17 — The Quiet Abundance
50:08 — Abundance Without Asking
53:01 — Water Over Stones
55:51 — Wisteria Wind

🌀 Enough is its own kind of abundance.
🍃 Sit with what has already been given.

Subscribe for more Japanese ambient meditation journeys 🌿
```

---

## §9 — Tags (verify VidIQ scores; < 450 chars)

```
stillwave, japanese zen music, meditation music, zen music, ambient music, calming music, relaxing music, healing music, inari, japanese god of prosperity, kitsune, music for abundance, music for gratitude, koto music, shakuhachi flute music, japanese meditation music, zen meditation music, a fox spirit resting beside a meditating figure in a misted rice paddy under a full moon and a distant torii gate, joe hisaishi
```

---

## §10 — Thumbnail

- **Already delivered/composited by user** — 稲荷 vertical white kanji upper-left, INARI white serif low-centre, colossal fire-gold kitsune behind a torii tunnel, kneeling figure, stone fox guardian statue, full moon. Saved as `stillwave/assets/inari-1h-thumb.jpg`.
- Note the thumbnail dramatizes the scale (colossal spirit) versus the calmer actual long-form scene (normal-sized fox) — standard, acceptable packaging practice; not a mismatch, just the cover doing its job.

---

## §11 — Pinned Comment

```
🌀 INARI (稲荷) — the quiet god of the full harvest. 🍃 What does "enough" feel like when you stop chasing more? Subscribe for more Japanese ambient meditation journeys 🌿
```

---

## §12 — Community Post (day-of)

```
INARI (稲荷) in Japanese Culture: A Concise Overview

稲荷 (Inari Ōkami) is one of Japan's most widely worshipped kami — deity of rice, agriculture, industry and prosperity, honored at more shrines than any other Shinto god. The head shrine, Fushimi Inari Taisha in Kyoto, is famous for its thousands of vermillion torii gates donated by grateful worshippers over centuries. Foxes (kitsune) are Inari's sacred messengers, and stone fox guardians stand watch at Inari shrines across the country. Here a lone figure sits in quiet meditation as a fox spirit rests nearby beneath a rising moon — a reminder that abundance is something to receive with gratitude, not chase.
```

---

## §14 — Shorts (already produced by user)

**Note:** Shorts visuals were made independently this time (not via the channel's usual §3c 10-candidate frame process). Copy pack below only — attach to whatever Shorts video already exists.

**🔒 Open question — Concept Short vs teaser only?** The channel's RELOCKED rule requires a *standalone* Concept Short (cultural-education, built from §12) in addition to any teaser Short. Confirm which one exists already so the right SEO pack below gets used (or both, if both were made).

### 📋 Shorts — copy-paste pack

**Title**
```
Inari: Japan's God of Rice, Foxes and Prosperity 🦊 #shorts
```
**A/B Title**
```
What Is Inari? The Kami of Abundance and Gratitude 🦊 #shorts
```
**Description**
```
稲荷 Inari — god of rice, prosperity and abundance, honored at more shrines than any other kami in Japan.

五穀豊穣 — a bountiful harvest for all.

Full one-hour Japanese zen session on the channel 🌿

#inari #japanese #zen #meditation #shorts
```
**Tags**
```
inari, japanese god of prosperity, kitsune, shinto deity, japanese mythology, fushimi inari, koto, zen, meditation, gratitude, stillwave
```
**Pinned comment**
```
🌀 稲荷 INARI — the quiet god of the full harvest. Full one-hour session on the channel 🌿
```

Settings: **Not for kids** · playlist **StillWave Shorts** · Related video → long-form INARI.
