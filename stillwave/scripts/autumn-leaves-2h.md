# Autumn Leaves Falling — 2H Japanese Zen Music for Deep Sleep

## Meta

- **Slug:** autumn-leaves-2h
- **Working title (user):** Autumn Leaves Falling | 2 Hours of Calm Japanese Zen Music for Deep Sleep
- **Suggested title (puts `Music` in the first half, per the Topic-Categorization rule):** `Japanese Zen Music for Deep Sleep — Autumn Leaves Falling | 2 Hours of Calm`
- **Music:** Lyria, MP3 input. 32 raw → 1 exact duplicate dropped (`11.mp3`) → 31 tracks, 1:51:58. Topped up with 2 unused tracks from `musashi-RESERVE` (`Night Forest Meditation (7)`, `(12)`) → **33 tracks, ~1:59:08**.
- **Overlay:** `assets/autumn-leaves-ichiyo-chishu-overlay.png` (一葉知秋 / Ichiyō chishū / One falling leaf tells of autumn), checked on the delivered frame: kanji sit over the lantern pedestal, lantern windows stay clear.
- **Frame:** `assets/autumn-leaves-2h-thumb-source.jpg` is the thumbnail with baked-in text; the video needs the clean frame.
- **Lantern flicker:** CapCut overlay of a CC0 candle-flame clip in Screen blend, masked to the lantern windows (see chat 2026-11-04).

## §2 — Order and rename

The selector saw every track as variant 0 and kept them alphabetical, so takes of the same number (`1 (1)`, `1`, ...) sat next to each other. The new order plays all `(1)` takes first, then the plain takes, with the two Musashi reserve tracks placed at #11 and #24. No two neighbours share a number. Timestamps come from the selector's start column plus the Musashi tracks' rounded lengths, so they can drift by a few seconds.

**🇺🇦 RU:** Скрипт отбора не различил варианты и поставил дубли одного номера подряд. Новый порядок: сначала все `(1)`, потом остальные, два трека из запаса Musashi стоят на №11 и №24. Таймкоды могут уходить на несколько секунд.

**Before running:** copy `Night Forest Meditation (7).wav` and `Night Forest Meditation (12).wav` from `musashi-RESERVE` into `autumn-leaves-ALBUM`.

```powershell
$folder = "C:\Users\jdan1\OneDrive\Desktop\autumn-leaves-ALBUM"
$map = @{
  '01 - 1 (1).wav' = '01 - Red Maple Over Still Water.wav'
  '03 - 2 (1).wav' = '02 - The First Leaf Lets Go.wav'
  '05 - 3 (1).wav' = '03 - Moonlight on the Temple Roof.wav'
  '07 - 4 (1).wav' = '04 - A Lantern Warm in the Mist.wav'
  '09 - 5 (1).wav' = '05 - Leaves Drifting Toward the Pond.wav'
  '11 - 6 (1).wav' = '06 - The Garden After Dusk.wav'
  '13 - 7 (1).wav' = '07 - Crimson Shadows, Quiet Stones.wav'
  '15 - 8 (1).wav' = '08 - A Slow Autumn Breath.wav'
  '17 - 9 (1).wav' = '09 - The Moon Above the Maples.wav'
  '19 - 10 (1).wav' = '10 - Mist Rising From the Water.wav'
  'Night Forest Meditation (7).wav' = '11 - Night Forest, Falling Leaves.wav'
  '21 - 11 (1).wav' = '12 - Embers of the Season.wav'
  '22 - 12 (1).wav' = '13 - The Pond Holds the Moon.wav'
  '24 - 13 (1).wav' = '14 - Soft Footsteps on Fallen Leaves.wav'
  '26 - 14 (1).wav' = '15 - A Cool Wind Through the Pines.wav'
  '28 - 15 (1).wav' = '16 - The Lantern Keeps Its Flame.wav'
  '30 - 16 (1).wav' = '17 - Golden Leaves on Dark Water.wav'
  '02 - 1.wav' = '18 - The Temple Sleeps.wav'
  '04 - 2.wav' = '19 - Where the Maple Leaves Rest.wav'
  '06 - 3.wav' = '20 - A Season Letting Go.wav'
  '08 - 4.wav' = '21 - Quiet Hours Before Frost.wav'
  '10 - 5.wav' = '22 - Red Leaves, Silver Mist.wav'
  '12 - 6.wav' = '23 - The Night Garden Breathes.wav'
  'Night Forest Meditation (12).wav' = '24 - One Leaf on the Surface.wav'
  '14 - 7.wav' = '25 - The Old Stone Lantern.wav'
  '16 - 8.wav' = '26 - Autumn Moon, Empty Sky.wav'
  '18 - 9.wav' = '27 - Ripples Under the Maples.wav'
  '20 - 10.wav' = '28 - The Forest Turns to Gold.wav'
  '23 - 12.wav' = '29 - Drifting Into Sleep.wav'
  '25 - 13.wav' = '30 - The Last Leaves of the Year.wav'
  '27 - 14.wav' = '31 - A Long Autumn Night.wav'
  '29 - 15.wav' = '32 - Moonlight Fading Into Mist.wav'
  '31 - 16.wav' = '33 - Only the Quiet Remains.wav'
}
$files = @(Get-ChildItem -LiteralPath $folder -Filter '*.wav')
foreach ($f in $files) {
  if ($map.ContainsKey($f.Name)) { Rename-Item -LiteralPath $f.FullName -NewName $map[$f.Name] }
  else { Write-Host "NOT IN LIST: $($f.Name)" }
}
Write-Host "Done."
```

## §8 — Tracklist

```
0:00 Red Maple Over Still Water
3:14 The First Leaf Lets Go
6:10 Moonlight on the Temple Roof
9:34 A Lantern Warm in the Mist
13:51 Leaves Drifting Toward the Pond
17:26 The Garden After Dusk
20:51 Crimson Shadows, Quiet Stones
24:13 A Slow Autumn Breath
27:56 The Moon Above the Maples
31:36 Mist Rising From the Water
35:25 Night Forest, Falling Leaves
39:08 Embers of the Season
42:17 The Pond Holds the Moon
45:50 Soft Footsteps on Fallen Leaves
49:54 A Cool Wind Through the Pines
53:44 The Lantern Keeps Its Flame
57:21 Golden Leaves on Dark Water
1:01:28 The Temple Sleeps
1:04:32 Where the Maple Leaves Rest
1:07:41 A Season Letting Go
1:11:07 Quiet Hours Before Frost
1:14:46 Red Leaves, Silver Mist
1:18:52 The Night Garden Breathes
1:22:36 One Leaf on the Surface
1:26:03 The Old Stone Lantern
1:29:30 Autumn Moon, Empty Sky
1:33:00 Ripples Under the Maples
1:36:40 The Forest Turns to Gold
1:40:21 Drifting Into Sleep
1:44:06 The Last Leaves of the Year
1:47:20 A Long Autumn Night
1:51:19 Moonlight Fading Into Mist
1:54:48 Only the Quiet Remains
```
