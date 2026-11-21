# ZAZEN — 2H Japanese Zen Music (Kanji-Concept series)

**Format:** full album, 2H cap (locked). Long-form only for this step — Shorts package (teaser + Concept Short) is still pending, see §14.
**Overlay:** `assets/zazen-shikantaza-overlay.png` (只管打坐 / Shikan taza / Just sitting, nothing else)
**Hero image (also thumbnail base):** `assets/zazen-2h-source.jpg`
**Playlist (add to in Studio):** Japanese Zen Music
**Upload:** Not for kids · Scheduled first · Related video = none yet (set when the Shorts exist)

---

## §0 Concept

**EN:** ZAZEN (坐禅) — "sitting meditation." Dōgen's shikantaza ("just sitting, nothing else") is the core of the practice: no goal, no insight to chase. The hero frame shows exactly that: a monk kneeling at dawn in front of a colossal white Buddha in the clouds. The music stays flat and unchanging from first second to last, because a meditation that builds is no longer a meditation.

**🇺🇦 RU:** ZAZEN (坐禅) — «сидячая медитация». Ядро практики — сикантаза Дōгэна («только сидеть, ничего больше»): без цели и без инсайта, который нужно поймать. Кадр показывает ровно это: монах на коленях на рассвете перед гигантским белым Буддой в облаках. Музыка остаётся ровной от первой до последней секунды: медитация, которая нарастает, перестаёт быть медитацией.

---

## §6a Wisdom Overlay

- **Phrase:** 只管打坐 / Shikan taza / Just sitting, nothing else
- **File:** `assets/zazen-shikantaza-overlay.png` (transparent, 1920x1080)
- **CapCut:** TEXT layer on the top track, start 0:03, end 0:14, fade-in 2s, fade-out 2s, no glow / shadow / box. Cream #F5EAD2, Liberation Serif Bold.

**🇺🇦 RU:** Прозрачный PNG кладётся текстовым слоем на верхнюю дорожку, старт 0:03, конец 0:14, fade-in и fade-out по 2 с, без свечения, тени и подложки.

---

## §2 Mastering (done)

- `master-album.py`: 49 raw tracks → `ZAZEN-mastered` (target -16 LUFS, TP -1.5 dB, 48 kHz / 24-bit)
- `select-album.py --cap 120 --min-length 2.5`:
  - **ALBUM: 42 tracks, 1:57:56** → `zazen-ALBUM`
  - **RESERVE (Vol. 2): 3 tracks** → `zazen-RESERVE` (`Dawn Biwa Silence`, `Misty Mountain Exhale`, `Evolving Zen Zazen Meditation`)
  - Dropped by `--min-length`: `First Light Focus` (0:55), `Morning Clarity` (1:03), `Sho in Morning Fog` (2:22)
  - Not placed (calmness measurement failed): `Zenith Rin Meditation 35 BPM` — copy manually to RESERVE if you want to keep it
- Clipping warnings on `Evolving Zen Zazen Meditation` and `Misty Mountain Exhale` — both are in RESERVE, not in the album. Regenerate them in Suno if you ever use them.

**🇺🇦 RU:** В альбом 42 трека (1:57:56), в RESERVE — 3. Два трека с клипингом (`Evolving…`, `Misty…`) ушли в RESERVE, в альбом не попали. `Zenith Rin Meditation 35 BPM` не попал никуда из-за ошибки измерения, его можно добавить в RESERVE вручную.

---

## §8 Tracklist — poetic names (copy-paste)

Raw filename → poetic name, in album order. Numeric prefix stays (CapCut sorts by filename).

```
01 - The Breath Before the Biwa
02 - Breath in the Temple Hall
03 - A Long Exhale in the Cedar Hall
04 - Biwa Notes Dissolving Into Air
05 - No Mind, Nothing Held
06 - Counting the Breaths Without Counting
07 - One Breath, Then Another
08 - Dissolving Into Stillness
09 - Still Dissolving, Still Here
10 - The Reflection of Endless Breath
11 - Endless Bell Over the Valley
12 - Silence Beneath the Temple Bell
13 - A Temple Bell at the Edge of Sleep
14 - Zen Stillness, Without End
15 - First Light, One Exhale
16 - Three Minutes Sitting in First Light
17 - First Light, Sitting Still
18 - The Silence That Comes at Dawn
19 - Grounded in the Dawn Reflection
20 - The First Light Exhale, Grounded
21 - Hollow Quietude Settles In
22 - Hollow Silence, Breath by Breath
23 - Cathedral of Bells
24 - Morning Fog Settling Over the Hills
25 - Nothing Left to Do
26 - Returning With the Bell's Echo
27 - Returning Without Judgment
28 - Serene Dawn, Seated
29 - Settling Into the Slow Hours
30 - Settling Into the Cushion
31 - The Silent Peak Reflects
32 - Stillness Holding Its Breath
33 - Zenith Meditation Over Sleeping Peaks
34 - Breath Decaying Into the Temple
35 - Temple Dawn Opening Slowly
36 - Bell Meditation at Temple Dawn
37 - Three Minutes of Clear Zen
38 - Vast Stillness, Low Bell
39 - Weightless Fog and Slow Decay
40 - Zazen, Stillness and Breath
41 - Zen Temple at Dawn
42 - Zenith Exhale Into the Valley
```

### PowerShell rename script (run once, in the `zazen-ALBUM` folder's parent)

Save as `rename-zazen.ps1` next to the album folder, or paste into PowerShell. Matches on the numeric prefix, so it is safe to re-run.

```powershell
$folder = "C:\Users\jdan1\OneDrive\Desktop\zazen-ALBUM"
$names = @{
  '01' = 'The Breath Before the Biwa'
  '02' = 'Breath in the Temple Hall'
  '03' = 'A Long Exhale in the Cedar Hall'
  '04' = 'Biwa Notes Dissolving Into Air'
  '05' = 'No Mind, Nothing Held'
  '06' = 'Counting the Breaths Without Counting'
  '07' = 'One Breath, Then Another'
  '08' = 'Dissolving Into Stillness'
  '09' = 'Still Dissolving, Still Here'
  '10' = 'The Reflection of Endless Breath'
  '11' = 'Endless Bell Over the Valley'
  '12' = 'Silence Beneath the Temple Bell'
  '13' = 'A Temple Bell at the Edge of Sleep'
  '14' = 'Zen Stillness, Without End'
  '15' = 'First Light, One Exhale'
  '16' = 'Three Minutes Sitting in First Light'
  '17' = 'First Light, Sitting Still'
  '18' = 'The Silence That Comes at Dawn'
  '19' = 'Grounded in the Dawn Reflection'
  '20' = 'The First Light Exhale, Grounded'
  '21' = 'Hollow Quietude Settles In'
  '22' = 'Hollow Silence, Breath by Breath'
  '23' = 'Cathedral of Bells'
  '24' = 'Morning Fog Settling Over the Hills'
  '25' = 'Nothing Left to Do'
  '26' = 'Returning With the Bell''s Echo'
  '27' = 'Returning Without Judgment'
  '28' = 'Serene Dawn, Seated'
  '29' = 'Settling Into the Slow Hours'
  '30' = 'Settling Into the Cushion'
  '31' = 'The Silent Peak Reflects'
  '32' = 'Stillness Holding Its Breath'
  '33' = 'Zenith Meditation Over Sleeping Peaks'
  '34' = 'Breath Decaying Into the Temple'
  '35' = 'Temple Dawn Opening Slowly'
  '36' = 'Bell Meditation at Temple Dawn'
  '37' = 'Three Minutes of Clear Zen'
  '38' = 'Vast Stillness, Low Bell'
  '39' = 'Weightless Fog and Slow Decay'
  '40' = 'Zazen, Stillness and Breath'
  '41' = 'Zen Temple at Dawn'
  '42' = 'Zenith Exhale Into the Valley'
}
Get-ChildItem -LiteralPath $folder -Filter '*.wav' | ForEach-Object {
  if ($_.Name -match '^(\d{2}) - ') {
    $n = $Matches[1]
    Rename-Item -LiteralPath $_.FullName -NewName ("$n - " + $names[$n] + ".wav")
  }
}
Write-Host "Done."
```

**🇺🇦 RU:** Скрипт переименовывает файлы по числовому префиксу (`01 - …`), так что его можно запускать повторно. Сохрани как `rename-zazen.ps1` или вставь в PowerShell.

---

## §8a Description (copy-paste, English only)

Title, A/B, description, tags, pinned comment and Community Post are each in their own block, one field per block.

### Title

```
ZAZEN — 坐禅 | Japanese Zen Music for Stillness & Focus
```

### A/B Title

```
ZAZEN — 坐禅 | Japanese Zen Music for Sitting Meditation & Inner Calm
```

### Description

```
zazen meditation, zen music, japanese zen music, shikantaza, sitting meditation, biwa music, temple bell music, meditation music, focus music, stillness, a monk sitting in silence at dawn.

🌀 ZAZEN means "sitting meditation."
Sit with nothing to achieve,
and the sitting itself becomes the practice.

Dawn breaks over a misted valley. A monk kneels on a dark wooden floor, facing a colossal white Buddha rising out of the clouds, while incense curls in the still air beside him. Somewhere below, a temple bell rings once and fades. The breath comes in and goes out, and nothing else is asked of you.

0:00 The Breath Before the Biwa
2:49 Breath in the Temple Hall
5:24 A Long Exhale in the Cedar Hall
8:22 Biwa Notes Dissolving Into Air
11:18 No Mind, Nothing Held
13:57 Counting the Breaths Without Counting
16:53 One Breath, Then Another
19:33 Dissolving Into Stillness
22:19 Still Dissolving, Still Here
25:07 The Reflection of Endless Breath
27:48 Endless Bell Over the Valley
30:31 Silence Beneath the Temple Bell
33:26 A Temple Bell at the Edge of Sleep
36:20 Zen Stillness, Without End
39:13 First Light, One Exhale
42:06 Three Minutes Sitting in First Light
44:59 First Light, Sitting Still
47:35 The Silence That Comes at Dawn
50:25 Grounded in the Dawn Reflection
53:23 The First Light Exhale, Grounded
56:19 Hollow Quietude Settles In
59:10 Hollow Silence, Breath by Breath
1:01:43 Cathedral of Bells
1:04:35 Morning Fog Settling Over the Hills
1:07:09 Nothing Left to Do
1:09:39 Returning With the Bell's Echo
1:12:31 Returning Without Judgment
1:15:24 Serene Dawn, Seated
1:18:15 Settling Into the Slow Hours
1:21:14 Settling Into the Cushion
1:23:58 The Silent Peak Reflects
1:26:49 Stillness Holding Its Breath
1:29:35 Zenith Meditation Over Sleeping Peaks
1:32:21 Breath Decaying Into the Temple
1:35:11 Temple Dawn Opening Slowly
1:37:59 Bell Meditation at Temple Dawn
1:40:57 Three Minutes of Clear Zen
1:43:44 Vast Stillness, Low Bell
1:46:39 Weightless Fog and Slow Decay
1:49:40 Zazen, Stillness and Breath
1:52:20 Zen Temple at Dawn
1:55:08 Zenith Exhale Into the Valley

🌀 Let the breath lead. Let thoughts pass like mist.
🍃 Nothing to do. Nowhere to be.

Subscribe for more Japanese zen meditation journeys 🌿
```

### Tags

```
stillwave, zen music, japanese zen music, zazen meditation, shikantaza, sitting meditation, meditation music, focus music, study music, sleep music, deep focus music, zen meditation music, biwa music, temple bell music, japanese meditation music, peaceful ambiance, serene ambience, evening relaxation, buddhist monk meditating at dawn temple with giant buddha in mist, joe hisaishi
```

### Pinned comment

```
Two hours, nothing to achieve. If this helped you slow down, tell me where you're listening from. 🌿
```

### Community Post (publish day-of or day-before, 4–6h before the long-form)

```
ZAZEN (坐禅) in Japanese Culture: A Concise Overview

Zazen (坐禅) means "sitting meditation": 坐 is to sit, and 禅 comes from the Sanskrit dhyāna, meditative absorption. In Japanese Zen, especially the Sōtō school taught by Dōgen in the 13th century, zazen is practiced without a goal. Dōgen called it shikantaza, "just sitting, nothing else": no insight to chase, no calm to achieve, only posture, breath, and attention, with whatever arises allowed to pass. For centuries monks have sat this way at dawn in mountain temples, facing the light with nothing to do. What remains when there is nothing left to do?
```

---

## §14 Shorts (pending — not built yet)

Still to produce, per the locked Shorts rules:
- **Teaser Short** (cross-promo to the long-form) — 9:16 frames, 3 beats (hook + kanji + wisdom line)
- **Concept Short** (standalone teaching Short) — 5–6 full-sentence captions built from the Community Post text above, via `concept-shorts-build.py`
- **Shorts image set** — 10 candidate 9:16 prompts; the user picks 6

**🇺🇦 RU:** Shorts ещё не сделаны: тизер, отдельный обучающий Concept Short (5–6 полных фраз из текста Community Post) и 10 кандидатов-кадров 9:16. Делаю после того, как подтвердишь альбом и название.

---

## §15 Thumbnail (pending — concept only)

**Concept:** the hero image is the thumbnail base. Kanji-Concept layout: 坐禅 large in sumi-ink brush, upper-center, over the misted sky; ZAZEN in cream #F5EAD2 Liberation Serif Bold, low, on the floor beneath the monk. Build with a compose script cloned from `muga-compose-thumb.py`.

**🇺🇦 RU:** Превью: 坐禅 крупно тушью вверху по центру, ZAZEN кремовым внизу под монахом. Собирается скриптом по образцу `muga-compose-thumb.py`. Пока только концепт, сам файл не сделан.
