# Script Template — StillWave Long-form

Copy this file to `scripts/<slug>.md` and fill in. Output of an `SW: [theme]` trigger should land here so each video has a single source of truth.

---

## Meta

- **Title:** _filled below_
- **Slug:** (kebab-case, e.g. `tea-house-rain-2h`)
- **Format:** Long-form / Shorts
- **Length:** 2H / 3H / 8H
- **Phase:** 1 (soft intro) / 2 / 3
- **Aesthetic:** Hybrid (modern productivity + Japanese accent) / Legacy (иероглиф / Hz / sumi-e)
- **Status:** idea | suno | image | encoded | scheduled | published
- **Upload date:**

---

## 1. 🎵 Suno Prompt A — Style field

> Describe instruments / atmosphere / BPM. ALWAYS end with locked tail.

```

```

## 2. 🎵 Suno Prompt B — Lyrics field

> ALWAYS use the bracket structure. Scene-based descriptions only — never abstract emotional adjectives.

```
[no lyrics, no vocals, instrumental only]
[opening: ]
[section A: ]
[section B: ]
[section C: ]
[loop point: ]
[mood: ]
[texture: ]
```

---

## 3. 🎨 NanoBanana prompt 16:9 (the thumbnail AND the video visual)

> Photorealistic. Hybrid aesthetic per `CLAUDE.md` §Aesthetic. NO text in image.

```

```

## 4. 🎨 NanoBanana prompt 9:16 (vertical version for Shorts cross-promo)

```

```

---

## 5. 🛠️ ffmpeg encode command

> Combines the 16:9 still image with the Suno-generated audio into a single MP4.

```bash
ffmpeg -loop 1 -i thumbnail.jpg -i music.mp3 \
  -c:v libx264 -tune stillimage -pix_fmt yuv420p -r 1 \
  -c:a aac -b:a 192k -shortest -t [LENGTH_SECONDS] output.mp4
```

`-t` for length: 2H = `7200`, 3H = `10800`, 8H = `28800`.

---

## 5a. 🈴 Wisdom Overlay — kanji / romaji / gloss

> Every long-form video (except Pomodoro timer) opens with this. See `CLAUDE.md` §Wisdom Overlay for full spec. Pick a REAL Japanese phrase matched to THIS video's theme — never reuse.
> *CapCut: TEXT → верхний трек. 0:00–0:03 = сцена без текста → Fade In 2s → 5s hold → Fade Out 2s → clip end 0:14. Шрифт Liberation Serif Bold, cream #F5EAD2, слева над тёмной зоной.*

```
[KANJI — large]
[romaji — medium]
"[English gloss — 2-5 words]"
```

**Placement in this video's frame:** [describe: e.g. "upper-left, over the dark interior wall"]

**Why this phrase:** [1 sentence — why it fits this video's theme]

---

## 6. 📝 YouTube Title

> Per current Phase format (see `CLAUDE.md` §Title format).

```

```

## 7. 📝 YouTube Description (English)

> ≥ 250 chars. Concept explanation + benefits list + use cases + CTA + hashtag block.

```

```

## 8. 🏷️ Tags (15-20, primary keywords first, comma-separated)

```

```

## 9. # Hashtags (3-5, top of description or pinned)

```

```

## 10. 📌 Pinned comment

> Subscription CTA + low-friction engagement question (emoji vote / one-word answer).

```

```

## 11. 🔁 A/B title variant

```

```

---

## Post-publish metrics

| Metric | 48h | 7d | 30d |
|--------|-----|----|----|
| Views  |     |    |    |
| Avg view duration |  |  |  |
| Watch time (h) | | | |
| Likes  |     |    |    |
| Comments |   |    |    |
| Subs gained |       |    |    |

### Notes — what worked / what didn't