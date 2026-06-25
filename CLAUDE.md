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

YouTube Shorts channel — animated AI cat (Brain) explains **cat psychology, cat behavior, cat facts** (core) + occasional **Brain Science** (first-person science facts). Cats are the backbone; Brain Science is a rare accent, always in Brain's own first-person voice.

#### 🎯 FORMAT POLICY — mixed, cats-led (updated 14 июн 2026, supersedes old cats-only rule)

> ⚠️ **This replaces the old "ABSOLUTE RULE — cats-only" (11 мая 2026).** That strict cats-only period stalled the channel (~37 subs), so as of early June 2026 we returned to a **mixed format**: Cat Psychology/Behavior/Facts as the **core**, plus **Brain Science** (renamed from "Brain Hacks") as an occasional accent — but **only in Brain's first-person voice** so it still reads as "the same cat character," not a generic narrator on an off-topic video.

- ✅ **CORE rubrics (the backbone, default for every slot):** Cat Psychology, Cat Behavior, Cat Facts, Cat Communication, Cat Health, Cat History/Evolution, Cat Senses, Cat Bonding.
- ✅ **Brain Science (occasional accent, first-person only):** Brain narrates a science fact **as himself, from his POV** (e.g. "A Black Hole Would Stretch ME Into Spaghetti" — first-person re-upload 8 июн). Keep it rare (≤1 per week), keep the cat character central. The June first-person re-uploads are the validated pattern.
- ❌ **STILL FORBIDDEN — generic third-person off-topic** (the format that caused the crash): human-psychology / What If / Did You Know / Kids Trend videos delivered by a faceless narrator with no first-person cat framing. The demotion came from *audience confusion* (generic off-topic content on a cat-identity channel), not from science per se.
- ❌ **Anti-patterns** (compilation, AI-fiction, single-cat bio, persona-less narration) — see the locked list below; those are unchanged.
- During **recovery**, lean cats-heavy; reserve Brain Science for when there's a strong first-person hook. If unsure whether a topic fits, surface it and confirm before drafting.
- All title-style references — including the competitor `Мир Глазами Кошек` formulas — apply primarily to cat content.

**Historical lesson (why the crash happened — keep this in mind):** 11 мая – 7 мая 2026 BrainCatAI lost ~40-50× traffic because **third-person, off-topic, persona-less** videos (Sky Blue / Doorway Effect / Vagus Nerve / Black Hole) were posted to a cat-identity channel → YouTube read it as audience confusion → demoted the whole channel. The fix is NOT "never do science" — it's "**never break the cat persona / never go generic off-topic**." First-person Brain Science keeps the persona intact and is allowed. Legacy non-cat scripts (Sky Blue, Doorway Effect, Vagus Nerve, original Black Hole, Goosebumps, 6-7 Kids Trend) live in `scripts/_archive/` — don't duplicate them or make third-person sequels.

#### ❌ Anti-patterns — formats/practices we DON'T do (locked 30 мая 2026, from Nexlev+vidIQ analysis `analytics/2026-05-30-channel-analysis-nexlev.md`)

We stay in "cat psychology explainer" niche AND we don't drift to formats that have views but no moat:

- ❌ **NO compilation / repost нарезки** (CatExy / Cat Ranking style) — others' clips → copyright risk + zero knowledge moat + kills the expert-persona advantage.
- ❌ **NO AI-fiction / sketch series** (Orange Cat Chaos Lab style) — different audience, race to absurdity, loses educational identity.
- ❌ **NO single-cat biographical narrative** (Cats5ive / Boy the Flip Cat style) — about one specific cat → doesn't scale as a brand.
- ❌ **NO generic faceless narration without persona** — **Brain-as-cat-scientist IS the moat.** Lean into the persona: recurring mascot, mini-series, signature sign-off. Don't make videos that could be on any cat channel.
- ❌ **NO grammar errors in titles** — kills CTR and trust (e.g. "Does cats have 9 lives?" must be "Do Cats Have 9 Lives?"). Always proofread before publish.
- ❌ **NO key-behavior at END of title** — the specific behavior people search/recognize must be at the **START** of the title. Bad: "The REAL Reason for Why Your Cat Stares". Good: "Why Your Cat Stares — The REAL Reason".
- ❌ **NO abandoning what worked** — when a video hits (killer 22 May 5.2% CTR, TV 27 May leader, signs 21 May), **double down with 2-3 follow-ups on the same pattern within 2 weeks** (algorithm already knows who to show it to). We've been doing this (killer → stare-at-nothing; signs → trust-signs) — keep it as a rule.

**Benchmark target:** Furever Stories (44.2K subs, ~$8.1K, "Why Do Cats Not Like Belly Rubs?" 3.8M) — same niche, same model, executed better. That's our trajectory.

> 📅 **Cadence decision (locked 30 мая 2026, Dan):** **1 video/day** during recovery. Nexlev recommended 4-5/week to avoid diluting quality, but on stage-recovery (algo just starting to push via search 68%) the daily signal of activity matters more — slowing down now risks signalling "channel stalled." Revisit cadence once recovery is confirmed (subs growing, Shorts-feed retention > 30%, then consider switching to 5/week to up quality-per-video).

> 🕒 **Publish-slot rule (2 июн 2026, data-validated, Jerusalem UTC+3):** **Default = 15:00 локального**, validated by trust-signs (31 мая, 15:00 → **54 views / #1 of last 10 in 38h = best recovery signal**). Допустимое окно: **13:00-15:00** — 13-14:00 = пре-drop pattern (24 апр – 5 мая когда канал делал 700-1500 v/day), 15:00 = current recovery-validated slot. **НЕ идти позже 15:00** и НЕ возвращаться к 18:00-21:00 (период падения 10-27 мая). Пересмотреть когда наберём ≥3 видео с 100+ просм или Shorts-feed retention > 50%.

> ⏱️ **Upload-lead rule (7 июн 2026, Karena #7 LOCKED):** **загружать видео в YouTube за 3 часа до публикации** как **Scheduled / Unlisted** — НЕ Public сразу. Для 15:00 publish slot = upload к **12:00 локального**. За 3 часа: (1) видео рендерится до 4K (если выложить Public сразу — ранние зрители видят пиксели → retention падает), (2) Gemini читает контент → лучше targeting, (3) копирайт-чекер находит проблемы заранее. **Никогда** не жать Public сразу после загрузки. Полные 9 пост-публикационных правил Карены в [`braincatai/karena-playbook.md`](./braincatai/karena-playbook.md#-часть-1c--9-пост-загрузочных-заповедей-карены-что-не-делать-после-публикации).

> 🛑 **Post-publish freeze rule (7 июн 2026, Karena #8 LOCKED):** **после публикации НЕ менять title / thumbnail / description / tags**. Это не работает (Карена тестировал многократно — никаких изменений не вытаскивают видео в широкую органику; первое впечатление = data-профиль уже сформирован). Если после публикации заметили ошибку (грамматика в title, неправильный thumbnail) → **unlist + перевыложить как новое видео** (data starts fresh, лучше edit). Всё критичное — проверять ДО публикации через бот SEO Scorecard.

> 👀 **Self-view freeze rule (7 июн 2026, Karena #1+#2 LOCKED):** после публикации **НЕ смотреть своё видео** со своего YouTube-аккаунта если не досмотришь до конца — твой просмотр считается и портит retention/targeting. **НЕ слать ссылки** на видео в Telegram/Insta/чаты/друзьям — чужие data-профили загрязняют algorithm targeting. Если хочется проверить — смотри в Творческой Студии (не считается за просмотр). Метрики проверяем **раз в 24-48ч**, не каждые 5 минут (Karena #9 — anti-burnout).


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

**🔒 Pipeline (LOCKED 22 мая 2026 — user directive, do NOT deviate, do NOT propose other tools):**
**ALL images are generated in Nano Banana 2** (it holds Brain best — beats Nano Banana Pro and every other model; this is part of the standard, treat every image prompt as a Nano Banana 2 prompt) → **animation in Kling 3.0 image-to-video** (animate the Nano Banana 2 still with a motion-only prompt + "preserve input image") → **overlays/text/numerals + assembly in CapCut** → **VO via Google Vids TTS** (mouth closed). Static/reaction scenes (the majority) can skip Kling entirely and use a Ken Burns zoom on the Nano Banana 2 still.

> ⚠️ **Lesson (cost the user a full redo, 22 мая 2026):** do NOT send the user to generate images in Veo / Flow / Focal / OpenArt-Seedance / character-training etc. **Images = Nano Banana 2, period.** Tool-churn caused them to regenerate everything. Only Kling is used, and only for the animation step on a Nano Banana 2 image.

**Channel:** [@braincatai](https://www.youtube.com/@braincatai) · channel ID `UCMKcrIw1l1u_WU0M9Cv-DKw` · uploads playlist `UUMKcrIw1l1u_WU0M9Cv-DKw`

**Source of truth files:**
- `braincatai/karena-playbook.md` — **🎯 ALL Karena Roshaian Shorts rules in ONE place** (8 заповедей + строгий порядок SEO Pack + почему). **Read this before any script / SEO / thumbnail / upload task.** Canonical — if it conflicts with anything else, this file wins.
- `braincatai/director-checklist.md` — **master production playbook** with mandatory mantras, per-stage checklists, troubleshooting table, and analytics-based learnings. Read this before starting any new video.
- `braincatai/style-guide.md` — character, color, audio, editorial, locked AI prompts
- `braincatai/channel-about.md` — canonical YouTube channel description (cats + Brain Science)
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

**🛠️ YT Analytics dashboard (user's custom self-hosted bot — ALWAYS use this for pre-publish + discovery):**

Self-hosted YouTube analytics tool (own implementation of vidIQ + Social Blade combined).

**Where the code lives:**
- Repo: `jdan1980-ai/dan-documents`, branch `claude/seo-toolkit`
- User's local path: `C:\Users\jdan1\projects\dan-documents`

**How user runs it (Windows):**
- Desktop shortcut "Start Bot" (green icon) — auto-starts + opens browser
- Or manual:
  ```
  cd C:\Users\jdan1\projects\dan-documents
  git checkout claude/seo-toolkit
  .\venv\Scripts\activate
  uvicorn app.main:app --reload
  ```
- Open at **`http://127.0.0.1:8000`** (use 127.0.0.1, NOT `localhost` — Windows firewall blocks `localhost`)

**Recovery if bot won't start / can't see API key:**
```
taskkill /F /IM python.exe
```
Then start again.

**Channels configured:** BrainCatAI (`@braincatai`) and StillWave (`@stillwavezen`)

**Routes / sections (17 features):**
| Route | Section | Purpose |
|-------|---------|---------|
| `/channel` | АНАЛИЗ | Stats / outliers / upload frequency |
| `/seo` | PRE-PUBLISH | SEO Scorecard (title + description + tags + overall) |
| `/title-batch` | PRE-PUBLISH | Compare up to 10 title variants, scored |
| `/thumbnail` | PRE-PUBLISH | Contrast / readability / weight analysis |
| `/breakout` | DISCOVERY | What broke out in 7-90 days |
| `/trends` | DISCOVERY | Google Trends overlay |
| `/forecast` | INSIGHTS | Revenue forecast, Grade A++..F |
| `/velocity` | INSIGHTS | views/hour + 30-day projection |
| `/compare` | АНАЛИЗ | 2 channels side-by-side |
| (+ 8 more) | various | Auto-tags, Время, Comments, History, Competitor, etc. |

**Bot output files committed to `claude/seo-toolkit` branch (current as of branch tip):**
- `BRAINCAT_FULL_REVIEW.md` — detailed analysis of all 14 published Shorts with diagnosis + title rewrites
- `CHANNELS_SNAPSHOT.md` — channel statistics snapshot (last update visible in file header)
- `BRAINCAT_PINNED.md`, `STILLWAVE_PINNED.md` — pinned comment libraries
- `TITLE_REWRITES.md` — suggested title improvements
- `data/channels_snapshot.json` — machine-readable snapshot

**Access from assistant's sandbox:**
- Assistant CANNOT reach `http://127.0.0.1:8000` directly (network isolation)
- Workarounds:
  1. **Best**: read latest snapshot files committed to `claude/seo-toolkit` branch (`git show origin/claude/seo-toolkit:CHANNELS_SNAPSHOT.md`, `BRAINCAT_FULL_REVIEW.md`, etc.)
  2. Ask user for screenshot of a specific section if file data is stale
  3. Ask user to commit fresh snapshot to repo if needed

**When to ask user for screenshot from this dashboard:**
- Picking next topic → "Ключевики" or "Breakout" section
- Validating a draft title → "SEO Scorecard" or "Title A/B Batch"
- Reviewing thumbnail before upload → "Тумбнейл"
- Checking what's already published / outliers / channel state → "Канал" or "Видео"
- Researching competitors → "Competitor" or "Сравнение каналов"
- Planning upload time → "Время"

**CRITICAL — required check ORDER before recommending any topic / verifying what's published:**

1. **FIRST** → read `braincatai/production-status.md` (canonical source of truth for what's been published, scheduled, and in progress) — this file is updated by user as they publish, more reliable than any external snapshot
2. **THEN** → read `BRAINCAT_FULL_REVIEW.md` and `CHANNELS_SNAPSHOT.md` on `claude/seo-toolkit` branch for performance metrics (note the snapshot date — may be days/weeks stale)
3. **THEN** → ask user for fresh screenshot of YouTube Studio Content tab OR for fresh bot snapshot if either prior source is unclear or stale

**Lesson learned 17 мая 2026:** assistant recommended `slow-blink` for May 18 publish without checking `production-status.md` first — turned out it was already published May 9. Wasted user's time + risked recommending duplicate content. Always start with `production-status.md`.

**CRITICAL — keyword research tool priority (always free bot first, paid vidIQ MCP only as fallback):**

User's self-hosted bot has a free `/keywords` (POST `/keywords/research`) endpoint that uses YouTube search-no-quota — same data as vidIQ but FREE. ALWAYS use the bot for keyword research first. The paid `vidiq_keyword_research` MCP (5 credits/call) is fallback ONLY when bot is unreachable AND user explicitly confirms to spend credits.

**Workflow for keyword research (cache-first):**
1. **CHECK CACHE FIRST** → `braincatai/keyword-research/vidiq-cache.json` for the keyword (or near-synonym). If found and `fetched` <60 days old → **use cached data, ZERO cost**
2. **CHECK BOT** → ask user to run query in bot's `/keywords` section → screenshot results → paste in chat
3. **vidIQ MCP fallback** → only if cache miss AND bot unreachable AND user explicitly confirms to spend 5 credits per call
4. **AFTER ANY new vidIQ call** → ALWAYS write the result to `vidiq-cache.json` so future sessions can reuse it. Increment `total_credits_spent`. This is mandatory.

See `braincatai/keyword-research/README.md` for full schema + workflow.

**Lessons learned 17 мая 2026:**
- Burned ~25 vidIQ credits checking topics user already had in production OR could check for free in the bot. Don't waste paid credits on free-tool tasks.
- User's insight: vidIQ data stays relevant 30-60 days for cat niche → cache once, reuse for weeks. Implemented as `vidiq-cache.json` with all today's queries pre-loaded.

### StillWave (`/stillwave`)

YouTube channel — Japanese ambient · meditation · sleep · focus music. Handle: @stillwavezen.

**Pipeline:** Suno AI v5.5 (music) → NanoBanana (image 16:9 + 9:16) → Flow / Kling (video loop) → CapCut + ffmpeg (edit) → Canva MCP (thumbnail).

**Source of truth files:**
- `stillwave/CLAUDE.md` — project rules + 5 triggers (`SW:`, `SWS:`, `GAP: SW`, `CAL:`, `THUMB:`)
- `stillwave/published-videos.md` — every published video with stats
- `stillwave/competitor-research/competitor-tracker.md` — 5 tracked competitors
- `stillwave/content-ideas.md` — backlog (output of GAP/CAL runs)
- `stillwave/production-status.md` — pipeline tracker

**Trigger summary** (full spec in `stillwave/CLAUDE.md`):
- `SW: [тема]` → 11-item long-video package (Suno + Nano + Flow + YouTube copy)
- `SWS: [тема]` → 11-item Shorts package
- `GAP: SW` → top 10 unused themes + top 3 recommendations
- `CAL: [месяц]` → analytics + monthly calendar (4 videos / week)
- `THUMB: [тема]` → 4 Canva variants

#### MANDATORY rules (do not skip)

**Every time a script is created OR meaningfully edited, ALWAYS update the full SEO Pack — never skip tags.** The user has flagged this as a recurring miss.

> 🎯 **All Karena Roshaian rules now live in ONE canonical file: [`braincatai/karena-playbook.md`](./braincatai/karena-playbook.md).** It holds the 8 Shorts commandments (no hashtags in title, phone-only upload, Unlisted/Scheduled first, Not-for-kids, related-video funnel, 3-sec hook, app-update) AND the strict SEO Pack output order (Title → Alt titles → Description → Tags → Hashtags-body-only → Pinned → Thumbnail) AND the mandatory tag sets. **Read that file before any script / SEO / thumbnail / upload task — do not make the user re-explain.** If it ever conflicts with this summary, the playbook wins.

If editing the script's title, scenes, or VO, **re-verify tags reflect the new title and content**. Tags are not optional and must be reviewed on every edit.

**Every time a new script is created, ALWAYS append its pinned comment to `braincatai/pinned-comments.md`** — never skip. The pinned comment is already drafted inside each script's editing notes. Add it as the next numbered entry in the published or scheduled section, with date or "TBD". This file is the canonical place the user goes to copy-paste the comment when uploading.

**🗣️ Comment voice rule (locked 22 мая 2026, user directive): write EVERY comment like a real human, not a bot/marketer.** Applies to pinned comments AND replies. Casual, conversational, like an actual cat owner chatting. **Make it genuinely messy/organic, NOT polished:** lowercase, occasional run-on or fragment, a weirdly specific personal detail ("brought me a single sock at 4am lol"), "lol/omg/i cant", trailing thought instead of a clean question. **VARY the structure** — do NOT use the same statement→aside→question pattern every time (that's a tell). **Avoid:** engagement-bait formulas ("Drop a 🐾 if yes", "Comment below 👇"), clever similes / writerly phrasing ("like I'm a gazelle", "proudly dropped"), perfect grammar, marketing tone, emoji spam (1-2 max). Litmus test: if it reads like a marketer trying to sound casual, rewrite it messier.

**Other locked rules** (full detail in `style-guide.md`):
- Lock only Brain's character, NOT the background. Backgrounds are per-video.
- 1–3 locations max per video; identical wording across scenes that share a location. **Paste the FULL locked location detail (walls, floor, rug, armchair, window, plant) verbatim into EVERY scene prompt that shares it — do NOT shorthand it to just "INT. COZY LIVING ROOM".** Shorthand makes the AI improvise a different floor/rug each scene (locked 28 мая 2026 after circus rendered a beige patterned rug in one shot, a knit blanket in another, the sage rug in a third).
- **Locked rug = ONE plain SOLID sage-green woven rug — NO pattern, NO border, NO fringe, simple rectangular shape.** Solid + simple = fewest generation errors and stays consistent across scenes (user directive 28 мая: "закрепи тот ковёр который проще генерить чтоб меньше ошибок"). Add `patterned rug, beige rug, oriental/persian/floral rug, fringed rug, blanket on the floor instead of rug, different rug each scene` to negatives.
- CTA scene must take place in one of the video's existing locations — never a generic confetti/bokeh outro.
- Brain's mouth stays **closed** throughout — no lip-sync, no talking motion. Reactions go through eyes, ears, whiskers, body. Exceptions: held jaw-drop on shock, single yawn, one soft meow on CTA.
- Brain has **4 paws** (2 front + 2 back). The only constraint is the count — don't over-specify paw positions in prompts (it makes every shot look identical). NEVER show 5 paws or extra limbs. **All 4 paws — front AND back — are fully ginger, NEVER white socks/back-paws.** The AI keeps adding white socks ESPECIALLY on the back paws (caught in circus Sc 4, 28 мая 2026) — call out "both front and both back paws fully ginger" in the prompt + add `white back paws, white hind paws, white socks on back legs` to negatives.
- Brain's eyes are **bright emerald green** (`#3DDC84`) — never brown/amber/hazel. Warm lighting tends to tint them; always include the hex spec and `EYE COLOR RULE (strict)` in prompts. **Only the small IRIS is green; the sclera (white of the eye) stays PURE WHITE.** The `#3DDC84` spec keeps flooding the whole eyeball green — text alone ("iris set in white sclera") wasn't enough (recurred 25 мая). **Robust fix = describe eye ANATOMY, lead with white:** *"big round Pixar-style eyes, each a LARGE PURE WHITE sclera surrounding a medium EMERALD-GREEN iris (#3DDC84) with a black pupil; only the small iris is green, white of the eye stays pure white, never a fully-green eyeball."* Mention green once, lead with white. Add `green sclera, green eye-whites, fully green eyes, green-tinted eyeballs` to negatives. **Strongest lever: attach a known-good Brain image (correct white-sclera eyes) as a reference in Nano Banana 2** — eye anatomy carries from the reference better than any text.
- Each scene's voiceover ≤ 8 sec of speech (Veo 3 max clip length).
- **Music (Suno) prompts are written for 1 minute (~60s), not 56s** (locked 28 мая 2026 — user directive "промты для музыки пиши на 1 мин"). Gives buffer to cover the full video + end-card without the track cutting off early. Keep the time-coded structure (hook sting / build / payoff swell / soft close) but stretch it across ~60s.
- **VO is written in normal sentence case — NOT all-caps.** User tried UPPERCASE VO on 24 мая 2026 and called it off ("насчёт заглавных букв отбой, в след раз делай как раньше"). Write every VO (EN + RU) in normal case going forward. Keep EN and RU on separate lines / separate copy-blocks so each can be copy-pasted alone.
- **Every Shorts script MUST include a thumbnail prompt (Nano Banana 2) + thumbnail negatives — in its OWN dedicated `## 🖼️ ТУМБНЕЙЛ` H2 section, NOT buried inside the SEO Pack.** Locked 26 мая 2026 (user directive "Добавляй промт для тумбнейл в скрипты для каждого шортса"), reinforced 28 мая 2026 (user couldn't find it inside the circus script's SEO Pack — "почему в файле нет промта для тубиналс?"). It must be a clearly-marked standalone section so the user finds it instantly. No script ships without it. The template's thumbnail spec already has the channel-locked typography (Fredoka One / Nunito Bold, Electric Yellow #FFD23F, charcoal outline) + anatomy-eye rule + anti-realism wording — reuse it from `script-template.md`.
- **Thumbnail = «5 Signs» formula** (locked 27 мая 2026 — currently the best CTR on the channel per user's YouTube Studio data, surpassing killer-machine). Every thumbnail uses this skeleton: lицo 60% кадра + dilated emerald eyes locked into viewer + ONE visible hook-object (~20-25% area) + желтая text-плита bottom 25% (2 строки ALL CAPS Electric Yellow #FFD23F + charcoal outline, slight 2-4° tilt) + emoji marker (💔 negative / 🤯 mind-blow / 💚 warm / ❓ mystery / 😼 smug-predator). Heavy DOF blurred living-room background. The ONLY variable per video is the **emotion + hook-object + text** — typography, anatomy, colors stay locked. Full spec + cheat-sheet of emotion→topic mapping live in `script-template.md` thumbnail block.
- **Thumbnail emphasis (locked 28 мая 2026, user + YouTube guidance): EXTREME close-up + SHORT punchy headline.** (1) Crop tight — Brain's face/expression fills ~55-65% of the frame so the EMOTION reads instantly on a tiny phone thumbnail; don't let him shrink into the scene. (2) Thumbnail text must be **ultra-short and bold — max ~3-4 words per line, max 2 lines** (e.g. "38 YEARS OLD?!", "YOUR TV IS BROKEN?!", "CATS CAN BE TRAINED?!"). No full sentences, no small text. Big contrast, readable at thumbnail size. Curiosity/shock word does the work, not the title repeated. (3) **Text BIG + RAISED (locked 28 мая 2026):** the text plate must be LARGE (~85-90% of frame width) and positioned in the LOWER-MIDDLE (~55-70% height), NOT at the very bottom edge — Shorts thumbnails get the bottom covered by the phone UI / duration badge, so bottom-edge text is hard to read. User feedback: "надпись чуть крупней и выше а то её плохо видно на тел."
- VO must work for kids AND adults — no jargon, no scary words. See `style-guide.md` §9 swap table.
- Scientist/doctor/detective/etc. costume scenes — see `style-guide.md` §2 thematic costumes table. Wardrobe must keep collar + heart tag visible at the V-cut neckline.
- **Visualize the VO literally — show, don't pose.** If the VO names a concrete thing or action, the visual must literally show it (Brain licking the hair, holographic mother+kitten, thought-bubble of clumsy kitten, etc.). Generic "Brain sits with X expression" wastes Veo 3 credits. See `style-guide.md` §5d for tools (holograms, thought-bubbles, off-frame humans, costumes).
- **Lock the Human owner the same way Brain is locked.** When a scene needs a human in frame, use the locked spec from `style-guide.md` §2b: adult woman ~30, long chestnut-brown wavy hair (mid-back), cream-colored V-neck sweater, slim feminine build, Pixar 3D cartoon style, ALWAYS face-out-of-frame / turned away. Generate the human once → save as `assets/owner-reference.png` → attach as Nano Banana reference image in every subsequent scene to prevent drift between scenes (was happening: brunette in Sc 1, dark-haired man in Sc 2 — fixed 15 мая 2026).
- **All on-screen text MUST be in English** — channel is English-language (@braincatai). This applies to: thumbnails (title plate, arrow callouts), in-video overlays ("SAY THEIR NAME", "ADOPTED ✓", "TOP SCORE"), scene captions, chart labels in lab scenes. Russian alt-titles in scripts are ONLY for potential future RU mirror channel — never used on the current EN channel. Locked 15 мая 2026 after the assistant slipped Russian "ВОТ КАК ОНА ВИДИТ ВАС" into a thumbnail prompt.
- **All on-screen text/numerals in a single video MUST use ONE LOCKED FONT and ONE LOCKED STYLE.** This applies to: cartoon numerals in image prompts ("1", "2", "3" in curiosity-gap and build-up scenes), category lower-thirds ("1. GUARD", "2. SEPARATION", "3. TERRITORY"), in-video overlay phrases ("EVERY TIME", "BLINK = SOUND", "VERIFY"), chart labels in lab scenes, thumbnail text plate. If a video uses a soft pastel-yellow rounded sans for the curiosity-gap "3", then EVERY numeral/overlay/caption in that video must be the same soft pastel-yellow rounded sans — not a serif here and a brush there. The full channel-wide locked typography spec lives in `braincatai/style-guide.md` §13 (font family, weight, color, stroke). Locked 16 мая 2026 after typography drift made overlays feel like different videos stitched together.

## 📋 Self-contained prompt delivery (MANDATORY — locked 22 мая 2026, user directive)

**Every prompt the assistant hands to the user must be copy-paste ready with ALL locks already baked in — the user must NEVER have to assemble or paste anything extra.** Do this automatically, every time, without being asked:

- **Any image prompt** (Nano Banana) → automatically PREPEND the full **Locked Brain Prompt** (style-guide §8) at the start. The user copies one block and it already contains Brain's full locked look (kitten proportions, emerald #3DDC84 eyes, glasses, brown collar + heart tag, ginger paws/no white socks, 2 ears, 4 paws, Pixar cartoon / not photoreal).
  - 🚫 **NEVER use a placeholder** like `[Locked Brain Prompt]`, `[вставь Locked Brain сверху]`, "paste Brain here", etc. — in ANY prompt, in scripts OR in chat. The full Locked Brain text MUST be written out verbatim by the assistant in every single Brain image prompt. A placeholder = the user has to assemble the prompt = a miss. (Locked 10 июн 2026 after wake-up script shipped with `[Locked Brain Prompt]` placeholders in all 8 scenes + thumbnail.)
- **Any animation prompt** (Veo) → automatically INCLUDE the full **Veo anti-drift rules block** (EYE COLOR / GLASSES / SINGLE-CHARACTER / STYLE / ANATOMY / MOUTH / MOTION) before STYLE.
- **Any prompt with the human owner** → automatically include the HUMAN RULE + HAND COUNT RULE.
- Negatives block always included with the prompt.

If the assistant delivers a prompt missing these, that's a miss — fix it before the user spends credits. The canonical blocks live in `braincatai/style-guide.md`; scripts already embed them per-scene, but any prompt written fresh in chat must also be self-contained.

## 🛑 Veo 3 prompt pre-flight verification (MANDATORY — assistant runs this before delivering any Veo 3 prompt)

Locked 16 мая 2026 after user paid Veo credits to render bathroom Sc 4 with a phantom 3rd ear + chubby drift that should have been caught at the prompt review stage. **Veo 3 generations cost real money ($0.50-2 per scene × 8 scenes = $4-16 per video minimum, plus retries). Every Veo prompt the assistant delivers MUST be pre-flight verified against this checklist BEFORE handing it to the user.**

### Pre-flight checklist (run mentally on every Veo prompt before delivery)

For the **whole prompt**:
- [ ] Does it contain the full LOCKED BRAIN spec (kitten age + 2 ears + 4 paws + emerald #3DDC84 + glasses + collar)?
- [ ] Does it contain the full ANATOMY PRESERVATION RULE (anti phantom-ear + anti chubby-drift + identity-stays-IDENTICAL-to-input)?
- [ ] Does it contain MOUTH RULE (mouth closed throughout, no lip-sync)?
- [ ] Does it contain EYE COLOR RULE (#3DDC84 throughout, anti brown/amber)?
- [ ] If scene has on-screen text → TYPOGRAPHY LOCK block + TYPOGRAPHY PRESERVE RULE?
- [ ] If scene has the human owner → full LOCKED HUMAN OWNER block + HUMAN RULE (female + anti-male negatives)?
- [ ] If scene has the locked location → full prop-locked location block pasted verbatim (matches every other scene in this location)?

For **camera & motion** (high-drift-risk scenarios):
- [ ] **Static camera + 7-second hold = highest Veo drift risk.** If the shot is static, add a small motion element (subtle push-in, dolly, micro-zoom) to keep Veo "engaged" — pure static holds tend to introduce extra anatomy artifacts as Veo "fills time"
- [ ] If 7+ seconds with minimal motion → flag to user: consider 4-5s instead OR add motion
- [ ] Pattern-interrupt slow-mo scenes are second-highest drift risk → reinforce ANATOMY RULE explicitly
- [ ] **CHARACTER DIRECTION must match motion direction in Nano Banana input image.** If the scene requires Brain to move toward a target (chasing, walking to a door, leaping at lap), the input image MUST show Brain in PROFILE or 3/4-FROM-BEHIND oriented in that direction — NEVER 3/4-frontal or facing camera. Veo cannot re-orient a character mid-animation; it animates motion in the direction the body is already facing in the input image. Locked 16 мая 2026 after bathroom Sc 1: Nano Banana rendered Brain facing camera while woman walked away in deep background → Veo added motion forward → Brain ran TOWARD viewer while woman walked AWAY (directional contradiction). When the user sends a Nano Banana image and the character orientation contradicts the scene's motion direction, STOP before they spend a Veo credit and ask them to regenerate the image first.

For **clip length**:
- [ ] Veo 3 max single-clip length = 8 seconds. If beat needs >8s → split into 2 clips
- [ ] Longer clips = more drift opportunity. Default to ≤7s, only go longer when story-beat absolutely needs it

For **cost/risk awareness**:
- [ ] Flag any scene that's likely to fail or need retries (text-heavy, multiple characters, complex motion, static-camera holds)
- [ ] When flagging, propose a cheaper fallback (Google Vids overlay, image-only + Ken Burns, reusable universal clip)
- [ ] Estimate "retry risk" honestly: GREEN (likely first-try success), YELLOW (50/50, may need 2 tries), RED (likely needs 2+ retries — propose fallback)

For **delivery format** (how the prompt is handed to user):
- [ ] State explicitly: "I pre-flight verified this against the checklist — flags: [list any RED/YELLOW flags + recommended fallbacks]"
- [ ] If something on the checklist is missing → fix BEFORE delivering, not after the user spends credits
- [ ] If the scene is high-drift-risk → tell the user upfront so they can decide whether to spend the credit or use a fallback

### Real example of past failure (the lesson that triggered this rule)

Bathroom Sc 4 — Brain in sentry pose at doorway, static camera 7s, "very subtle zoom" (i.e. essentially no motion). I delivered the Veo prompt with only "ANATOMY RULE (strict): Brain has exactly 4 paws — 2 front, 2 back. NEVER show 5 paws or extra limbs." — no ear-count lock, no anti-drift language, no identity-preservation. Result: Veo morphed Brain into a chubbier-bodied generic cartoon kitten with a phantom 3rd ear sticking out of his head. User paid credits for an unusable clip.

**What I should have done:** caught the static-camera-7s = highest drift risk → flagged it → reinforced ANATOMY RULE with anti-ear + identity-preservation tokens → optionally proposed shortening to 5s. Instead I delivered raw and the user paid for the mistake.

### When you (Claude) skip the checklist

You'll know you skipped because you delivered a Veo prompt without an "I verified against checklist — flags: [...]" line. If you catch yourself doing that, immediately ask the user to HOLD the generation and re-verify. Better to delay 30s than to waste $2.

## Notes

- Add project-specific conventions, commands, and context here as the repository grows.
