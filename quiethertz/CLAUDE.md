# Quiet Hertz — Project Instructions

New channel, built to replicate the validated "Healing Quiet Tonight" format (see `stillwave/competitor-tracker.md` for the teardown this is based on — channel UCSJmN2W_LRf8Qa8uK3J1dtg, 1,840 subs, 2.37M views, +2.19M views in 30 days). **Separate channel from StillWave on purpose** — keeps StillWave's Japanese-zen Topic Category clean, lets this one post daily without diluting either brand.

## Channel info

- **Working name:** Quiet Hertz (placeholder — pick final name/handle at channel creation, doesn't affect any content below)
- **Niche:** Solfeggio/healing-frequency sleep music. Same "frequency + benefit" title formula as the competitor, same near-daily cadence.
- **Google account:** same account as StillWave (Brand Account) — separate channel, separate branding, separate upload schedule.
- **Not for kids.** Scheduled or Unlisted first publish, same Karena rules as StillWave.

## 🔒 Why this works (the competitor pattern, confirmed via VidIQ 2026-10-08)

- **Near-daily cadence** (competitor: 1 video/day, 73 videos in ~83 days) — visuals are NOT bespoke per video, so this is sustainable without a Flow/CapCut pipeline.
- **One title formula, frequency combo rotates:** `[Hz number(s)] + [sleep/healing hook] + [specific benefit] + #N`. The `#N` / `★N` numbering is deliberate — they re-run the same winning hook repeatedly (same trick as StillWave's A/B title testing, just more aggressive).
- **No bespoke visual per video.** One reusable dark abstract background + a text overlay that only changes the Hz number and tagline. This is the entire reason the cadence is possible — skip hero-image generation and Flow loops entirely for this channel.
- **Length 2H20M–4H**, not fixed — matches whatever the mastered album runs to, no padding needed.
- **Most uploads get modest views (300–5,000), a steady minority break out (10K–95K)** — classic volume+lottery. Expect the same here; judge the channel by the aggregate, not any single video.

## 🎨 Visual template — CORRECTED 2026-10-08 from real competitor thumbnails

**Not a single reused background.** The real competitor format (confirmed from actual thumbnail screenshots) is: **one consistent character design** + **a rotating set of themed background environments**, matched in color/mood to each video's Hz combo and benefit. Animated (Flow/Kling loop), not static.

### Character — LOCKED, same in every video

A translucent, glowing wireframe/digital silhouette of a human body, rendered as fine luminous circuit-like lines over a dark void (no skin, no solid surface — pure light-wireframe). Reclining or curled in a sleeping/resting pose (lying on back, or curled on side with one arm under the head). The **brain is the focal glowing core** — a bright, intricately-lit organic shape inside the skull, color-matched to the video's palette (see below). For "full body / spine regeneration" videos specifically, extend the glow down the spine as a second luminous channel (matches the DNA-helix thumbnail). The figure is always alone, centered or slightly off-center, floating in its themed environment.

### Background environment — ONE per video, rotate across the 10, color-matched to the Hz/benefit theme

| Theme | Background | Palette |
|---|---|---|
| Sleep / insomnia relief | Rising soft waveform bands + warm sunrise gradient behind the figure | warm orange → magenta → purple |
| Mental clarity / overthinking | Geometric neural-network rings and nodes radiating from the head, deep space | teal / cyan / electric blue |
| Emotional / heart healing | A large faceted crystal heart with a small ringed planet behind it, deep space | indigo / soft blue-white |
| Detox / nervous system reset | Bioluminescent underwater forest, drifting jellyfish, soft glowing kelp | teal-green / cyan |
| Spiritual / third eye / cosmic | Spiral galaxy / nebula filling the background | green-gold / deep violet |
| DNA repair / full-body regeneration | A golden DNA double helix spiraling beside the figure, its glow extending down the spine | amber / gold |

### Full copy-paste NanoBanana prompt template (fill in `[BACKGROUND]` and `[PALETTE]` per video from the table above)

```
Photorealistic 3D digital art, 16:9, 4K, dark cinematic background. A translucent glowing wireframe silhouette of a human body — fine luminous circuit-like lines over pure darkness, no skin, no solid mass, only glowing structure — reclines in a sleeping, resting pose, floating alone in a dark void. The brain is the clear focal point: a bright, intricately detailed glowing organic core inside the skull, radiating soft light. [BACKGROUND]. Overall palette: [PALETTE], with deep black negative space surrounding the glowing elements so they read clearly against the dark. Soft bloom, particle glow, cinematic depth of field, serene and otherworldly mood — healing, not clinical. No text, no letters, no logos, no watermark.
```

### Animation (Flow/Kling, per background type — six loop treatments to design once, then reuse across any video that shares that background)

**🔒 Corrected 2026-10-08 from a clearer competitor reference image the user shared.** The body itself is completely motionless throughout — it never moves, breathes, or shifts pose. The animation is: **a wave/current of light travels along the body's wireframe on a loop**, as if the healing frequency itself is passing through — moving from the headphone, down the energy cable, across the torso, and along the limbs, then looping back to repeat. This traveling pulse is the primary motion element, not a secondary detail.

Camera locked, no pan/zoom. Animate: (1) **the healing wave** — a bright pulse of amber light travels slowly along the body's wireframe lines and the headphone cable, on an 8-sec loop, last frame matching first; (2) the glowing brain pulses with an extremely slow, gentle breathing rhythm, in sync with or independent of the traveling wave; (3) the background's signature motion — waveform bands undulate slowly / neural rings rotate almost imperceptibly / the crystal heart catches a faint inner light shift / jellyfish drift and kelp sways / the galaxy's arms turn at a barely-perceptible rate / the DNA helix rotates slowly on its axis. The body's pose and position never change. If a loop proves too slow to produce at this cadence, a single static frame is an acceptable fallback — competitor channels in this niche ship static-adjacent (near-zero motion) video and it does not appear to hurt performance.

## 🛠️ Pipeline (lightweight — no CapCut required)

1. **Music:** Lyria, batch-generate per §1 prompts in `scripts/batch-01.md`. 2-3 takes per variant. **🔒 Composition locked 2026-10-08 (user confirmed from the real competitor's music):** a continuous background drone/pad, with a real piano playing rare, isolated single notes over it — long silences between notes, never a phrase or repeating pattern. Not drone-only. Every prompt in `batch-01.md` already carries this.
2. **Mastering:** reuse StillWave's tools (copied into `quiethertz/tools/`):
   ```
   python master-album.py "<raw-folder>"
   python select-album.py "<raw-folder>" "<raw-folder>-mastered" --slug <SLUG> --cap 180 --min-length 2.5
   ```
   Cap 180 min (3H) as a default target — adjust per video, competitor ranges 2H20M-4H.
3. **Assembly — ffmpeg, NOT CapCut** (one hero image/loop per video — generated once from the character+background template above, then still no manual editing beyond encoding):
   ```bash
   ffmpeg -loop 1 -i background.jpg -i album.wav \
     -c:v libx264 -tune stillimage -pix_fmt yuv420p -r 1 \
     -c:a aac -b:a 192k -shortest output.mp4
   ```
   If using the Flow loop instead of a static image:
   ```bash
   ffmpeg -stream_loop -1 -i loop.mp4 -i album.wav \
     -c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p \
     -c:a aac -b:a 192k -shortest output.mp4
   ```
4. **Thumbnail:** `assets/compose-thumb.py` (template script, parameterized by Hz text + tagline — do not redesign per video).
5. **Upload:** manual via Studio, same Karena checklist as StillWave (Not for kids, Scheduled first, no hashtags in title).

## 📝 Title formula (LOCKED — matches the validated competitor pattern)

```
[Hz number(s)] [Sleep Music / Healing Music] — [hook clause], [specific benefit] #1
```

- Lead with the Hz number AND "Sleep Music" / "Healing Music" in the first half — same Topic-Categorization logic as StillWave (`Music` word early = correct algorithmic categorization).
- Rotate specific benefits: insomnia relief, DNA repair, toxin/melatonin release, nervous system reset, third eye/pineal activation, emotional healing (fear/guilt release), spinal/full-body regeneration. Never generic ("relaxation", "calm") alone — competitor data shows specific outcomes outperform.
- `#1` on every new hook — leaves room to re-run the same hook as `#2`, `#3` later if it breaks out, exactly like the competitor.

## 🏷️ Tags — base set (reuse on every video, same logic as StillWave's locked base set)

```
solfeggio frequencies, healing frequency, deep sleep music, sleep music, meditation music, relaxing music, healing music, insomnia relief, stress relief music, binaural beats, frequency healing, calming music, background music, ambient music, sound healing, sleep meditation, relaxation music, bedtime music, anxiety relief, deep relaxation
```
Add 3-5 long-tail tags specific to the video's Hz combo and benefit.

## Source-of-truth files

- `CLAUDE.md` — this file
- `scripts/batch-01.md` — first 10-video package (titles, music prompts, tags, descriptions, pinned comments)
- `production-status.md` — pipeline tracker, same format as StillWave's
- `assets/compose-thumb.py` — reusable thumbnail template script
- `tools/master-album.py`, `tools/select-album.py` — copied from StillWave, same usage
