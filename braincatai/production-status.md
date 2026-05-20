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
| 17 мая | Вс | Why Your Cat FOLLOWS You to the Bathroom | Cat Psychology | `why-cats-follow-bathroom` | **11** |
| **18 мая (сегодня)** | **Пн** | The Real Reason Your Cat Sits Above You | Cat Psychology | `why-cats-sit-above-you` | TBD — ⚠️ vidIQ 25.6 (RED override) |

🚨 **Lesson learned 17 мая 2026 (double-publish kill):** 15 мая вышли ДВА видео в один день — Giant (44 views) + Stares (**4 views**). Алгоритм задушил второе видео. **НИКОГДА не публиковать два Shorts в один день** — даже если одно сильнее. Один день = один Short максимум.

⚠️ **Override 18 мая:** `why-cats-sit-above-you` опубликован вне vidIQ-плана (score 25.6 RED, 0 monthly). User decision: канал в recovery mode → лучше потратить слот на инстинкт-тему чем держать сильную в очереди. Трекаем результат для валидации.

### План на 19–28 мая — 10-дневный календарь (сдвинут 18 мая после Sits Above You)

> vidIQ research: 13 тем проверено. Все ниже порога GREEN. Выбраны лучшие YELLOW + competitor-proven темы.
> 🏆 Скрытый джекпот: `cat facts mind blowing` — score **73.8 / 9,953 monthly / competition 5** — добавлять в теги каждого видео.

| Дата | День | Тема | Slug | vidIQ | Статус |
|------|------|------|------|-------|--------|
| 19 мая | Вт | Cats Can Hear 5 Times What You Can | `cats-hear-you-blinking` | — | 📅 scheduled (uploaded 18 мая) |
| 20 мая | Ср | Cats Understand Their Names Better Than You Think | `why-cats-ignore-you` | 59.47 / 8,757 | 📅 scheduled (uploaded 19 мая) |
| 21 мая | Чт | **5 Signs Your Cat DOESN'T Love You** (negative-mirror) | `signs-cat-doesnt-love-you` | **67.55 / 14,333 GREEN** ⭐ + @williamcat 8.8M proof | ✅ скрипт готов → производство |
| ~~21 мая~~ | ~~Чт~~ | ~~Your Cat's Tail Is Talking~~ | ~~`why-cats-wag-their-tails`~~ | 62.59 / 5,400 | ⏸️ отложено (swapped for GREEN negative-mirror) |
| 22 мая | Пт | Your Cat Invented a Language Just for YOU | `why-cats-meow-only-at-humans` | 60.70 / 3,685 | ✍️ нужен скрипт |
| 23 мая | Сб | When Your Cat Stretches at You, It's Saying This | `why-cats-stretch-at-you` | 60.13 / 5,378 | ✍️ нужен скрипт |
| 24 мая | Вс | Why Your Cat Acts Like Water Is Poison | `why-cats-hate-water` | 60.88 / 3,659 | ✍️ нужен скрипт |
| 25 мая | Пн | Your Cat Is Older Than You Think 🐱 | `cat-years-to-human-years` | competitor proof | ✍️ нужен скрипт |
| 26 мая | Вт | 3 Things Your Cat Can Sense That You Can't | `cat-superpowers-senses` | targets 73.8/9,953 | ✍️ нужен скрипт |
| 27 мая | Ср | Why Your Cat Hates When You Leave | `why-cats-hate-being-left-alone` | TBD | ✍️ нужен скрипт |
| 28 мая | Чт | _Нужна 10-я тема — выбрать из vidIQ-кэша_ | TBD | TBD | ✍️ нужен скрипт |

🚨 **Канал в recovery mode:** view-counts с 8 мая упали с 800-1300 до 10-44. Причина — non-cat видео (Sky Blue, Doorway, Vagus, Black Hole). До восстановления — **только cats**, 1 видео в день, никаких double-publish.

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

## 🔑 Кандидаты на 13-19 мая (черновик)

Источник: backlog в `content-ideas.md`. Финализируется после vidIQ анализа (12 мая возвращаются credits).

### 13 мая (Ср — Cat Psychology)
- 🟢 **Why Cats Hate Closed Doors** — universal experience, low Shorts saturation
- 🟢 Why Your Cat Stares at You for No Reason

### 15 мая (Пт — What If?)
- 🟢 **What If Earth Stopped Spinning?** — visual extreme, cat flying off scenery
- 🟢 What If Humans Had Tails?
- 🟢 What If You Fell Through Earth?

### 16 мая (Сб — Cat Psychology)
- 🟢 **Your Cat Sees You as a Giant Weird-Looking Cat** — relatable mind-blow, новая для нас
- 🟢 Why Cats Roll on Their Backs (NOT for belly rubs)

### 17 мая (Вс — Did You Know)
- 🟢 **Your Stomach Gets a New Lining Every Few Days** — universal mind-blow
- 🟢 Cleopatra Lived Closer to the Moon Landing Than to the Pyramids
- 🟢 Sharks Existed Before Trees

### 18 мая (Пн — Cat Psychology)
- 🟢 **Why Cats Slow Blink** ✅ уже сделан — переиспользуем сильную тему
- 🟢 Why Your Cat Meows ONLY at Humans (not other cats)
- 🟢 Cats Can Hear You Blinking

### 19 мая (Вт — Brain Hacks)
- 🟢 **Why You Forget Names Instantly** — universal experience
- 🟢 The Phantom Vibration Effect (you feel phone buzz that didn't happen)
- 🟢 Why You Can't Tickle Yourself

---

## Pipeline статус в работе (текущие скрипты)

| Slug | Дата | 📝 | 🎨 | 🎬 | 🎞️ | ⏰ | 📤 |
|------|------|----|----|----|-----|-----|-----|
| `orange-cats-are-boys` | 8 мая | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ |
| `why-cats-slow-blink` | 9 мая | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ |
| `whats-inside-a-black-hole` | 10 мая | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ |
| `why-cats-lick-your-hair` | 11 мая | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ |
| `why-music-gives-you-goosebumps` | 12 мая | ✅ | 🟡 in progress | ⏳ | ⏳ | ⏳ | ⏳ |
| `why-cats-hate-closed-doors` | 13 мая | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ |
| `why-kids-say-6-7` | LEGACY non-cat — снять с очереди | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| `where-your-cat-sleeps` | 12 мая | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ опубликован |
| `13-words-cats-understand` | 16 мая | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| `why-cats-stare-at-you` | 17 мая | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| `your-cat-sees-you-as-giant-cat` | 15 мая | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ опубликован |
| `why-cats-follow-bathroom` | 17 мая | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ опубликован |
| `why-cats-sit-above-you` | 18 мая | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ опубликован (override) |
| `cats-hear-you-blinking` | 19 мая | ✅ | ✅ | ✅ | ✅ | ✅ | 📅 scheduled |
| `why-cats-ignore-you` | 20 мая | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |

(Уточни — какие именно стадии уже готовы. Я предполагал что для запланированных в YouTube всё готово до scheduled статуса.)

---

## Как использовать этот файл

- **Мне (Claude):** обновляю при каждой правке/новом скрипте
- **Тебе:** одна страница где видно что где находится, что нужно делать дальше, и что в очереди
- **Pipeline статусы:** ⏳ pending → 🟡 in progress → ✅ done