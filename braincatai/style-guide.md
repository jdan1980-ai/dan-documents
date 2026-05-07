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

- **Opens his mouth as if talking.** Brain's mouth stays **closed** during voiceover. The narration is off-camera — Brain doesn't speak the words. He reacts with **eyes, ears, whiskers, body**. Mouth opening is allowed ONLY for: brief jaw-drop on shock (held), yawn (sleepy), or one soft meow on CTA — never repetitive open/close that mimics talking.
- **Raises both front paws at the same time.** Brain has exactly **4 paws** (2 front + 2 back). **AT MOST ONE paw is raised or extended at a time** — for waving, pointing, holding objects, gestures. The other 3 paws can be in **any natural pose** (sitting, tucked, draped, on a surface) — don't over-specify them. The only hard constraint is the count (4) and the single raise (1). Two-paw poses cause AI generation artifacts (5+ legs, extra limbs).
- Appears without **glasses** or **collar with gold heart tag** (signature elements — always on)
- Looks photorealistic or 2D-flat (always Pixar 3D render)
- Looks angry/aggressive — keep it warm and curious

### Thematic costumes (use only for matching scene topics)

When a scene's voiceover references a specific role (scientists, doctors, detectives, astronauts, chefs, etc.), Brain dresses for the role to visually reinforce the topic. The costume goes **on top of his locked elements** — collar, gold heart tag, and gold-framed glasses **must always remain visible**. Use sparingly: usually one themed scene per video, never the whole video.

| Voiceover topic | Brain's outfit | Setting |
|------------------|----------------|---------|
| "Scientists tested it…" / studies / experiments | Tiny white **lab coat** over collar (collar visible) | Cozy micro-lab — desk, microscope, clipboard, pastel wall chart |
| "Doctors found…" / medical / health | Small white **doctor's coat** + tiny stethoscope around neck | Cozy clinic corner |
| "Detectives discovered…" / investigation / mystery | Small **trench coat** + tiny magnifying glass in paw | Dim cozy study with case board |
| "Astronauts found…" / space / NASA | Tiny **space suit** with helmet open | Soft starlit window backdrop |
| "Historians proved…" / ancient / history | Tiny **scholar's robe** + small scroll | Cozy library nook |
| "Chefs say…" / food / cooking | Small white **chef's hat** + tiny apron | Warm cozy kitchen |

**Rules for every costume:**
- Collar with gold heart tag stays visible at the neckline (NEVER covered)
- Gold-framed glasses stay on
- Costume is small, clean, Pixar-style — never realistic or sterile
- Add a `WARDROBE RULE (strict)` block in the Veo 3 prompt locking the costume + visibility of collar/glasses

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

### 5b. Scene variety & dynamism (retention rule)

Identical framing across 8 scenes = viewers swipe away. Every script must deliberately vary three axes per scene to keep eyes engaged:

**1. Shot size — rotate, never repeat back-to-back:**
- Extreme close-up (eye / mouth / paw detail)
- Close-up (face fills frame)
- Medium close-up (head + shoulders + collar tag)
- Medium (full body of Brain + immediate prop)
- Wide / establishing (Brain inside the location, smaller in frame)
- Overhead / top-down (rare, for impact)

**2. Camera motion — at least 3 different moves across 8 scenes:**
- Static (default — overuse = boring)
- Slow push-in (1–5 % over the clip — emotional moments)
- Slow pull-back (reveals more of the world)
- Slight dolly left or right
- Tilt up / down (when Brain looks up at something)
- Whip-pan transition (between scenes, not within)

**3. Brain's pose / angle — never two scenes in a row from the same angle:**
- Front-facing (camera looks at Brain head-on)
- 3/4 view (most flattering, default)
- Profile (side view — strong for action like cheek-rub, lick, telescope)
- From behind (over-the-shoulder showing what Brain is seeing)
- Low angle looking up (makes Brain feel authoritative — good for scientist scenes)
- High angle looking down (makes Brain feel small/cute — good for hook beats)

**Per-scene checklist (apply when writing every shot):**

- [ ] Is this shot size different from the previous scene's?
- [ ] Is the camera doing something different from the previous scene? (static is allowed but no more than 2 statics in a row)
- [ ] Is Brain's angle to camera different from the previous scene?
- [ ] Is something on screen always moving (tail flick, ear twitch, whisker twitch, blink, fur ripple, glow pulse)?
- [ ] Does the cut land on a VO beat or stress, not a fixed 7-sec interval?

**Anti-pattern (avoid):** 6+ scenes of "Brain sitting medium close-up facing camera" — even if expressions vary, the framing reads as a single static talking-head and retention drops.

**Pro tip:** Sketch the 8 shot sizes before writing prompts. A rhythm like CU → wide → low-medium → push-in CU → side profile → slow zoom CU → overhead → centered medium is far more dynamic than 8 medium-close-ups in a row.

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
Cute orange tabby kitten named Brain, big round sparkling VIVID
EMERALD GREEN eyes (bright pure emerald green iris #3DDC84 — NOT
brown, NOT amber, NOT yellow, NOT hazel, NOT golden), small thin
round gold-framed glasses, brown leather collar with gold
heart-shaped tag engraved "Brain", soft fluffy orange fur with
darker tabby stripes, pink nose, long white whiskers, Pixar 3D render
style, cinematic lighting, 4K, vertical 9:16 composition.
```

Then append: **the locked scene/world block for this video** (see §8b) **+ the per-shot action and expression**.

> ⚠️ **Eye color trap:** Warm/golden lighting often causes Nano Banana and Veo 3 to render Brain's eyes as brown/amber/hazel even though "green" is in the prompt. Always specify EMERALD GREEN with hex `#3DDC84`, repeat the green-eye reminder in the per-shot description, and include all wrong colors in negatives. For Veo 3, add an explicit `EYE COLOR RULE (strict)` block alongside ANATOMY and MOUTH rules.

### Negative prompts (always include)

```
2D, flat, anime, cel-shaded, photorealistic cat, multiple cats,
low quality, blurry, distorted face, extra limbs, extra paws,
five legs, six legs, both front paws raised, two paws raised together,
missing glasses, missing collar, missing heart tag, watermark,
text in image, logo, ugly, scary, aggressive expression,
mouth open as if talking, lip-sync, talking cat,
mouth movement, chattering,
brown eyes, amber eyes, yellow eyes, hazel eyes, golden eyes,
dark eyes, brown iris, amber iris, wrong eye color,
eye color tinted by lighting, warm-tinted eyes
```

### Animation prompt rule (Veo 3)

Veo 3 generates the cleanest motion when prompts are **structured by time** rather than written as a flowing paragraph. Use this template:

```
SHOT: [camera framing + movement] (e.g. "Static medium close-up, eye-level")

TIME 0–Xs: [Brain's pose / micro-movement]
TIME X–Ys: [main action]
TIME Y–Zs: [reaction / effect]
TIME Z–end: [closing beat]

EYE COLOR RULE (strict): Brain's eyes are BRIGHT EMERALD GREEN (#3DDC84) throughout the entire [N] seconds. NOT brown, NOT amber, NOT yellow, NOT hazel, NOT golden. Warm/golden lighting must NOT tint the iris brown or amber. The iris stays vivid emerald green even in shadow, even when half-closed during a slow blink.

ANATOMY RULE (strict): Brain has exactly 4 paws — 2 front, 2 back. NEVER show 5 paws or extra limbs. Don't over-specify paw positions in the prompt — just keep the count at 4.

MOUTH RULE (strict): Mouth stays completely closed the entire [N] seconds. No lip-sync. No chewing motion. No chattering. No mouth movement of any kind. All emotion comes through eyes, ears, and whiskers.

STYLE: Pixar 3D render, cinematic warm lighting, vertical 9:16, soft depth of field.
```

Exceptions to MOUTH RULE (state explicitly per shot when used, or Veo will default to closed):
- Brief held jaw-drop for shock (single beat, not repeated)
- Single yawn for sleepy/bored beat
- One soft meow at CTA (single mouth motion, then closed)

### Veo 3 prompt principles (apply to every scene)

1. **Timeline > flowing description.** Break the action into 2–4 timed beats. Veo struggles to sequence "look, then raise paw, then glow" in one sentence — it tries to do all three at once.
2. **Concrete physical details, not abstractions.** "Ears slightly forward, single whisker twitch" works. "Knowing look" doesn't.
3. **Camera always stated.** "Static medium close-up" / "Slow push-in" / "Slight dolly right". Veo defaults to weird camera moves if you don't lock it.
4. **One main action arc per shot.** A 7-second clip should have one big motion — not three. Stack 2–3 micro-beats around it (settling pose, the action, the closing blink).
5. **Hard mouth rule in its own block.** Never bury "mouth closed" inside a sentence with other actions — it gets ignored. Put it in a dedicated MOUTH RULE block with multiple repeated negations.
6. **Avoid metaphors in motion descriptions.** "Hidden button" → "soft glow under his paw, three pulses, small radius". "Like accepting a medal" → "raises paw, places flat on chest, holds for 1 second".
7. **Specify glow/light effects with numbers.** "Three pulses, small radius" not "a glowing pulse". "Cyan tint" not "soft color".
8. **End each clip with a held beat or blink.** Veo handles transitions between shots better when the end is calm rather than mid-motion.

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

### CTA variants (final voiceover line of every video)

The last line of every Short is a "follow Brain" sign-off, varied to match the topic. Pick one per video:

- `Follow Brain... for more cat secrets.` — cat psychology videos
- `Follow Brain... for more brain hacks.` — brain/psychology videos
- `Follow Brain... for more facts that break your brain.` — general "wow" facts
- `Follow Brain for more facts that tune up your brain.` — brain/health/wellness videos
- `Follow Brain... for more "wait, what?!" moments.` — surprise / mind-blow facts

Always lead with the topic-specific emotional close BEFORE the follow line (see existing scripts for examples).

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
- ❌ **Wrong eye color** — Brain's eyes must be BRIGHT EMERALD GREEN (`#3DDC84`), never brown, amber, yellow, hazel, or golden. Warm lighting must not tint the iris. Always include the eye-color spec + hex in image prompts and an `EYE COLOR RULE (strict)` block in Veo 3 prompts.
- ❌ **Brain opening his mouth as if talking / lip-syncing the voiceover** — Brain never speaks the lines. Mouth stays closed; reactions through eyes and body only.
- ❌ **Brain raising two paws simultaneously** — causes 5+ legs / extra limb artifacts. AT MOST ONE paw raised at a time. The other 3 paws can be in any natural pose — don't over-specify.
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
