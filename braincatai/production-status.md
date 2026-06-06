# Production Status — BrainCatAI

Single source of truth для статуса каждого видео по pipeline. Обновляется при каждом изменении статуса.

**Pipeline стадии:** 📝 script → 🎨 images → 🎬 animated → 🎞️ assembled → ⏰ scheduled → 📤 published

---

## 📌 Locked rules (17 мая 2026 — Karena Roshaian playbook)

Applied channel-wide. **Full canonical spec → [`karena-playbook.md`](./karena-playbook.md)** (всё в одном месте).

- **NO hashtags in title field** — #shorts attracts bouncing audience → kills retention → algo stops promoting
- **Tags fill toward 500 chars** — brand 20% + broad 20% + narrow-specific 40-50%. Mandatory: `braincatai`, `cat facts mind blowing`, `cat behavior explained`
- **Upload via phone only** — only mobile YT app lets you pick stop-frame for thumbnail
- **First publish = Unlisted or Scheduled, never direct Public** — prevents algo seeing compressed garbage
- **"Not for kids" always** — For kids → YouTube Kids → wrong audience
- **Link Short → long-form via Related video** — funnel: feed → Short → long-form
- **First 3 seconds = 90% of retention weight** — hook must have: intrigue + benefit + urgency + relatability
- **Update phone YT app before every upload** — stale app breaks upload

**📊 Stats check-in: ~31 мая 2026** — посмотреть как изменились метрики у видео, опубликованных с новыми тегами (STARES, GIANT и далее). Сравнить CTR/retention с предыдущими видео.

---

## 🗓️ Расписание

### Опубликовано

| Дата | День | Видео | Рубрика | Slug | Метрики |
|------|------|-------|---------|------|---------|
| 22 апр | Вт | Your Cat's Purr Can Heal Your Bones | Cat Psychology | — | См. analytics |
| 23 апр | Ср | The Secret Behind Your Cat's Mysterious Stare | Cat Psychology | — | См. analytics |
| 24 апр | Чт | How Cats ALWAYS Land on Their Feet | Cat Psychology | — | См. analytics |
| 25 апр | Пт | Why Cats "Make Biscuits" on You | Cat Psychology | — | См. analytics |
| 26 апр | Сб | Your Cat Doesn't Know Your Face | Cat Psychology | — | См. analytics |
| 27 апр | Вс | Why Cats Sleep 16 Hours a Day | Cat Psychology | — | См. analytics |
| 28 апр | Пн | Why Cats Are AFRAID of Cucumbers | Cat Psychology | — | См. analytics |
| 29 апр | Вт | Why Your Cat Chooses a Box Over a $100 Bed | Cat Psychology | — | См. analytics |
| 30 апр | Ср | Does Cats Have 9 Lives? | Cat Psychology | — | См. analytics |
| 1 мая | Чт | How Cats SCAMMED Humans for 10,000 Years | Cat Psychology | — | См. analytics |
| 2 мая | Пт | Why Is the Sky Blue? | Brain Hacks | `why-is-the-sky-blue` | См. analytics |
| 3 мая | Сб | Why Your Cat Brings You Dead Things | Cat Psychology | `why-cats-bring-dead-things` | См. analytics |
| 4 мая | Вс | Why Does Your Cat Push Things Off Tables? | Cat Psychology | — | См. analytics |
| 5 мая | Пн | Why Your Cat Chirps At Birds | Cat Psychology | — | См. analytics |
| 6 мая | Ср | Why You Forget Walking Into a Room | Brain Hacks | `why-you-forget-walking-into-room` | published — TBD |
| 7 мая | Чт | The "Stop Stress" Button (Vagus Nerve) | Brain Hacks | `your-body-calm-down-button` | published — TBD (затем перевыпуск 14 мая — придержан) |
| 8 мая | Пт | Your Cat's COLOR Tells You Its Gender | Cat Psychology | `orange-cats-are-boys` | published TBD |
| 9 мая | Сб | Your Cat Says "I Love You" (Slow Blink) | Cat Psychology | `why-cats-slow-blink` | published TBD |
| 10 мая | Вс | What's Inside a Black Hole? | Brain Hacks (LEGACY non-cat) | `whats-inside-a-black-hole` | published TBD |
| 11 мая | Пн | Why Your Cat Licks Your Hair | Cat Psychology | `why-cats-lick-your-hair` | published TBD |
| 12 мая | Вт | If Your Cat Sleeps on You... (Sleeping Positions) | Cat Psychology | `where-your-cat-sleeps` | 21 |
| 13 мая | Ср | Why Cats LOSE THEIR MIND at Closed Doors | Cat Psychology | `why-cats-hate-closed-doors` | 14 |
| 14 мая | Чт | You Say THESE Words, Your Cat HEARS You! | Cat Psychology | `13-words-cats-understand` | 17 |
| 15 мая | Пт | Your Cat Thinks YOU'RE a Giant Weird Cat 🐱 | Cat Psychology | `your-cat-sees-you-as-giant-cat` | 44 |
| 15 мая | Пт | 🚨 Your Cat STARES at You for No Reason | Cat Psychology | `why-cats-stare-at-you` | **4** ⚠️ double-publish penalty |
| 17 мая | Вс | Why Your Cat FOLLOWS You to the Bathroom | Cat Psychology | `why-cats-follow-bathroom` | **6** |
| 18 мая | Пн | The Real Reason Your Cat Sits Above You | Cat Psychology | `why-cats-sit-above-you` | **4** — ⚠️ vidIQ 25.6 RED override, валидирован как «не стоило» |
| 19 мая | Вт | Cats Can Hear 5 Times What You Can | Cat Psychology | `cats-hear-you-blinking` | **5** |
| 20 мая | Ср | Cats Understand Their Names Better Than You Think | Cat Psychology | `why-cats-ignore-you` | **13** |
| 21 мая | Чт | 5 Signs Your Cat DOESN'T Love You (negative-mirror) | Cat Psychology | `signs-cat-doesnt-love-you` | **19** (1 лайк) |
| 22 мая | Пт | Your Cat Is a Perfect Killing Machine 🏆 | Cat Psychology | `your-cat-killing-machine` | **18** (24ч CTR 5.2% / 31с — лучший хук) |
| 23 мая | Сб | 5 Things Your Cat Loves That You Never Do | Cat Behavior | `things-cats-love` | **8** |
| 24 мая | Вс | Why Your Cat Stares at Nothing (killer-formula #2) | Cat Psychology | `why-cats-stare-at-nothing` | **3** (свежий) |
| 25 мая | Пн | When Your Cat Stretches at You, It Means This | Cat Behavior | `why-cats-stretch-at-you` | **3** (свежий) |
| 26 мая | Вт | This Cat Lived 38 Years — Her Owner's Strange Secret | Cat Facts | `worlds-oldest-cat` | **6** — mind-blow record (Creme Puff) |
| 27 мая | Ср | Your TV Looks BROKEN to Your Cat | Cat Facts | `your-cat-sees-your-tv` | **13** ⭐ (лидер пачки — первая 5-Signs обложка) |

🚨 **Lesson learned 17 мая 2026 (double-publish kill):** 15 мая вышли ДВА видео в один день — Giant (44 views) + Stares (**4 views**). Алгоритм задушил второе видео. **НИКОГДА не публиковать два Shorts в один день** — даже если одно сильнее. Один день = один Short максимум.

⚠️ **Override 18 мая:** `why-cats-sit-above-you` опубликован вне vidIQ-плана (score 25.6 RED, 0 monthly). User decision: канал в recovery mode → лучше потратить слот на инстинкт-тему чем держать сильную в очереди. Трекаем результат для валидации.

🕒 **Publish-slot rule (2 июн 2026, data-validated):** **Default = 15:00 локального (Jerusalem UTC+3)** — validated by trust-signs 31 мая (15:00 → 54 views / #1 of last 10 in 38h = best recovery signal). Окно 13:00-15:00 ок; 13-14 = пре-drop pattern, 15:00 = current recovery slot. НЕ позже 15:00. НЕ возвращаться к 18-21 (период падения). Пересмотреть при ≥3 видео с 100+ просм.

### План на ближайшие слоты (26+ мая)

> 🏆 Channel-wide tag jackpot: `cat facts mind blowing` — score **73.8 / 9,953 monthly / competition 5** — добавлять в теги каждого видео.

| Дата | День | Тема | Slug | vidIQ | Статус |
|------|------|------|------|-------|--------|
| **26 мая** | **Вт** | **This Cat Lived 38 Years — Her Owner's Strange Secret** (Creme Puff / Jake Perry, mind-blow record) | `worlds-oldest-cat` | "oldest cat ever" **64.94 / 8,562 / comp 25.7** (YELLOW-GREEN, pivot из RED cat-years 25.84/0) | ✅ опубликован 26 мая (2 просм, свежий) |
| 27 мая | Ср | **Your TV Looks BROKEN to Your Cat** (vision / flicker-fusion mind-blow) | `your-cat-sees-your-tv` | "cat vision" **64.20 / 9,246 / cached** | ✅ опубликован 27 мая (13 просм — лидер пачки) |
| 28 мая | Чт | **Cats CAN Be Trained — The Circus Secret** (cat training + circus story, counterintuitive + warm twist) | `circus-cat-training` | "cat training" **66.58 / 17,769 / comp 28.7 GREEN** (pivot из RED circus-cats 21/0) | ✅ скрипт+промты готовы → производство |
| 29 мая | Пт | **A Cat Went to SPACE?! 5 Famous Cats Who Made History** (story-листикл, Brain-host) | `famous-cats-history` | "top 10 cats" **71.41 / 11,518 / comp 12.4 GREEN-jackpot** (pivot из YELLOW famous cats 57.85) | ✅ скрипт+промты готовы → производство |
| 30 мая | Сб | **5 Cat Sounds You Must NEVER Ignore** (listicle) | `cat-sounds-never-ignore` | "cat sounds" **74.82 / 110,700 / comp 25.9 GREEN-JACKPOT** (крупнейший ключ канала) | ✅ скрипт+промты готовы → производство |
| 31 мая | Вс | **5 Signs Your Cat SECRETLY Trusts You** (signs-листикл, позитив-зеркало) | `signs-cat-trusts-you` | "cat trust signs" **67.10 / 13,321 / comp 24.6 GREEN** | ✅ опубликован 31 мая 15:00 → **54 views / #1 of last 10 in 38h** ⭐ (retention 41.6% — зона роста) |
| 1 июн | Пн | **Why Your Cat Suddenly BITES When You Pet It** (overstimulation + 3 warning signs) | `why-cats-bite-when-petting` | "why does my cat bite me" **60.49 / 19,847 GREEN** + competitor 37x breakout/115K (bot title 89/100) | ✅ скрипт+промты готовы → производство |
| 2 июн | Вт | **What Your Cat's TAIL Is Telling You — 5 Secret Signals** (5-Signs формула, counter-intuitive: cat wag ≠ dog wag, #4 warm payoff) | `why-cats-wag-their-tails` | "why cats wag their tails" **62.59 / 5,400 / comp 27.1** (кэш) + related GREEN `cat body language` 64.78 / `cat affection signs` 67.09 / `understanding cats` 69.26 | ⏰ uploaded, scheduled 2 июн **13:00** (A/B vs trust 15:00) |
| 3 июн | Ср | **5 Tiny Things That Make Your Cat Love You DEEPLY** (5-Signs формула, active how-to, remix Cats Insider 135k formula, #4 quiet company = warm payoff) | `how-to-bond-with-your-cat` | "how to bond with your cat" **🟢 69.79 / 17,435 / comp 20.5 GREEN-JACKPOT** (highest overall за сессию) + related GREEN `cat enrichment ideas` 67.23 / `cat behavior explained` 66.43 / `how cats show love` 65.61 | ✅ скрипт+промты готовы → производство |
| 4 июн | Чт | **5 Things Your Cat Dreams About — #4 Is YOU** (5-Signs + science-mystery + warm twist + mind-blow финал) | `what-cats-dream-about` | "what do cats dream about" **🟢 67.06 / 4,517 / comp 14.2 GREEN-JACKPOT** (LOWEST comp в кэше) + cluster ~18k monthly | ✅ скрипт+промты готовы → производство |
| 5 июн | Пт | **5 Cat Owner Mistakes (You're Doing #3)** (anti-pattern listicle, negative-mirror как 21 мая "DOESN'T Love You", high-CTR + #3 callout = curiosity gap, warm twist на #5 play) | `5-cat-owner-mistakes` | "cat owner mistakes" **🟢🟢 67.18 / 22,260 / comp 29.4 GREEN-JACKPOT** (highest VOLUME за всё время, бьёт bond 17,435) + cluster `cat health` 73.29 / `understanding cats` 68.85 / `cat health tips` 68.12 / `whisker fatigue` 61.00 | ⏰ uploaded, scheduled 5 июн 15:00 |
| 6 июн | Сб | **5 Reasons Your Cat Goes WILD at Night — #4 Means Trouble** (zoomies, FRAPs science, cross-link к owner-mistakes #5 play; #4=stress warning, #5=warm joy twist) | `cat-zoomies-explained` | "cat zoomies" **🟢 66.83 / 12,928 / comp 25 GREEN-strong** (3-я по силе в кэше — after owner-mistakes 22k и bond 17k) | ✅ скрипт+промты готовы → производство |
| 7 июн | Вс | **5 STRANGE Things Your Cat Does — Explained** (collected oddities listicle, FEED-BAIT format — replicate Chirps 5 May 1.2k / Dead Things 3 May 1k formula; new Rule 14 hybrid voice + Sc 8 comment-bait) | `5-strange-cat-behaviors-explained` | "strange cat behaviors explained" **🟢 63.12 / 14,691 / comp 35.5 GREEN** (3-я по volume, feed-bait potential) + sub-cluster `cat licking plastic bags` 64.35/4,828 | ✅ скрипт+промты готовы → производство |
| 8 июн | Пн | **Why Your Cat HEADBUTTS You — It's NOT Affection** (single-fact counter-intuitive deep-dive, mind-blow reframe = killer DNA; cross-link к bond) | `why-cats-headbutt-you` | "why does my cat headbutt me" **🟢 63.27 / 4,918 / comp 24.5 YELLOW-strong** + cluster GREEN `cat affection` 67.47, `cat communication` 70.51 | ✅ скрипт+промты готовы → производство |

**Бэклог YELLOW (cached, available):**
- `why-cats-wag-their-tails` 62.59 / 5,400 — лучший AVAILABLE в кэше
- `why-cats-hate-water` 60.88 / 3,659
- `why-cats-meow-only-at-humans` 60.70 / 3,685
- `cat-jealousy` 59.01 / 5,156

🚨 **Канал всё ещё в recovery mode:** ср. ~14 просм/видео за последние 15. Killer-видео (22 мая) показал лучший CTR (5.2%) и retention (31с), НО в сумме всего 18 просмотров — хук работает, охват алгоритм почти не даёт. До восстановления — **только cats**, 1 видео в день, никаких double-publish.

📊 Снапшоты: [`analytics/2026-05-25-snapshot.md`](./analytics/2026-05-25-snapshot.md). Чек-ин ~31 мая.

### Long-form pipeline

| Видео | Старт production | Publish target | Статус |
|-------|------------------|-----------------|--------|
| Cat Evolution (15 мин) | 8 мая 2026 | июнь 2026 | 📝 структура есть, скрипт ⏳ |

#### Cat Evolution — 8-day production sprint

User decision: **1 день = 1 эпоха** + 1 day для assembly. Темп copy текущий Shorts pipeline.

| День | Дата | Задача | Деливерабл |
|------|------|--------|-----------|
| **Day 1** | 8 мая Пт | **Foundation** | Brain Reference Sheet + 5 костюмов + 6 локаций в style-guide + полный VO script (~1700 слов) + asset shotlist по эпохам |
| Day 2 | 9 мая Сб | 🌳 Эра 1: Proailurus | ~12 ассетов для 1:00-3:00 |
| Day 3 | 10 мая Вс | 🦷 Эра 2: Saber-tooths | ~12 ассетов для 3:00-5:00 |
| Day 4 | 11 мая Пн | 🌍 Эра 3: Spread | ~12 ассетов для 5:20-7:20 |
| Day 5 | 12 мая Вт | 🏺 Эра 4: Egyptian (anchor) | ~14 ассетов для 7:20-9:30 |
| Day 6 | 13 мая Ср | 🏠 Эра 5: Modern breeds | ~12 ассетов для 9:50-11:50 |
| Day 7 | 14 мая Чт | 🧬 Эра 6: Future | ~10 ассетов для 11:50-13:30 |
| **Day 8** | 15 мая Пт | **Assembly** | Hook + intro + emotional close + Google Vids склейка + Google Vids TTS VO + Suno music + subtitles + thumbnail + SEO + schedule |

Финиш: **15 мая** → публикация в июне с 2+ неделями буфера на полировку.

---

## Pipeline статус — последние/активные

| Slug | Дата | 📝 | 🎨 | 🎬 | 🎞️ | ⏰ | 📤 |
|------|------|----|----|----|-----|-----|-----|
| `why-cats-stretch-at-you` | 25 мая | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ опубликован |
| `why-cats-stare-at-nothing` | 24 мая | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ опубликован |
| `things-cats-love` | 23 мая | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ опубликован |
| `your-cat-killing-machine` | 22 мая | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ опубликован 🏆 |
| `signs-cat-doesnt-love-you` | 21 мая | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ опубликован |
| `why-cats-ignore-you` | 20 мая | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ опубликован |
| `cats-hear-you-blinking` | 19 мая | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ опубликован |
| `why-cats-sit-above-you` | 18 мая | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ опубликован (vidIQ override) |
| `why-cats-follow-bathroom` | 17 мая | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ опубликован |
| `why-cats-stare-at-you` | 15 мая | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ опубликован (double-publish жертва) |
| `your-cat-sees-you-as-giant-cat` | 15 мая | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ опубликован |
| `worlds-oldest-cat` | 26 мая | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ опубликован |
| `your-cat-sees-your-tv` | 27 мая | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ опубликован (13 просм) |
| `circus-cat-training` | 28 мая | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| `famous-cats-history` | 29 мая | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| `cat-sounds-never-ignore` | 30 мая | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| `signs-cat-trusts-you` | 31 мая | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| `why-cats-bite-when-petting` | 1 июн | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| `why-cats-wag-their-tails` | 2 июн | ✅ | ✅ | ✅ | ✅ | ✅ | ⏰ scheduled 13:00 (A/B) |
| `how-to-bond-with-your-cat` | 3 июн | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| `what-cats-dream-about` | 4 июн | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| `5-cat-owner-mistakes` | 5 июн | ✅ | ✅ | ✅ | ✅ | ✅ | ⏰ scheduled 15:00 |
| `cat-zoomies-explained` | 6 июн | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| `5-strange-cat-behaviors-explained` | 7 июн | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| `why-cats-headbutt-you` | 8 июн | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |

> Легаси не-кошачьи скрипты (Sky Blue / Black Hole / 6-7 / Goosebumps / Doorway / Vagus) перенесены в `scripts/_archive/`.

(Уточни — какие именно стадии уже готовы. Я предполагал что для запланированных в YouTube всё готово до scheduled статуса.)

---

## Как использовать этот файл

- **Мне (Claude):** обновляю при каждой правке/новом скрипте
- **Тебе:** одна страница где видно что где находится, что нужно делать дальше, и что в очереди
- **Pipeline статусы:** ⏳ pending → 🟡 in progress → ✅ done