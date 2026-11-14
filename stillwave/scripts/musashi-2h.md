# MUSASHI — 2H Japanese Zen Music (samurai meditation)

## Meta

- **Slug:** musashi-2h
- **Concept:** Miyamoto Musashi — more than sixty duels, never defeated, then he walked away and trained stillness (Reigandō cave, *The Book of Five Rings*). The album is "the mind before the strike".
- **Music:** Lyria, MP3 input. 37 raw → 1 exact duplicate dropped → **ALBUM: 32 tracks, 1:59:54** → `musashi-ALBUM`. RESERVE: 4 tracks.
- **Playlist (add to in Studio):** Japanese Zen Music
- **Overlay:** `assets/musashi-banri-ikku-overlay.png` (万理一空 / Banri ikkū / Ten thousand truths, one emptiness), 0:03–0:14.
- **Status:** 🟡 music mastered and reordered. Hero frame not yet delivered (overlay placement to re-check).

---

## §2 — Mastering and reorder

`select-album.py` could not tell the Lyria variants apart (filenames don't follow the `PREFIX_variant` pattern, so every track scored as variant 0) and left them in alphabetical order: 13 "Breath of the Bamboo" in a row, then 11 "Night Forest Meditation" in a row. The order below interleaves the three source groups (numbered 1–5 tracks, Breath of the Bamboo, Night Forest Meditation) so no two neighbours come from the same group (anti-Content-ID, and less repetition for the listener).

Timestamps are derived from the selector's start column, so they may drift by a second or two from the real file lengths.

**🇺🇦 RU:** Скрипт отбора не различил варианты (имена файлов не в формате `PREFIX_вариант`), поэтому оставил треки по алфавиту: 13 «Breath of the Bamboo» подряд, потом 11 «Night Forest Meditation». Новый порядок перемешивает три группы так, что соседние треки всегда из разных групп. Таймкоды посчитаны по колонке start, возможна погрешность в секунду-две.

### Reorder + rename script (keyed on the current full filenames; safe to re-run)

```powershell
$folder = "C:\Users\jdan1\OneDrive\Desktop\musashi-ALBUM"
$map = @{
  '09 - Breath of the Bamboo (1).wav' = '01 - The Bamboo Before Dawn.wav'
  '22 - Night Forest Meditation (1).wav' = '02 - A Night in the Old Forest.wav'
  '10 - Breath of the Bamboo (2).wav' = '03 - Wind Through the Bamboo Grove.wav'
  '23 - Night Forest Meditation (2).wav' = '04 - The Forest Holds Its Breath.wav'
  '11 - Breath of the Bamboo (3).wav' = '05 - The Swordsman Sits Down.wav'
  '24 - Night Forest Meditation (3).wav' = '06 - Moonlight on the Cedar Path.wav'
  '12 - Breath of the Bamboo (4).wav' = '07 - Bamboo Bending, Never Breaking.wav'
  '01 - 1 (1).wav' = '08 - The Mind Before the Strike.wav'
  '13 - Breath of the Bamboo (5).wav' = '09 - One Breath Among the Stalks.wav'
  '25 - Night Forest Meditation (4).wav' = '10 - Owl Hour on the Mountain.wav'
  '14 - Breath of the Bamboo (6).wav' = '11 - A Hut at the Edge of the Grove.wav'
  '02 - 1.wav' = '12 - Sixty Duels, Then Silence.wav'
  '15 - Breath of the Bamboo (7).wav' = '13 - Green Shadows, Still Mind.wav'
  '26 - Night Forest Meditation (5).wav' = '14 - The Dark Between the Trees.wav'
  '03 - 2 (1).wav' = '15 - The Way of the Empty Hand.wav'
  '16 - Breath of the Bamboo (8).wav' = '16 - The Bamboo Does Not Hurry.wav'
  '27 - Night Forest Meditation (10).wav' = '17 - A Lantern Far in the Forest.wav'
  '04 - 2.wav' = '18 - The Scroll of Earth.wav'
  '17 - Breath of the Bamboo (9).wav' = '19 - Breathing With the Grove.wav'
  '28 - Night Forest Meditation (11).wav' = '20 - Stillness of the Night Pines.wav'
  '05 - 3 (1).wav' = '21 - The Scroll of Water.wav'
  '18 - Breath of the Bamboo (10).wav' = '22 - Light Through Bamboo Leaves.wav'
  '29 - Night Forest Meditation (13).wav' = '23 - The Forest Sleeps Deeply.wav'
  '06 - 3.wav' = '24 - The Scroll of Fire.wav'
  '19 - Breath of the Bamboo (11).wav' = '25 - The Grove at Rest.wav'
  '30 - Night Forest Meditation (14).wav' = '26 - Mist Over the Night Path.wav'
  '07 - 5 (1).wav' = '27 - The Scroll of Wind.wav'
  '20 - Breath of the Bamboo (12).wav' = '28 - Where the Bamboo Grows Quiet.wav'
  '31 - Night Forest Meditation (15).wav' = '29 - The Last Hour of Night.wav'
  '08 - 5.wav' = '30 - The Scroll of the Void.wav'
  '21 - Breath of the Bamboo.wav' = '31 - A Single Leaf Settles.wav'
  '32 - Night Forest Meditation.wav' = '32 - The Cave at Reigando.wav'
}
$files = @(Get-ChildItem -LiteralPath $folder -Filter '*.wav')
foreach ($f in $files) {
  if ($map.ContainsKey($f.Name)) { Rename-Item -LiteralPath $f.FullName -NewName $map[$f.Name] }
  else { Write-Host "NOT IN LIST: $($f.Name)" }
}
Write-Host "Done."
```

---

## §8 — Description (copy-paste)

```
Japanese zen music for samurai meditation, deep focus and sleep — two hours of stillness inspired by Miyamoto Musashi.

Miyamoto Musashi fought more than sixty duels and was never defeated. Then he walked away from all of it. What he was really training, in the cave, on the mountain, in the quiet hours before dawn, was stillness. This is that stillness, written as sound.

Two hours of calm Japanese meditation music built around one idea: the mind before the strike. Soft koto, low shakuhachi, resonant rin bells and a slow, deep drone, moving at an unhurried pace with no sudden changes, so nothing pulls you out of the state you are trying to reach.

There are no battles in this music. No percussion, no rise and fall, no dramatic turn. Only a room that stays still while your breathing slows down.

0:00 The Bamboo Before Dawn
3:20 A Night in the Old Forest
7:00 Wind Through the Bamboo Grove
10:18 The Forest Holds Its Breath
13:53 The Swordsman Sits Down
17:26 Moonlight on the Cedar Path
21:26 Bamboo Bending, Never Breaking
25:01 The Mind Before the Strike
29:15 One Breath Among the Stalks
32:15 Owl Hour on the Mountain
36:03 A Hut at the Edge of the Grove
39:51 Sixty Duels, Then Silence
44:06 Green Shadows, Still Mind
48:09 The Dark Between the Trees
51:44 The Way of the Empty Hand
55:44 The Bamboo Does Not Hurry
59:24 A Lantern Far in the Forest
1:03:02 The Scroll of Earth
1:07:09 Breathing With the Grove
1:11:09 Stillness of the Night Pines
1:14:33 The Scroll of Water
1:18:47 Light Through Bamboo Leaves
1:22:44 The Forest Sleeps Deeply
1:26:28 The Scroll of Fire
1:30:13 The Grove at Rest
1:34:08 Mist Over the Night Path
1:37:52 The Scroll of Wind
1:41:35 Where the Bamboo Grows Quiet
1:45:27 The Last Hour of Night
1:48:54 The Scroll of the Void
1:53:07 A Single Leaf Settles
1:56:30 The Cave at Reigando

Listen at a comfortable, low volume. This music is designed to sit underneath your attention, not on top of it.

Subscribe for new Japanese zen music every week 🌿
https://www.youtube.com/@stillwavezen

All music and visuals on this channel are original works created for StillWave Zen. Please do not reuse or re-upload.
```
