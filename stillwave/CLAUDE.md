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

## 🎨 Aesthetic — HYBRID spec (Spacious Tokyo Penthouse baseline)

**Default backdrop for all hybrid videos:** Spacious open-plan luxury Japanese penthouse on a high floor of a Tokyo / Osaka / Kyoto skyscraper at night. **Massive corner-wrap or full-wall floor-to-ceiling glass windows** are the dominant visual feature (>50% of visible interior surfaces). Beyond the glass: massive Japanese cityscape — countless neon signs (kanji + katakana in pink, cyan, electric green, warm amber), distant skyscrapers with lit windows extending to horizon, **red taillight streaks of cars on highways below**, warm yellow street lights of Tokyo creating a sea of urban glow.

The room **breathes** — high ceilings (12–14 ft), generous negative space across floor and walls, sense of luxury through emptiness. Three light sources balance the scene:

- 🔥 **Fireplace** (warm amber, left wall) — modern linear gas fireplace embedded in a slate stone or charcoal-stained wood feature wall, long horizontal flame visible behind tinted glass
- 💻 **Open MacBook screen glow** (warm soft, on the desk) — laptop is ALWAYS OPEN with content actively visible (writing app / code editor / research notes — match the use case)
- 🌃 **Cool neon city** through the windows (right / back) — pink, cyan, amber accents through possibly rain-streaked glass

Every new-format thumbnail/scene must include all six:

1. **Spacious open-plan luxury Japanese penthouse interior** — high ceilings, sense of breathing room, dark walnut / cedar / oak finishes + slate stone accents, low desk or kotatsu-style table
2. **Massive floor-to-ceiling windows** showing big Japanese city night view (neon kanji/katakana signs, distant skyscrapers, red taillight streaks below) — windows must be the dominant feature, NOT a small accent
3. **Modern minimalist fireplace** on a side wall — long horizontal flame, warm amber glow casting into the room
4. **OPEN MacBook with active screen content** — writing app / code editor / research notes (match the use case). Screen content rendered as **abstract horizontal text-stripe patterns**, NEVER readable letters (avoids garbled-text artifact)
5. **ONE Japanese accent** (rotate per video):
   - 🌿 Bonsai (black pine, juniper) on desk
   - 🏮 Andon paper lantern (warm amber glow) on desk or windowsill
   - 🍵 Japanese ceramic tea cup with steam
   - 📜 Hanging scroll with kanji calligraphy on wall (atmospheric only, unreadable)
   - 🌸 Ikebana arrangement
   - 🎴 Shoji-inspired interior screens (modern interpretation, not traditional)
6. **Photorealistic cinematic style**:
   - Ultra-wide 16:9 cinematic framing showing the spacious room
   - Shallow depth of field on the foreground prop, city lights + fireplace flame as soft glowing bokeh
   - Muted dark interior palette (charcoal blacks, walnut/cedar browns, slate gray stone) contrasted with vibrant but soft neon city accents (pink, cyan, amber) AND warm fireplace amber
   - Atmospheric depth: 4 distinct planes (foreground prop / mid-ground room with fireplace / background floor-to-ceiling windows / far-background neon Tokyo skyline)
   - **NO text, NO logos, NO watermarks** in image (laptop screen UI doesn't count — describe screen content as abstract stripe patterns, not readable letters)

This Spacious Tokyo Penthouse backdrop is the LOCKED visual signature of StillWave. Every hybrid video uses it. Different videos vary the **prop, mood (rainy / clear / misty / snowing), Japanese accent, and laptop screen content** — but the spacious penthouse + massive windows + fireplace stays consistent. Builds brand recognition.

### Laptop screen content per use case

| Video use case | Screen content (described as abstract patterns) |
|----------------|-------------------------------------------------|
| Coding / programming | Dark VS Code-style editor with horizontal stripes in green/blue/orange syntax-highlight colors (NOT readable code) |
| Writing / journaling | Clean dark writing app with paragraph-shaped horizontal text stripes and a blinking cursor (NOT readable text) |
| Studying / research | Notes app with mixed text stripes and occasional bigger heading blocks, dark mode |
| Trading / analysis | Dark trading dashboard with abstract candle-stick chart shapes and number stripes |
| Reading | E-reader-style page with horizontal text stripes, warm reading mode |

## Old format (иероглиф / Hz / sumi-e) — still allowed in Phase 1–2

Continue using the original style for the videos that aren't in the new format yet. Don't kill it — phase it down per the table above.

---

## 🛠️ Pipeline

Long-form has TWO mode options. **Default = Mode B (looped motion)** for the Phase 1 batch and beyond — gives the video life (rain on glass / fireplace flicker / laptop screen activity) without overspending on credits.

### Mode A — Static image + audio (cheapest, no Flow/Kling)

| Stage | Long-form |
|-------|-----------|
| Music | Suno AI v5.5 |
| Image | NanoBanana 16:9 |
| Video | ❌ Not generated — single still image |
| Assembly | `ffmpeg` loops the still for the audio length |
| Thumbnail | Same NanoBanana 16:9 image |

```bash
ffmpeg -loop 1 -i thumbnail.jpg -i music.mp3 \
  -c:v libx264 -tune stillimage -pix_fmt yuv420p -r 1 \
  -c:a aac -b:a 192k -shortest -t 7200 output.mp4
```

Use for: budget runs, fastest turnaround, or if Flow/Kling gives bad results.

### Mode B — Looped motion video + audio (default for Phase 1+)

| Stage | Long-form |
|-------|-----------|
| Music | Suno AI v5.5 |
| Image | NanoBanana 16:9 (start frame) |
| Video | **Flow / Kling — 8-second seamless loop** with subtle motion (rain on glass, fireplace flicker, laptop screen activity) |
| Assembly | `ffmpeg -stream_loop -1` repeats the 8-sec loop for the full audio length |
| Thumbnail | Same NanoBanana 16:9 image |

```bash
ffmpeg -stream_loop -1 -i loop.mp4 -i music.mp3 \
  -c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p \
  -c:a aac -b:a 192k -shortest -t 7200 output.mp4
```

Faster alternative (no re-encode — requires loop already in 1080p H.264 yuv420p):

```bash
ffmpeg -stream_loop -1 -i loop.mp4 -i music.mp3 \
  -c:v copy -c:a aac -b:a 192k -shortest -t 7200 output.mp4
```

For specific length use `-t 7200` (2H), `-t 10800` (3H), `-t 28800` (8H).

### Loop motion rules (for Flow / Kling prompts)

- **Camera locked** — no pan, zoom, dolly, or shake. Frame stays identical to the start image.
- **3–4 motion elements only** — rain on glass / fireplace flicker / laptop screen activity / steam from a cup. Pick 3–4 max.
- **Everything else still** — bonsai, tea cup itself, table, walls, furniture, distant city. Static.
- **Distant cars / red taillights:** static shapes — NOT visibly moving (full traffic motion would be too distracting for ambient focus).
- **Loop must be perfectly seamless** — last frame matches first frame. The looped audio is 2–3 hours long, so any seam shows up 900+ times. Pick repeating cycles for typewriter screen text and rain to ensure clean loop join.
- **Subtle, not dramatic** — viewers leave this on for hours. Distracting motion = swipe-away.

### Shorts pipeline (unchanged)

| Stage | Tool |
|-------|------|
| Music | Suno AI v5.5 |
| Image | NanoBanana 9:16 |
| Video | Flow / Kling 9:16 (15–60 sec subtle motion loop — Shorts still need motion) |
| Assembly | CapCut + ffmpeg |

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

### 🌅 Smooth start and end (mandatory — fixes Suno's abrupt-cut problem)

By default Suno generates tracks with **hard starts and hard endings** — sudden instrument onsets at 0:00 and abrupt cuts at the end. For ambient / focus music this is jarring, and for multi-track CapCut assembly it makes seamless crossfades impossible.

**Every Suno generation for StillWave MUST include explicit fade-in / fade-out instructions** in both Prompt A and Prompt B.

#### In Prompt A (Style field)

Add this phrase before the locked tail:

```
gradual fade-in from silence at the start (3-4 seconds), gentle fade-out to silence at the end (6-8 seconds), no abrupt cuts.
```

This is ~110 chars — leave room within the 1000-char Suno Style limit.

#### In Prompt B (Lyrics field)

Update the template — `[opening]` now starts with fade-in instruction, and replace the old `[loop point]` with a `[closing]` section that ends with fade-out:

```
[no lyrics, no vocals, instrumental only]
[opening: 3-4 second gentle fade-in from silence, then [описание вступления]]
[section A: описание части A]
[section B: описание части B]
[section C: описание части C]
[closing: instruments gradually fade out to silence over 6-8 seconds, last note decays softly into silence, no abrupt cut at the end]
[mood: образ/сцена/состояние]
[texture: фактура звука]
```

**Why fades on every track (not just album start/end):**

- Track 1 of the album needs a fade-in so the album doesn't start with a sudden burst
- Track N (final) needs a fade-out so the album doesn't cut off abruptly
- Tracks 2 through N-1 in the middle ALSO need soft starts and soft ends — this lets CapCut crossfades between adjacent tracks look natural (a hard-onset track 5 will sound abrupt even mid-album)
- The fade durations are short enough (3-4s in, 6-8s out) that they don't eat musically meaningful content

**When fade rule does NOT apply:** Shorts (<60 sec), where you actually need a strong hook in the first 2 seconds — for those, replace fade-in with a single attention-grabbing onset (a temple bell, a held note, a soft pad swell from silence to peak in 1 second).

---

## 📝 Title format — VidIQ-validated (Phase 1+)

### Canonical formula (Tokyo Rain Vol. 1 scored 93/100 on VidIQ)

```
[Scene Keyword] [Use Case + Hook] | [Duration + Differentiator] Vol. N
```

**Examples:**

- `Tokyo Rain Deep Work Marathon | 1 Hour Uninterrupted Vol. 1` (live, 93/100)
- `Tokyo Snowfall Coding Marathon | 1 Hour Uninterrupted Vol. 2`
- `528 Hz Japanese Zen Healing Marathon | 1 Hour Uninterrupted Vol. 1`

**Field-by-field guide:**

| Slot | Role | Examples |
|------|------|----------|
| **Scene Keyword** | The unique scene-bait (must lead — it's the differentiator vs every other "deep focus music" video) | `Tokyo Rain`, `Tokyo Snowfall`, `528 Hz Japanese Zen` |
| **Use Case + Hook** | What the viewer is doing, framed with a strong noun like `Marathon` / `Sprint` / `Session` | `Deep Work Marathon`, `Coding Marathon`, `Healing Marathon`, `Study Sprint`, `Writing Session` |
| **Duration + Differentiator** | After the pipe `|` — duration + ONE killer word that promises something concrete | `1 Hour Uninterrupted`, `2 Hours Distraction-Free`, `90 Min Flow State` |
| **Vol. N** | Series counter at the end. Counters are independent per series (POWER HOUR / HEALING HOUR) | `Vol. 1`, `Vol. 2`, ... |

### Critical rules

- **Length under 60 characters.** Mobile feeds cut at 60-65 chars. Tokyo Rain Vol. 1 = 59 chars.
- **Lead with the scene, not "Best/Top/Deep/Quiet Music"** — generic openers waste prime real estate.
- **No "Power Hour" / "Healing Hour" in the title text.** Series brand is carried by:
  - Thumbnail overlay (`POWER HOUR` / `HEALING HOUR` white bold, see Design rules)
  - YouTube playlist title (`POWER HOUR`, `HEALING HOUR`)
  - Description body
  Keeping series name OUT of the title frees ~10 chars for stronger keywords.
- **Always run VidIQ before publishing** — target ≥85/100. If a candidate scores below, swap one slot (usually the "Differentiator" word) and retest.
- **Иероглиф stays out of title** (kept in description, playlist titles, tags only).

### Source of truth for next Vol. number

`production-status.md` table. Always check the table before assigning a new Vol. N.

## 🎨 Design rules

- **Photorealistic cinematic** style (NOT sumi-e / illustration)
- **No glow / effects on text anywhere** — plain solid colors only when text is needed
- **All YouTube copy in English** (descriptions, titles, tags, hashtags)

### Series-brand thumbnail overlay (POWER HOUR / HEALING HOUR)

Every video in a series gets a clean white series-brand text overlay on top of the NanoBanana 16:9 image. **Locked style — all overlays MUST use these parameters:**

- **Font:** Bebas Neue Regular — vendored at `stillwave/assets/fonts/BebasNeue-Regular.ttf`
- **Color:** pure white `#FFFFFF`
- **Letter spacing:** 0.25 × font size (wide tracking)
- **Position:** top-center, baseline at ~12% from top
- **Effects:** NONE — no shadow, no glow, no stroke, no outline

The vendored font ensures every overlay across both POWER HOUR and HEALING HOUR has identical letterforms and spacing — no visual drift between sessions or operators.

**Reusable generator:** `stillwave/gen_series_overlay.py`

```bash
python3 stillwave/gen_series_overlay.py "POWER HOUR"
python3 stillwave/gen_series_overlay.py "HEALING HOUR" --size all
python3 stillwave/gen_series_overlay.py "DEEP NIGHT" --size standard
```

Outputs transparent PNG overlays (1280×720) into `stillwave/assets/`:

| Size | Font | Use case |
|------|------|----------|
| `<slug>-compact.png` | 90px (~50% width) | Tight thumbnails, small text emphasis |
| `<slug>-standard.png` ⭐ | 120px (~62-70% width) | **Default** — used on most thumbnails |
| `<slug>-large.png` | 150px max, auto-shrinks to ≤95% width | When you want the brand to dominate |
| `<slug>-overlay.png` | alias for `-standard.png` | Backward-compat name |
| `<slug>-*-preview.png` | same overlay on dark-navy bg | Sanity-check the look before compositing |

Existing assets:
- POWER HOUR — `power-hour-compact / standard / large / overlay` (+ previews)
- HEALING HOUR — `healing-hour-compact / standard / large / overlay` (+ previews)

**Workflow on phone or desktop:**

1. Generate NanoBanana 16:9 for the new video
2. Open [photopea.com](https://www.photopea.com) (free in-browser Photoshop)
3. File → Open → load NanoBanana image as base layer
4. File → Open & Place → add the matching `<slug>-standard.png` overlay
5. (Optional) Nudge text position so it doesn't overlap a bright neon / fireplace area
6. File → Export As → PNG → upload to YouTube Studio as custom thumbnail

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

---

## 🔑 YouTube Data API v3 access

**Key location:** `/root/.config/youtube-api-key` (chmod 600, NOT in repo). Never commit, never paste in chat.

**Read pattern:**

```bash
KEY=$(cat /root/.config/youtube-api-key)
```

**Channel ID for StillWave:** `UC188FjOT6tivjPOPfZ69s7Q` (handle: `@stillwavezen`).

**Useful endpoints (curl + jq):**

```bash
# Channel stats (subs, total views, video count)
curl -s "https://www.googleapis.com/youtube/v3/channels?key=$KEY&id=UC188FjOT6tivjPOPfZ69s7Q&part=statistics,snippet,contentDetails" | jq

# All uploads playlist (use uploads playlist ID returned above — UU + channel ID)
curl -s "https://www.googleapis.com/youtube/v3/playlistItems?key=$KEY&playlistId=UU188FjOT6tivjPOPfZ69s7Q&maxResults=50&part=snippet,contentDetails" | jq

# Video full metadata (incl. tags) — comma-separated IDs
curl -s "https://www.googleapis.com/youtube/v3/videos?key=$KEY&id=VIDEO_ID1,VIDEO_ID2&part=snippet,statistics,contentDetails" | jq

# Search by keyword (100 quota units — use sparingly)
curl -s "https://www.googleapis.com/youtube/v3/search?key=$KEY&q=power+hour+focus+music&maxResults=20&order=viewCount&part=snippet,id" | jq
```

**Quota:** 10,000 units / day. Common costs: channel/video/playlistItems = 1, search = 100.

**Common workflows:**
- After publish — pull video metadata with `videos.list` to verify SEO landed correctly
- Competitor audit — get top channel videos via `playlistItems` from their uploads playlist
- Tag mining — pull `videos.list` for top-performing competitor videos to see exact tags they use
- Trend check — `search.list` with topic keyword + `order=viewCount` to find the breakouts