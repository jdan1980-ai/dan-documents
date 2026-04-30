# BrainCatAI — Style Guide

The single source of truth for the channel's visual, audio, and editorial style. Every script, prompt, and edit should pull from this file. Update it when something works (or fails) consistently.

---

## 1. Channel Identity

- **Name:** BrainCatAI
- **Tagline:** "Facts that break your brain. Explained by a cat."
- **Promise:** Every video, the viewer learns one mind-blowing thing in under 60 seconds.
- **Tone in one sentence:** Smart, playful, slightly sarcastic — like a curious friend, not a teacher.

---

## 2. The Cat (Main Character)

### Look

- **Species:** Generic shorthair cat, slightly stylized (not realistic)
- **Body:** Round, plush proportions — head ~40% of body height for expressiveness
- **Fur color:** **Warm cream/beige** with soft white belly and paws *(lock this)*
- **Eyes:** Oversized, **bright cyan-blue**, glossy highlights — eyes are the main acting tool
- **Markings:** Small dark grey spot on left ear (signature detail for recognition)
- **Pupils:** Cartoon-flexible — can go pinprick (shock), heart (love), spiral (confused), star (excited)

### Personality

- Curious, slightly know-it-all, but humble when wrong
- Reacts BIG (faces, full-body) — never stiff
- Breaks the fourth wall (looks at camera) on hooks and CTAs
- Smart but not arrogant — shares discovery, doesn't lecture

### Expressions (recurring)

| State | Use case | Visual cue |
|-------|----------|------------|
| 😱 Shock | Hook reveal | Wide eyes, jaw drop, fur poof |
| 🤔 Curious | Setup | Head tilt, paw on chin, raised brow |
| 🤯 Mind-blown | Payoff | Eyes spiral, sparks/stars around head |
| 😏 Smug | "I told you" moments | Half-lidded eyes, smirk, paw flick |
| 😴 Bored | Skipping over filler | Yawn, slumped pose |
| 😉 Wink | CTA/outro | One eye closed, raised paw |

### What the cat NEVER does

- Speaks visibly (mouth syncing) — voiceover only, the cat *reacts*
- Wears clothes regularly (only situational: spacesuit, lab coat)
- Has photorealistic detail
- Looks angry/aggressive — keep it warm

---

## 3. Color Palette

Lock these for visual consistency.

| Role | Name | Hex | Use |
|------|------|-----|-----|
| Primary | Cream Cat | `#F5E1B8` | Cat fur |
| Belly | Warm White | `#FFF6E3` | Cat belly, paws, chin |
| Accent | Cyan Eye | `#3FD0F2` | Cat eyes, key glow effects |
| Brand | Electric Yellow | `#FFD23F` | On-screen text, thumbnails |
| Hot | Coral Red | `#FF5C5C` | Alarm/wrong/wow text |
| Background dark | Midnight | `#0F1B2D` | Space, "what if" scenes |
| Background light | Sky Mint | `#D9F2EC` | Default scenes |
| Outline | Soft Charcoal | `#2A2A2A` | Cat outlines, text shadow |

**Rules:**
- Never more than 3 dominant colors in one frame
- Yellow text on dark background = highest CTR for thumbnails
- Coral red ONLY for "wow"/correction moments — keep it rare so it stays loud

---

## 4. Typography

| Use | Font | Weight | Notes |
|-----|------|--------|-------|
| Thumbnails | **Bangers** or **Komika Axis** | Bold | All caps, slight tilt 2–4° |
| On-screen captions | **Inter** or **Montserrat** | 800 | All caps, bright yellow, charcoal stroke 4px |
| End-card / channel name | **Bangers** | Regular | Pair with cat wink |
| Body (descriptions, etc.) | **Inter** | 400 | Standard |

**Caption rules:**
- Max **4 words at a time** on screen
- Show only when narrator is saying that beat
- Position: **top third** of frame (Shorts UI covers bottom)

---

## 5. Animation & Motion

- **Frame rate:** 30 fps (24 fps for cinematic beats)
- **Aspect:** 1080x1920 (9:16)
- **Style:** 2D flat with soft shading, slight squash & stretch
- **Cuts:** Fast — average shot length **2–3 seconds** (longer = retention drop)
- **Transitions:** Whip pans, zooms, simple dissolves. No fancy 3D wipes.
- **Cat motion:** Always something moving — tail flick, ear twitch, blink. **Never a static cat for >1 sec.**

### Beat-to-shot mapping

| Beat | Shot type |
|------|-----------|
| Hook | Close-up on cat face, fast push-in |
| Setup | Wide establishing, cat + topic visible |
| Explanation | Medium with diagrams/overlays |
| Payoff | Close-up reaction + bold text |
| CTA | Cat looking at camera, brand colors |

---

## 6. Audio

### Voiceover

- **Voice:** Energetic, curious, slightly playful (think science YouTuber, not documentary narrator)
- **Pace:** 120–140 wpm — fast enough to feel urgent, slow enough to follow
- **TTS option:** ElevenLabs "Adam" or "Charlie"
- **No accents that sound like a teacher** — sound like a friend who just discovered this

### Music

- **Mood:** Upbeat curious, light synth, ~100–120 BPM
- **Volume:** -18 LUFS music, -12 LUFS voice (voice always 6 dB above music)
- **Sources:** Epidemic Sound, Artlist (track in description if required)

### SFX (use sparingly — max 4 per video)

| Cue | When |
|-----|------|
| Whoosh | Scene transitions |
| Record scratch | Hook reveal / "wait, what?" |
| Ding/sparkle | "Aha!" payoff moments |
| Meow | CTA / channel sting |
| Boom | Big reveal text drop |

---

## 7. Editing Rules

1. **Hook in first 2 seconds, no exceptions.** Cold open, no logo intro.
2. **Cut every time the speaker stops for breath.** Dead air = swipe-away.
3. **Always something on-screen text-wise during voiceover** — text reinforces audio.
4. **Subtitles burned in.** Most viewers watch muted.
5. **End with a question or "follow"** — never a long outro.
6. **No more than 1 channel logo per video** (end card only, ~1 sec).

---

## 8. Locked AI Prompt Block

Paste this **exact string** at the top of every animation prompt. It locks visual consistency across videos.

```
2D animated cat character, BrainCatAI style:
cream/beige fur (#F5E1B8), warm white belly,
oversized cyan-blue eyes (#3FD0F2) with glossy highlights,
small dark grey spot on left ear, expressive cartoon proportions,
soft flat shading, charcoal outlines, vertical 9:16 composition,
vibrant playful colors, clean background, no text in image.
```

Then append the per-shot description after this block.

### Negative prompts (always include)

```
realistic cat, photorealistic, multiple cats,
low quality, blurry, distorted face, extra limbs,
watermark, text, logo, ugly, scary, aggressive expression
```

---

## 9. Editorial Voice (Writing Style)

### Do

- Open with a contradiction or shocking fact ("The sky isn't actually blue.")
- Use "you" — speak directly to the viewer
- Short sentences. Punchy rhythm.
- Use one analogy per video — make the abstract concrete
- End with a teaser or question

### Don't

- Start with "Hi guys, today we're going to talk about…"
- Use jargon without immediate plain-English translation
- Apologize ("Sorry this is complicated…")
- Pad with "umm" or filler
- Promise more than the video delivers (clickbait that under-delivers)

### Vocabulary tier

- 8th-grade reading level. If a 13-year-old wouldn't get it, simplify.
- Exception: when teaching a *new* term, define it on screen + voice.

---

## 10. Title & Thumbnail Patterns

### Title formulas (proven for Shorts)

- `Why [thing] is actually [surprise]`
- `You've been [doing X] wrong`
- `[Famous thing] is a lie`
- `What if [extreme]?`
- `The reason [thing] will shock you`

**Length:** 40–60 characters. Add 🐱 at the end for brand recognition.

### Thumbnail recipe

1. Cat face at 60% scale, expressive (shock/wow/wink)
2. **2–4 words max** in Electric Yellow with charcoal stroke
3. One iconic visual element (planet, brain, equation) at edge
4. Charcoal or Midnight background
5. No clutter — readable at thumbnail size

---

## 11. Don'ts (Brand Killers)

- ❌ Photorealistic cat
- ❌ Slow openings ("Hello everyone…")
- ❌ More than 1 idea per video
- ❌ Politics, controversy, NSFW
- ❌ AI hallucinated "facts" without source
- ❌ Mixing this cat with other characters as recurring co-stars (guests OK, but the cat is alone)

---

## 12. Versioning

- v1.0 — Initial style guide
- Update this file when a rule changes. Add a note in the [content-ideas](./content-ideas.md) or specific script if it's a one-off exception.
