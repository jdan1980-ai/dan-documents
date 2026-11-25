# YUKI — Samurai Meditation Music (2 Hours)

## Meta
- **Status (2026-11-25):** hero 16:9 approved (`assets/yuki-2h-source.jpg`, 2000×1124 crop); animation by Google Flow (the still has snow already flying, a code loop would freeze it — Flow moves it); thumbnail + overlay done; music: `music-bank/yuki` (11 good tracks) after the Content ID check; optional CC0 blizzard SFX bed under the music.
- **Concept:** a lone samurai in a straw kasa stands in a mountain blizzard, scarf and robe streaming in the wind, facing a snow-covered temple gate with one warm lantern under the full moon. Replaces the first (calm courtyard) frame, which the user found not clickable.
- **Playlist:** Japanese Zen Music + Samurai Meditation Music — Japanese Zen for Focus & Sleep.

## §4 — Flow loop (8 s, camera locked)
```
Animate this exact image as a calm, seamless 8-second loop. The camera is completely locked: no pan, no zoom, no dolly, no shake; the frame stays identical to the image from the first second to the last. A steady, strong winter wind blows from left to right for the WHOLE clip: fine snow drifts and streams across the entire frame at a constant pace from the first frame to the last, and thin veils of powder snow lift gently off the ground. The samurai stands perfectly still in the same place, only breathing slowly; his long scarf, the hem of his kimono, his hakama and the cords of his straw hat flutter continuously in the wind. The warm paper lantern under the temple gate flickers softly. The moon, the mountains, the gate and the pine trees stay still, only the snow on the pine branches trembles slightly. Slow, quiet, hypnotic motion, no sudden gusts. The last frame matches the first frame.
```
Check: the samurai must not walk or turn; camera still; snow from frame 1 to the end; if the seam shows, crossfade two passes (as KATANA).

## §6a — Wisdom overlay
- **雪中松柏** · *Setchū no shōhaku* · "Evergreen in the snow": the pine and cypress stay green under snow — integrity that hardship cannot change.
- File: `assets/yuki-setchu-shohaku-overlay.png`, UPPER-LEFT over the dark storm sky (`make_overlay.py --kanji-size 88 --pitch 100 --dx -40 --dy -600 --scrim 150`), text ends at x 494, clear of the hat. The lower-left is bright snow and could not hold cream text.
- CapCut: top track, 0:03 → 0:14, fade 2 s / 2 s.

**🇺🇦 RU:** «Сосна зеленеет и под снегом» — стойкость, которую не меняют трудности. Оверлей вверху слева над тёмным небом: внизу слева яркий снег.

## §5 — Thumbnail v2
`assets/yuki-compose-thumb-v2.py` → `assets/yuki-2h-thumb-v2.jpg`: series layout (雪, YUKI, rules, SAMURAI MEDITATION MUSIC) on the left over the dark sky. Known flaw: the subtitle line ends over the sword hilt; readable, but tighter than other thumbnails.
