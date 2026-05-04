# End Card (Outro) — Brain Style

Reusable end-card asset. Drops in **after Scene 8** of any BrainCatAI Short. Brain waves, "Thanks For Watching" pops in, Like + Subscribe buttons bounce in.

> **Two length variants:** pick **Short (3 sec)** to keep video under 60 sec, or **Full (6 sec)** for a standalone outro.

---

## 🔒 Locked Brain Prompt (always prepend to image prompt)

```
Cute orange tabby kitten named Brain, big round sparkling green eyes, small thin round gold-framed glasses, brown leather collar with gold heart-shaped tag engraved "Brain", soft fluffy orange fur with darker tabby stripes, pink nose, long white whiskers, Pixar 3D render style, cinematic lighting, 4K, vertical 9:16 composition.
```

**Negative prompts (Nano Banana):**

```
2D, flat, anime, cel-shaded, photorealistic cat, multiple cats, low quality, blurry, distorted face, extra limbs, extra paws, five legs, six legs, both front paws raised, two paws raised together, missing glasses, missing collar, missing heart tag, watermark, ugly, scary, aggressive expression, mouth open as if talking, lip-sync, talking cat, duplicate text, repeated text, double labels, two subscribe buttons, two like buttons, "SUBSCRIBE" written twice, multiple labels, repeated words, stuttered text, garbled text, misspelled text
```

---

## 🎨 Image prompt (Nano Banana) — **DEFAULT: text-free, icons only**

Mentioning the words "LIKE" or "SUBSCRIBE" in an AI image prompt makes the model render them in **two places** — once on the button face and once as a label nearby. The cleanest fix: **don't put any text in the AI image at all**. Just generate Brain + two button-shaped objects with icons. Then add all text (THANKS FOR WATCHING / LIKE / SUBSCRIBE) as **overlays in Google Vids** where you have full font and animation control.

```
Cute orange tabby kitten named Brain, big round sparkling green eyes, small thin round gold-framed glasses, brown leather collar with gold heart-shaped tag engraved "Brain", soft fluffy orange fur with darker tabby stripes, pink nose, long white whiskers, Pixar 3D render style, cinematic lighting, 4K, vertical 9:16 composition. Brain sitting centered facing camera, ONLY his right front paw is raised in a friendly mid-wave gesture (the left front paw stays firmly on the ground, both back paws on the ground — total of 4 paws visible, NO extra limbs), big warm smile in the eyes (mouth closed), gold heart-shaped collar tag glinting prominently. To the bottom-left of Brain: a single floating 3D rounded red square button with a clean white thumbs-up icon centered on it, NO text or letters anywhere on or near the button, soft outward glow. To the bottom-right of Brain: a single floating 3D red rectangular button shape with a single white bell icon centered on it, NO text or letters anywhere on or near the button, soft outward glow. Empty negative space above Brain's head and around both buttons reserved for text overlays to be added later — keep that space clean and uncluttered. NO text, NO words, NO letters, NO labels anywhere in the image. Soft warm honey-colored ambient background with gentle bokeh, peaceful celebratory mood.
```

### Then add text overlays in Google Vids (after rendering)

| Overlay | Position | Style |
|---------|----------|-------|
| **THANKS FOR WATCHING** | Top of frame | Bangers font, Electric Yellow `#FFD23F`, charcoal `#2A2A2A` stroke, bounce-in animation |
| **LIKE** | Small text under thumbs-up button (optional — icon is recognizable) | White, Inter Bold, simple fade-in |
| **SUBSCRIBE** | White text on the red rectangle (centered over the bell icon shifts left) | White, Bangers, simple fade-in or pulse |

Generate Brain + buttons **once**, save as `assets/end-card-base.png`, then reuse for every video — text overlays are added per-video at edit time.

### 🛟 Alternative: with text rendered by AI (less reliable)

If you really want the AI to render the text directly (skipping Google Vids overlay step), use this prompt — but be ready to regenerate 2–3 times until the text comes out clean:

```
Cute orange tabby kitten named Brain, big round sparkling green eyes, small thin round gold-framed glasses, brown leather collar with gold heart-shaped tag engraved "Brain", soft fluffy orange fur with darker tabby stripes, pink nose, long white whiskers, Pixar 3D render style, cinematic lighting, 4K, vertical 9:16 composition. Brain sitting centered facing camera, ONLY his right front paw is raised in a friendly mid-wave gesture (the left front paw stays firmly on the ground, both back paws on the ground — total of 4 paws visible, NO extra limbs), big warm smile in the eyes (mouth closed), gold heart-shaped collar tag glinting prominently. Above his head: large bold cartoon text reading "THANKS FOR WATCHING" rendered EXACTLY ONCE in bright Electric Yellow #FFD23F with thick charcoal #2A2A2A stroke, slight playful tilt of 3 degrees. To the bottom-left of Brain: ONE single floating 3D rounded red square button with a clean white thumbs-up icon — NO words, NO letters, NO text labels of any kind on or near this button. To the bottom-right of Brain: ONE single floating 3D red rectangular YouTube subscribe button with the single word "SUBSCRIBE" rendered EXACTLY ONCE in clean white text directly on the button face — and a small bell icon also on the button — NO duplicate "SUBSCRIBE" text anywhere else, NO additional labels around the button. Total of THREE pieces of text in the entire image: "THANKS FOR WATCHING" (top), "Brain" engraved on collar tag, and "SUBSCRIBE" (on right button) — no other text exists anywhere. Soft warm honey-colored ambient background with gentle bokeh, peaceful celebratory mood.
```

---

## 🎬 Animation prompt — **Short variant (3 sec stinger)**

Use this when you want the end card right after Scene 8's wink and need to keep total runtime ≤ 60 sec.

```
SHOT: Static medium shot, eye-level, Brain centered.

TIME 0–1s: Brain raises ONLY his right front paw and gives a warm friendly side-to-side wave (two small waves). His left front paw stays firmly on the ground. Total of 4 paws visible — no extra limbs. Big smile in the eyes.

TIME 1–2s: The "THANKS FOR WATCHING" text bounces in from the top with a soft pop and settles with a gentle wobble. Simultaneously the LIKE button (bottom-left) and SUBSCRIBE button (bottom-right) bounce in from off-screen and pulse once each — LIKE pulses with a tiny "+1" spark, SUBSCRIBE pulses red with a small bell-ring shimmer.

TIME 2–3s: Brain holds the wave pose (one paw still raised, the other still on the ground) with a slow warm blink, gold heart tag glints once.

ANATOMY RULE (strict): Brain has exactly 4 paws — 2 front, 2 back. Only ONE front paw is raised at a time. The other front paw and both back paws stay on the ground. NEVER show 5 paws, extra limbs, or both front paws raised together.

MOUTH RULE (strict): Mouth stays completely closed the entire 3 seconds. No lip-sync. No chewing motion. No chattering. No mouth movement of any kind. All emotion comes through eyes, ears, whiskers, and the single-paw wave.

STYLE: Pixar 3D render, cinematic warm lighting, vertical 9:16, soft depth of field.
```

---

## 🎬 Animation prompt — **Full variant (6 sec standalone outro)**

Use this when you want a longer, more polished closing — standalone outro, or when video runtime allows.

```
SHOT: Static medium shot, eye-level, Brain centered, frame includes Brain plus space for buttons and text.

TIME 0–1.5s: Brain raises ONLY his right front paw and gives a warm friendly side-to-side wave (three small waves). His left front paw stays firmly on the ground. Total of 4 paws visible — no extra limbs. Big smile in the eyes. Gold heart tag glints softly.

TIME 1.5–3s: Brain lowers his right paw back to the ground. The "THANKS FOR WATCHING" text bounces in from the top with a soft pop, lands, and settles with a gentle wobble. Brain glances up at the text with a happy nod.

TIME 3–4.5s: The LIKE button (bottom-left) bounces in from off-screen and pulses bright with a small "+1" sparkle. Half a beat later the SUBSCRIBE button (bottom-right) bounces in and pulses red with a tiny bell-ring shimmer.

TIME 4.5–6s: Brain winks slowly at camera. He raises his right front paw ONCE (left paw stays on ground) and points first at the LIKE button, then sweeps the same paw to point at the SUBSCRIBE button. Soft warm light pulses around him.

ANATOMY RULE (strict): Brain has exactly 4 paws — 2 front, 2 back. At any moment, AT MOST ONE front paw is raised. The other front paw and both back paws always stay on the ground. NEVER show 5 paws, extra limbs, or both front paws raised together.

MOUTH RULE (strict): Mouth stays completely closed the entire 6 seconds. No lip-sync. No chewing motion. No chattering. No mouth movement of any kind. All emotion comes through eyes, ears, whiskers, and gestures. ONE optional soft single meow allowed at TIME 5.5s as the wink lands — single mouth motion, then closed again.

STYLE: Pixar 3D render, cinematic warm lighting, vertical 9:16, soft depth of field.
```

---

## 🎵 Audio cues for the end card

- 0:00 — soft "ta-da!" chime as Brain waves
- 0:01 (or 0:1.5 in full) — bouncy pop on "THANKS FOR WATCHING" text
- 0:01.5 (or 0:3 in full) — "ding!" on LIKE button + "tap!" on SUBSCRIBE button
- Final beat — one soft meow + light shimmer

Keep music **soft + uplifting**, fading out gently into silence.

---

## How to use this in Google Vids

1. Generate the Nano Banana image once, save as `assets/end-card-base.png`
2. Drop the image into Veo 3 with the Short or Full animation prompt → save as `assets/end-card-3s.mp4` or `end-card-6s.mp4`
3. **In every video assembly:** drop the chosen end-card clip after Scene 8
4. **Captions:** the "THANKS FOR WATCHING" text is already in the visual — no burn-in subtitles needed for this clip
5. **VO during end card:** none. Let the music breathe.

## When to use which variant

| Variant | Use when |
|---------|----------|
| **Short (3 sec)** | Default. Total video stays under 60 sec, algorithm-friendly. |
| **Full (6 sec)** | Special / pinned videos, milestone uploads, or when Scene 8 has been shortened to ~4 sec. |

---

## Style notes

- Brain's mouth stays closed (one optional meow in Full variant)
- Background is **neutral warm glow** so this clip works regardless of which location was used in the main video
- Uses brand colors: Electric Yellow (`#FFD23F`) text + Charcoal (`#2A2A2A`) stroke (per [style-guide.md §3](./style-guide.md#3-color-palette))
- LIKE + SUBSCRIBE buttons are YouTube-canonical red so viewers recognize them instantly
