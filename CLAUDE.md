# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## Repository

`jdan1980-ai/dan-documents` — personal documents repository.

## Projects

### BrainCatAI (`/braincatai`)

YouTube Shorts channel — animated AI cat (Brain) explains **cat psychology, cat behavior, cat facts**. Cats only.

#### 🚫 ABSOLUTE RULE — cats-only channel (do not violate)

User policy as of 11 мая 2026: **every BrainCatAI video must be about cats.** YouTube's algorithm demoted previous off-topic videos (Brain Hacks / What If / Did You Know / Kids Trend) for "content doesn't fit channel". Even when one off-topic video (Sky Blue) outperformed expectations, the channel paid for the others.

- ✅ ALLOWED rubrics: Cat Psychology, Cat Behavior, Cat Facts, Cat Communication, Cat Health, Cat History/Evolution, Cat Senses
- ❌ FORBIDDEN rubrics (do NOT propose, do NOT script): Brain Hacks, What If, Did You Know (non-cat), Kids Trend, anything physics/space/anatomy/psychology of humans
- ❌ FORBIDDEN even with a "cat angle": stretching a human topic onto Brain. The topic itself must be feline.
- If user asks to deviate ("let's do a Brain Hacks one"), surface this rule and ask them to confirm before drafting.
- All title-style references — including the competitor `Мир Глазами Кошек` formulas — apply only to cat content.

Existing non-cat scripts in the repo (Sky Blue, Doorway Effect, Vagus Nerve, Black Hole, Goosebumps, 6-7 Kids Trend) are **legacy** — do not duplicate, do not generate sequels in those niches. Their slots in the schedule should be swapped for cat topics where still possible.

**Pipeline:** 8 scenes → image in Nano Banana → animation in Veo 3 → assembly in Google Vids.

**Channel:** [@braincatai](https://www.youtube.com/@braincatai) · channel ID `UCMKcrIw1l1u_WU0M9Cv-DKw` · uploads playlist `UUMKcrIw1l1u_WU0M9Cv-DKw`

**Source of truth files:**
- `braincatai/director-checklist.md` — **master production playbook** with mandatory mantras, per-stage checklists, troubleshooting table, and analytics-based learnings. Read this before starting any new video.
- `braincatai/style-guide.md` — character, color, audio, editorial, locked AI prompts
- `braincatai/script-template.md` — copy-paste template for every new video
- `braincatai/content-ideas.md` — backlog
- `braincatai/scripts/<slug>.md` — one file per video
- `braincatai/analytics/` — performance reviews and API snapshots

**Live API queries** (key in `/root/.config/youtube-api-key`):
```bash
KEY=$(cat /root/.config/youtube-api-key)
curl -s "https://www.googleapis.com/youtube/v3/channels?key=$KEY&id=UCMKcrIw1l1u_WU0M9Cv-DKw&part=statistics" | jq
curl -s "https://www.googleapis.com/youtube/v3/playlistItems?key=$KEY&playlistId=UUMKcrIw1l1u_WU0M9Cv-DKw&maxResults=50&part=contentDetails" | jq
```

### StillWave (`/stillwave`)

YouTube channel — Japanese ambient · meditation · sleep · focus music. Handle: @stillwavezen.

**Pipeline:** Suno AI v5.5 (music) → NanoBanana (image 16:9 + 9:16) → Flow / Kling (video loop) → CapCut + ffmpeg (edit) → Canva MCP (thumbnail).

**Source of truth files:**
- `stillwave/CLAUDE.md` — project rules + 5 triggers (`SW:`, `SWS:`, `GAP: SW`, `CAL:`, `THUMB:`)
- `stillwave/published-videos.md` — every published video with stats
- `stillwave/competitor-tracker.md` — 5 tracked competitors
- `stillwave/content-ideas.md` — backlog (output of GAP/CAL runs)
- `stillwave/production-status.md` — pipeline tracker

**Trigger summary** (full spec in `stillwave/CLAUDE.md`):
- `SW: [тема]` → 11-item long-video package (Suno + Nano + Flow + YouTube copy)
- `SWS: [тема]` → 11-item Shorts package
- `GAP: SW` → top 10 unused themes + top 3 recommendations
- `CAL: [месяц]` → analytics + monthly calendar (4 videos / week)
- `THUMB: [тема]` → 4 Canva variants

#### MANDATORY rules (do not skip)

**Every time a script is created OR meaningfully edited, ALWAYS update the full SEO Pack — never skip tags.** The user has flagged this as a recurring miss. The SEO Pack must include:

1. **Title** (40–70 chars, end with `🐱 | Cat Psychology` for channel brand)
2. **Description** (≥ 250 chars, repeat main keyword 2–3×, include 5+ supporting keywords, end with hashtag block + follow CTA)
3. **Tags** (20–25 tags, mix broad + medium + long-tail, total under 450 chars). The base set is **always** included:
   ```
   cat psychology, cat facts, cat behavior, cat secrets, cat science,
   cat communication, cat body language, feline behavior, understanding cats,
   facts about cats, animal facts, animal science, did you know,
   mind blowing facts, brain cat, cat facts daily, cat behavior funny,
   cat domestication, cats vs humans
   ```
   Then add 5–10 long-tail tags specific to the video.
4. **Hashtags**: top-3 for title bar (`#shorts #catpsychology #catfacts`) + extended set in description body
5. **Thumbnail concept**

If editing the script's title, scenes, or VO, **re-verify tags reflect the new title and content**. Tags are not optional and must be reviewed on every edit.

**Every time a new script is created, ALWAYS append its pinned comment to `braincatai/pinned-comments.md`** — never skip. The pinned comment is already drafted inside each script's editing notes. Add it as the next numbered entry in the published or scheduled section, with date or "TBD". This file is the canonical place the user goes to copy-paste the comment when uploading.

**Other locked rules** (full detail in `style-guide.md`):
- Lock only Brain's character, NOT the background. Backgrounds are per-video.
- 1–3 locations max per video; identical wording across scenes that share a location.
- CTA scene must take place in one of the video's existing locations — never a generic confetti/bokeh outro.
- Brain's mouth stays **closed** throughout — no lip-sync, no talking motion. Reactions go through eyes, ears, whiskers, body. Exceptions: held jaw-drop on shock, single yawn, one soft meow on CTA.
- Brain has **4 paws** (2 front + 2 back). The only constraint is the count — don't over-specify paw positions in prompts (it makes every shot look identical). NEVER show 5 paws or extra limbs.
- Brain's eyes are **bright emerald green** (`#3DDC84`) — never brown/amber/hazel. Warm lighting tends to tint them; always include the hex spec and `EYE COLOR RULE (strict)` in Veo 3 prompts.
- Each scene's voiceover ≤ 8 sec of speech (Veo 3 max clip length).
- VO must work for kids AND adults — no jargon, no scary words. See `style-guide.md` §9 swap table.
- Scientist/doctor/detective/etc. costume scenes — see `style-guide.md` §2 thematic costumes table. Wardrobe must keep collar + heart tag visible at the V-cut neckline.
- **Visualize the VO literally — show, don't pose.** If the VO names a concrete thing or action, the visual must literally show it (Brain licking the hair, holographic mother+kitten, thought-bubble of clumsy kitten, etc.). Generic "Brain sits with X expression" wastes Veo 3 credits. See `style-guide.md` §5d for tools (holograms, thought-bubbles, off-frame humans, costumes).

## Notes

- Add project-specific conventions, commands, and context here as the repository grows.
