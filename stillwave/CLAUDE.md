# StillWave (@stillwavezen) — Project Instructions

This file is the single source of truth for the StillWave channel. All production work must follow these rules.

## Channel info

- **Channel:** StillWave
- **Handle:** [@stillvavezen](https://www.youtube.com/@stillwavezen)
- **Niche:** Japanese ambient · meditation · sleep · focus music
- **Aesthetic:** dark navy/teal, minimalist, zen
- **Tagline:** Sleep · Focus · Meditation
- **Cadence:** 4 videos / week

## Pipeline

| Stage | Tool |
|-------|------|
| Music | Suno AI v5.5 |
| Images | NanoBanana (Google AI) — 16:9 thumbnail + 9:16 Shorts |
| Video | Flow / Kling |
| Edit | CapCut (Russian + English) + ffmpeg |
| Thumbnails | Canva MCP via Claude (`THUMB:` trigger). Backup: Python/Pillow script |

---

## 🎵 Suno rules

### Style field (Prompt A)

- Describe instruments, atmosphere, BPM
- ALWAYS end with the locked tail:

```
instrumental only, no vocals, no singing, no chanting, no spoken word, pure instrumental
```

### Lyrics field (Prompt B)

ALWAYS use this format:

```
[no lyrics, no vocals, instrumental only]
[opening: описание вступления]
[section A: описание части A]
[section B: описание части B]
[section C: описание части C]
[loop point: как зацикливается]
[mood: образ/сцена/состояние]
[texture: фактура звука]
```

### Scene-based descriptions ONLY

| ✅ Use | ❌ Don't use |
|--------|--------------|
| moss on stone steps, mist rising from still pond | emotional, powerful |
| samurai sitting by fire, mind clear | sweeping, uplifting |
| temple bell at dawn, frost on bamboo | beautiful, moving |

Concrete imagery — never abstract emotional adjectives.

---

## 📝 Title format

```
[Иероглиф] — [Romaji] | [English phrase] — [benefit]
```

Example:
```
森林浴 — SHINRIN-YOKU | Ancient Cedar Forest — Deep Healing
```

## 🎨 Design rules

- **No glow / effects on text** — plain solid colors only
- **All YouTube copy in English** (descriptions, titles, tags, hashtags)

---

## ⚡ Triggers

When the user types one of these in chat, follow the trigger spec exactly.

### `SW: [параметры]` → LONG VIDEO package

**Pre-production (always do first):**

1. Google Trends check for the topic
2. Search top 3 competitor videos on the same topic
3. Identify content gap before proceeding

**Deliver this 11-item package:**

1. **Suno Prompt A** — Style field (instruments / atmosphere / BPM + locked tail)
2. **Suno Prompt B** — Lyrics field ([no lyrics, no vocals, instrumental only] + scene structure)
3. **NanoBanana prompt 16:9** (4K, dark navy/teal, photorealistic, no text)
4. **NanoBanana prompt 9:16** (vertical Shorts version, same theme)
5. **Flow / Kling prompt 16:9** (ultra slow motion, 0.2-0.3× speed, loop)
6. **YouTube Title** (иероглиф — romaji | English — benefit)
7. **YouTube Description** (English, SEO, concept explanation, benefits list, timestamps, CTA)
8. **Tags** (15-20, primary keywords first)
9. **Hashtags** (3-5)
10. **Pinned Comment** (subscription CTA + engagement question)
11. **A/B Title Variant**

### `SWS: [тема]` → SHORTS package

**Pre-production:** Google Trends + competitor Shorts check, identify gap.

**Deliver this 11-item package:**

1. **Concept & Hook** (first 2 seconds)
2. **NanoBanana prompt 9:16** (vertical, 4K)
3. **NanoBanana prompt 16:9** (horizontal version)
4. **Flow / Kling prompt 9:16** (15-60 sec loop)
5. **Text overlay** (3 lines max, plain solid colors)
6. **Shorts Title** (max 60 chars, hook-first)
7. **Description** (2-3 lines + link to full video)
8. **Tags** (10-15)
9. **Hashtags** (5-7, `#shorts` last)
10. **Pinned Comment** (engagement question CTA)
11. **A/B Title Variant**

### `GAP: SW` → CONTENT GAP analysis

1. Review `published-videos.md`
2. Search competitors for new content
3. Google Trends: japanese zen meditation keywords
4. **TOP 10 unused themes** with: иероглиф + romaji + English / Why gap exists / Suggested title / Demand: High/Medium/Low
5. **TOP 3 recommendations** with priority order

### `CAL: [месяц]` → MONTHLY CALENDAR + ANALYTICS

**Step 1 — Analytics:** Pull VidIQ analytics (@stillwavezen). Metrics: views, watch time, avg duration, subscribers, likes, comments. Best/worst performer. Best upload day + time. Best format (Hz / иероглиф / Study With Me).

**Step 2 — Competitor check:** New videos from competitors since last CAL. New trends or formats they test.

**Step 3 — Gap (mini):** 16 best unused themes for the month.

**Step 4 — Calendar (4 videos / week):** For each slot: Week + Day (best day from analytics) / Video concept + format / Priority (🔥 High / 🟡 Medium / 🟢 Experiment) / Effort (Low / Medium / High).

**Step 5 — Recommendations:** Best format to double down this month / one experiment to try / what to stop doing / thumbnail+title pattern working best.

### `THUMB: [тема]` → CANVA THUMBNAIL

1. Generate 4 variants via Canva MCP. Style: dark navy/teal, sumi-e ink wash texture, traditional Japanese calligraphy kanji, plain solid white text — no glow on text.
2. User picks variant (1-4)
3. Convert to editable Canva design
4. Return edit link

---

## Source-of-truth files in this folder

- `CLAUDE.md` — this file (project rules + triggers)
- `published-videos.md` — every published video with stats; update after each upload
- `competitor-tracker.md` — 5 tracked competitors
- `content-ideas.md` — backlog (output of `GAP:` and `CAL:` runs)
- `production-status.md` — pipeline tracker per video