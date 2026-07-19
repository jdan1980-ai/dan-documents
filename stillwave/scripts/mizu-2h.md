# MIZU — 水 | 2H Japanese Zen Music & Water Garden

## Meta

- **Title:** MIZU — 水 | Japanese Zen Music & Water Garden Sounds for Deep Calm & Sleep
- **Slug:** `mizu-2h`
- **Format:** Long-form (Kanji-Concept Series)
- **Length:** target ≤ 2:00:00 (~36 mastered tracks; generate ~40, trim)
- **Aesthetic:** Japanese garden at dusk — tsukubai (蹲踞) stone water basin with bamboo kakei spout, thin continuous stream, moss, stone lantern glow. NOT spa (no plumeria/towels — Bali aesthetic is off-brand).
- **Playlist (add to in Studio):** Japanese Zen Music
- **Status:** 🚧 IN PRODUCTION (package created 2026-07-19)
- **Concept note:** MIZU (水) — water. Zen ideal of effortless power: water never argues with the rock, and always wins. **FIRST StillWave video with a continuous nature-sound bed** — tsukubai water trickle mixed ~−20 dB under the full 2H album. Opens the water/nature tag cluster (VidIQ 2026-07-19: `water sounds` 115K/mo comp 41, `nature sounds` 511K/mo comp 38, `spa music` 193K/mo comp 50 — all softer than `meditation music` 45).

## §0 — Pre-production (done 2026-07-19)

- **Trend/competitor check (VidIQ):** Relax-TV `ZEN WATER GARDEN — Relaxing Zen Music with Water Sounds in 4K` — 342K views, breakout 5.9, category **Music** → winning formula = music + water layered. `Zen Garden 4k` (4.3K subs) — pure water ambience, no music → sits in **Lifestyle (sociology)**, most videos 1–4K views. Confirms: music-first, water as bed, `Music` in title first half (Pomodoro lesson).
- **Gap:** Japanese-garden-specific water content (tsukubai/kakei visual) is nearly absent — cluster is dominated by generic 3D-render gardens and spa imagery. Our photoreal Japanese still-life + kanji brand slots into an empty aesthetic.

---

## §1 — Suno prompts

Batch naming: `MIZU` = A · `MIZU 2` = B · `MIZU 3` = C. Generate ~40 (A×14, B×13, C×13), master, keep best ~36. Interleave A/B/C in final lay-down — no two adjacent tracks share an opening (SATORI Content ID lesson).

> Water bed is added in CapCut, NOT in Suno — keep tracks clean of water SFX so the bed loops independently and Content ID sees unique music.

### Prompt A — Style field (batch MIZU — bell-led opening)

```
Japanese zen ambient, deeply calm and fluid. Sparse shakuhachi bamboo flute with long breathy notes, soft koto plucks resonating in silence, warm slow synth pads like still water, occasional low temple bell with long decay. 50 BPM, extremely slow and flowing, phrases that drift like ripples widening on a pond. Gentle, transparent, meditative — music that moves the way water moves, never forcing. instrumental only, no vocals, no singing, no chanting, no spoken word, pure instrumental
```

### Prompt B — Lyrics field (batch MIZU)

```
[no lyrics, no vocals, instrumental only]
[opening: single low temple bell strike, 4 seconds of resonance, then shakuhachi enters quietly]
[section A: shakuhachi drifts in long unhurried phrases, pad swells slowly underneath]
[section B: koto plucks like drops falling into a stone basin, wide silence between notes]
[section C: flute and koto weave gently, everything slow and transparent]
[loop point: fades to near-silence with a last soft bell resonance, ready to begin again]
[mood: dusk in a moss garden, a bamboo spout pours a thin thread of water into a stone basin, ripples widen and settle]
[texture: shakuhachi, koto, warm pads, distant temple bell, still evening air]
```

### Batch B — `MIZU 2` (koto-led opening)

Style: same as A, reorder instrument list to lead with koto (`Sparse koto plucks resonating in silence, soft shakuhachi...`).
Lyrics: change opening line to:
```
[opening: sparse koto plucks, 3-5 slow notes alone, then a warm pad swells underneath]
```

### Batch C — `MIZU 3` (pad-led opening)

Style: same as A, lead with pads (`Warm slow synth pads like still water, sparse shakuhachi...`).
Lyrics: change opening line to:
```
[opening: slow swelling drone pad alone for the first 6-8 seconds, no melodic instrument until the flute enters softly]
```

### 💧 Water-sound bed (NEW — assembled in CapCut)

- Source: royalty-free/CC0 "small stone fountain / water trickle" loop 1–2 min (Pixabay SFX / freesound), gentle THIN stream — not a river, not a waterfall, no birds.
- CapCut: own audio track, loop the clip across the full 2H, volume **~−20 dB relative to music** (music clearly in front, water = texture you notice only when you listen for it), 2s fade-in at 0:00, fade-out with the last track.
- QA: listen at 3 random points on phone speaker — water must never mask the flute.

---

## §2 — Mastering

Same two-pass loudnorm pipeline as IKIGAI/WABI SABI (`master-album.py`): −16 LUFS, TP −1.5 dB, 28 Hz low-cut, 48 kHz/24-bit. Folder `Suno-Mizu` → `Suno-Mizu-mastered`, then `tracklist-timestamps.py` for §8.

---

## §3 — NanoBanana 16:9 (PRIMARY — tsukubai still life)

```
Photorealistic cinematic still life, Japanese tea garden at dusk. A weathered round tsukubai stone water basin (蹲踞) sits right-of-center on mossy stones, filled with dark still water. A bamboo kakei spout pours ONE thin continuous silver thread of water into the basin, small ripples widening on the surface. Deep green moss on the stones, a hint of raked gravel behind. In the soft-focus background right, a weathered stone lantern with a warm flame glowing inside its fire-box — the single warm light accent. Dusk blue-hour light, dark tranquil atmosphere, muted palette of deep greens, wet stone grey and one warm amber accent. Shallow depth of field, atmospheric mist very subtle in the far background. Keep the lower-left corner as dark, empty negative space for a text overlay — no bright objects or busy detail in the bottom-left third. Keep the bottom-right corner as calm, dark, low-detail space — no subject or bright detail there (logo placement). No people, no text, no letters, no watermark. 4K, cinematic composition.
```

**Alt — with monk (Kanji-Concept classic):** same scene, add `a lone buddhist monk in dark robes kneels at the basin, back to camera, lower third of frame, face never visible, ladling water with a wooden hishaku dipper` — hero basin stays upper-right.

> 🔒 No airborne particles (no falling leaves/petals). Water stream + ripples are the motion story.

## §3b — NanoBanana 9:16 (Shorts)

```
Photorealistic cinematic vertical composition, Japanese tea garden at dusk. A weathered round tsukubai stone water basin in the lower half of frame, dark still water, a bamboo kakei spout entering from upper right pours one thin continuous silver thread of water into the basin, ripples widening. Deep green moss on wet stones, soft blue-hour dusk light, one warm amber glow from a stone lantern soft-focus in the upper background. Muted dark palette, tranquil, meditative. No people, no text, no letters, no watermark. 4K.
```

---

## §4 — Flow / Kling prompt (16:9 loop)

```
Camera locked, no camera movement at all. Seamless loop. Animate ONLY: (1) the thin water stream pouring continuously from the bamboo spout — constant, unbroken flow; (2) small ripples widening gently across the basin surface, calm and regular; (3) the stone lantern flame glowing with a soft slow flicker; (4) very subtle mist drifting slowly in the far background. Everything else perfectly still — basin, stones, moss, bamboo, background. Slow, hypnotic, meditative. Last frame matches first frame exactly for a perfect loop.
```

> Falling water + ripples = continuous motion, inherently seam-free. If adding a shishi-odoshi variant clip: it MUST complete exactly ONE full fill-tip-return cycle per clip, ending in the start position (cyclic-motion rule).

---

## §6a — Wisdom Overlay

- Line 1 (kanji): **上善若水**
- Line 2 (romaji): *Jōzen wa mizu no gotoshi*
- Line 3 (gloss): The highest good is like water
- Cream `#F5EAD2`, Liberation Serif Bold, left side over the dark moss/gravel zone. 0:00–0:03 scene+sound only → fade-in 2s → hold ~5s → fade-out 2s, gone by 0:14.

---

## §7 — Title

```
MIZU — 水 | Japanese Zen Music & Water Garden Sounds for Deep Calm & Sleep
```
(`Music` lands by char ~22 ✅ · 74 chars ✅ · no hashtags ✅)

**A/B variant:**
```
MIZU — 水 | Japanese Water Garden Zen Music for Sleep, Stress Relief & Calm
```

---

## §8 — Description (Hikari 5-block; tracklist added after mastering)

```
japanese zen music, water sounds, zen garden, meditation music, sleep music, nature sounds, japanese water garden, relaxing music, spa music, healing music, shakuhachi flute, koto music, calming music for stress relief — a two-hour Japanese zen session beside a stone water basin at dusk, gentle water trickling beneath every note.

🌀 MIZU means "water."
It never argues with the stone,
and it always finds its way.

Dusk settles over the moss garden. A bamboo spout pours one thin silver thread into the tsukubai basin, and the ripples widen, and settle, and widen again. A stone lantern holds its small flame against the coming night. The flute breathes in long phrases; the koto falls like slow drops. Beneath it all, the water never stops — and never hurries.

Tracklist:
[added after mastering — mood-poetic names, no Hz, no technical terms]

🌀 Be like water — soft, and unstoppable.
🍃 Let one thought pass. Then the next.

Subscribe for more Japanese ambient meditation journeys 🌿
```

---

## §9 — Tags (Hikari formula — verify scores in VidIQ before upload)

```
stillwave, water sounds, nature sounds, zen music, japanese zen music, meditation music, sleep music, relaxing music, calming music, spa music, healing music, ambient music, background music, shakuhachi flute music, koto music, flute music, mizu, japanese water garden, zen garden, water fountain sounds, zen meditation music, japanese meditation music, mindfulness music, peaceful ambiance, serene ambience, evening relaxation, japanese zen garden at dusk with tsukubai stone water basin bamboo fountain and stone lantern, joe hisaishi
```

No hashtags in title or description body (Kanji-Concept lock).

---

## §10 — Thumbnail

- Background: §3 primary image (basin right-of-center).
- **水** LARGE upper-center (single kanji — the biggest brush glyph we've run), cream `#F5EAD2`, IPA Mincho; **MIZU** in Liberation Serif Bold below, smaller, tracked.
- Corners: lower-left free/dark (no text needed there — kanji carries the click), lower-right = logo.
- Compose with a PIL script (adapt `wabi-sabi-2h-compose-thumb.py`) once the source image is picked.

---

## §11 — Pinned Comment

```
🌀 MIZU (水) — water.

It never argues with the stone.
It always finds its way.

Where does your mind go when you hear running water? Share below 👇

If this session helped — subscribe. New journeys every week 🌿
```

---

## §12 — Community Post (day-of, 4–6h before publish)

```
MIZU (水) in Japanese Culture: A Concise Overview

MIZU (水) simply means "water" — yet in Japanese thought it carries an entire philosophy. The tsukubai stone basin placed at the entrance of every tea garden asks guests to kneel and rinse their hands: purification through humility. Zen teachers point to water as the model of ideal action — 上善若水, "the highest good is like water," soft enough to yield to every stone, persistent enough to carve through mountains. In the garden, the thin thread falling from a bamboo spout is not decoration; it is a clock without hours, marking time by ripples instead of numbers.
```

Image: the long-form thumbnail.

---

## §14 — Shorts (cross-promo package)

- **Concept/Hook (0–2s):** close-up of the water thread hitting the basin — *"This sound has calmed Japan for 400 years"*
- **Visual:** §3b vertical + Flow loop (stream + ripples only, camera locked, 20–30s)
- **Text overlays (gold, TOP — proven WABI SABI layout):** `This sound has calmed Japan for 400 years` → `水 MIZU — water` → `Full 2-hour session on the channel`
- **Title:** `The Water Sound Japan Uses to Calm the Mind 🌿 #shorts` (≤60 ✅)
- **Description:** `MIZU (水) — the tsukubai water basin of Japanese tea gardens. Full 2-hour zen session on the channel 🌿 [link]`
- **Tags:** `water sounds, zen garden, japanese garden, mizu, zen music, meditation, relaxing sounds, tsukubai, calming sounds, stillwave`
- **Pinned:** `🌀 MIZU — water never argues with the stone. The full 2-hour session is on the channel 🌿`
- **Upload:** Related video → long-form · Playlist **StillWave Shorts — Japanese Zen & Frequencies** · Not for kids · Scheduled, day after the long-form.
