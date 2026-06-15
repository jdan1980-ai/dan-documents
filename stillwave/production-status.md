# StillWave — Production Status

Single source of truth for the StillWave pipeline. Update at every status change.

**Pipeline stages:** 📝 concept → 🎵 suno generated → 🎨 image generated → 🎬 video generated → 🎞️ assembled → ⏰ scheduled → 📤 published

---

## Published

See `published-videos.md` for the full table with metrics.

## In production / scheduled

> Pipeline для long-form статической картинки: 📝 script → 🎵 suno generated → 🎨 image generated → 🎬 ~~not needed~~ → 🎞️ ffmpeg encoded → ⏰ scheduled → 📤 published.

| Slug | Title | Length | 📝 | 🎵 | 🎨 | 🎞️ | ⏰ | 📤 |
|------|-------|--------|----|----|----|-----|-----|-----|
| `mushin-no-mind-state` | MUSHIN — 無心 \| Japanese Zen Music for No-Mind State, Deep Focus & Inner Stillness | 2H 01min 11sec (38 tracks) | ✅ | ✅ | ✅ thumb + Shorts cover | ✅ CapCut assembled | ✅ **scheduled Tue Jun 16, 18:00 MSK** (`CamT9sohYQM`) | ⏳ |
| `tokyo-apartment-rain-1h` | Power Hour Focus Music — Tokyo Apartment Rain | 1H 04min 48sec (24 tracks) | ✅ | ✅ | ✅ | ✅ | ✅ **scheduled May 10, 14:00** | ⏳ |

### MUSHIN — 無心 scheduled Tue Jun 16, 18:00 MSK (`CamT9sohYQM`)

**FIRST Kanji-Concept Series video.** Built on the locked formula from competitor analysis 2026-06-15 (Hikari Zen TAO 973K, RollinSound BUDŌ/TORA/IKIGAI, Seiiki KAMI 428K). The bet: Healing Hour Vol.1 + Vol.2 plateaued because we used Ghibli + Hz format instead of the proven Kanji-Concept + photoreal-cinematic + lone-monk + symbolic-visual-hook formula. MUSHIN implements the full corrected formula.

**SEO can't be verified pre-publish** (VidIQ public API doesn't return Scheduled videos). Verify post-publish:
- **Wed Jun 17 morning (~12-14h after live):** pull metadata, confirm Topic Categories = `Music` (not Lifestyle like 50/10!), title intact, description intact, tags intact
- If Topic = Lifestyle → rename title immediately (per CLAUDE.md Topic-Categorization rule)

**Why 18:00 MSK Tue is OK for Healing Hour:** unlike Pomodoro/work-music (which peaks weekday mornings), meditation/sleep/focus content has 24/7 demand. Evening drops catch the wind-down + sleep-prep audience.

**Review schedule:**
- **48h** — Thu Jun 18, 18:00: log views/likes/comments + VPH + verify Topic still Music
- **7d** — Tue Jun 23: real read. Success benchmarks:
  - D7 views > 200 → MUSHIN formula works, **plan next Kanji-Concept** (SATORI/YUGEN/KENSHO)
  - D7 views 50-150 → format helps a bit but channel-authority is still the ceiling
  - D7 views < 50 → format wasn't the magic bullet; channel needs a different lever (cross-platform, paid boost, fundamental pivot)
- **30d** — Thu Jul 16: final snapshot; lock or unlock the Kanji-Concept Series template

**Asset references in repo:**
- Script: `stillwave/scripts/mushin-no-mind-state.md` (full description Hikari-style, 38-track tracklist, tags Hikari formula, pinned, Shorts package)
- Thumbnail: `stillwave/assets/mushin-no-mind-thumb.jpg` (16:9, vertical 無心 tategaki cream + MUSHIN romaji)
- Shorts cover: `stillwave/assets/mushin-no-mind-shorts-cover.jpg` (9:16, kanji + MUSHIN + Japanese Zen Music)

**Shorts cross-promo decision logic:**
- If D2 long-form views > 50 → drop Shorts cover D3-D4 (Fri Jun 19 / Sat Jun 20)
- If D2 < 50 → skip Shorts (cross-promo on 50-sub channel doesn't work, per 25/5 and 50/10 lessons)

**Update 2026-06-15:** user chose **D1 drop strategy** instead — Shorts publishes Wed Jun 17 18:00 MSK (exactly 24h after long-form), regardless of long-form D1 performance. Rationale: catch the long-form's D1-D2 algorithmic test while it's still hot, rather than wait for the plateau (D3-D4 delayed strategy failed on Pomodoro 25/5 with only 11 views on Shorts). New experimental cross-promo timing — we'll learn from the comparison vs Pomodoro 25/5 delayed.

### Tokyo Apartment Rain — review schedule

After publish (May 10, 14:00):
- **48h review** — May 12, 14:00 → pull live API data, log views/likes/comments/CTR
- **7d review** — May 17, 14:00 → full retention analysis + comment mining + first lessons
- **30d review** — June 9, 14:00 → final perf snapshot, decide if pattern goes into Power Hour series template
| `bonsai-desk-night-2h` | Deep Focus Music — Bonsai Desk Late Night | 2H | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⚠️ predates locked Pomodoro look (hourglass + chroma timer + music-breathing). Reshape before producing. |
| ~~`lantern-glow-study-3h`~~ | ~~Quiet Hours Focus Music — Lantern Glow Study~~ | ~~3H~~ | ~~✅~~ | — | — | — | — | — | 🪦 **Dropped 2026-05-31** — 2H cap rule (CLAUDE.md). Length above 2H no longer in scope. |
| `healing-hour-vol-1-528hz-kyoto-zen-garden` | 528 Hz Healing Frequency \| Kyoto Zen Garden Meditation to Stop Overthinking | 1H 02min | ✅ | ⏳ | ✅ 16:9 + thumb done | ⏳ | ⏳ | ⏳ |
| `power-hour-528hz-tokyo-sound-bath` | 528 Hz Deep Sleep Music \| Tokyo Sound Bath for Anxiety Relief & Healing | 1H | ✅ | n/a (existing audio) | ✅ bowl thumb | n/a | ✅ rebrand applied | ✅ **published/scheduled 21.5** (`-1RE1P98_u8`) |
| `power-hour-pomodoro-tokyo-rain-25-5` | Pomodoro Study With Me — Deep Focus Music \| Tokyo Rain 25/5 for Coding & Studying | 2H (25/5 ×4) | ✅ | ✅ | ✅ gold thumb | ✅ CapCut assembled | ✅ | ✅ **published Tue Jun 2, 07:00 MSK** (`zjtGEZISKbg`) |
| `power-hour-pomodoro-tokyo-rain-50-10` | Pomodoro Study Timer 50/10 — 2H Deep Focus Music \| Tokyo Rain for Coding & Studying | 2H (50/10 ×2) | ✅ | ⏳ | ✅ reuse 25/5 image (re-tag) | ⏳ | ⏳ | ⏳ Target ~9-10.6, after 25/5 D7 read |

### Power Hour Pomodoro 25/5 — published Tue Jun 2, 07:00 MSK (`zjtGEZISKbg`)

First full Power Hour Pomodoro. Locked series look debuted: gold chroma-key live timer overlay (FOCUS 25:00 / BREAK 05:00) + music-breathing gong fades (50s taper into focus, 10s dip into breaks) + hourglass signature + gold thumbnail.

**SEO landed clean (verified 2026-06-02):** title 82c, full description with Pomodoro schedule + 36-track tracklist + 10 hashtags in body, 27 tags (Karena 20/20/40-50: brand `stillwave`/`stillwave pomodoro` + broad `pomodoro`/`study with me`/`focus music` + narrow `pomodoro 25 5`/`2 hour pomodoro`/`deep work pomodoro`/`pomodoro timer 2 hours`), topic categories = **Electronic Music + Music** (NOT Religion like 963 — landed in the right cluster 🎯), duration 2:00:12.

**Slipped from Mon Jun 1 to Tue Jun 2** — day later than planned. Tuesday morning still hits the work-week start surge for the pomodoro/study cluster, so timing remains valid.

Review schedule (don't judge before day 7 — algo push lands days 4–14):
- **48h** — Thu Jun 4, 07:00 → log VPH + views/likes/comments; just log, don't conclude
- **7d** — Tue Jun 9 → real read. Success = sustained VPH + functional repeat-use signals (saves, returning viewers) clearly beating a flat curve
- **30d** — Thu Jul 2 → final snapshot; decide if the Pomodoro template (gold timer + gong fades) becomes the locked Power Hour focus format

**Shorts cross-promo plan:** drop Pomodoro Shorts cover on D3 (Fri Jun 5) or D4 (Sat Jun 6) to re-ignite long-form after the initial algo test plateaus (per our Healing Hour pattern). Skip if D1 < 30 views — Shorts won't save a dead launch.

### Pomodoro 25/5 — D2 read (2026-06-04)

- D0 (06-02): 5 views, VPH 23 🔥
- D1 (06-03): 41 (+36), like-rate 4.9%, 1 comment
- **D2 (06-04): 48 (+7), VPH=0, like-rate 4.2%, 2 likes**

Mixed read — NOT a flop (like 963's D5=32), but NOT a hit (Kyoto's D2=137 was much stronger). Same plateau pattern as the rest of channel: D1 algo test → cliff. Channel-level: subs flat at 49 (7 days unchanged), views baseline ~15/day.

**The signal that matters:** like-rate 4.2% beats Kyoto's 2.5%. Engagement is real — discovery is the bottleneck. Format works for who finds it; problem is reach, not retention.

### Pomodoro 25/5 — Shorts cross-promo published (2026-06-04, D2)

- **Shorts ID:** `9_nAWLAhInY`
- **Title:** `25 Min Pomodoro Deep Focus 🍅`
- **Published:** Thu Jun 4, 09:00 MSK (D2 of long-form; D1 = 41 views was above the 30-view threshold, so cross-promo greenlit one day earlier than D3/D4 target)

Shorts review:
- **24h (Fri Jun 5, 09:00):** log Shorts views. Healthy Shorts on small channel = 100-500 in first 24h. < 50 = dead.
- **48h (Sat Jun 6):** if Shorts is alive (> 100), check long-form lift — did Shorts traffic re-ignite Pomodoro 25/5 VPH? That's the whole point of delayed-drop strategy.
- **7d (Thu Jun 11):** long-tail check. If Shorts is climbing, the cross-promo template is locked.

### Power Hour Pomodoro 50/10 — in production (target ship ~9-10.6)

Second Pomodoro variant — long-block 50/10 (50 min focus / 10 min break × 2 = exactly 2H). Keyword-driven build off VidIQ data pulled 2026-06-02:

- **`pomodoro 50/10` 162,007/mo** (comp 32) vs our 25/5 `pomodoro 25 5` 7,598/mo → **~2.5× larger market**
- **`study timer` 171,519/mo at comp 21** → added to title and tags, near-uncompetitive keyword
- **`作業用bgm` 169K/mo in Japan** → JP-language tags + 1 JP hashtag in description body to catch Japanese market (already biggest study-music market by share)

Production reuse — 50/10 ships fast because almost everything is locked from 25/5:
- ✅ Same penthouse 16:9 scene (re-tag thumbnail `25/5 · 2H` → `50/10 · 2H`)
- ✅ Same vertical 9:16 Shorts cover (re-tag)
- ✅ Same Suno music DNA prompts (just generate a new full album)
- ✅ Same Flow video loop
- ✅ New chroma-key timer overlays `timer-focus-50min-chroma.mp4` + `timer-break-10min-chroma.mp4` (rendered 2026-06-02)
- ✅ Same music-breathing fade pattern (just 3 gongs: 50:00 / 1:00:00 / 1:50:00 instead of 7)

**Decision logic before ship:**
- Pomodoro 25/5 D2 read (Thu Jun 4) — if it shows ANY life (VPH > 0.5, D2 > 50 views), keep going on 50/10 prep
- Pomodoro 25/5 D7 read (Tue Jun 9) — final go/no-go on 50/10 ship. If 25/5 flopped like 963, **rethink instead of doubling down**
- Ship 50/10: ideally **Mon/Tue ~16-17.6** (after 25/5 D7 read + Suno album generation + CapCut assembly)

A/B benchmark on D7 of 50/10 — does the bigger-keyword market + study-timer tag translate to lift over 25/5? If yes → lock 50/10 as the primary Power Hour Pomodoro format. If no → 25/5 stays.

### Power Hour Pomodoro 50/10 — published Wed Jun 10, 09:00 MSK (`V4xwN0RRdpw`) + Shorts Jun 11 (`t_valshIMi4`)

**Long-form D5 read (2026-06-15):** 24 views, 2 likes, 1 comment, like-rate **8.3% 🔥** — HIGHEST engagement on the channel ever recorded. But raw views WEAK (×0.5 vs 25/5 at D5=52).

**Shorts D4 read:** 11 views, 0 likes, 1 comment — dead (same fate as 25/5 Shorts: cross-promo doesn't work on 50-sub channels).

**🚨 Two critical issues found 2026-06-15:**

1. **Topic categorization is WRONG — `Lifestyle (sociology)`** instead of `Music` for both 50/10 videos. YouTube put them in the wrong recommendation pool, killing music-cluster discovery. Root cause: the published long-form title was changed from our locked `Pomodoro Study Timer 50/10 — 2H Deep Focus Music | Tokyo Rain for Coding & Studying` to **`Need to Focus? 2 Hours of Tokyo Rain & Productivity | Pomodoro Study Timer 50/10`** — the productivity-question hook pushed it into lifestyle classification. The word "Music" disappeared from the first half of the title. Algorithm reads first words as most important. **Fix:** rename to our locked title to recover Music classification.

2. **Shorts description is BROKEN BOILERPLATE.** Some AI/app substituted in unrelated Lightroom/Premiere content: `"Explore the nuances of color temperature and visual comfort in our latest video, showcasing how various lighting conditions can impact a scene. We demonstrate effective techniques for editing color in Lightroom and how to color grade using tools like Adobe Premiere Pro."` Completely off-topic. **Fix:** replace with the proper Pomodoro 50/10 Shorts description from script §SHORTS PACKAGE.

**Main lesson from 50/10 launch:**

The 8.3% like-rate is **the strongest engagement signal we've ever had** — the format IS working for the audience that finds it. The discovery layer is the bottleneck, not the content. This validates pushing forward with the channel-positioning + Topic-categorization fixes rather than abandoning the Pomodoro thesis.

### Pomodoro 25/5 — D13 read (2026-06-15)

- D3: 52 · D6: 60 · **D13: 65** (Δ +5 in 7 days, ~0.7/day) — full plateau
- Like-rate 3.1% (still solid)
- Cross-promo Shorts at 11 views — totally dead, did not re-ignite long-form
- Verdict: not a flop, not a hit. Beats 963, beats Sound Bath rebrand. Loses to Kyoto's D13 ~150.

### Channel snapshot 2026-06-15

- **Subs: 50** (+1 in 11 days: 49 on Jun 4 → 50 on Jun 12, then static) — practical plateau
- Views: 5690 → 5794 (+104 in 11 days = ~9.5/day baseline drift)
- 3 videos uploaded in window (25/5 Shorts, 50/10 long, 50/10 Shorts)
- All recent uploads got the same plateau treatment from the algorithm — channel-authority bottleneck is real

### 🔴 Key lesson (2026-06-15) — Topic categorization must be controlled by title

Music videos MUST classify as `Music` topic. If YouTube classifies a video as `Lifestyle (sociology)` (as it did for both 50/10 entries), the video is routed to lifestyle-vlog recommendation pool, where ambient/focus music has no audience match.

**Topic classification is driven by:**
1. **First words of title** — front-load `Music` or genre keyword (`Deep Focus Music`, `Zen Music`, `Ambient Music`)
2. Tags ordering — early tags weigh more
3. Description content
4. Channel-level category

Our locked Power Hour Pomodoro title format `Pomodoro [Modifier] [N/N] — 2H Deep Focus Music | Tokyo Rain ...` puts `Music` in the second clause. The 50/10 publish swapped to `Need to Focus? 2 Hours of Tokyo Rain & Productivity | Pomodoro Study Timer 50/10` — no "Music" in first half, "Productivity" loaded — boom, classified as Lifestyle.

**Rule going forward:** Every long-form music video title MUST contain `Music` or a clear music-genre word (`Zen Music`, `Focus Music`, `Ambient`, `Lofi`) in the first 50% of the title. Question hooks like `Need to Focus?` are NOT to be used for music classification reasons — they read as lifestyle/productivity content.

### Power Hour Tokyo Sound Bath — rebrand applied (2026-05-21)

Rebrand of `-1RE1P98_u8` went live 21.5 (title + tags + description + DEEP CALM thumbnail + Power Hour playlist all applied; hashtags last to add). Review schedule — **do not judge before day 7** (BrainCatAI Lesson 3: videos catch the algo push days 4–14):

- **48h** — May 23: pull VidIQ VPH + views/likes; just log, don't conclude
- **7d** — May 28: real read. Success = VPH > 0 sustained + clearly beating the old 53-view stall = rebrand moved it into a live cluster
- **30d** — Jun 20: final snapshot; decide if the penthouse-sound-bath pattern becomes a Power Hour template

## Series restructure (2026-05-20)

The original "528 Hz Japanese Zen Music Marathon Vol. 1" (`-1RE1P98_u8`) stalled at 53 views — its photoreal penthouse visual sat in the Deep Work cluster, not healing. Decision: **move it into Power Hour** (where that penthouse visual belongs) via a Studio-only rebrand, and **relaunch Healing Hour clean** in the validated Ghibli aesthetic.

- **Healing Hour Vol. 1** = the Ghibli Kyoto Zen Garden video (was "Vol. 2") — `healing-hour-vol-1-528hz-kyoto-zen-garden.md`
- **Power Hour 528 Hz Tokyo Sound Bath** = the rebranded old video — `power-hour-528hz-tokyo-sound-bath.md`
- De-dup: Healing Hour Vol. 1 owns **Stop Overthinking**; Power Hour Sound Bath owns **Deep Sleep & Anxiety Relief** (both 528 Hz, distinct outcomes, no cannibalization)

### Healing Hour series — running ledger

| Vol | Date | Title | Hz | Visual | Status | Early data | Notes |
|-----|------|-------|----|----|--------|-----------|-------|
| Sound Bath (moved out) | 2026-05-14, rebrand 05-21 | 528 Hz Deep Sleep Music \| Tokyo Sound Bath for Anxiety Relief & Healing (`-1RE1P98_u8`) | 528 | Photoreal penthouse → DEEP CALM | ✅ rebrand applied | **56, stalled** | Rebrand of a stalled video barely moved it. Lesson: reviving a stalled video ≈ doesn't work. |
| **1** | **2026-05-21** | **528 Hz Healing Frequency \| Stop Overthinking** (`po4jmYdX2_w`) | 528 | Ghibli Kyoto garden, QUIET MIND | ✅ **published 05-21** | D1=64 · D2=137 🔥 · D3=147 · D6=157 · **D10=157** · likes 4 · like-rate 2.5% · comments 1 | Strong D2 burst (137), then **HARD PLATEAU from D4** — D6 to D10 = ZERO new views, VPH=0 since D8. Algo gave it the test, dropped it cold. Like-rate below 3% threshold. Diagnosis: thumbnail/title pulled click, retention/recommend signals didn't carry. Compare 852 Hz Monks' Secret: 4 → 268 by D5 (sustained climb) — we DIDN'T match that pattern. |
| **2** | **2026-05-26** | **963 Hz Frequency of God \| Pineal Gland Activation for Spiritual Awakening** (`pwnoQYJjgOo`) | 963 | Ghibli Mount Koya night, gold AWAKEN, stone lantern, intro 天地一如 | ✅ **published 05-26** | **D1=12** · D2=29 · D3=31 · **D5=32, 0 likes, 1 comment** | 🔴 **FLOPPED.** Original log "D1≈400" was misattribution — channel +432 on 05-26 came from Shorts cross-promo + recommended-to-backlog wave, NOT this long-form (per-video VPH stats show real D1=12, D5=0.10). **Mystery-frame hypothesis BUSTED:** "Frequency of God" + gold thumb + cosmic Ghibli underperforms "Stop Overthinking" + cream cream. Worse than Kyoto on every metric. Don't lock the template — shelve. |

### Channel-level signal (2026-05-19 → 2026-05-31)

- Subs: **38 → 49 (+11 in 12 days)**, then **stalled at 49 since 05-28** (4 days flat). Initial bump was real, but momentum gone.
- Views growth crashed: 05-26 +432 → 05-29 +26 → 05-31 **+5**. Algo boost fully exhausted, channel back to ~5-15/day baseline.
- **Correction (2026-05-31):** the 05-26 +432 jump was earlier attributed to the 963 long-form. Per-video data shows that's wrong — 963 itself only got ~12 views D1. The +432 came from Shorts cross-promo and old-video recommendation surges. Healing Hour long-form is NOT the channel growth lever we thought.

### 🔴 Key lesson (2026-05-31) — Healing Hour pattern under question

Two-of-two Healing Hour videos hit D2 push and then plateaued. The Ghibli aesthetic + keyword-front title gets the **click**, but the **watch/retention/save signals** aren't sustaining the algorithmic push. Diagnosis options (need YouTube Studio retention data to confirm):
- Audio not compelling enough to keep viewers past 30s
- Title overpromises ("Frequency of God" → people expect more)
- Wrong audience segment from the click (curiosity, not intent)
- Saturated cluster — competitors do it better/longer

**Until diagnosed: pause more Healing Hour launches.** Pomodoro Mon 06-01 is the next test in a different cluster.

### 🏆 Key lesson (2026-05-22) — fresh upload >> rebrand of a stalled video

Same frequency (528 Hz), same week, two approaches:
- **Sound Bath** = rebrand of the stalled `-1RE1P98_u8` → **60 views by D17, still flat** (rebrand confirmed dead 05-31)
- **Healing Hour Vol. 1** = fresh upload `po4jmYdX2_w` → **157 by D10** (also plateaued, but ×2.6 better than rebrand)

YouTube gives a new upload a clean algorithmic test; a stalled video stays suppressed even after a full rebrand. **Going forward: re-upload fresh rather than try to revive a dead video.**

### Tracking — Healing Hour Vol. 1 (`po4jmYdX2_w`)
- ✅ 48h (05-23): D2=137 logged
- ✅ 7d (05-28): plateau confirmed at 157 — verdict: **template did NOT work, mystery-frame stays unvalidated**
- 30d (06-20): final snapshot

### Tracking — 963 Mount Koya (`pwnoQYJjgOo`)
- ✅ 48h (05-28): D2=29
- ✅ 7d-ish (05-31, D5): 32 — verdict: **flop, mystery-frame hypothesis BUSTED**
- 30d (06-25): final snapshot

## Phase 1 batch — week of May 13–19

These are the first 3 hybrid-format videos for the gradual transition (Phase 1 = 1 of 4 / week, but we're running 3 as a test batch). Each script file under `scripts/` has the full 11-item `SW:` package: Suno A + Suno B + NanoBanana 16:9 + NanoBanana 9:16 + ffmpeg command + Title + Description + Tags + Hashtags + Pinned comment + A/B variant.

| Date | Slug | Aesthetic-lean | Why |
|------|------|----------------|-----|
| TBD | `tokyo-apartment-rain-1h` | Tokyo apartment + heavy rain on glass + neon city + tea + bonsai. **Power Hour format (1H 04min, 24 Suno tracks, no loop)** | Catches "1 hour focus music" + "power hour" search demand. Lower production overhead than 2H. |
| TBD | `bonsai-desk-night-2h` | Tokyo apartment + open MacBook (warm screen glow) + bonsai + neon city | Most "coding/programming" hook, laptop is the hero |
| TBD | `lantern-glow-study-3h` | Tokyo apartment + paper andon lantern (warm vs neon contrast) + closed laptop + book | Most "scholarly/study" hook, lantern is the hero, longest at 3H |

Mix the 3 with current иероглиф / Hz format videos so the channel doesn't shift too fast.

## Workflow per video

1. Trigger `SW: [theme]` or `SWS: [theme]` in chat — get the 11-item package
2. Generate music in Suno (Prompts A + B)
3. Generate image in NanoBanana (16:9 + 9:16)
4. Generate video loop in Flow / Kling
5. Edit + master in CapCut + ffmpeg
6. Generate thumbnail via `THUMB: [theme]` → Canva
7. Schedule upload in YouTube Studio
8. After publish: update `published-videos.md` with views at 48h / 7d / 30d