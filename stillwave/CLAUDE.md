# StillWave (@stillwavezen) — Project Instructions

This file is the single source of truth for the StillWave channel. All production work must follow these rules.

## Channel info

- **Channel:** StillWave
- **Handle:** [@stillwavezen](https://www.youtube.com/@stillwavezen)
- **Niche:** Japanese ambient → **expanding to deep work / focus music for coding / studying / late-night work** (gradual hybrid pivot, see Phase plan below)
- **Aesthetic:** **HYBRID** — modern productivity scene + 1 Japanese accent (see §Aesthetic below)
- **Tagline:** Sleep · Focus · Meditation · Deep Work
- **Cadence:** 4 videos / week

## ⏳ Format transition plan (May 2026 — June 2026)

> **Why gradual?** YouTube's algorithm takes 2–3 weeks to "re-categorize" a channel after a niche shift. Sudden change kills 30–50% of impressions. We phase the new format in slowly.

| Phase | Period | New-format videos / week | Old format (иероглиф / Hz) / week |
|-------|--------|---------------------------|------------------------------------|
| **Phase 1** — soft intro | weeks 1–2 (May 8 → May 22) | 1 of 4 | 3 of 4 |
| **Phase 2** — half-and-half | weeks 3–4 (May 22 → Jun 5) | 2 of 4 | 2 of 4 |
| **Phase 3** — new norm | week 5+ (from Jun 5) | 3–4 of 4 | 1 of 4 (legacy / niche) |

**Current phase:** Phase 1 (soft intro). Update this line as we move forward.

---

## 🎨 Aesthetic — HYBRID spec (Tokyo Skyscraper Apartment baseline)

**Default backdrop for all hybrid videos:** Modern luxury minimalist Japanese apartment on a high floor of a Tokyo / Osaka / Kyoto skyscraper at night, with floor-to-ceiling windows or balcony showing the massive Japanese cityscape — countless neon signs (kanji + katakana in pink, cyan, electric green, warm amber), distant skyscrapers with lit windows extending to horizon, red taillight streaks of cars on highways below, warm yellow street lights of Tokyo creating a sea of urban glow.

Every new-format thumbnail/scene must include all five:

1. **Modern luxury Japanese apartment interior** (high floor) — minimalist, dark walnut / cedar / oak finishes, low desk or kotatsu-style table, floor-to-ceiling windows or balcony
2. **Big Japanese city night view through windows** — neon signs (kanji/katakana characters glowing in pink/cyan/green/amber), distant skyscrapers with lit windows, **red taillight streaks of cars on highways below**, warm yellow street lights, occasional rain on glass
3. **Modern productivity prop** (one or more): closed/open MacBook, ceramic coffee mug, open notebook with leather cover, brass desk lamp, fountain pen
4. **ONE Japanese accent** (rotate per video):
   - 🌿 Bonsai (black pine, juniper) on desk
   - 🏮 Andon paper lantern (warm amber glow) on desk or windowsill
   - 🍵 Japanese ceramic tea cup with steam
   - 📜 Hanging scroll with kanji calligraphy on wall (atmospheric only, unreadable)
   - 🌸 Ikebana arrangement
   - 🎴 Shoji-inspired interior screens (modern interpretation, not traditional)
5. **Photorealistic cinematic style**:
   - 16:9 wide cinematic framing, slightly asymmetric
   - Floor-to-ceiling window dominates the right (or left) side of the frame
   - Shallow depth of field on the foreground prop, city lights as soft bokeh through the glass
   - Muted dark interior palette (charcoal blacks, walnut/cedar browns) contrasted with vibrant but soft neon city accents (pink, cyan, amber) and red taillight streaks
   - Atmospheric depth: 3 distinct planes (foreground prop / mid-ground floor-to-ceiling window / background neon Tokyo skyline)
   - **NO text, NO logos, NO watermarks** in image

This Tokyo-apartment backdrop is the NEW visual signature of StillWave. Every hybrid video uses it. Different videos vary the **prop, mood (rainy / clear / misty / snowing), interior light (warm laptop glow / paper lantern / desk lamp), and Japanese accent** — but the apartment + neon city view stays consistent. Builds brand recognition.

## Old format (иероглиф / Hz / sumi-e) — still allowed in Phase 1–2

Continue using the original style for the videos that aren't in the new format yet. Don't kill it — phase it down per the table above.

---

## 🛠️ Pipeline

| Stage | Long-form video | Shorts |
|-------|------------------|--------|
| Music | Suno AI v5.5 | Suno AI v5.5 |
| Image | NanoBanana 16:9 | NanoBanana 9:16 |
| Video | **❌ NOT NEEDED — static image + audio** | Flow / Kling 9:16 (motion still required for Shorts) |
| Assembly | **`ffmpeg`** combines image + audio | CapCut + ffmpeg |
| Thumbnail | The same NanoBanana 16:9 image — no separate thumbnail step | Frame extracted from Shorts |

### ffmpeg encode command (long-form static-image videos)

```bash
ffmpeg -loop 1 -i thumbnail.jpg -i music.mp3 \
  -c:v libx264 -tune stillimage -pix_fmt yuv420p -r 1 \
  -c:a aac -b:a 192k -shortest output.mp4
```

For specific length use `-t 7200` (2H), `-t 10800` (3H), `-t 28800` (8H).

> **`-r 1`** = 1 frame per second (since image is static, no need for higher fps — saves filesize 30×).

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
| programmer awake at 3 AM, bonsai watching, code on screen | sweeping, uplifting |
| temple bell at dawn, frost on bamboo | beautiful, moving |

Concrete imagery — never abstract emotional adjectives.

---

## 📝 Title format (3-phase evolution)

### Phase 1 (current) — keyword-first English, иероглиф dropped from title

```
Quiet Focus Music — Japanese Tea House Rain | 2H Deep Work
```

### Phase 2 — add brand prefix "StillWave —"

```
StillWave — Quiet Tea Garden Focus | 2H Coding & Writing
```

### Phase 3 — established branded format

```
StillWave — Lantern Glow Focus | 3H Late Night Coding
```

**Иероглиф stays in:** description body, playlist titles, tags. **Removed from:** video title, thumbnail.

## 🎨 Design rules

- **Photorealistic cinematic** style (NOT sumi-e / illustration)
- **No text on thumbnail image** — the title handles itself in YouTube UI
- **No glow / effects on text anywhere** — plain solid colors only when text is needed
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
3. **NanoBanana prompt 16:9** (4K, photorealistic, hybrid aesthetic, no text)
4. **NanoBanana prompt 9:16** (vertical version of the same scene for Shorts cross-promo)
5. **ffmpeg encode command** with target length
6. **YouTube Title** (per current Phase format)
7. **YouTube Description** (English, SEO, concept explanation, benefits list, timestamps if applicable, CTA)
8. **Tags** (15-20, primary keywords first)
9. **Hashtags** (3-5)
10. **Pinned Comment** (subscription CTA + engagement question)
11. **A/B Title Variant**

### `SWS: [тема]` → SHORTS package

**Pre-production:** Google Trends + competitor Shorts check, identify gap.

**Deliver this 11-item package:**

1. **Concept & Hook** (first 2 seconds)
2. **NanoBanana prompt 9:16** (vertical, 4K, hybrid aesthetic)
3. **NanoBanana prompt 16:9** (horizontal version)
4. **Flow / Kling prompt 9:16** (15-60 sec subtle motion loop — Shorts still need motion)
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
3. Google Trends: japanese zen + deep focus + work music keywords
4. **TOP 10 unused themes** with: theme + suggested title (current Phase) + Why gap exists / Demand: High/Medium/Low
5. **TOP 3 recommendations** with priority order

### `CAL: [месяц]` → MONTHLY CALENDAR + ANALYTICS

**Step 1 — Analytics:** Pull VidIQ analytics (@stillwavezen). Metrics: views, watch time, avg duration, subscribers, likes, comments. Best/worst performer. Best upload day + time. Best format (Hz / иероглиф / Deep Work hybrid).

**Step 2 — Competitor check:** New videos from MERSO / Power Hour Focus / Hikari Zen / etc. since last CAL. New trends or formats they test.

**Step 3 — Gap (mini):** 16 best unused themes for the month, balanced for the current Phase ratio.

**Step 4 — Calendar (4 videos / week):** For each slot: Week + Day (best day from analytics) / Video concept + format (new hybrid OR legacy иероглиф) / Priority (🔥 High / 🟡 Medium / 🟢 Experiment) / Effort (Low / Medium / High).

**Step 5 — Recommendations:** Best format to double down this month / one experiment to try / what to stop doing / thumbnail+title pattern working best.

### `THUMB: [тема]` → CANVA THUMBNAIL (legacy / special-case)

Default for new format: **NanoBanana 16:9 image is the thumbnail itself** — no Canva step needed.

Use Canva ONLY when a special variant is needed (e.g., text overlay for a viral hook, A/B test). Old style (dark navy/teal, sumi-e ink wash, kanji calligraphy, plain solid white text) is still available but not the default.

---

## Source-of-truth files in this folder

- `CLAUDE.md` — this file (project rules + triggers)
- `script-template.md` — copy-paste template for every new video
- `published-videos.md` — every published video with stats; update after each upload
- `competitor-tracker.md` — tracked competitors (Hikari Zen, RollinSound, MERSO, Power Hour Focus, etc.)
- `content-ideas.md` — backlog (output of `GAP:` and `CAL:` runs)
- `production-status.md` — pipeline tracker per video
- `scripts/<slug>.md` — one file per video