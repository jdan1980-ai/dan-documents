# BrainCatAI — Director Checklist

> Master checklist for building any new BrainCatAI Short. Before starting a script, read the "Always remember" section. During production, scan the per-stage checklists. When AI output looks wrong, jump to "Troubleshooting".

This checklist is the **operating playbook** — it consolidates everything we've learned from analytics + AI generation pitfalls. Single source of truth alongside [`style-guide.md`](./style-guide.md).

---

## 🧭 Always remember (the 5 mantras)

1. **Hook in 2 seconds, retention dies at 5.** Open with the most visually striking moment — not the setup. The first frame must startle.
2. **Show the VO literally — never pose it.** If VO names a thing, the visual must be that thing. (See [§5d](./style-guide.md#5d-visualize-the-vo-literally--show-dont-pose).)
3. **Vary every scene** — shot size, camera move, Brain's angle, action. 8 medium-CU scenes in a row = swipe. (See [§5b](./style-guide.md#5b-scene-variety--dynamism-retention-rule).)
4. **Brain is alive** — every scene needs a clear ACTION beat (pounce, swat, fur poof, leap), not just an expression. (See [§5c](./style-guide.md#5c-make-brain-alive--action-over-poses-retention-rule).)
5. **One pattern interrupt per video** — sudden zoom, freeze flash, slo-mo. Once, on the twist. Used twice = loses power.

---

## 📊 Analytics-based lessons (real data, not theory)

### Lesson 1 — *Why You Forget Why You Walked Into a Room* (May 6, 2026)

| Metric | Result | Read |
|--------|--------|------|
| Stayed to watch | **35.96%** (above channel avg) | 🟢 Topic + thumbnail strong — people choose it from the feed |
| Total views | 78 | 🟡 Below normal — algorithm not pushing yet |
| Retention 5s | **108% → 75%** sharp drop | 🔴 Lost a quarter of viewers at 5s mark — that's where Brain just sits and starts theory |
| Retention 11s | down to 25% | 🔴 Cumulative bleed |

**What killed retention:**
- 00:22–00:34 — the same shot for 12 seconds while Brain explains theory. Static. Shorts viewers can't sit through 10+ sec without a cut/zoom/movement.
- 00:42–00:48 — end card overloaded with **SUBSCRIBE / THE END / THANK YOU** stacked text. Visual noise covered Brain's face.

**What we change for every future video:**
- ✅ **Cold open is the visual moneyshot** (the unique/striking moment), not the setup. For Doorway Effect that would be the "memory beam" shot at 00:18 — re-cut to start there.
- ✅ **No shot held longer than 5 seconds without something moving** — pan / zoom / cut / new prop / new pose. Static-emotion shots are forbidden mid-video.
- ✅ **Slow digital zoom-in on "secret info" reveals** — when explaining the key insight, push in 5–8% to create "you're being told something special" feeling.
- ✅ **End card = ONE phrase** ("Follow Brain for more brain hacks"). NEVER stack SUBSCRIBE + THANK YOU + THE END. Don't cover Brain's face with overlay.
- ✅ **Trim filler VO phrases** in middle scenes — every word earns its place. If a phrase doesn't add a new beat, cut it.

> When new analytics come in — add a Lesson section here with the same structure (what worked / what bled / what we change).

---

## ☑️ Pre-flight checklist (before writing a script)

- [ ] **Topic verified** in `content-ideas.md` — exists in backlog, marked 🟡 not done?
- [ ] **Niche tagged correctly** — Cat Psychology / Brain Hacks / Kids Trend / What If / Did You Know
- [ ] **CTA variant chosen** — match niche per [`style-guide.md` §9](./style-guide.md#cta-variants-final-voiceover-line-of-every-video)
- [ ] **Demand check** — high search volume, low Shorts saturation. (vidIQ when credits return.)
- [ ] **Audience promise** — one-sentence: what does the viewer learn or feel?
- [ ] **The visual moneyshot** identified — what's the ONE shot people will remember? Plan to put it at the cold open.

## ☑️ VO writing checklist

- [ ] **≤ 8 sec speech per scene** (Veo 3 max clip length)
- [ ] **80–120 words total** — ≈ 50 sec at 130 wpm + pauses + 3 sec end card = under 60
- [ ] **Kids AND adults** — no jargon, no scary words. ([`style-guide.md` §9 swap table](./style-guide.md#9-editorial-voice-writing-style))
- [ ] **Hook in first 2 seconds** — contradiction, shock, pattern break
- [ ] **Mid-roll insurance:** at the 22–30 sec point, a "wait — *this* is the wild part" beat
- [ ] **CTA variant matches niche** — cat secrets / brain hacks / wait what / facts that tune up your brain / facts that break your brain
- [ ] **Filler phrases removed** — read out loud, cut anything that doesn't add a new fact/beat

## ☑️ Locations / structure

- [ ] **1–3 locations max** — exact wording reused for shared scenes
- [ ] **CTA scene (Sc 8) lives in one of the existing locations** — never generic confetti/bokeh
- [ ] **Scene→location map** filled at top of script
- [ ] **Visual variety planned** — 8 scenes shouldn't all be same room same angle. ([§5b](./style-guide.md#5b-scene-variety--dynamism-retention-rule).)

## ☑️ Per-scene checklist (8 scenes)

For each scene, before you write the prompts, answer:

| Scene | Beat | Required punch |
|-------|------|----------------|
| 1 | HOOK | Snap reaction in first 2 sec — fur poof / jaw drop / eyes pop / head whip / leap. **Use the visual moneyshot here, not setup.** |
| 2 | Curiosity gap | A specific micro-action — paw raise, head tilt, tail-as-question-mark, lean toward camera |
| 3 | Setup | Brain physically interacts with the explanatory prop (chart, hologram, scientist costume, etc.) |
| 4 | Build-up | Anticipation — Brain stalks, crouches, freezes, pause… |
| 5 | Core | Visual payoff — transformation, reveal, BAM-flash, big reaction |
| 6 | Twist | **Pattern interrupt** — slo-mo / zoom / freeze flash / heart pupils. ONE per video, here. |
| 7 | Bonus | Visual joke or callback — small physical comedy beat |
| 8 | CTA | Wave + personality (ear flick, tail curl, slow blink, soft meow). **NEVER stack SUBSCRIBE + THANKS + LIKE on screen.** ONE clean line. |

## ☑️ Per-scene shot variety check

For each scene, vary at least 2 of these from the previous scene:

- [ ] **Shot size** — extreme CU / CU / medium CU / medium / wide / overhead
- [ ] **Camera move** — static / slow push-in / pull-back / dolly L-R / tilt / slow zoom-in
- [ ] **Brain's angle** — front / 3-quarter / profile / from behind / low-angle / high-angle

**Anti-pattern:** never two static medium-CUs of Brain facing camera in a row. Even if expressions vary, framing reads as one talking head.

**Static shot rule:** no shot held >5 sec without a camera move OR a new prop/pose change. (Doorway Effect lesson.)

---

## ☑️ Image prompt checklist (per scene)

Every Nano Banana prompt must include these locked elements:

- [ ] **Locked Brain block** prepended (kitten lock + emerald green eye spec + Pixar 3D cartoon + collar with Brain tag + glasses)
- [ ] **Location block** copy-pasted exactly (don't paraphrase between scenes that share a location)
- [ ] **Costume description** if applicable (lab coat / spacesuit / jersey / headphones — see [`style-guide.md` §2](./style-guide.md#thematic-costumes-use-only-for-matching-scene-topics))
- [ ] **Per-shot action** — what specifically Brain is doing (verb-driven, not state-driven)
- [ ] **Composition / framing** — extreme CU / wide / overhead / etc.
- [ ] **Visualize VO literally** — if VO names X, X must be in the frame
- [ ] **Negative space reserved** — if a Google Vids overlay (text/badge) goes here, mark the area uncluttered

## ☑️ Negative prompts (always include)

```
2D, flat, anime, cel-shaded, photorealistic cat, realistic cat features, real cat photo,
photoreal fur detail, multiple cats, low quality, blurry, distorted face, extra limbs,
extra paws, five legs, six legs, both front paws raised, two paws raised together,
missing glasses, missing collar, missing heart tag, watermark, garbled text, illegible text,
ugly, scary, aggressive expression, mouth open as if talking, lip-sync, talking cat,
mouth movement, chattering, brown eyes, amber eyes, yellow eyes, hazel eyes, golden eyes,
dark eyes, brown iris, amber iris, wrong eye color, eye color tinted by lighting,
warm-tinted eyes, adult cat, mature cat, teenage cat, narrow adult face, slim adult muzzle,
lean adult features, aged-up cat, defined adult cheekbones, slim adult eyes,
individual photoreal hair strands, costume covering collar, hidden heart tag
```

---

## ☑️ Animation prompt checklist (Veo 3)

Every Veo 3 prompt must follow the timeline format and include all locked rule blocks:

```
SHOT: [camera framing + movement + kitten reminder]

TIME 0–Xs: [pose / micro-movement]
TIME X–Ys: [main action]
TIME Y–Zs: [reaction / effect]
TIME Z–end: [closing beat — held or blink]

EYE COLOR RULE (strict): bright emerald green #3DDC84 throughout, NOT brown/amber/yellow/hazel/golden, warm lighting must NOT tint iris.

ANATOMY RULE (strict): exactly 4 paws — 2 front, 2 back. NEVER 5 paws or extra limbs.

MOUTH RULE (strict): mouth stays closed — no lip-sync, no chewing, no chattering. Exceptions: held jaw-drop / single yawn / one soft meow on CTA / single sustained lick. State exception explicitly when used.

CONSISTENCY RULE (strict): preserve young Pixar kitten proportions throughout — round baby-face, plump cheeks, big baby-eyes, small button nose, soft cartoon shapes. Veo must NOT age him up to a mature cat.

WARDROBE RULE (strict, when costume applies): brown collar and gold heart-shaped tag clearly visible at the V-cut neckline. Costume does NOT cover them. Glasses on. ONE costume item per video — never doubled.

STYLE: Pixar 3D CARTOON render (Disney/Pixar character, NOT photoreal), cinematic lighting, vertical 9:16, soft DOF.
```

Add as needed:
- **POSITION RULE** — when Brain interacts with a prop (telescope, desk, pillow), lock his physical position there for the whole clip
- **DIRECTION RULE** — for transformations (stretch, fur-poof), specify the direction explicitly so Veo doesn't reverse it
- **TONE RULE** — for potentially scary content (black hole, predator), state "comic Pixar cartoon NOT horror"
- **HEADPHONES / HOLOGRAM / THOUGHT-BUBBLE / TEXT / NEGATIVE SPACE** rules — apply when relevant
- **HUMAN RULE** — when a person appears, face fully turned away, only back of head + hair visible

---

## ☑️ Visual storytelling tools (instead of generic poses)

When the VO names something concrete, use one of these to literalize it:

| Tool | Use case | Example |
|------|----------|---------|
| **Hologram beside Brain** | Showing other characters / scientific concepts | Mother cat licking kitten (hair-licking video Sc 5) |
| **Thought-bubble above Brain** | What Brain is thinking | Clumsy kitten failing to groom (hair-licking video Sc 6) |
| **Reflection in glasses / mirror / water** | What Brain sees | Black hole reflected in his glasses (Sc 1 black-hole) |
| **Off-frame human, face turned away** | When VO involves the viewer / human directly | Hair-lick scene (hair-licking Sc 4) |
| **Costume on Brain** | "Scientists / doctors / chefs / detectives / etc." | Lab coat + chart (slow-blink Sc 5) |
| **Slo-mo zoom-in** | "Pattern break" / "secret info" reveal moment | Spaghettification (black-hole Sc 5) |
| **Freeze-frame white flash** | Pattern interrupt at the punchline | 6-7 gesture (kids-trend Sc 5) |

---

## ☑️ End card / CTA checklist

After the 8 scenes:

- [ ] **One clean line** — "Follow Brain for more brain hacks" (or matching niche variant)
- [ ] **Brain's face is NOT covered** by SUBSCRIBE button or LIKE icon — overlay around him, not on him
- [ ] **Maximum 1 button + 1 text label** at end card. NOT all three of SUBSCRIBE / THANK YOU / THE END at once.
- [ ] **End-card length ≤ 3 sec** to keep total Short under 60 sec
- [ ] See [`end-card.md`](./end-card.md) for the canonical reusable end card

---

## ☑️ SEO + upload checklist

- [ ] **Title** — 40–70 chars, ends with `🐱 | Cat Psychology` (or `🐱 | Brain Hacks`)
- [ ] **Description** — ≥ 250 chars, main keyword 2–3×, 5+ supporting keywords, hashtag block, follow CTA
- [ ] **Tags** — 20–25 total, base set always included (see CLAUDE.md), 5–10 video-specific long-tail, total under 450 chars
- [ ] **Hashtags** — top-3 in title bar (`#shorts #catpsychology #catfacts` or `#shorts #brainhacks #...`)
- [ ] **Thumbnail concept** documented in script
- [ ] **Pinned comment** drafted in script's editing notes — append to [`pinned-comments.md`](./pinned-comments.md) when uploading

---

## 🚑 Troubleshooting AI generation failures

If you see this in the output → fix it like this.

| Symptom | Root cause | Fix |
|---------|-----------|-----|
| Brain's eyes brown/amber/hazel | Warm lighting tints iris despite "green" in prompt | Add hex `#3DDC84`, multiple "NOT brown, NOT amber..." in negatives, `EYE COLOR RULE (strict)` block in Veo |
| Brain looks adult / realistic / slim muzzle | Locked prompt too short, no kitten lock | Use full kitten-lock prompt: "YOUNG ORANGE TABBY KITTEN, ~4 mo, NOT adult, plump cheeks, big baby-eyes, Pixar 3D CARTOON not photoreal" |
| 5+ legs / extra paws | Two paws raised at once or over-specified poses | Just say "exactly 4 paws — 2 front, 2 back. NEVER 5 paws or extra limbs". Don't over-specify positions |
| Mouth opens as if talking | "Mouth closed" buried in prompt | Dedicated `MOUTH RULE (strict)` block at end of Veo prompt with multiple "no lip-sync, no chewing, no chattering" |
| Two pairs of headphones (one on neck) | Collar + headphones zone confused | `HEADPHONES RULE (strict)` — exactly ONE pair on head, NEVER second on neck. Around neck: ONLY brown collar |
| Costume covers heart tag | Wardrobe item drawn over the collar | `WARDROBE RULE (strict)` with "deep V-cut neckline showing the brown collar and gold heart tag prominently" |
| Two cats in scene | Hologram / thought-bubble interpreted as second character | `HOLOGRAM RULE` / `THOUGHT-BUBBLE RULE` — clearly stylized 2D doodle, NOT realistic 3D cat |
| Garbled text in image | AI struggles with text rendering | `TEXT RULE (strict)` specifying exact characters + "NO garbled letters, NO repeated text". For complex text, leave negative space and add overlay in Google Vids |
| Floating pillow / object not anchored | AI loses spatial relationships | Explicit "RESTING DIRECTLY ON THE BED, the bed sheets visibly tuck around it" + `PILLOW RULE` |
| Transformation reverses (stretched → normal) | Start image was already in end state | Generate START image in initial state, write `DIRECTION RULE` locking the direction normal → transformed |
| Scary tone instead of cute | "Predator instinct / death / void" trigger horror render | `TONE RULE (strict)` — "comic Pixar cartoon stretching, NOT horror. Bug-eyed funny panic, never agonized" |
| Static shot held too long (retention drop) | One pose for 10+ sec | Add a slow zoom or cut to fresh angle every 4–5 sec. See "Static shot rule" above |
| End card overloaded (SUBSCRIBE + LIKE + THANK YOU + THE END) | Stacked overlays | One phrase only. Place around Brain, not on his face |

---

## 📝 When you finish a video

- [ ] Update `production-status.md` row to ✅ for the stage you completed
- [ ] After publish, log views/retention/likes at 48h / 7d / 30d
- [ ] If retention drops anywhere, **add a Lesson section** to "Analytics-based lessons" above
- [ ] If pinned comment gets >5 replies, log the engagement question pattern that worked

---

## 🔁 Living document

This checklist updates whenever:
- A new analytics review reveals a learning → add to "Analytics-based lessons"
- A new AI failure pattern appears → add to "Troubleshooting"
- A new visual storytelling tool works → add to "Visual storytelling tools"

Keep it lean. Cut rules that aren't actually being broken. Add only what new evidence demands.