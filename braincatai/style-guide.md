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

## 2b. The Human (Brain's owner — locked character)

User noted 15 мая 2026: when a script needs a human in frame (lap, hand, head, silhouette), Nano Banana / Veo 3 used to drift between scenes — one scene shows a brunette woman, the next a different woman or even a man. This **breaks the illusion that Brain has ONE owner**. Lock the human the same way Brain is locked.

### The Locked Human spec (paste verbatim into every scene that includes a human)

Updated 16 мая 2026 after recurring man/woman swap in Nano Banana — strengthened with explicit female markers + anti-male negatives baked into the prompt body (not relying on reference image).

```
LOCKED HUMAN OWNER (same identity in every scene of this video — identical render every time): an adult WOMAN in her early 30s, Brain's owner — slim FEMININE build with narrow shoulders and soft feminine silhouette (NEVER male, NEVER a man, NEVER broad-shouldered, NEVER muscular). Long flowing CHESTNUT-BROWN wavy hair, mid-back length, soft natural volume, clearly cascading down her back (NEVER short hair, NEVER dark/black hair, NEVER blonde, NEVER grey, NEVER bald). Soft cream-colored long-sleeve V-neck sweater (NEVER a hoodie, NEVER dark clothing). Pale-medium skin tone. Pixar 3D cartoon style perfectly matching Brain's render. Face FULLY turned away from camera at all times — NO face, NO profile, NO chin, NO mouth, NO eyes, NO eyebrows, NO ear visible at any moment.
```

**Always append to the Negative prompts block** of any script that includes a human:

```
man, male figure, male owner, masculine build, broad shoulders, muscular body, short hair, dark hair, black hair, brown short hair, blonde hair, grey hair, bald head, beard, mustache, hoodie, dark clothing, different person between scenes, different owner, multiple owners, gender swap, swapped character
```

**HUMAN RULE template for Veo 3 prompts** (paste in every Veo prompt with the human):

```
HUMAN RULE (strict — LOCKED OWNER, female, same identity across the entire video): The owner is an adult WOMAN in her early 30s — slim feminine build, long chestnut-brown wavy hair (mid-back length, cascading down her back), soft cream V-neck sweater. NEVER male, NEVER a man, NEVER short hair, NEVER dark/black hair, NEVER broad-shouldered, NEVER bald. Face FULLY turned away from camera the entire 7 seconds — NO face, NO profile, NO chin, NO mouth, NO eyes, NO ear visible at any point. Stays completely still — only Brain moves.
```

### Why she must NEVER show her face

- Removes AI face-artifact risk (drift between scenes is most visible in faces)
- Keeps the channel feeling universal — every viewer projects themselves onto the owner
- Avoids face-rights / likeness concerns

### Allowed visible parts (rotate per scene)

| Scene type | Visible part |
|------------|-------------|
| Lap / seated | Back of head + hair + shoulder + sweater + hands in lap |
| Headbutt / cheek-rub | Side of neck / jaw zone only (NO face) |
| Hand / wrist scenes | Hand + wrist + sweater cuff only (no body above wrist) |
| Sleeping on chest | Torso + collarbone + sweater, head CROPPED OFF above frame line |
| Walking away | Back of head + hair + sweater + (sometimes) lower body |
| Thought-bubble / iris | Stylized back-of-head silhouette in cartoon overlay only |

### Reference workflow (Nano Banana / Veo 3)

1. **First successful render** of the human in any scene → save as `assets/owner-reference.png`
2. **Every subsequent scene** with the human → attach this image as character reference in Nano Banana before running the prompt
3. **Always include the locked spec text above** in the prompt body — even with reference image attached, the text spec is anti-drift insurance

### What changes per scene (does NOT break the lock)

- Pose (sitting / lying / walking)
- Visible angle (which body part is in frame)
- Hand position
- Whether she's holding something

### What MUST stay constant

- Hair: chestnut-brown, mid-back length, wavy
- Sweater: cream-colored, long-sleeve, V-neck
- Build: slim feminine
- Style: Pixar 3D cartoon (not photo)
- Always turned away / face never visible

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

### 5c. Make Brain alive — action over poses (retention rule)

Static talking-head Brain kills retention. Brain is a curious energetic kitten — **every scene needs a clear action beat, not just an emotion held for 7 seconds**. Viewers swipe away when nothing physically happens.

**Action vocabulary to use in prompts:**

| Beat type | Verbs |
|-----------|-------|
| Snap reactions | pounces, lands, recoils, flinches, jumps back, snaps head, double-takes, fur poofs, ears snap back, tail puffs |
| Investigations | sniffs, paws at, taps, pokes, peers, leans, tilts head, follows with eyes |
| Movement | scampers, dashes, darts, leaps into frame, slinks, pivots, circles |
| Play | swats, stalks, crouches, springs, play-bows, chases (off-camera) |
| Comedy beats | freeze-frame mid-air, slow recover, slow blink double-take, exaggerated shrug |

**Anti-vocab (drop from prompts — they read as static):**

- "sits and looks at camera"
- "has a [emotion] expression"
- "holds eye contact"
- "maintains the pose"
- "stays still while X happens around him"

If your prompt could describe a stuffed-animal-on-a-stick, rewrite it.

**Stack 2–3 micro-motions per scene** (overlap them on the timeline):

> Bad: "Brain sits with curious expression."
> Good: "Brain's tail flicks twice → ears swivel forward → he leans in slightly → eyes dart to the side → blink → looks back at camera."

**Reaction shots > pose shots.** Brain should react to something — an off-camera sound, an on-screen prop, a sudden glow, a falling object. Reactions feel alive; poses feel posed.

**Pattern interrupt (exactly one per video):** somewhere in the 8 scenes, do something visually surprising — sudden zoom, freeze-frame with screen-flash, Brain breaks the fourth wall with a knowing wink, a prop suddenly appears/transforms, quick speed-ramp (slow → fast). Place it on the twist or payoff beat. Used once, it spikes retention; used more, it loses power.

**Beat-by-beat punch checklist (apply to every scene):**

| Beat | Required punch element |
|------|------------------------|
| HOOK (Sc 1) | Snap reaction — eyes pop / fur poof / jaw drop / head whips around. The first 2 seconds must startle. |
| Curiosity gap (Sc 2) | A specific micro-action (paw raises, head tilt, tail curl into question mark) — never just "thinks" |
| Setup (Sc 3) | Brain physically interacts with the explanatory prop (swats chart, points dramatically, jumps onto desk) |
| Build-up (Sc 4) | Anticipation — Brain crouches, pauses, freezes, builds tension |
| Core (Sc 5) | The big visual payoff — transformation / reveal / movement spike |
| Twist (Sc 6) | Pattern interrupt — pupil shape changes, hearts appear, color shift, freeze flash |
| Bonus (Sc 7) | Callback or visual joke — small physical comedy beat |
| CTA (Sc 8) | Wave + personality — ear flick during wave, tail curl, slow blink, soft meow |

**Per-script test:** read the 8 animation prompts in sequence. If you can't picture distinct physical actions in each, rewrite.

### 5d. Visualize the VO literally — show, don't pose (credit-saver rule)

**If the VO names a concrete thing or action, the visual must literally show it.** Don't waste Veo 3 credits on generic "Brain sits with X expression" shots when the VO is describing something specific that can be shown.

**Examples:**

| VO line | ❌ Lazy visual | ✅ Literal visual |
|---------|----------------|--------------------|
| "Your cat licks your hair" | Brain on a bed looking smug | Brain mid-lick on a strand of human's hair (face turned away) |
| "Mother cats lick kittens to clean them" | Brain looking warmly at camera | Holographic cartoon of mother cat licking a tiny kitten |
| "Your cat thinks YOU are a clumsy kitten" | Brain with caring expression | Thought-bubble above Brain showing a cartoon clumsy kitten failing to groom itself |
| "Cats stretch like a noodle in a black hole" | Brain looking surprised in space | Brain's body literally stretched 4× into a noodle |
| "Cats slow blink to say 'I love you'" | Brain looking at camera lovingly | Brain performing a deliberate slow blink + tiny heart pupils |
| "Scientists tested it" | Brain looking thoughtful | Brain in lab coat with chart/diagram of the experiment |

**Tools to literalize abstract VO without rendering "multiple cats":**

- **Holographic floating illustration** beside Brain (cartoon stylized, never photoreal — used for "mother cat licks kitten", "cats spread across the planet", scientific diagrams)
- **Thought-bubble above Brain's head** (used for what Brain is thinking — "your cat thinks YOU are a clumsy kitten", "cat dreams of mice")
- **Reflection in glasses / mirror / water** (used for showing the human / showing what Brain sees)
- **Off-frame human (face turned away)** (for VO lines that involve the viewer/human directly)
- **Costume on Brain** (scientist / detective / chef / explorer / saber-tooth / Egyptian — see §2 thematic costumes)

**Why this matters:**

1. **Retention** — viewers stay when each scene visually delivers a fresh idea
2. **Credits** — Veo 3 clips cost real money; a generic talking-head is a wasted clip
3. **Memorability** — viewers remember the visual moment, not the text on top of it
4. **Algorithm** — distinct frames per scene → higher engagement signal → more reach

**Per-scene check:** open every script's animation prompt next to its VO line. Ask: *if I muted the audio, would a viewer still understand what's being said from the visual alone?* If no, rewrite the visual.

---

## 6. Audio

### Voiceover

- **Voice:** Energetic, curious, slightly playful (think science YouTuber, not documentary narrator)
- **Pace:** 120–140 wpm — fast enough to feel urgent, slow enough to follow
- **TTS option:** Google Vids TTS "Adam" or "Charlie"
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

Updated 16 мая 2026 after Veo 3 introduced phantom 3rd ear + chubby adult-cat drift in bathroom Sc 4 video render. Tightened with kitten-age proportions + EXACTLY 2 EARS lock + anti-artifact tokens.

```
Cute orange tabby kitten named Brain (8-10 week old kitten, NOT adult,
NOT chubby, NOT pudgy — slender petite kitten body with small chest,
slim torso, delicate proportions, small paws), big round sparkling VIVID
EMERALD GREEN eyes (bright pure emerald green iris #3DDC84 — NOT
brown, NOT amber, NOT yellow, NOT hazel, NOT golden), small thin
round gold-framed glasses, brown leather collar with gold
heart-shaped tag engraved "Brain", soft fluffy orange fur with
darker tabby stripes, pink nose, long white whiskers, EXACTLY 2 EARS
(one left, one right — both pointed perky triangle kitten ears,
perfectly symmetric, NO third ear, NO extra fur tuft, NO ear-shaped
artifact on head), Pixar 3D render style, cinematic lighting, 4K,
vertical 9:16 composition.
```

Then append: **the locked scene/world block for this video** (see §8b) **+ the per-shot action and expression**.

### ANATOMY PRESERVATION RULE (paste verbatim in every Veo 3 prompt)

Veo 3 can morph anatomy during the 7-second animation even if the input image is clean. Add this rule to every Veo 3 prompt to lock Brain's anatomy through animation:

```
ANATOMY PRESERVATION RULE (strict — Veo must NOT morph Brain): Brain's anatomy must stay perfectly stable through the entire 7 seconds — EXACTLY 2 ears (one left, one right, perfectly symmetric, NO phantom third ear appearing during animation, NO extra fur tuft on head, NO ear-shaped artifact materializing in any frame), exactly 4 paws (2 front + 2 back, NO 5th paw, NO extra limb), kitten body proportions held constant (slender petite 8-week-old kitten, NEVER morphing into chubby adult cat, NEVER expanding chest, NEVER changing body size).

EAR SHAPE & SIZE LOCK (strict — most important, added 16 мая 2026 after bathroom Sc 4 video showed ears elongating frame-by-frame into bat/vampire shape): Brain's ears MUST stay IDENTICAL in shape and size to the input image throughout all 7 seconds — small rounded kitten triangle ears, NEVER growing taller frame-by-frame, NEVER elongating into pointy bat-shape, NEVER stretching upward, NEVER becoming adult cat ears, NEVER morphing into vampire/devil ears. If the input image shows small soft kitten ears at frame 0, the ears MUST be the EXACT same small soft kitten ears at every subsequent frame — zero ear-size drift, zero ear-shape drift, zero ear-position drift.

Brain's identity must be IDENTICAL to the input image throughout — same face, same fur saturation, same eye color #3DDC84, same glasses position, same collar. NO character drift, NO off-model frames, NO anatomy morphing through animation.
```

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

User noted 15 мая 2026 (twice): environment drifts between scenes in the same location. In Sc 1 the rug is plain sage-green; in Sc 2 it suddenly has a pattern. In Sc 1 there's one snake plant by the window; in Sc 4 the plant is missing or replaced by a different species. This breaks the illusion of "one room" and confuses viewers.

The fix is **strict prop-locking** + **verbatim location paste**.

### The rules — non-negotiable

1. **Pick 1–3 locations max per video.** More than that breaks visual flow.
2. **Lock each location as a named block** at the top of the script with a **single descriptive paragraph that lists every prop with its exact position, color, count, and pattern**.
3. **Identical wording = identical look — PASTE VERBATIM.** If Sc 1 and Sc 5 share a location, the FULL location block must appear character-for-character identical in BOTH image prompts. **NEVER abbreviate to "Same living room"** — that's the bug. Nano Banana imagines fresh details when given short input.
4. **Lock props by:**
   - **Exact color** (not "green rug" — say "sage-green #8FA88B" or "plain sage-green woven")
   - **Pattern** (or NO pattern — explicit: "plain weave, no pattern")
   - **Count** (one snake plant, not "some plants")
   - **Species/material** (snake plant Sansevieria specifically, not "leafy plant")
   - **Position** (on the right / center / by the window — same in every scene)
5. **The CTA scene (Sc 8 universal) is exempt** — it uses neutral bokeh on purpose to be reusable.
6. **Group scenes by location** in the script's Scene → location map so it's obvious which scenes share a setting.

### Prop-lock checklist for each location

When writing a location block, lock:

- [ ] **Floor** — material + tone (e.g. "warm honey-amber wooden floorboards")
- [ ] **Walls** — color (e.g. "soft cream-painted walls")
- [ ] **Main furniture** — type, color, position (e.g. "cream linen armchair on the RIGHT with a folded amber knit throw")
- [ ] **Rug** — exact color, weave, pattern (e.g. "plain sage-green woven rug, NO pattern, in the center")
- [ ] **Window** — type, position, light direction (e.g. "tall window on the LEFT with sheer linen curtains, soft warm afternoon daylight from the left")
- [ ] **Plant(s)** — species + count + position (e.g. "ONE leafy snake plant — Sansevieria — with 5-7 upright sword-shaped dark-green leaves with lighter variegated stripes, beside the window")
- [ ] **Side props** — type + count + position (e.g. "ONE small wooden side-table on the LEFT holding ONE brass desk lamp (OFF) and ONE small open book lying face-down")
- [ ] **Wall art** — present or NOT (e.g. "NO wall art" or "ONE framed nature print in soft focus on the back wall")
- [ ] **Lighting** — direction + temperature (e.g. "soft warm honey-amber ambient with daylight bloom from the left")
- [ ] **Atmosphere** — depth of field, mood (e.g. "cozy lived-in atmosphere, shallow depth of field")

If a prop is NOT mentioned in the locked block, it must NOT appear in any scene's image. If a prop IS mentioned, it MUST appear in every scene's frame (when the angle allows) — same color, same count, same position.

### Example — properly locked location

```
INT. COZY LIVING ROOM — DAY. Cozy modern living room. WALLS: soft cream-painted. FLOOR: warm honey-amber wooden floorboards. RUG: plain sage-green woven rug (no pattern, no border) in the center of the floor. ARMCHAIR: ONE low cream linen armchair on the RIGHT side of frame with ONE folded amber knit throw blanket draped on its arm. SIDE-TABLE: ONE small wooden side-table on the LEFT side of frame holding ONE brass desk lamp (OFF, lampshade cream-colored) and ONE small open book lying face-down beside the lamp. WINDOW: ONE tall window in the BACKGROUND with sheer linen curtains letting in soft warm afternoon daylight from the upper-right. PLANT: ONE leafy snake plant (Sansevieria) with 5–7 upright sword-shaped dark-green leaves with lighter variegated cream-green stripes, positioned in a small terracotta pot BESIDE the window on the floor. NO other plants. NO wall art (clean cream wall behind). LIGHTING: soft warm honey-amber ambient with daylight bloom from the window. Cozy lived-in atmosphere, shallow depth of field — armchair and window slightly soft-focus.
```

### What to do in each image prompt

```
[Locked Brain block from §8]
[Locked Human block from §2b if a human is in this scene]
[The FULL location block above — copy-paste VERBATIM, do not abbreviate]
[Per-shot framing: MEDIUM CLOSE-UP, eye-level, etc.]
[Per-shot action: Brain mid-leap onto armchair, etc.]
```

### Verification before generation

Before pasting the prompt into Nano Banana, eyeball-check:

1. Is the full location block present (not "Same living room")?
2. Are the rug / armchair / plant / side-table / lamp wording exactly the same as previous scenes?
3. If something must change (e.g. armchair moved out of frame because we cut wider), state it explicitly: "the cream armchair is NOT in this frame" — don't just omit silently.

### Why this matters for monetization

YouTube algorithm scores **brand consistency**. When the same set appears identical across scenes, viewers perceive professional production quality → higher watch-through → algorithm boost. Drift = amateur-looking = swipe-away.

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

---

## 13. Typography Lock (on-screen text — numerals, overlays, captions, thumbnails)

Locked 16 мая 2026 after typography drift made overlays inside one video feel like cuts from different videos (one scene's "3" was rounded pastel-yellow sans, another scene's "1. GUARD" was a sharp serif outline). All on-screen text in a single video — and ideally across the channel — must share ONE font family + ONE color palette + ONE style treatment.

### Canonical channel-wide typography lock

| Element | Spec |
|---------|------|
| **Font family** | Rounded geometric sans-serif (Pixar-friendly cartoon font). Reference: **Nunito Bold / Quicksand Bold / Fredoka One** — soft rounded terminals, no sharp serifs, no hand-drawn brush. |
| **Weight** | Bold (700) for primary overlays; Semibold (600) for secondary lower-thirds |
| **Case** | ALL CAPS for hooks/numerals/category labels ("EVERY TIME", "1. GUARD", "BLINK = SOUND"). Title Case acceptable for longer captions only. |
| **Primary fill color** | Soft pastel-yellow `#FFE066` (warm friendly, matches Brain's emerald-on-cream palette) |
| **Secondary fill color** | Cream-white `#FFF8E7` for lower-thirds against warm backgrounds |
| **Accent fill (thumbnails only)** | Electric Yellow `#FFD23F` for thumbnail title plate |
| **Stroke / outline** | Solid charcoal `#2B2B2B` outline, 4–6px (scales to text size). Keeps text readable on any background. |
| **Drop shadow** | Soft black 30% opacity, 4px Y-offset, 8px blur — subtle depth only, NEVER a hard offset shadow. |
| **Numerals style** | Same font family — cartoon rounded sans bold pastel-yellow with charcoal stroke. NEVER serif, NEVER hand-drawn, NEVER different font from the captions. |
| **Sparkle / particle accents** | Soft white sparkle particles around important numerals (`"3"`, `"#1"`) — keep particle style consistent across all videos. |
| **Forbidden** | Sharp serif fonts, brush-script fonts, Comic Sans, Papyrus, Impact-style football fonts, gradient text fills, neon/metallic text, multiple different fonts in one video |

### What this applies to (all must use the spec above)

1. **In-image cartoon numerals** baked by Nano Banana — "1", "2", "3" in curiosity-gap and build-up scenes (e.g. `_universal-scene-8.md`, `why-cats-follow-bathroom.md` Sc 2)
2. **Lower-third category captions** added in Google Vids — "1. GUARD", "2. SEPARATION", "3. TERRITORY", "REASON #1", etc.
3. **In-video overlay phrases** — "EVERY TIME", "BLINK = SOUND", "VERIFY", "SAY THEIR NAME", "ADOPTED ✓", "TOP SCORE"
4. **Chart labels in lab scenes** (Sc 3 scientist) — "HUMAN 20Hz–20kHz", "CAT 48Hz–85kHz", "1. GUARD" axis labels
5. **Burn-in subtitle font** (top third, max 4 words) — same Bold rounded sans, slightly smaller
6. **Thumbnail title plate** — same font family, Electric Yellow `#FFD23F` accent fill, larger weight, thicker stroke

### How to specify in image prompts (Nano Banana)

When the prompt includes ANY on-screen text or numeral, paste this typography lock into the prompt body verbatim:

```
TYPOGRAPHY LOCK (strict — same font in every overlay across this video and the channel): All on-screen text/numerals rendered in BOLD ROUNDED GEOMETRIC SANS-SERIF font (Pixar cartoon style, Nunito Bold / Fredoka One look — soft rounded terminals, NO serifs, NO brush-script, NO hand-drawn). Fill color: soft pastel-yellow #FFE066. Solid charcoal #2B2B2B outline 4-6px. Soft black drop-shadow 30% opacity. ALL CAPS. NEVER use a serif font, NEVER use a brush font, NEVER mix multiple fonts.
```

And append to the negative prompts:

```
serif font, hand-drawn text, brush-script font, Comic Sans, Papyrus, Impact font, gradient text, neon text, metallic text, multiple fonts, mixed typography, sharp serifs on numerals, calligraphy
```

### How to specify in Google Vids overlays

When adding lower-thirds / category captions / overlay phrases in Google Vids:

1. Font family: **Nunito Bold** (or Fredoka One if Nunito unavailable)
2. Fill: `#FFE066` (or `#FFF8E7` if background is warm)
3. Stroke: `#2B2B2B` outline 4-6px
4. Drop shadow: subtle black 30% 4px/8px
5. Animation: gentle fade-in (0.3s) + pop-scale-up 1.05× hold + fade-out (0.3s) — same micro-animation for every text element

### Verification before generation / before publish

- [ ] Open the previous published video of the channel — is the new video's text in the same font family?
- [ ] Open Scene 2 numeral + Scene 4 lower-third + thumbnail title — all three use the same font?
- [ ] If a chart label is added in Sc 3, does it match the in-image numerals from Sc 2?
- [ ] Negative prompts include the typography forbidden list?

### Why this matters

Brand consistency is the cheapest retention lever — viewers subconsciously recognize a channel by its typography before its content. Mixed fonts inside one video feel "unfinished" or "compiled from different sources" → trust drops → swipe-away rate goes up. Locking the font is a 0-cost retention boost.

---

## 📝 Known issues + planned fixes (TODO — apply on next batch)

User feedback: Brain looks **slightly different across scenes of the same video** — sometimes chubbier (Sc 2 of hair-licking), sometimes more adult/realistic (low-angle CU like Sc 4), sometimes off-color (overhead like Sc 7). This is classic AI character drift between independent generations.

### Root causes
- The Locked Brain prompt is short (no body proportions, no age, no saturation lock)
- Each Nano Banana generation is independent — text-only locking can't perfectly hold a character
- Camera angles (low / overhead / wide) bias the AI toward chubby / adult / faded interpretations

### Planned fixes (apply when revising the style guide / template)

**A. Extend the Locked Brain prompt** with proportion + age + saturation locks:

```
Cute orange tabby kitten named Brain — YOUNG KITTEN (~4 months equivalent, NOT adult, NOT teenage), small lean kitten body (NOT chubby, NOT plump, NOT fat), Pixar kitten proportions (large head + small slender torso + plump cheeks + small button nose), big round sparkling VIVID EMERALD GREEN eyes (#3DDC84) at ~30% of face area (kitten-baby proportions), small thin round gold-framed glasses, brown leather collar with gold heart-shaped tag engraved "Brain", soft fluffy orange fur — saturation locked at medium-warm tabby orange #F2994A primary with burnt sienna #B65A2C stripes (NOT brighter, NOT darker, NOT washed out), pink nose, long white whiskers, Pixar 3D render style, cinematic lighting, 4K, vertical 9:16 composition.
```

**B. Add a CONSISTENCY RULE block to every Veo 3 prompt** alongside EYE COLOR / ANATOMY / MOUTH:

```
CONSISTENCY RULE (strict): Preserve Brain's body proportions, fur saturation, and kitten-age appearance EXACTLY from the start frame. Do NOT age him up. Do NOT make him chubbier or thinner. Do NOT shift the fur color saturation between frames.
```

**C. Per-angle anti-drift guards**

- **Overhead / top-down shots:** add `"Brain stays in his normal lean kitten proportions at this angle — overhead view does NOT make him look chubby or fat. Fur saturation stays at medium tabby orange #F2994A even with the floor color reflecting light upward."`
- **Low-angle close-ups:** add `"Low angle does NOT make Brain look adult, imposing, or older — he stays as a young plump-cheeked kitten."`
- **Wide / pulled-back shots:** add `"Brain stays clearly recognizable as the same young kitten — at distance his body proportions and fur saturation must not drift."`

**D. Generate a Brain Reference Sheet (highest-leverage fix)**

Standard production move:
1. Generate ONE canonical Brain image — frontal portrait, neutral background, neutral light, perfect proportions
2. Save as `braincatai/assets/brain-reference.png`
3. For every new scene, use Nano Banana's **image-to-image / reference-image** feature with this canonical image as the reference
4. Result: drastically tighter character consistency across an entire video

This is the single biggest fix. Text-only character locks always drift; image-anchored locks drift much less.

### When to apply

Apply A + B + C **before the next batch of scripts**, or in a single sweeping refactor of style-guide.md / script-template.md. Apply D **before starting the long-form Cat Evolution video** — character consistency matters more there than in 60-sec Shorts.
