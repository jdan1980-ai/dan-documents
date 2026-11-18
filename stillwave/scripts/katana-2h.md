# KATANA — Samurai Meditation Music (2 Hours)

## Meta

- **Slug:** katana-2h
- **Concept:** the katana not as a weapon in a fight but as the samurai's soul (刀は武士の魂): a bare blade at rest, honoured in silence.
- **Why now (VidIQ data already collected 2026-11-17):** Zen Samurai Meditations released "KATANA — 刀" two weeks earlier: 7.2K views, 2.7x breakout, still ~5 views/hour. SHOGUN postponed ("shogun music" < 750 searches/month).
- **Playlist (add to in Studio):** Japanese Zen Music
- **Order:** MUSHIN II → KATANA → SHOGUN.
- **Rule exception (user decision 2026-11-18):** for this video the katana IS shown unsheathed. It is never held, never raised, never in a fighting pose: the bare blade rests on its own, the samurai kneels with empty hands.

**🇺🇦 RU:** Катана не как оружие в бою, а как душа самурая: обнажённый клинок в покое, перед которым сидят в тишине. По решению пользователя в этом видео клинок обнажён, но его никто не держит и не поднимает.

## §3 — Hero image (NanoBanana 16:9), two variants

### Variant A — the colossal blade (big-icon pattern, recommended)
```
Photorealistic cinematic still, 16:9, 4K, like a frame from a Kurosawa film. A colossal ancient Japanese katana, unsheathed, its bare steel blade many times taller than a man, stands upright, driven point-first into a flat rock at the top of a misty mountain ridge at dawn, like an ancient monument. The long, gently curved blade shows a clear wavy temper line (hamon) and a mirror polish; the dark silk-wrapped handle and round iron guard rise high above. The first golden light of sunrise catches the cutting edge in one bright line. At the foot of the rock, small against the blade, a lone samurai in a plain dark hakama and dark kimono kneels in seiza, back to camera, face never visible, his empty hands resting on his thighs. He carries no sword of his own. Below and behind, a sea of clouds fills the valleys and distant mountain ridges fade into mist. The left third of the frame is calm, open sky and soft mist. Deep blue-grey palette with ONE strong accent: the golden light on the steel. High contrast, reverence, profound stillness. No text, no letters.
```

### Variant B — the blade on the stand, inside the temple
```
Photorealistic cinematic still, 16:9, 4K, like a frame from a Kurosawa film. Night inside an old wooden Japanese temple hall. In the foreground, large in the frame, a single unsheathed katana rests horizontally on a low black-lacquered sword stand on a raised wooden altar; its black lacquered scabbard lies beside it on the stand. The bare steel blade shows a clear wavy temper line (hamon) and a mirror polish. One narrow beam of cold moonlight falls through a high window and runs exactly along the length of the blade, making the edge glow. Behind the stand, further back and smaller, a lone samurai in a plain dark hakama and dark kimono kneels in seiza facing the blade, face in shadow and turned slightly down, his empty hands resting on his thighs. Dark wooden pillars, a faint wisp of incense smoke rising straight up from a small bowl on the altar. The left third of the frame is calm, dark wooden wall. Deep charcoal and aged-wood palette with ONE strong accent: the cold silver light on the steel. High contrast, reverence, profound stillness. No text, no letters.
```

**🇺🇦 RU:** Вариант A — огромная катана, воткнутая в скалу на вершине горы, на рассвете; самурай сидит маленький у её подножия. Это схема «один огромный образ», как у тигра и дракона. Вариант B — обнажённая катана на подставке в храме, лунный луч идёт ровно по клинку, самурай сидит перед ней. Он камернее и ближе к MUSHIN. В обоих вариантах самурай без меча в руках, левая треть пустая под текст.

### Variant C — slow kata before battle (chosen frame, 2026-11-18)

Frame: `stillwave/assets/katana-2h-source.jpg` (black bars cropped, 3840x2160). The samurai on a mountain ledge above a sea of clouds, bare katana in a forward middle guard, empty scabbard at the hip. The left third is bright mist (mean brightness ~110–160, the old frames were 8–20), so text there must be **dark ink**, not cream.

**🇺🇦 RU:** Выбран кадр с тренировкой. Левая треть светлая (туман), поэтому текст там будет тёмный, как тушь на бумаге, а не кремовый.

## §4 — Flow loops v2 (2026-11-18): living atmosphere + three kata moves

First Flow test: only the blade moved, the mist and the clothes stood still. Fix: the wind, mist and cloth motion go FIRST in the prompt and are stated for the whole clip. Each move is a separate 8 s clip that starts AND ends on the same frame (Flow: Frames to video, first frame = last frame = `katana-2h-source.jpg`), so the three clips can be joined in any order without a jump: 1 → 2 → 3 = 24 s, repeated ~300 times in 2 hours instead of ~900.

Do not generate fast and slow it down in CapCut: Flow renders 24 fps, a 3x slow-down leaves 8 fps (stutter) or optical-flow artefacts on the thin blade and the mist. Ask for slow motion in the prompt instead.

**🇺🇦 RU:** В первом тесте двигался только клинок. Теперь ветер, туман и одежда стоят в начале промпта и заданы на весь клип. Три разных движения — три клипа по 8 секунд, у каждого первый и последний кадр одинаковые, поэтому их можно склеить в любом порядке. Быстро снимать и замедлять в CapCut не советую: будет дёргаться или клинок поплывёт.

### Move 1 — lower and return
```
Camera completely locked, no pan, no zoom. Throughout the entire clip, from the first frame to the last, a steady mountain wind blows from left to right: the sea of clouds below flows continuously through the valleys and low around the foot of the rocks, far beneath the ledge; the air around the samurai and his sword is clear, the sleeves of his kimono and the wide hakama ripple and flutter constantly in the wind, loose strands of his hair stir. The rocks, the ledge and the edges of the frame stay exactly as in the first frame, only the mist moves across them. The samurai slowly lowers the katana from this forward guard until the blade points down at the rock in front of him, then slowly raises it back to exactly the same forward guard as in the first frame, like a breath out and a breath in. His feet stay planted, both hands stay on the handle, the blade stays straight, rigid and keeps its exact shape and length, the empty scabbard stays at his hip. Real-time slow, graceful motion. The last frame matches the first frame exactly.
```

### Move 2 — side guard and return
```
Camera completely locked, no pan, no zoom. Throughout the entire clip, from the first frame to the last, a steady mountain wind blows from left to right: the sea of clouds below flows continuously through the valleys and low around the foot of the rocks, far beneath the ledge; the air around the samurai and his sword is clear, the sleeves of his kimono and the wide hakama ripple and flutter constantly in the wind, loose strands of his hair stir. The rocks, the ledge and the edges of the frame stay exactly as in the first frame, only the mist moves across them. The samurai slowly draws the katana down and back to his right side, the blade low behind his right hip pointing back, his body turning slightly, holds for a moment, then slowly brings it forward again to exactly the same forward guard as in the first frame. His feet stay planted, both hands stay on the handle, the blade stays straight, rigid and keeps its exact shape and length, the empty scabbard stays at his hip. Real-time slow, graceful motion. The last frame matches the first frame exactly.
```

### Move 3 — one slow cut and return
```
Camera completely locked, no pan, no zoom. Throughout the entire clip, from the first frame to the last, a steady mountain wind blows from left to right: the sea of clouds below flows continuously through the valleys and low around the foot of the rocks, far beneath the ledge; the air around the samurai and his sword is clear, the sleeves of his kimono and the wide hakama ripple and flutter constantly in the wind, loose strands of his hair stir. The rocks, the ledge and the edges of the frame stay exactly as in the first frame, only the mist moves across them. The samurai slowly raises the katana a little higher, then performs one slow, smooth, unhurried practice cut, the blade gliding diagonally downward from upper right to lower left like a calm brush stroke, holds the finished position for a moment, then slowly returns the blade to exactly the same forward guard as in the first frame. His feet stay planted, both hands stay on the handle, the blade stays straight, rigid and keeps its exact shape and length, the empty scabbard stays at his hip. Real-time slow, graceful motion. The last frame matches the first frame exactly.
```


**Lesson (2026-11-18):** the first "cut" clip grew a pine branch at the right edge between ~1 s and ~6 s that is not in the start frame or in the "lower" clip. Cause: the prompt asked for "the small pine bushes on the ledge sway", and the clip framing had no bushes, so Flow invented them. The phrase is removed; the prompts now say the rocks and the frame edges stay as in the first frame.

**🇺🇦 RU:** В клипе с разрезом у правого края появлялась ветка сосны, которой нет ни в стартовом кадре, ни во втором клипе. Причина — в промпте было «кусты на уступе качаются», а в кадре клипа кустов не было, и Flow их дорисовал. Фразу убрал.

**Lesson 2 (2026-11-18):** in the same clip a small puff of mist appeared under the blade during the cut. Cause: the prompt put "thick mist across the whole frame", so Flow tied the mist to the blade's motion. Fix: the mist now lives only in the valleys and low around the foot of the rocks, the air around the samurai is described as clear, and the cut is a slow practice stroke, not a strong one.

**🇺🇦 RU:** Под клинком при разрезе появлялось облачко. Причина — в промпте туман был «по всему кадру», и Flow связал его с движением меча. Теперь туман только внизу, в долинах и у подножия скал, воздух вокруг самурая чистый, а разрез — медленное тренировочное движение, а не сильный удар.

## §5 — Video loop, overlay, thumbnail (2026-11-18)

- **Loop:** `KATANA_loop_19s_v2.mp4` — the reworked cut clip + the lowering clip, joined with 0.5 s dissolves, seamless (seam diff 0.73 vs median 0.36 per frame). Repeat in CapCut for 2 hours.
- **Overlay:** `stillwave/assets/katana-ken-zen-ichinyo-overlay.png`, placed UPPER-LEFT over the sky (`--dy -560`, scrim 140). Placement checked on a frame of the Flow loop, which is darker and bluer than the still.
- **Thumbnail:** `stillwave/assets/katana-2h-thumb-v2.jpg` (built by `katana-compose-thumb-v2.py`): same v2 layout as BUSHIDO / DOJO / MUSHIN II, but in **dark ink** (black brush 刀, dark serif KATANA) because the left third of the still is bright mist.

**🇺🇦 RU:** Оверлей стоит слева вверху, на небе, проверен на кадре из самого видео (оно темнее картинки). Превью в том же стиле v2, но тёмной тушью: слева на кадре светлый туман, белый текст там не читается.

## §6a — Wisdom overlay

- **剣禅一如** · *Ken zen ichinyo* · "The sword and Zen are one" — the teaching of Yagyū Munenori and Takuan: the swordsman's skill and the Zen mind are a single practice.
- CapCut: top track, 0:03 → 0:14, fade in 2 s / fade out 2 s.

**🇺🇦 RU:** 剣禅一如 — «меч и дзэн едины». Учение Ягю Мунэнори и монаха Такуана: мастерство меча и дзэнский ум — одна практика.

## §7 — Title
```
KATANA — 刀 | Samurai Meditation Music for Focus, Discipline & Inner Strength
```
A/B:
```
Samurai Meditation Music — KATANA 刀 | The Sword and Zen Are One (2 Hours)
```

## §8 — Description (timestamps and track names are filled in after the album is chosen)
```
Ken zen ichinyo (剣禅一如): the sword and Zen are one. For the old masters, practice with the katana was never only about cutting. Every slow movement was a way to train the mind: the same calm attention, the same breath, again and again, until nothing else was left.

Two hours of samurai meditation music for that kind of practice. A low shakuhachi flute, warm koto plucked one note at a time, a deep string drone underneath like steady breathing, and long silences between the phrases. No drums, no beats, nothing that rises or builds. One quiet level from the first minute to the last.

Use it for:
- deep focus, study and long work sessions
- training, stretching and slow movement
- seated meditation and breathwork
- a calm mind before sleep

[TRACKLIST]
(the cycle repeats until 2:00:00)

More from StillWave Zen:
MUSHIN — Japanese Zen Music for Deep Focus: https://youtu.be/CamT9sohYQM
BUSHIDO — Japanese Samurai Music for Calm & Quiet Discipline: https://youtu.be/pxjc2GIyvBY
Miyamoto Musashi — Samurai Meditation for Stress Relief: https://youtu.be/mJ3RMn3J4B8

"The mind must always be in a state of flow." — Takuan Sōhō, The Unfettered Mind

New Japanese Zen music every week. Subscribe if you want it in your feed.

#samuraimusic #katana #samuraimeditation #zenmusic #deepfocus
```

## §9 — Tags (24 tags, 478 characters)
```
stillwave, katana, katana music, samurai music, samurai meditation music, samurai sword, samurai training music, samurai relaxing music, japanese zen music, zen music, meditation music, focus music, deep focus music, study music, sleep music, relaxing music, shakuhachi flute music, koto music, japanese meditation music, ancient japan ambience, bushido, ken zen ichinyo, samurai practicing a slow kata with a katana on a misty mountain ridge above a sea of clouds, joe hisaishi
```

## §11 — Pinned comment
```
🌀 刀 KATANA — 剣禅一如, the sword and Zen are one: every slow movement trains the mind, not only the hand. 🍃 What is the one thing you practise again and again until it becomes calm? Subscribe for more Japanese zen focus sessions every week 🌿
```

**Upload settings:** Not for kids · Playlists "Japanese Zen Music" + "Samurai Meditation Music — Japanese Zen for Focus & Sleep" · first publish Scheduled/Unlisted · end screen → MUSHIN.
