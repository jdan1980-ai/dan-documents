# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## Repository

`jdan1980-ai/dan-documents` — personal documents repository.

## Projects

### BrainCatAI (`/braincatai`)

YouTube Shorts channel — animated AI cat (Brain) explains cat psychology and brain-bending facts.

**Pipeline:** 8 scenes → image in Nano Banana → animation in Veo 3 → assembly in Google Vids.

**Source of truth files:**
- `braincatai/style-guide.md` — character, color, audio, editorial, locked AI prompts
- `braincatai/script-template.md` — copy-paste template for every new video
- `braincatai/content-ideas.md` — backlog
- `braincatai/scripts/<slug>.md` — one file per video

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

**Other locked rules** (full detail in `style-guide.md`):
- Lock only Brain's character, NOT the background. Backgrounds are per-video.
- 1–3 locations max per video; identical wording across scenes that share a location.
- CTA scene must take place in one of the video's existing locations — never a generic confetti/bokeh outro.
- Brain's mouth stays **closed** throughout — no lip-sync, no talking motion. Reactions go through eyes, ears, whiskers, body. Exceptions: held jaw-drop on shock, single yawn, one soft meow on CTA.
- Brain has **4 paws** (2 front + 2 back) — only **ONE front paw at a time** is raised (wave/point/gesture). Both front paws raised together causes AI to generate 5+ legs / extra limbs.
- Each scene's voiceover ≤ 8 sec of speech (Veo 3 max clip length).
- VO must work for kids AND adults — no jargon, no scary words. See `style-guide.md` §9 swap table.

## Notes

- Add project-specific conventions, commands, and context here as the repository grows.
