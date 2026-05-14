# Trend Analysis — 13 мая 2026

> vidIQ pulled fresh data on cat-psychology shorts (last 3 months) + keyword research on 4 ready scripts to re-rank the upcoming queue by actual demand.

## Method

- `vidiq_outliers` keyword="cat psychology behavior", contentType=short, publishedWithin=threeMonths, sort=breakoutScore
- `vidiq_trending_videos` titleQuery="cat behavior psychology owner", publishedAfter=2026-02-13, sort=vph
- `vidiq_keyword_research` × 4 (one per candidate script)

vidIQ balance: 1938 → 1913 (~25 credits spent).

---

## 🏆 Key finding — "Cats see you as a giant cat" is the highest-demand topic

### vidIQ keyword scores (last 3 months)

| Script | Main keyword | Overall score | Monthly searches | Competition |
|--------|--------------|---------------|------------------|-------------|
| **`your-cat-sees-you-as-giant-cat`** | "your cat doesn't see you as human" | **71.47** | **50,361** | 26.6 (low) |
| `your-cat-sees-you-as-giant-cat` (alt) | "how cats see humans" | 69.58 | 25,972 | 24.9 |
| `why-cats-stare-at-you` | "why cats stare at you" | 67.32 | 8,504 | 19.7 |
| `why-cats-follow-bathroom` | "why your cat follows you to bathroom" | 62.84 | 4,496 | 24.7 |
| `cats-hear-you-blinking` | "cats hear blinking" | **0 / null** | 0 | n/a |

**Insight:** `cats-hear-you-blinking` has near-zero organic search demand — the hook is algorithm-only (works on the For You feed but won't get search clicks). The other three have solid keyword scores.

### Competitor outlier proof (3-month vidIQ outlier scan, cat Shorts)

The smoking gun for re-ranking — a 1.3k-subscriber channel hit **125k views in <2 months** with our exact angle:

| Video | Channel | Subs | Views | Breakout score | VPH | Relevance |
|-------|---------|------|-------|----------------|-----|-----------|
| **"How Cats Actually View Humans: Hint, It is Not as Owners"** | Mente Diversa | 1.35k | **125,392** | 12.87 | 682 | ⭐ Matches `your-cat-sees-you-as-giant-cat` directly |
| "What psychology says about your cat" | Saleem The Void | 8.1k | 156,333 | 269.06 | 171 | General psychology — overlaps stares/bathroom |
| "Why Is This Cat Copying Humans?" (copycat) | Meow Moments | 1.77k | 41,655 | 8.79 | 57 | Adjacent to giant-cat |
| "Ranking CATS COPYING OWNER Core Moments" | AniRank | 118k | 7,728,251 | — | **49,843** | Compilation but proves "cats mirror humans" topic is hot |

**Independent confirmation:** small-channel breakouts (1k–8k subs) hitting six-figure views on "how cats see humans" and "what psychology says about your cat" prove the audience is fed and hungry RIGHT NOW for psychology-explainer cat shorts.

---

## 📅 Proposed re-ranking of the upcoming queue

Current schedule has next 5 cat-only shorts in this order:

| Original date | Slug | Status |
|---------------|------|--------|
| 16 May | `13-words-cats-understand` | 📝 in production (Brain already done, Sc 8 universal pending) |
| 17 May | `why-cats-stare-at-you` | ⏳ |
| 18 May | `your-cat-sees-you-as-giant-cat` | ⏳ |
| 19 May | `why-cats-follow-bathroom` | ⏳ |
| 20 May | `cats-hear-you-blinking` | ⏳ |

### 🎯 Recommended new order (by vidIQ score + competitor evidence)

| New date | Slug | Reason for slot |
|----------|------|-----------------|
| 16 May (Сб) | `13-words-cats-understand` | Already in production — leave |
| **17 May (Вс)** | **`your-cat-sees-you-as-giant-cat`** ⬆️ moved from 18 | **50k monthly searches (×6 demand vs stares)** + competitor proof + Sunday = peak traffic. This is the strongest topic in the batch by far. |
| **18 May (Пн)** | **`why-cats-stare-at-you`** ⬇️ moved from 17 | 8.5k monthly, still solid. Pn = weekday but lower-traffic day for a still-strong topic. |
| 19 May (Вт) | `why-cats-follow-bathroom` | 4.5k monthly. Keep — universal experience hook still drives algorithm. |
| 20 May (Ср) | `cats-hear-you-blinking` | 0 search volume — pure algorithm play. Put last in batch; if Shorts feed picks it up it's bonus, if not minimal harm. |

### 📊 Summary of the swap

**Swap proposed:** `your-cat-sees-you-as-giant-cat` ⬅️➡️ `why-cats-stare-at-you` (move giant-cat one day earlier, push stares one day later).

**Why this matters:**
- giant-cat keyword demand is 6× higher than stares (50k vs 8.5k)
- Weekend (Sun) gets the highest organic traffic — give it our strongest topic
- Competitor evidence (Mente Diversa 1.3k subs → 125k views on identical angle) shows the YouTube algorithm is actively pushing this niche right now
- Lowest-demand video (blinking, 0 search) moves to the end of the batch — safest placement

---

## What stays the same

- ✅ `13-words-cats-understand` keeps 16 May (already in production)
- ✅ Daily cadence preserved — no gaps
- ✅ Vagus Nerve emergency reserve untouched
- ✅ All scripts are cat-only per the absolute rule

---

## Next steps if user approves the swap

1. Edit `production-status.md` to swap 17 ↔ 18 May
2. Update Meta/`Publish date:` in:
   - `your-cat-sees-you-as-giant-cat.md` (was 18 → now 17)
   - `why-cats-stare-at-you.md` (was 17 → now 18)
3. Reorder `pinned-comments.md` entries to match
4. Commit + push

---

## Raw vidIQ outliers data (top 5 hits, last 3 months, cat-psychology Shorts)

| # | Title | Channel | Subs | Views | Breakout | VPH |
|---|-------|---------|------|-------|----------|-----|
| 1 | What psychology says about your cat | Saleem The Void | 8.14k | 156,333 | 269 | 171 |
| 2 | Let's do a simple intelligence test for cats | Buhes Nuhwd | 3.03k | 867,678 | 264 | 0.08 |
| 3 | Confusing cat behavior compilation (multiple) | Various | 50k–353k | 24M–33M | 916–1611 | 2–3 |
| 4 | How Cats Actually View Humans: Hint, It is Not as Owners | Mente Diversa | 1.35k | 125,392 | 12.87 | 682 |
| 5 | Why Is This Cat Copying Humans? | Meow Moments | 1.77k | 41,655 | 8.79 | 56 |
