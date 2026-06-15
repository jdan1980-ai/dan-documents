# Power Hour — Pomodoro Tokyo Rain 50/10 Deep Focus

> Internal slug uses `power-hour-pomodoro-tokyo-rain-50-10`. Public copy carries no Vol. number; the Power Hour playlist groups the series.

## Meta

- **Title:** Pomodoro Study Timer 50/10 — 2H Deep Focus Music | Tokyo Rain for Coding & Studying
- **Series:** Power Hour (Tokyo penthouse focus marathon)
- **Playlist (add to in Studio):** `Power Hour — Deep Focus & Pomodoro`
- **Format:** Long-form, **2H total**, **50/10 ×2** Pomodoro variant (50 min focus / 10 min break, twice = exactly 2H)
- **Aesthetic:** Tokyo penthouse + rain on glass + MacBook (code editor) + 砂時計 hourglass (Power Hour locked signature)
- **Outcome owned:** **long-form deep work** — sister to 25/5 (`power-hour-pomodoro-tokyo-rain-25-5.md`). 25/5 = classic Cirillo for fast cycles; 50/10 = long-block deep work, the bigger search market
- **Status:** 📝 script ready — awaiting Suno (full album) + image (reuse 25/5 penthouse 16:9 OR re-gen) + CapCut assembly
- **Upload date:** TBD (target ~9-10.6, after Pomodoro 25/5 D7 read)

> **Why Pomodoro 50/10 next:** VidIQ — `pomodoro 50/10` **162,007/mo** (comp 32) vs our `pomodoro 25 5` 7,598/mo. The 50/10 search market is **~2.5× larger** than 25/5. Bonus: `study timer` **171,519/mo at comp 21** — a near-uncompetitive keyword we add to the title to grab cheap impressions. Score expectations: title ≥ 79 (matches 25/5 baseline).

---

## 1. 🎵 Suno Prompt A — Style field

Same Power Hour DNA as 25/5 — warm analog pad + distant koto + sub-bass pulse every 16 bars + 60 BPM + NO rain (rain layered in CapCut). Full album of UNIQUE tracks (~20 tracks ≈ 2H). Reuse the prompt from `power-hour-pomodoro-tokyo-rain-25-5.md` §1 verbatim — the music DNA is shared across the Pomodoro variants.

## 2. 🎵 Suno Prompt B — Lyrics field

Same as `power-hour-pomodoro-tokyo-rain-25-5.md` §2.

---

## 3. 🎨 NanoBanana prompt 16:9

**REUSE the existing image** from `power-hour-pomodoro-tokyo-rain-25-5.md` §3 — the locked Power Hour penthouse scene (penthouse + chair + MacBook front + hourglass on right windowsill + fireplace + neon Tokyo rain). Same scene = brand consistency across the Pomodoro variants. The current thumbnail `assets/power-hour-pomodoro-tokyo-rain-thumb.jpg` (gold POMODORO) can be reused with **only the tag changed: `50/10 · 2H` instead of `25/5 · 2H`**.

## 4. 🎨 NanoBanana prompt 9:16 (Shorts)

Same as `power-hour-pomodoro-tokyo-rain-25-5.md` §4 — reuse the locked penthouse-vertical image. Shorts cover tag: `STAY IN FOCUS · 50/10 · 2H`.

---

## 5. 🎬 Flow / Kling motion loop

Same as 25/5 — reuse the existing penthouse loop (rain + hourglass sand + fireplace flame + laptop cursor + cars moving). The loop is video-format agnostic.

---

## 6. 🍅 Pomodoro 50/10 structure (2 cycles in 2H)

| Time | Phase | Gong at | Fade pattern |
|------|-------|---------|--------------|
| 0:00 → 50:00 | FOCUS 1 | 50:00 | down 50s → 🔔 → up 10s |
| 50:00 → 1:00:00 | BREAK 1 | 1:00:00 | down 10s → 🔔 → up 10s |
| 1:00:00 → 1:50:00 | FOCUS 2 | 1:50:00 | down 50s → 🔔 → up 10s |
| 1:50:00 → 2:00:00 | BREAK 2 | (2:00:00 end / fade out) | down 50s → end |

**Only 3 gongs total** (vs 7 in 25/5) — long blocks, less interruption. This is by design: 50-min Cirillo-extended sessions for people doing deep work / studying / heavy coding where context-switching every 25 min is too costly.

### 🔒 Transition signature — "music breathing" (same as 25/5)

| Switch | Fade DOWN | 🔔 | Fade UP | Why |
|--------|----------|----|---------|------|
| **FOCUS → BREAK** (50:00, 1:50:00) | 50s slow taper | gong | 10s rise | long taper releases the deep-work state |
| **BREAK → FOCUS** (1:00:00) | 10s quick dip | gong | 10s rise | short dip = fast re-engage |

CapCut volume keyframes on the music track — drop to ~15-20%, gong lands at trough, ramp back. Only ~3 pairs of keyframes across 2H. Trivial load.

### 🔒 Live timer overlay — PRE-RENDERED CHROMA-KEY (drop-on-top)

- **Files (in `assets/`):** `timer-focus-50min-chroma.mp4` (FOCUS `50:00 → 00:00`, ~37 MB) and `timer-break-10min-chroma.mp4` (BREAK `10:00 → 00:00`, ~7 MB). Same gold + dark-choke-outline scheme as 25/5.
- **Make transparent in CapCut:** select clip → Video → Remove background → Chroma key → eyedropper green → adjust Intensity/Shadow.
- **Usage:** drop `timer-focus-50min` at 0:00 and 1:00:00; drop `timer-break-10min` at 50:00 and 1:50:00.
- **Look:** locked Pomodoro gold scheme (label + digits both gold `#E4C46C`, bold Liberation Serif, fixed-width digits, dark choke outline). Upper-center.

### ⚠️ MANDATORY pre-publish QA — gong/timer sync check

Same rule as 25/5 — scrub to each gong timestamp, verify timer shows `00:00`:

| Gong at | Timer clip starting at | Should show |
|---------|------------------------|-------------|
| 50:00 | FOCUS clip at 0:00 | `FOCUS 00:00` |
| 1:00:00 | BREAK clip at 50:00 | `BREAK 00:00` |
| 1:50:00 | FOCUS clip at 1:00:00 | `FOCUS 00:00` |

**Quickest sanity check:** scrub to 50:00 first — if clean, the rest follows (timer clip duration is locked at 50:00 exactly).

---

## 7. 📝 YouTube Title

```
Pomodoro Study Timer 50/10 — 2H Deep Focus Music | Tokyo Rain for Coding & Studying
```

(81 chars. Front-loads two giant keywords: **`Pomodoro Study Timer`** = `pomodoro` 1.1M + `study timer` 171K (comp 21 = cheap impressions!) + `pomodoro study with me` 64K. Then `50/10` 162K. Then `Deep Focus Music` (genre) + `Tokyo Rain for Coding & Studying` (brand + format + use case).)

## 8. 📝 YouTube Description (copy-paste ready)

```
Pomodoro Study Timer 50/10 — 2H Deep Focus Music | Tokyo Rain for Coding & Studying

Two hours of long-block deep work, Pomodoro 50/10 — 50 minutes deep focus, 10 minutes break, twice. The long-block Pomodoro variant for coding, studying, and writing where breaking every 25 minutes costs too much momentum.

High above the neon glow of Tokyo, with rain on the glass and the slow fall of sand in the hourglass, this 2-hour 50/10 session is built to carry you through two full long-focus blocks. A soft Japanese temple bell marks every transition. No talking, no climaxes — just the warm pulse of the city below the music, the rain, and your work in front of you.

Built for:
• Long-block deep work, coding, writing, studying
• Pomodoro 50/10 technique (×2 cycles in 2 hours)
• Study-with-me sessions
• Deep work that needs 50-minute focus blocks instead of 25
• Anyone who wants to sit down and just go

🕰️ The Hourglass
The sand falling in the Japanese hourglass (砂時計 sunadokei) is the recurring symbol of every Power Hour session — one turn, one focus block, time well spent.

🍅 Pomodoro 50/10 schedule
0:00 — FOCUS 1 starts (50 min)
50:00 — BREAK 1 (10 min)
1:00:00 — FOCUS 2 starts (50 min)
1:50:00 — BREAK 2 (10 min)
2:00:00 — done

🎵 Tracklist
[fill in track timecodes after Suno export — derive start of track N from end of track N-1]

▶ Subscribe to StillWave for new Power Hour focus sessions every week.
🔔 Tap the bell so you don't miss the next one.

#pomodoro #studytimer #studywithme #deepfocus #focusmusic #tokyorain #codingmusic #studymusic #pomodoro5010 #workmusic #stillwave #作業用bgm
```

> Tracklist timecodes are TRACK START times, fill in after Suno export. Last track must end at 2:00:00 ± few seconds. The Pomodoro schedule block is what YouTube auto-chapters; tracklist entries are clickable links, not chapters.

## 9. 🏷️ Tags (Karena 20/20/40-50, target ~450 chars / ~25-27 tags)

```
stillwave, stillwave pomodoro, tokyo rain pomodoro, stillwave focus music, pomodoro, study with me, study timer, deep focus music, focus music, pomodoro music, study music, work music, concentration music, pomodoro 50 10, pomodoro 50/10, 2 hour pomodoro, pomodoro deep focus music, study with me pomodoro, tokyo rain study music, pomodoro music for coding, pomodoro timer 2 hours, deep work pomodoro, focus playlist, lofi pomodoro, pomodoro timer, 作業用bgm, 勉強bgm
```

Distribution (Karena 20/20/40-50):
- **Brand (~20%):** `stillwave`, `stillwave pomodoro`, `stillwave focus music`, `tokyo rain pomodoro` (4 of 27 = ~15%)
- **Broad (~20%):** `pomodoro`, `study with me`, `focus music`, `study music`, `deep focus music` (5 of 27 = ~19%)
- **Narrow / long-tail (~50%):** `pomodoro 50 10`, `pomodoro 50/10`, `2 hour pomodoro`, `pomodoro music for coding`, `pomodoro timer 2 hours`, `deep work pomodoro`, `study with me pomodoro`, `pomodoro deep focus music`, `tokyo rain study music`, `study timer`, `concentration music`, `work music`, `pomodoro music`, `pomodoro timer`, `focus playlist`, `lofi pomodoro`, `作業用bgm`, `勉強bgm` (18 of 27 = ~67%)

**Japanese tags `作業用bgm` + `勉強bgm`** target the 169K/mo Japan-specific work-music market — our Japanese aesthetic + JP search demand = free traffic.

## 10. 🏷️ Hashtags

```
#pomodoro #studytimer #studywithme #deepfocus #focusmusic #pomodoro5010 #作業用bgm
```

Top-3 (for description body, NOT title per Karena #1): `#pomodoro #studytimer #studywithme`. Plus the extended set above in description body. The `#作業用bgm` Japanese hashtag is the JP discovery hook.

## 11. 📌 Pinned Comment

```
🍅 50 minutes deep focus, 10 minutes rest, twice. Built for the kind of work that needs long blocks — coding, studying, writing. The bell tells you when. What are you working on today? Drop one word ↓
```

---

## 🎨 Thumbnail (16:9, figure-8 lower-left)

**REUSE the 25/5 thumbnail and re-composite the tag only.** Same penthouse + chair + MacBook + hourglass + rain + neon. Same gold `POMODORO`. Tag changes:
- Before: `25/5 · 2H`
- After: `50/10 · 2H`

Final file: `assets/power-hour-pomodoro-tokyo-rain-thumb-5010.jpg` — I'll composite this when the 25/5 D7 read confirms we're shipping the 50/10.

---

# 📱 SHORTS PACKAGE (cross-promo → long-form)

> Same file = both formats. Figure-8 does NOT apply to 9:16 — text upper third, bottom = Shorts UI.

**Cover (9:16):** reuse the existing Shorts cover image, re-composite text:
- `POMODORO`
- `STAY IN FOCUS`
- `50/10 · 2H`
All gold. File: `assets/power-hour-pomodoro-shorts-cover-5010.jpg`.

**9:16 visual:** reuse vertical penthouse from 25/5.

**Text hook (0–2s, upper/center):**
```
50 minutes deep focus.
→ Pomodoro 50/10. Tokyo Rain. ×2.
```

**Shorts Title:**
```
50/10 Pomodoro Deep Focus 🍅
```

**Description:**
```
Two hours of long-block deep focus — Pomodoro 50/10 × 2 cycles, Tokyo Rain edition. The hourglass sand falls, the temple bell marks each break. Built for coding, studying, and work that needs longer blocks than the classic 25/5.

▶ Full 2H 50/10 Pomodoro: [paste long-form link after upload]

Subscribe to StillWave for new Power Hour focus sessions every week.

#shorts #pomodoro #studytimer #studywithme #deepfocus #focusmusic #pomodoro5010 #codingmusic
```

**Tags:**
```
pomodoro, study with me, study timer, deep focus music, focus music, pomodoro music, pomodoro 50 10, 50/10 pomodoro, classic pomodoro, pomodoro timer, stillwave, deep work, work music, tokyo rain
```

**Hashtags (top-3):** `#shorts #pomodoro #studytimer`

**Pinned comment:**
```
🍅 50 minutes. One long block. What are you about to focus on? Drop one word — and tap 👍 if you're starting now.
```

> Upload: Not for kids = Yes · link Short → long-form via Related video (Karena #6). Drop the Shorts D3-D4 after long-form launch (re-ignite signal pattern).

---

## Post-publish metrics

| Metric | 48h | 7d | 30d |
|--------|-----|----|-----|
| Views | | | |
| VPH (avg) | | | |
| Likes / like-rate | | | |
| Comments | | | |
| Subs gained | | | |

Benchmark: compare directly against Pomodoro 25/5 (same channel, same scene, same era) — if 50/10 outperforms 25/5 by ≥30% on D7, the keyword bet (`study timer` + `pomodoro 50/10` 162K) paid off and we lock 50/10 as the primary Power Hour Pomodoro format. If 25/5 wins, the long-block variant is too niche and we stick with 25/5.
