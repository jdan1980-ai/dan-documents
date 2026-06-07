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

### Lesson 2 — *Why Your Cat Chirps At Birds* viral push (May 9, 2026)

| Metric | May 5 | May 9 (4 days later) |
|--------|-------|----------------------|
| Views | 30 | **1 254** (×42 growth) |
| Likes | 2 | **47** (×24 growth) |
| Like rate | 6.7% | **3.7%** (highest on channel) |

YouTube algorithm pushed this video hard between days 1–4. What set it apart:

- ✅ **Universally relatable behavior** — every cat owner has heard their cat make that bird-chatter sound
- ✅ **Clean title pattern** — `Why Your Cat [does X]` (proven Shorts hook)
- ✅ **49 sec length** (sweet spot)
- ✅ **Plain canonical tags** — used the base 19 cat-psychology tags only, no custom drift

**Tag insight from API pull (top 3 channel videos):**

| Video | Tag strategy | Result |
|-------|--------------|--------|
| Sky Blue (1 373 v) | 20 tags, mismatched (`cats ancient egypt` on a physics video — leftover from Egyptian Domestication video) | Worked **despite** mismatch — title hook strong enough |
| Box Bed (1 360 v) | 19 tags, content-matched | Worked — both signals aligned |
| **Chirps At Birds (1 254 v + viral push)** | **Base 19 canonical only — zero custom** | **Cleanest tag set, biggest engagement** |

**What we change for every future video:**
- ✅ **Tag rule simplified:** base 19 canonical + **3–5 video-specific** (must match content). Stop carrying over tags from previous videos that don't fit.
- ✅ **Title pattern doubled-down:** lead Cat Psychology videos with `Why Your Cat [does X]` whenever possible. Universal-relatable cat behaviors are the algorithm's favorite.
- ✅ **Engagement-rate matters more than total likes:** 47 likes on 1 254 views (3.7%) signals algorithm to push. Aim for ≥3% like rate via stronger hooks and emotional payoffs.

### Lesson 3 — Hook strength matters more than niche label (May 9, 2026 — revised)

| Video | Niche | Hook | Universally relatable? | Result |
|-------|-------|------|------------------------|--------|
| Sky Blue | Brain Hacks (cat-tagged) | "Why Is the Sky Blue?" — childhood question every kid asks | ✅✅✅ | **1 373 views** ⭐ |
| Doorway Effect | Brain Hacks | "Why you forget walking into a room" — relatable but uses abstract jargon | ✅ medium | 88 v at 3 days (too early to judge) |
| Vagus Nerve | Brain Hacks | "Stop stress button" — anatomy jargon | ⚠️ academic | 10 v at 2 days (too early) |

> **Initial reading was wrong.** Sky Blue (1 373 v) proves Brain Hacks CAN hit on this channel. The differentiator isn't niche — it's **hook accessibility**.

**Revised lesson:**
- ✅ Brain Hacks works on this channel **if the hook is universally accessible** (childhood question, common phenomenon, popular-science term everyone knows)
- ⚠️ Brain Hacks struggles when the topic uses academic / jargon framing in the hook (`Doorway Effect`, `Vagus Nerve`, `frisson`)
- ❌ DON'T conclude after 2–3 day data — videos can take 4–14 days to find their algorithmic push (Chirps At Birds went from 30 → 1 254 views between days 4 and 8)

**What we change for new scripts:**
- ✅ For Brain Hacks topics, **lead title with the universally-relatable form**, save the academic term for the body:
  - "Why You Forget Walking Into a Room" — keep, but body should immediately reference the everyday experience before naming "Doorway Effect"
  - "Stop Stress Button Inside Your Body" — keep, but explain it before saying "vagus nerve"
- ✅ **Wait 7 days minimum** before declaring a video underperformed
- ✅ **Don't rework finished scripts** based on 2–3 day signals — ship them, gather real data, iterate the NEXT batch

**Already-finished unpublished scripts — KEEP AS-IS, don't reframe:**
- `why-cats-lick-your-hair.md` — Cat Psychology, ship
- `whats-inside-a-black-hole.md` — hook "What's inside a black hole?" is as universal as Sky Blue, ship
- `why-music-gives-you-goosebumps.md` — goosebumps is a universal physical experience, ship
- `why-kids-say-6-7.md` — high search-intent for parents (they actively Google this), ship

### Lesson 4 — First 2 seconds must already be in motion (May 9, 2026)

User feedback: "Static prompts killed the dynamics in the first seconds. Transitions/ignition effects don't compensate."

**My pattern problem:** I kept writing scripts where Sc 1 opens with `Brain calmly listening / sitting / looking with X expression for 1.5–2 seconds, then snap reaction at 2s`. That's a Pixar feature-film opening, NOT a Shorts opening.

**Why it kills retention:**
- Shorts viewers decide to swipe in **first 1–2 seconds**
- "Calm establish" wastes the most valuable real estate of the entire video
- By the time the snap reaction lands at 2s, ~30–40% of viewers are gone

**The fix — open ALREADY in motion, not establishing toward motion:**

| ❌ Writing pattern to ban | ✅ Replacement pattern |
|---------------------------|-----------------------|
| `TIME 0–1.5s: Brain sits calmly with X expression` | `TIME 0–0.5s: Brain LEAPS / POUNCES / SHAKES OFF / WHIPS HEAD AROUND — already mid-motion at frame 1` |
| `TIME 0–2s: tail flicks once` | `TIME 0–1s: tail puffs + ears flatten + eyes dilate + fur ripples + camera zoom-punches all simultaneously` |
| `Brain looks at camera, then reacts` | `Open ON the reaction — fur already poofed, jaw already dropped, eyes already wide, camera already mid-zoom` |
| Snap reaction held FROM 0–4s ✓ | Snap reaction held from 0–4s, with secondary motion (whisker twitches, fur settle, eye refocus) layered through it |

**Motion stacking — every scene needs ≥3 simultaneous motion elements (not sequential):**

1. **Brain's body** — leap, pounce, stride, shake-off, lean, settle, pivot
2. **Brain's face/fine** — eye dilate / ear flick / whisker twitch / fur ripple / mouth held jaw-drop
3. **Camera** — push-in / zoom-punch / pull-back / dolly / tilt — never pure static for the hook
4. **Environment** — rain falls, dust drifts, sparkle particles, color shift, prop motion, light pulse
5. **Bonus (optional)** — visual element timed to VO beat (object drops on stress word, lightbulb flash on "AHA")

**Transition effects (ignition / fade / whoosh) DON'T compensate** for static scenes. Polished transitions between two boring shots are still two boring shots — the viewer already swiped.

**What we change for every future script:**

- ✅ **Sc 1 HOOK opens IN mid-action** — not establishing toward action. The scene starts at peak. Frame 1 = jaw-dropped + fur-poofed + eyes-wide.
- ✅ **No "calm establish" pattern** — banned phrase: "Brain sits / looks calmly with X expression for the first N seconds"
- ✅ **Stack 3+ simultaneous motion elements** per scene — not "first this, then that" sequential — they happen at the same time
- ✅ **Camera always doing something on Sc 1** — even tiny continuous push-in (3% over 7 sec) beats pure static

**Action verbs to lead with in Sc 1 (re-emphasis from §5c):**

`pounces, lands, slams, whips around, recoils, flinches, jumps in, snaps head, fur poofs, tail puffs, ears snap back, eyes blow wide, jaw drops, shakes off, hops onto, leaps into, springs from, dashes in`

**Anti-vocab BANNED in Sc 1 (don't use even if "before the action"):**

`sits, calmly, looks at, half-lidded, tail flick, glances, gentle, settles, peers, observes`

These can appear in Sc 7-8 but **never in the hook**.

### Lesson 5 — Brain is the SUBJECT of the fact, not a narrator of it (June 7, 2026)

User insight (confirmed against data): our early videos gave **dry third-person facts** ("Cats can hear 5× better than humans"). The single best signal we have — Sky Blue (1 373 v) — worked partly because the fact was framed *through* the character's world. The fix is to make **Brain live the fact in first person**, speaking directly to "you".

**Why this lifts the hook / Stayed-to-Watch** (our #1 problem — >60% swipe in first seconds, 0 subs gained over 26 videos in 30 days):
- A dry fact is a lecture — the brain filters it out. A first-person claim is a character + conflict + direct address, all in second one.
- Forces "show, don't pose" (per `CLAUDE.md`): if Brain *says* he'd jump higher, Veo must *show* him jumping — no wasted "Brain sits with X expression" shots.

| ❌ Dry third-person (ban in hook) | ✅ Brain as subject, first person + "you" |
|---|---|
| "Cats hear 5× better than humans" | "You whispered my name from the next room — I heard you before your mouth even opened." |
| "Cats always land on their feet" | "Throw me off the shelf. I land on my paws every time — here's my secret." |
| "Cats sleep 16 hours a day" | "While you were at work, I slept 16 hours. No regrets." |

**Rules for every new script (from June 8 onward):**
- ✅ **Hook VO is first person** — Brain says "I / me / my" and addresses the viewer as "you". No "cats do X" in Sc 1.
- ✅ **The fact happens TO or THROUGH Brain on screen** — he demonstrates it, not narrates it.
- ✅ Works on ANY niche (Cat Psychology, Brain Hacks, etc.) — this is a **framing** upgrade, NOT a topic switch. Do **not** pivot the channel to general science; keep the cat-led identity.
- ⚠️ Treat any "switch the whole channel to science" advice as rejected — n=1 (Sky Blue) is not a mandate to change niche.

### Lesson 6 — Brighter, higher-contrast thumbnails (June 7, 2026)

CTR sits ~1–3% on browse surfaces — viewers scroll past before the topic registers.

- ✅ **Brighter base** — push saturation/luminance on Brain and background; avoid dark/muddy frames that disappear in the feed.
- ✅ **Bigger, higher-contrast text** — fewer words, larger, bold outline so it's legible at thumbnail size.
- ✅ **One clear focal point** — Brain's face + emotion readable instantly.

### Rubric rename — "Brain Hacks" → "Brain Science" (June 7, 2026)

Science-fact videos (space, physics, biology) now use the title suffix **`| Brain Science`** instead of `| Brain Hacks`. Reasons: pun on the character's name (Brain), accurately signals real science (not "hacks"), and gives a clean two-rubric structure under Brain Cat: `| Cat Psychology` (cats, the backbone) + `| Brain Science` (first-person science experiments). Hashtag: `#brainscience`.

- ⚠️ NOT a niche switch — during recovery, cats stay the backbone; Brain Science is a rare inserted experiment (1 video per test), always first-person (Lesson 5).

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
- [ ] **First-person hook** — Brain says "I/me/my" + addresses "you"; fact happens THROUGH Brain, not narrated about cats (Lesson 5)
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
| 1 | HOOK | **Open IN motion, not toward it.** Frame 1 already shows the punch — fur poofed / jaw dropped / mid-leap. NO "calm establish for 1–2s". Stack 3+ simultaneous motions: body + face + camera + environment. **Use the visual moneyshot here, not setup.** See Lesson 4. |
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