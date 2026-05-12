# BrainCatAI — Remotion Hybrid Pipeline

Programmatic assembler for BrainCatAI Shorts. Mixes **Veo 3 animated clips** (for organic Brain motion) with **Remotion motion-graphic scenes** (for charts, glow effects, overlays). Outputs final 1080×1920 @ 30fps Short with burned-in subtitles, VO, and music.

First video using this pipeline: **`Where Your Cat Sleeps on Your Bed Reveals How Much They Trust You`** (script: `../scripts/where-your-cat-sleeps.md`).

---

## Pipeline split per scene

| Scene | Beat | Tool | Why |
|-------|------|------|-----|
| 1 | Hook on chest | **Veo 3** | Breathing + fur ripple + push-in — needs organic motion |
| 2 | Bed survey + 4 glow zones | **Remotion** | Static Brain (Nano Banana) + 4 animated glow circles |
| 3 | Scientist Brain at wall chart | **Remotion** | Static Brain in lab coat + animated heart-chart |
| 4 | TOP SCORE chest reveal | **Remotion** ⭐ | Biggest savings — chart burst + ribbon text |
| 5 | Scent shimmer at head | **Veo 3** | Intimate breathing motion |
| 6 | Slow-mo pull-back twist | **Veo 3** | Key pattern interrupt, must be cinematic |
| 7 | Paw on wrist + anchor glow | **Remotion** | Static close-up + breath-synced glow |
| 8 | CTA wave + soft meow | **Veo 3** | Emotional resolution, mouth exception |

**Veo 3 credits used: 4 (vs 8 baseline) — 50% savings.**

---

## Folder structure

```
remotion/
├── package.json
├── tsconfig.json
├── remotion.config.ts
├── src/
│   ├── index.ts              # registerRoot entry
│   ├── Root.tsx              # composition registry
│   ├── Main.tsx              # assembles 8 scenes + VO + music + end card
│   ├── lib/
│   │   ├── constants.ts      # 1080×1920, 30fps, durations, colors
│   │   ├── script.ts         # per-scene VO + source (veo vs remotion)
│   │   └── Subtitles.tsx     # burned-in captions, 4 words/chunk
│   └── scenes/
│       ├── Scene2BedSurvey.tsx
│       ├── Scene3LabChart.tsx
│       ├── Scene4TopScore.tsx
│       └── Scene7PawAnchor.tsx
└── public/                   # gitignored — drop assets here before render
    ├── assets/               # Nano Banana PNG backgrounds for Remotion scenes
    │   ├── scene2-bed-bg.png
    │   ├── scene3-brain-lab.png
    │   ├── scene4-brain-labcoat.png
    │   └── scene7-paw-wrist.png
    ├── clips/                # Veo 3 .mp4 clips for scenes 1, 5, 6, 8
    │   ├── scene1-hook.mp4
    │   ├── scene5-scent.mp4
    │   ├── scene6-twist.mp4
    │   └── scene8-cta.mp4
    └── audio/
        ├── vo.mp3            # one continuous ElevenLabs read
        └── music.mp3         # Suno/Udio bed
```

---

## Production order

1. **Generate assets in Nano Banana** — use the image prompts from `../scripts/where-your-cat-sleeps.md` for scenes 2, 3, 4, 7. Save as `public/assets/sceneN-*.png`.
2. **Render Veo 3 clips** for scenes 1, 5, 6, 8 from the animation prompts in the script. Save as `public/clips/sceneN-*.mp4`.
3. **Record VO** in ElevenLabs from the full voiceover block at top of the script. Save as `public/audio/vo.mp3`.
4. **Generate music** in Suno using the music prompt in the script. Save as `public/audio/music.mp3`.
5. **Preview in Remotion Studio:** `npm run dev` — opens browser at localhost:3000 with all compositions.
6. **Render final:** `npm run build` — outputs `out/short.mp4`.

---

## Commands

```bash
cd braincatai/remotion
npm install              # one-time
npm run dev              # Remotion Studio (preview/scrub)
npm run build            # render MainComposition → out/short.mp4

# render individual scene for QA
npx remotion render Scene4TopScore out/scene4.mp4
```

---

## Editing notes

- **Subtitles** are burned in via `Subtitles.tsx`. To disable for a custom upload, comment out `<Subtitles />` in `Main.tsx`.
- **VO timing:** the assembler assumes each scene's VO line fits in 7s. If your ElevenLabs read needs more time on a line, increase `SCENE_DURATION_SEC` in `constants.ts` (affects all scenes) or split that scene's VO into a separate `<Audio>` with custom timing.
- **Veo vs Remotion swap:** to flip a scene from Veo to Remotion (or back), edit `src/lib/script.ts` — change the `source` field. Then build the Remotion component if going that direction.
- **Adding text overlays** ("TOP SCORE", etc.) — overlay Remotion components even on Veo clips by adding them inside the `<Sequence>` in `Main.tsx` after the `<Video>` tag.

---

## Why this pipeline

- **Versioned video** — every render is reproducible from git, no Google Vids click-trail
- **Cheap iteration** — adjusting a chart pulse takes seconds vs re-generating in Veo
- **Consistent subtitles + brand** — single TSX file controls every video's typography
- **Hybrid economics** — Veo 3 only for what AI does uniquely well (organic Brain motion), Remotion for everything programmable
