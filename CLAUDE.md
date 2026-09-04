# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## Repository

`jdan1980-ai/dan-documents` — personal documents repository.

## Projects

### BrainCatAI (`/braincatai`)

YouTube Shorts channel — animated AI cat (Brain) explains cat psychology and brain-bending facts.

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

## 📋 Upload playbook — Karena Roshaian (applies to ALL channels)

Locked YouTube upload rules. Check every video against these before publishing — both StillWave and BrainCatAI.

1. **NO hashtags in the title field.** Hashtags live in the description body only.
2. **Fill tags up to ~500 chars**, distributed: **brand ~20% + broad ~20% + narrow/long-tail ~40-50%** (rest medium). Brand = channel name + signature series terms; broad = huge generic keywords; narrow = specific multi-word phrases that exactly match the video. No mismatched carryover tags.
3. **Upload from the phone only** — the phone lets you pick the freeze-frame for the thumbnail. (Custom uploaded thumbnails are fine and preferred where we have them.)
4. **First publish = Unlisted or Scheduled, never straight to Public.** Review, then flip.
5. **Always set "Not for kids"** (Made for kids = No).
6. **Link Short → long-form** via the Related video setting so the Short funnels to the full video.
7. **First 3 seconds = ~90% of retention weight.** Open ON the scene + sound immediately — no slow fade-in from black at 0:00. Any text overlay (wisdom card, etc.) comes AFTER the hook lands, never delaying it.
8. **Update the YouTube app before each upload** (avoids stale-version upload bugs).

### Public copy rules (titles, descriptions, pinned comments)

- **No specific weekdays.** Never write "every Wednesday" / "next Tuesday & Friday". Use **"next week" / "every week" / "the next one"**. Schedules change; specific days date the copy and break promises.
- **Don't lean on Vol. 1 / Vol. 2 numbering in public copy.** Refer to "the next session" / "the series" / "the next one". Volume numbers can stay in internal slugs/tracking docs for organization, but keep them out of public titles, descriptions, and pinned comments.

## Notes

- Add project-specific conventions, commands, and context here as the repository grows.
