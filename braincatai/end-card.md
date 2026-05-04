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
2D, flat, anime, cel-shaded, photorealistic cat, multiple cats, low quality, blurry, distorted face, extra limbs, missing glasses, missing collar, missing heart tag, watermark, ugly, scary, aggressive expression, mouth open as if talking, lip-sync, talking cat
```

---

## 🎨 Image prompt (Nano Banana)

Use this to generate the still that Veo 3 will animate. Background can be neutral warm OR matched to the video's main location (recommended: neutral warm glow so the end card works on every video).

```
Cute orange tabby kitten named Brain, big round sparkling green eyes, small thin round gold-framed glasses, brown leather collar with gold heart-shaped tag engraved "Brain", soft fluffy orange fur with darker tabby stripes, pink nose, long white whiskers, Pixar 3D render style, cinematic lighting, 4K, vertical 9:16 composition. Brain sitting centered facing camera, both front paws raised in a friendly mid-wave gesture, big warm smile in the eyes (mouth closed), gold heart-shaped collar tag glinting prominently. Above his head: large bold cartoon text "THANKS FOR WATCHING" in bright Electric Yellow #FFD23F with thick charcoal #2A2A2A stroke, slight playful tilt of 3 degrees. To the bottom-left of Brain: a floating 3D YouTube-style LIKE button (red thumbs-up icon inside a rounded button, soft outward glow). To the bottom-right of Brain: a floating 3D SUBSCRIBE button (red rectangular button with white text "SUBSCRIBE" and a small bell icon, soft outward glow). Soft warm honey-colored ambient background with gentle bokeh, peaceful celebratory mood.
```

---

## 🎬 Animation prompt — **Short variant (3 sec stinger)**

Use this when you want the end card right after Scene 8's wink and need to keep total runtime ≤ 60 sec.

```
SHOT: Static medium shot, eye-level, Brain centered.

TIME 0–1s: Brain raises both front paws and gives a warm friendly two-paw wave with a small bounce. Big smile in the eyes.

TIME 1–2s: The "THANKS FOR WATCHING" text bounces in from the top with a soft pop and settles with a gentle wobble. Simultaneously the LIKE button (bottom-left) and SUBSCRIBE button (bottom-right) bounce in from off-screen and pulse once each — LIKE pulses with a tiny "+1" spark, SUBSCRIBE pulses red with a small bell-ring shimmer.

TIME 2–3s: Brain holds the wave pose with a slow warm blink, gold heart tag glints once.

MOUTH RULE (strict): Mouth stays completely closed the entire 3 seconds. No lip-sync. No chewing motion. No chattering. No mouth movement of any kind. All emotion comes through eyes, ears, whiskers, and the wave gesture.

STYLE: Pixar 3D render, cinematic warm lighting, vertical 9:16, soft depth of field.
```

---

## 🎬 Animation prompt — **Full variant (6 sec standalone outro)**

Use this when you want a longer, more polished closing — standalone outro, or when video runtime allows.

```
SHOT: Static medium shot, eye-level, Brain centered, frame includes Brain plus space for buttons and text.

TIME 0–1.5s: Brain raises both front paws and gives a warm friendly two-paw wave (small bounce on each side). Big smile in the eyes. Gold heart tag glints softly.

TIME 1.5–3s: The "THANKS FOR WATCHING" text bounces in from the top with a soft pop, lands, and settles with a gentle wobble. Brain glances up at the text with a happy nod.

TIME 3–4.5s: The LIKE button (bottom-left) bounces in from off-screen and pulses bright with a small "+1" sparkle. Half a beat later the SUBSCRIBE button (bottom-right) bounces in and pulses red with a tiny bell-ring shimmer.

TIME 4.5–6s: Brain winks slowly at camera, raises one paw to point first at the LIKE button then at the SUBSCRIBE button. Soft warm light pulses around him.

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
