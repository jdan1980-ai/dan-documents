# Universal Scene 8 — Reusable CTA (Cat-Only)

> **Цель: сэкономить Veo 3 кредиты.** Этот Sc 8 генерится в Nano Banana + Veo 3 **ОДИН РАЗ**, сохраняется как `assets/universal-scene-8.mp4`, и дропается в Google Vids как Сцена 8 **во все cat-видео** канала.
>
> **Что меняется per-video:** только voiceover (записывается в ElevenLabs под конкретное видео). Визуал — один и тот же.
>
> **Локация:** нейтральная (теплый bokeh-фон без специфики комнаты) — чтобы не противоречил локациям предыдущих 7 сцен любого видео.

---

## 🎨 Image prompt (Nano Banana) — ОДИН РАЗ

```
Cute orange tabby kitten named Brain, big round sparkling VIVID EMERALD GREEN eyes (bright pure emerald green iris #3DDC84 — NOT brown, NOT amber, NOT yellow, NOT hazel, NOT golden), small thin round gold-framed glasses, brown leather collar with gold heart-shaped tag engraved "Brain", soft fluffy orange fur with darker tabby stripes, pink nose, long white whiskers, Pixar 3D render style, cinematic lighting, 4K, vertical 9:16 composition. NEUTRAL BACKGROUND — soft warm honey-amber bokeh background with no specific room identifiers, gentle out-of-focus warm ambient lighting, no furniture, no walls in focus, no location-specific props, soft warm halo around Brain, dreamy peaceful celebratory atmosphere, shallow depth of field. MEDIUM SHOT framing. Brain sits centered facing camera with a warm joyful expression, vivid emerald green eyes bright with affection, one front right paw raised in a friendly mid-wave gesture, the other front paw firmly on the ground, both back paws on the ground (total 4 paws visible), gold heart-shaped collar tag glinting prominently. Tail held in a soft happy upright curl behind him. Empty negative space at the top of the frame reserved for a per-video text overlay (e.g. "FOLLOW BRAIN") to be added in Google Vids if desired. Brain has 4 paws total — exactly 4.
```

**Negative prompts (Nano Banana):**

```
2D, flat, anime, cel-shaded, photorealistic cat, multiple cats, low quality, blurry, distorted face, extra limbs, extra paws, five legs, six legs, both front paws raised, two paws raised together, missing glasses, missing collar, missing heart tag, watermark, text in image, logo, ugly, scary, aggressive expression, mouth open as if talking, lip-sync, talking cat, mouth movement, chattering, brown eyes, amber eyes, yellow eyes, hazel eyes, golden eyes, dark eyes, brown iris, amber iris, wrong eye color, warm-tinted eyes, identifiable room, specific furniture, kitchen counter, bedroom bed, hallway door, lab equipment, bathroom tile, second cat
```

---

## 🎬 Animation prompt (Veo 3) — ОДИН РАЗ

```
SHOT: Static medium shot, eye-level, Brain centered. Slight slow PUSH-IN (~4% closer over 7 seconds). Brain has BRIGHT EMERALD GREEN eyes (#3DDC84) — not brown, not amber.

TIME 0–2s: Brain sits centered facing camera with bright happy vivid emerald green eyes, ears alert and forward. Tail does one slow happy flick. Gold heart tag catches the warm light once. The warm honey-amber bokeh background subtly shifts with soft light particles drifting.

TIME 2–5s: Brain raises ONLY his right front paw and gives a gentle friendly two-side-to-side wave. His left front paw stays firmly on the ground, both back paws stay on the ground (total 4 paws visible). Then Brain performs ONE deliberate SLOW BLINK at camera — eyes close slowly over 1.5 seconds, hold fully closed for 0.8 seconds, then open slowly.

TIME 5–7s: Brain lowers the waving paw back to the ground. He holds a warm soft gaze at camera. Gold heart tag glints once. Background light particles continue drifting softly.

EYE COLOR RULE (strict): BRIGHT EMERALD GREEN (#3DDC84) throughout. NOT brown, NOT amber.

ANATOMY RULE (strict): Brain has exactly 4 paws — 2 front, 2 back. At any moment AT MOST ONE front paw is raised. The other front paw + both back paws ALWAYS stay on the ground. NEVER show 5 paws or extra limbs or both front paws raised together.

MOUTH RULE (single soft meow exception on CTA): Mouth stays closed throughout. One single soft meow allowed at TIME 4s as the wave peaks — a single brief mouth motion, then fully closed again. NO lip-sync, NO repeated mouth motion.

SLOW-BLINK RULE: The slow blink at TIME 2–5s is a single deliberate motion — eyes close slowly over 1.5s, hold 0.8s, open slowly. NOT a normal fast blink, NOT multiple blinks.

BACKGROUND RULE: Neutral warm honey-amber bokeh ONLY — NO identifiable room, NO furniture in focus, NO walls, NO location-specific props. Pure dreamy warm ambient so this clip works as the closing scene of ANY cat video on this channel regardless of which locations were used in scenes 1–7.

STYLE: Pixar 3D render, cinematic warm honey-amber bokeh lighting, vertical 9:16, soft depth of field.
```

---

## 🎙️ Voiceover (recorded fresh per video in ElevenLabs)

Visual is universal but VO is per-video. Pick from this list of locked CTAs that match each ready script:

| Script | Sc 8 VO (record in ElevenLabs per video) |
|--------|-------------------------------------------|
| `13-words-cats-understand` | "Whisper your cat's name tonight. Watch the ear flick. Follow Brain for more cat secrets." |
| `why-cats-stare-at-you` | "Look up. Are they staring? Slow blink back. Follow Brain for more cat secrets." |
| `your-cat-sees-you-as-giant-cat` | "You've been adopted. Slow blink back. Follow Brain for more cat secrets." |
| `why-cats-follow-bathroom` | "Open the door. Let them guard you. Follow Brain for more cat secrets." |
| `cats-hear-you-blinking` | "You can't out-sneak a cat. Follow Brain for more cat secrets." |

---

## How to use this in Google Vids

1. **One-time setup:** generate the universal Sc 8 image in Nano Banana, then animate in Veo 3 with the above prompt. Save the rendered clip as `assets/universal-scene-8.mp4`.
2. **For every cat video:** import `assets/universal-scene-8.mp4` and drop it after Scene 7 as your Scene 8.
3. **Record the per-video VO** in ElevenLabs from the table above, align to the 7-second universal visual.
4. **Optionally add a text overlay** at the top of the universal Sc 8 in Google Vids (e.g. "FOLLOW BRAIN 🐱" in Electric Yellow `#FFD23F` with charcoal stroke).
5. **After Sc 8:** append the reusable end card from [`end-card.md`](../end-card.md) (Short variant, 3 sec) — that's also generated ONCE.

**Total credit savings:** 1 Veo 3 generation saved per video × N videos = N credits saved. Plus the end card is also single-generation reuse.
