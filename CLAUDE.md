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

### Debate the user when they propose something weak (locked 13 мая 2026)

User directive: **don't just agree because the user asked**. User is a newcomer and wants pushback when their idea is suboptimal. Treat them as someone who values being challenged with reasoning over being humored.

When to push back:

- User proposes a topic/title/strategy where I see a 2× better alternative supported by data
- User picks a workflow that wastes credits or time when a simpler version exists
- User makes a decision based on instinct that contradicts what their own analytics show
- User asks me to do something that breaks a previously-locked policy (cats-only, single-paw rule, etc.)
- User asks for something I know will reduce monetization potential

How to push back (be assertive, not passive):

- State my disagreement directly: "I think this is the wrong move because…"
- Show the data / past pattern that supports the alternative
- Propose a concrete better option with effort estimate
- Then ask "сделать так или всё-таки настаиваешь на своём варианте?" — let them override with full information

Don't:
- Soften disagreement to the point of being agreeable ("maybe consider…")
- Agree to start work and complain later
- Execute something I know is wrong without flagging

Do:
- Use the 🚨 Risk format if it's risky, 💡 Opportunity format if it's a missed win, or just a direct "disagree because X" if it's a judgment call
- Be specific about WHY my alternative is better (data, past KPI, vidIQ score, search volume, retention pattern)
- Defer to user if they confirm after seeing my argument — they're the owner

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

#### 🔍 MANDATORY — Pre-scripting vidIQ keyword check (locked 13 мая 2026)

**Before writing ANY new script, pull `vidiq_keyword_research` on the main keyword for that topic.** Do NOT skip this. Do NOT write a script until the keyword check is done and the user has seen the score.

Why locked: we wasted credits writing `cats-hear-you-blinking` (vidIQ score 0, zero search demand) when `your-cat-sees-you-as-giant-cat` was available at score 71.47 with 50,361 monthly searches and direct competitor proof of virality. **Every low-score script written = an opportunity to write a high-demand script lost.** User goal is monetization — every wasted slot delays Tier 1/Tier 2 thresholds.

**Protocol:**

1. User proposes a topic (or I propose a candidate from the backlog)
2. Run `vidiq_keyword_research` with the main keyword (e.g. "why cats stare at you")
3. Surface the result in this format:

```
🔍 vidIQ check for "[topic]":

- Main keyword: "[exact keyword]"
- Overall score: [X.XX]
- Monthly searches: [N,NNN]
- Competition: [X.X] (low/medium/high)
- Top related keyword: "[strongest related]" — score [Y], [M] monthly

Verdict: [GREEN >65 / YELLOW 50-65 / RED <50]
```

4. Decision gates:
   - **GREEN (overall >65, monthly >5k):** proceed to write the script
   - **YELLOW (50-65 or monthly 2-5k):** I propose an alternative cat topic from `content-ideas.md` or my own suggestion that scores higher, then user picks
   - **RED (<50 or monthly <2k):** I push back firmly with the "debate me" rule — explain why I think this is a waste of a production slot, propose 2-3 alternative cat topics with higher scores, ask user to confirm if they still want to proceed or pivot
5. If user overrides a YELLOW/RED after seeing the data → proceed but note the override in the script's Meta block ("⚠️ Written despite vidIQ score X — user override on [date]") so we can audit the call later

**Cost of the check:** 5 vidIQ credits per topic. With ~1938 credits in the bank that's 387 keyword checks before running dry. The cost of NOT checking (a low-score script): ~$50-65 in Veo/Nano production + 1 publishing slot + lost momentum during recovery.

**Related-keyword harvest:** when `vidiq_keyword_research` returns related keywords with score >60, save them in the script's Tags section AND consider them as future topic candidates. Add the top 2-3 to `content-ideas.md`.

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

**Every time a script is created OR meaningfully edited, ALWAYS update the full SEO Pack — never skip tags.** The user has flagged this as a recurring miss. The SEO Pack must include the items in **this exact output order** (locked 15 мая 2026 — title-bar hashtags right after the title because they paste into the same YouTube field):

1. **Title** (40–70 chars, end with `🐱 | Cat Psychology` for channel brand)
2. **Hashtags for title bar** (top 3 — `#shorts` always first — paste these at the end of the title field on YouTube)
3. **Alt titles to A/B test** (optional, for variant testing)
4. **Description** (≥ 250 chars, repeat main keyword 2–3×, include 5+ supporting keywords, end with extended hashtag block + follow CTA)
5. **Tags** (20–25 tags, mix broad + medium + long-tail, total under 450 chars). The base set is **always** included:
   ```
   cat psychology, cat facts, cat behavior, cat secrets, cat science,
   cat communication, cat body language, feline behavior, understanding cats,
   facts about cats, animal facts, animal science, did you know,
   mind blowing facts, brain cat, cat facts daily, cat behavior funny,
   cat domestication, cats vs humans
   ```
   Then add 5–10 long-tail tags specific to the video.
6. **Pinned comment** (with engagement question)
7. **Thumbnail concept**

(The title-bar hashtags are item 2 above — listed there because they paste into the YouTube title field. An extended hashtag set is included in the description block at item 4.)

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
