# BrainCatAI — Style Guide

The single source of truth for the channel's visual, audio, and editorial style. Every script, prompt, and edit should pull from this file. Update it when something works (or fails) consistently.

---

## 1. Channel Identity

- **Name:** BrainCatAI
- **Tagline:** "Facts that break your brain. Explained by a cat."
- **Promise:** Every video, the viewer learns one mind-blowing thing in under 60 seconds.
- **Tone in one sentence:** Smart, playful, slightly sarcastic — like a curious friend, not a teacher.

---

## 2. The Cat (Main Character) — "Brain"

### Look

- **Name:** Brain
- **Species:** Cute orange tabby kitten
- **Body:** Round, plush kitten proportions — large head, small body
- **Fur:** Soft fluffy orange with **darker tabby stripes**, pink nose, long white whiskers
- **Eyes:** Big, round, **sparkling green**, glossy highlights — main acting tool
- **Glasses:** Small, thin, round, **gold-framed** — always on Brain
- **Collar:** **Brown leather** with a **gold heart-shaped tag** engraved "Brain"
- **Pupils:** Expressive — can go pinprick (shock), heart (love), spiral (confused), star (excited)

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

### What Brain NEVER does

- Speaks visibly (mouth syncing) — voiceover only, Brain *reacts*
- Appears without **glasses** or **collar with gold heart tag** (signature elements — always on)
- Looks photorealistic or 2D-flat (always Pixar 3D render)
- Looks angry/aggressive — keep it warm and curious

---

## 3. Color Palette

Lock these for **Brain's character only**. Backgrounds and environments are NOT locked — they're chosen per video and must stay consistent within that video.

| Role | Name | Hex | Use |
|------|------|-----|-----|
| Fur primary | Tabby Orange | `#F2994A` | Brain's fur base |
| Fur stripes | Burnt Sienna | `#B65A2C` | Tabby stripes |
| Belly | Warm Cream | `#FFE7C2` | Belly, chin, paws |
| Eyes | Sparkle Green | `#3DDC84` | Brain's eyes |
| Accessories gold | Brass Gold | `#D4A93A` | Glasses frame + heart tag |
| Collar | Saddle Brown | `#7A4E2D` | Leather collar |
| Brand text | Electric Yellow | `#FFD23F` | On-screen text, thumbnails |
| Hot accent | Coral Red | `#FF5C5C` | "Wow" / correction text |
| Outline | Soft Charcoal | `#2A2A2A` | Text stroke, shadows |

**Rules:**
- Brain's colors are **locked across every video**
- Background/environment colors are chosen **per video** based on the story (kitchen, wild grass, living room, etc.)
- Yellow + charcoal stroke text always works for thumbnails regardless of background
- Coral red ONLY for "wow" moments — keep it rare so it stays loud

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
- **Style:** **Pixar-style 3D render** — soft fur, cinematic lighting, shallow depth of field, 4K detail. Background is per-video, not locked to a single look.
- **Cuts:** Fast — average shot length **2–3 seconds** (longer = retention drop)
- **Transitions:** Whip pans, zooms, simple dissolves. No fancy wipes.
- **Brain's motion:** Always something moving — tail flick, ear twitch, whisker twitch, blink. **Never static for >1 sec.**

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

Paste this **exact string** at the top of every image prompt. It locks **only Brain's look** — the world/background is chosen per video.

```
Cute orange tabby kitten named Brain, big round sparkling green eyes,
small thin round gold-framed glasses, brown leather collar with
gold heart-shaped tag engraved "Brain", soft fluffy orange fur with
darker tabby stripes, pink nose, long white whiskers, Pixar 3D render
style, cinematic lighting, 4K, vertical 9:16 composition.
```

Then append: **the locked scene/world block for this video** (see §8b) **+ the per-shot action and expression**.

### Negative prompts (always include)

```
2D, flat, anime, cel-shaded, photorealistic cat, multiple cats,
low quality, blurry, distorted face, extra limbs, missing glasses,
missing collar, missing heart tag, watermark, text in image, logo,
ugly, scary, aggressive expression
```

---

## 8b. Scene Continuity (per-video world locks)

The locked block in §8 only describes **Brain**. Every script must define its own visual world at the top and reuse the **exact same wording** across scenes that share a location.

### The rules

1. **Pick 1–3 locations max per video.** More than that breaks visual flow.
2. **Lock each location as a named block** at the top of the script (e.g., `INT. KITCHEN — DAY` or `EXT. WILD GRASS — GOLDEN HOUR`) with a single descriptive paragraph.
3. **Identical wording = identical look.** If Scene 1 and Scene 5 are both in the kitchen, paste the *exact same* kitchen description into both image prompts. Don't paraphrase.
4. **The CTA scene (Scene 8) must match the world.** End in one of the locations already used in the video, in the same lighting and style. Never end in a generic "purple bokeh + confetti" outro — that breaks continuity.
5. **Group scenes by location** in the script's structure so it's obvious which scenes share a setting.

### Example location block

```
INT. COZY LIVING ROOM — DAY
Cozy modern living room with warm wooden floor, soft beige sofa
in background, large window with soft afternoon daylight from the
left, small green potted plant near the window, warm honey-colored
ambient light, slight depth of field with sofa softly out of focus.
```

Then in each scene's image prompt:

```
[Locked Brain block from §8]
[INT. COZY LIVING ROOM — DAY paragraph above, copy-pasted exactly]
[Per-shot action: e.g., "Brain walks forward and gently places a small
toy mouse on the wooden floor, looks up at camera with calm expression."]
```

---

## 9. Editorial Voice (Writing Style)

### Audience: everyone (kids and adults)

Every script must work for **a 9-year-old AND a 40-year-old**. Write the way you'd talk to a curious friend at a coffee shop — warm, simple, direct. Not a teacher, not a presenter, not a robot.

**The rule:** if a 9-year-old wouldn't immediately get a word, swap it.

| ❌ Don't say | ✅ Say instead |
|--------------|----------------|
| prey | food / mouse / bird |
| insult | mean / rude |
| starve | not have food |
| wavelength | type of light |
| atmosphere | air around Earth |
| scatter | bounce around |
| frequency | beat / vibration |
| domesticated | tamed |
| ancestors | great-great-grandparents |
| evolved | changed over a long time |

### Do

- Open with a contradiction or shocking fact ("The sky isn't actually blue.")
- Use "you" and "your cat" — speak directly to the viewer
- **Short sentences.** Punchy rhythm. One idea per sentence.
- Use everyday words a kid hears at home
- Use one analogy per video — make the abstract concrete
- End with a teaser or warm sign-off

### Don't

- Start with "Hi guys, today we're going to talk about…"
- Use jargon without immediate plain-English translation
- Use dark/scary words for kids' ears (starve, kill, die, brutal, savage)
- Apologize ("Sorry this is complicated…")
- Pad with "umm," "basically," "actually" (overused), or filler
- Promise more than the video delivers (clickbait that under-delivers)

### Tone: human, not robotic

Read your script out loud. If it sounds like a Wikipedia entry, rewrite it. It should sound like *one person telling another person something cool*.

- ❌ "Felines possess a sophisticated hunting instinct…"
- ✅ "Cats are amazing hunters."
- ❌ "This phenomenon is caused by Rayleigh scattering."
- ✅ "Tiny bits of air bounce blue light all over the place."

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

- ❌ 2D / flat / anime style — must be Pixar 3D
- ❌ Brain without **glasses** or **heart-tag collar** (signature elements)
- ❌ Wrong fur color (must be orange tabby, not grey/black/cream)
- ❌ **Locking a single brand background across all videos** (e.g., always purple bokeh) — backgrounds are per-video, not channel-wide
- ❌ **Different versions of the same room across scenes** — if Scene 1 and Scene 4 are both in the kitchen, they must look identical (same lighting, same furniture, same angle of light)
- ❌ **CTA in a generic confetti/bokeh world** that doesn't match the rest of the video — Scene 8 must take place in one of the locations already used
- ❌ Slow openings ("Hello everyone…")
- ❌ More than 1 idea per video
- ❌ More than 3 distinct locations in one 60-second Short
- ❌ Politics, controversy, NSFW
- ❌ AI hallucinated "facts" without source
- ❌ Recurring co-stars — Brain is alone (one-off guests OK)

---

## 12. Versioning

- v1.0 — Initial style guide
- Update this file when a rule changes. Add a note in the [content-ideas](./content-ideas.md) or specific script if it's a one-off exception.
