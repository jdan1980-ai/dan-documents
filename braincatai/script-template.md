# Script Template — BrainCatAI Short

**Pipeline:** 8 scenes → image in Nano Banana → animation in Veo 3 → glue together.
**Total runtime:** ≤ 60 sec (target ~7 sec per scene).

Copy this file to `scripts/<slug>.md` and fill in the fields.
Every prompt and voiceover line is in its own code block — click the copy icon and paste straight into the tool.

---

## Meta

- **Title (working):**
- **Slug:** (e.g. `why-sky-blue`)
- **Category:** Science / Biology / Math / Psychology / AI / History / Trivia
- **Series:** Cat Asks Why / What If / TIL / standalone
- **Status:** idea | script | images | animation | edited | published
- **Date created:**
- **Publish date:**

## Audience Promise

One sentence — what does the viewer learn or feel?

> 

## ✍️ Voiceover rule

Every line must be understandable for **a 9-year-old AND a 40-year-old**. Write like you're telling a friend something cool, not like a textbook. No jargon, no scary words, no "umm/basically/actually." See [style-guide.md §9](./style-guide.md#9-editorial-voice-writing-style) for the swap table.

---

## 🔒 Locked Brain Prompt (always prepend)

Paste this at the **start of every Nano Banana image prompt** to lock Brain's look. Only Brain is locked — the background is chosen per-video below.

```
Cute orange tabby kitten named Brain, big round sparkling green eyes, small thin round gold-framed glasses, brown leather collar with gold heart-shaped tag engraved "Brain", soft fluffy orange fur with darker tabby stripes, pink nose, long white whiskers, Pixar 3D render style, cinematic lighting, 4K, vertical 9:16 composition.
```

**Negative prompts (Nano Banana):**

```
2D, flat, anime, cel-shaded, photorealistic cat, multiple cats, low quality, blurry, distorted face, extra limbs, missing glasses, missing collar, missing heart tag, watermark, text in image, logo, ugly, scary, aggressive expression, mouth open as if talking, lip-sync, talking cat
```

## ⚠️ Veo 3 animation rule — mouth stays closed

Every `🎬 Animation prompt` block in this script must end with:

```
Mouth stays closed throughout, no lip-sync, no talking motion. Expressions through eyes, ears, whiskers, and body.
```

Exceptions (state explicitly when used): brief held jaw-drop for shock, single yawn, one soft meow on CTA.

---

## 🏠 Scene Settings (lock locations for THIS video)

Pick 1–3 locations max for this video. Write each as a single descriptive paragraph and **paste the exact same wording** into every scene that uses that location. The CTA scene (Scene 8) must use one of these locations — never a generic outro background. See [style-guide.md §8b](./style-guide.md#8b-scene-continuity-per-video-world-locks).

### Location A — `INT. / EXT. NAME — TIME OF DAY`

```

```

### Location B — `INT. / EXT. NAME — TIME OF DAY` (delete if not used)

```

```

### Location C — `INT. / EXT. NAME — TIME OF DAY` (delete if not used)

```

```

### Scene → location map

| Scene | Location | Notes |
|-------|----------|-------|
| 1 | A | |
| 2 | A | |
| 3 | | |
| 4 | | |
| 5 | | |
| 6 | | |
| 7 | | |
| 8 (CTA) | **must match one above** | |

---

## Full Voiceover (whole video, single block)

Paste this into your TTS tool (e.g. ElevenLabs) as one read for natural pacing. Word target **80–120 words** ≈ 50 sec at 130 wpm.

```

```

---

# Scenes

---

## Scene 1 — HOOK (0–7 sec)

**Beat purpose:** grab attention in the first 2 seconds. Contradiction or shocking statement.
**Location:** A / B / C (mark from the map above)

**🎨 Image prompt (Nano Banana):**

> Format: `[Locked Brain prompt] + [exact location block from above] + [per-shot action]`

```

```

**🎬 Animation prompt (Veo 3):**

```
Camera motion + Brain's action + facial expression + duration ~7s
```

**🎙️ Voiceover:**

```

```

---

## Scene 2 — Curiosity gap (7–14 sec)

**Beat purpose:** promise the answer, make viewer need to keep watching.

**🎨 Image prompt (Nano Banana):**

```

```

**🎬 Animation prompt (Veo 3):**

```

```

**🎙️ Voiceover:**

```

```

---

## Scene 3 — Setup (14–21 sec)

**Beat purpose:** introduce the concept / context.

**🎨 Image prompt (Nano Banana):**

```

```

**🎬 Animation prompt (Veo 3):**

```

```

**🎙️ Voiceover:**

```

```

---

## Scene 4 — Build-up (21–28 sec)

**Beat purpose:** add the first piece of the explanation.

**🎨 Image prompt (Nano Banana):**

```

```

**🎬 Animation prompt (Veo 3):**

```

```

**🎙️ Voiceover:**

```

```

---

## Scene 5 — Core explanation (28–35 sec)

**Beat purpose:** deliver the key insight visually.

**🎨 Image prompt (Nano Banana):**

```

```

**🎬 Animation prompt (Veo 3):**

```

```

**🎙️ Voiceover:**

```

```

---

## Scene 6 — Twist / aha moment (35–42 sec)

**Beat purpose:** the "wow" payoff. Brain reacts mind-blown.

**🎨 Image prompt (Nano Banana):**

```

```

**🎬 Animation prompt (Veo 3):**

```

```

**🎙️ Voiceover:**

```

```

---

## Scene 7 — Bonus fact / contrast (42–49 sec)

**Beat purpose:** one extra surprising fact that reinforces the topic.

**🎨 Image prompt (Nano Banana):**

```

```

**🎬 Animation prompt (Veo 3):**

```

```

**🎙️ Voiceover:**

```

```

---

## Scene 8 — CTA / outro (49–56 sec)

**Beat purpose:** wink at camera, call to follow. Keep it ≤ 6 sec.

**🎨 Image prompt (Nano Banana):**

```

```

**🎬 Animation prompt (Veo 3):**

```

```

**🎙️ Voiceover:**

```

```

---

## 🎵 Music Prompt (paste into Suno / Udio / Mubert / ElevenLabs Music)

Write a single instrumental music prompt for the whole 60-sec video. Specify mood, instruments, BPM, build-up moments, no vocals, royalty-free.

```

```

**Alt prompt (shorter, for tools with character limits):**

```

```

## Assembly in Google Vids

1. Upload all 8 animated clips in order (Scene 1 → Scene 8)
2. Add VO track from TTS (one continuous file is easier — split clips if needed to match)
3. Add music track at -18 LUFS, voice at -12 LUFS (~6 dB voice over music)
4. Add burn-in captions, top third of frame, max 4 words on screen
5. Add SFX cues per editing notes below

## Editing Notes

- Cut between scenes with hard cuts or whip-pans
- Burn-in subtitles (max 4 words on screen at a time, top third)
- Voice -12 LUFS, music -18 LUFS
- Add SFX: whoosh on transitions, ding on aha moment, meow on CTA

## SEO Pack

> **vidIQ optimization rules (target 80+/100):**
> - **Title:** 40–70 chars, include main keyword (`cat psychology` always for this channel), use `|` to add the niche tag, end with 🐱
> - **Description:** ≥ 250 chars, repeat main keyword 2–3 times, include 5+ supporting keywords, include emoji, end with hashtag block + follow CTA
> - **Tags:** 20–25 tags, mix broad (1 word) + medium (2 words) + long-tail (3–5 words), total under 450 chars
> - **Hashtags in title bar:** only first 3 show under title — pick the 3 strongest, `#shorts` always first
> - Always include: `cat psychology, cat facts, cat behavior, brain cat, did you know, mind blowing facts`

**Final title** (40–70 chars, end with `🐱 | Cat Psychology`):

```

```

Alt titles to A/B test:

```


```

**Description (≥ 250 chars, repeat main keyword 2–3×):**

```


🐱 Follow Brain for more cat psychology, cat facts, and cat secrets every week.

#shorts #catpsychology #catfacts #catbehavior #braincatai #didyouknow #petfacts
```

**Tags (paste comma-separated into YouTube tags field — base set + 5–10 video-specific):**

Base set (always include):

```
cat psychology, cat facts, cat behavior, cat secrets, cat science, cat communication, cat body language, feline behavior, understanding cats, facts about cats, animal facts, animal science, did you know, mind blowing facts, brain cat, cat facts daily, cat behavior funny, cat domestication, cats vs humans
```

Video-specific (add 5–10 long-tail tags matching this video):

```

```

**Hashtags (top 3 show under the title — order matters):**

```
#shorts #catpsychology #catfacts
```

Extended set (for description body):

```
#shorts #catpsychology #catfacts #catbehavior #braincatai #didyouknow #petfacts
```

**Thumbnail concept:**

> 

---

## Post-publish metrics

| Metric | 48h | 7d | 30d |
|--------|-----|----|----|
| Views  |     |    |    |
| Avg view duration |  |  |  |
| Retention % |       |    |    |
| Likes  |     |    |    |
| Shares |     |    |    |
| Comments |   |    |    |
| Subs gained |       |    |    |

### Notes — what worked / what didn't
