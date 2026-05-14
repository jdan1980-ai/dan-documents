# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## Repository

`jdan1980-ai/dan-documents` — personal documents repository.

---

## 🚨 Proactive Risk Warning Rule (locked policy — do not skip)

User directive (13 мая 2026): **Always warn the user BEFORE executing if you see a risk they may not see.** Don't just be an order-taker. If you spot something that could hurt the channel / project / user's goal — surface it first, even if the user explicitly asked for the action.

### When to trigger a warning

Any of these patterns:

- **Niche-violation risk:** action contradicts a locked policy (e.g. proposing a non-cat video on BrainCatAI; non-ambient content on StillWave)
- **Algorithm/SEO penalty risk:** title/thumbnail/description choice could lower vidIQ score, trigger keyword-stuffing flag, hashtag-spam flag, audience-confusion demotion, copyright strike, etc.
- **Credit/cost waste risk:** producing a clip that's likely to fail Veo 3 (e.g. text-heavy scene without fallback, multiple characters in frame, etc.) without surfacing the cheaper fallback
- **Production drift risk:** locked character/style elements being weakened or removed across edits (e.g. losing kitten-lock, eye-color spec, collar/glasses requirement)
- **Schedule/cadence risk:** posting decision that could disrupt audience-identity signal during recovery, double-publish that confuses tracking, or premature publish of unfinished content
- **Data-driven risk:** keyword research, competitor data, or vidIQ score shows the action is suboptimal vs an obvious alternative
- **Reversibility risk:** any non-reversible action (delete vs unlist, force push, public schedule that's hard to retract)

### How to warn (format)

When you spot the risk, **STOP execution** and post a clear message structured as:

```
🚨 Heads up — I see a risk you might not have factored in:

**What I see:** [concrete observation, with data/links/file paths]
**Why it's a problem:** [mechanism, with evidence — past kpi, vidIQ data, channel pattern, etc.]
**Recommended action:** [what I'd do instead]
**Cost of ignoring it:** [realistic estimate — views lost, days delay, credits wasted, etc.]

Confirm to proceed anyway, or say which alternative to take.
```

Then **wait for user confirmation** before doing the risky action.

### Real example (the lesson that triggered this rule)

11 мая – 7 мая 2026 BrainCatAI lost ~40-50× traffic (from ~700-1500 v/day down to ~25 v/day) because non-cat videos (Sky Blue / Doorway Effect / Vagus Nerve / Black Hole) were posted to a cat-identity channel. YouTube's algorithm treated it as audience confusion and demotioned the entire channel.

**Where I (Claude) failed:** I was writing and shipping non-cat scripts (Brain Hacks, What If, Did You Know rubrics) without surfacing the channel-fit risk. The user only realised after seeing the analytics crash. I should have warned BEFORE the first non-cat script — "this could trigger a channel-fit demotion, do you want to keep going?".

**What recovery cost:** ~2-4 weeks of zero growth + unlisting 4 published videos + production stalled for several days.

This is the canonical example of "I saw what user didn't" — going forward, surface risks proactively in this exact format.

### Don't be a yes-man

- If user asks for X and you see X will hurt the goal → warn first, then execute if confirmed.
- If user asks for X and you see Y is a 2× better path (vidIQ score, search volume, retention pattern) → recommend Y with data before doing X.
- If user is about to make a reversible decision with downside → flag it; if irreversible → flag harder.
- "User asked for it" is not a reason to skip the warning. Confirmation is the gate, not silence.

### Opportunity-spotting (the flip side of risks)

Surface opportunities the user might miss — especially anything that moves monetization closer. User's stated goal as of 13 мая 2026: **channel monetization, not just audience growth**. Production costs $43-65 per video; break-even target is ~$1,000/month revenue. See [`braincatai/analytics/monetization-roadmap.md`](./braincatai/analytics/monetization-roadmap.md) for full math + 13-lever optimization list + monthly check-in schedule.

Trigger opportunity callouts when you see:

- **Higher-demand topic available** — current script topic scores X on vidIQ but you spot a higher-score alternative the user hasn't seen
- **Reusable asset opportunity** — a scene/template/prompt that could be generated once and reused, saving Veo 3 credits
- **Production efficiency win** — Google Vids overlay vs Veo render, batch optimization, fallback patterns
- **Cross-platform leverage** — RU mirror, longform bundle from existing Shorts (alt monetization path), TikTok/IG cross-post
- **Engagement window** — first-hour comments unanswered, missed pinned-comment, A/B thumbnail not used
- **Monetization milestone proximity** — when you spot the user crossing a tier threshold soon, surface it

Format opportunity callout as:

```
💡 Opportunity I see:

**What I notice:** [observation, with data]
**Why it matters:** [revenue/credits/audience implication, quantified if possible]
**Lift estimate:** [e.g. "+2-3× audience capture per video" / "$30-50/week saved"]
**Effort:** [low / medium / high — be honest]

Want me to apply it?
```

Then **wait for user yes/no** before executing.

---

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
