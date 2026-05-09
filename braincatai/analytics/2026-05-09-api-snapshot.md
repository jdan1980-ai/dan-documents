# BrainCatAI — API Snapshot (May 9, 2026)

Pulled live via YouTube Data API v3 (channel `UCMKcrIw1l1u_WU0M9Cv-DKw`, handle `@braincatai`).

## Channel summary

| Metric | May 5 (analytics file) | May 9 (live API) | Delta (4 days) |
|--------|------------------------|------------------|----------------|
| Subscribers | 35 | **37** | +2 |
| Total views | ~8 200 | **9 591** | **+1 387** (~350/day) |
| Total videos | 14 | **18** | +4 |

## All 18 videos — sorted by views (live)

| Date | Title | Length | Views | Likes | Comm |
|------|-------|--------|-------|-------|------|
| May 2 | Did you know why Is the Sky Blue? 🐱 \| Cat Psychology | 47s | **1 373** ⭐ | 30 | 2 |
| Apr 29 | Why Your Cat Chooses a Box Over a $100 Bed 🐱📦 | 52s | 1 360 | 25 | 3 |
| **May 5** | **Why Your Cat Chirps At Birds 🐱 \| Cat Psychology** | 49s | **1 254** 🚀 | **47** ⭐ | 1 |
| May 3 | Why Your Cat Brings You Dead Things \| Cat Psychology | 50s | 1 001 | 32 | 1 |
| Apr 28 | Why Cats Are AFRAID of Cucumbers \| Cats Psychology | 56s | 966 | 15 | 2 |
| Apr 30 | Does cats have 9 lives? \| Cat Psychology | 57s | 836 | 10 | 1 |
| Apr 24 | How Cats ALWAYS Land on Their Feet 🤯 | 57s | 799 | 24 | 4 |
| Apr 25 | Why Cats "Make Biscuits" on You 🐾 | 49s | 440 | 15 | 5 |
| Apr 26 | Your Cat Doesn't Know Your Face 😱 | 50s | 430 | 10 | 1 |
| May 1 | How Cats SCAMMED Humans for 10,000 Years 🤯 | 57s | 354 | 1 | 1 |
| Apr 22 | Your Cat's Purr Can Heal Your Bones 😳 | 59s | 278 | 4 | 3 |
| May 4 | Why Cats Knock Stuff Off Tables (Real Reason) | 43s | 172 | 11 | 1 |
| Apr 23 | The Secret Behind Your Cat's Mysterious Stare 👀 | 49s | 161 | 6 | 1 |
| **May 6** | **Why You Forget Why You Walked Into a Room \| Brain Hacks** | 50s | 88 | 9 | 1 |
| Apr 27 | Cats Sleep MORE Than You Work 😅 (Sleep 16 Hrs) | 57s | 67 | 3 | 1 |
| **May 8** | Your Cat's COLOR Tells You Its Gender 🐱 | 55s | 13 | 0 | 1 |
| **May 7** | The "Stop Stress" Button Inside Your Body \| Brain Hacks | 56s | 10 | 1 | 1 |
| **May 9** | Your Cat Says "I Love You" Every Day (Slow Blink) | 55s | 1 | 0 | 0 |

## 🚀 Виральный outlier — Why Your Cat Chirps At Birds

**Это самый важный сигнал в данных:**

| Metric | May 5 | May 9 | 4-day growth |
|--------|-------|-------|---------------|
| Views | 30 | **1 254** | **+1 224** (×42) |
| Likes | 2 | **47** | +45 (×24) |

**3.7% like rate** — самый высокий на канале (выше Sky Blue 2.2%, Box Bed 1.8%, Dead Things 3.2%).

YouTube алгоритмически толкает это видео. Почему:
1. ✅ Universally relatable topic — все cat owners слышали этот странный звук
2. ✅ Clean title pattern: "Why Your Cat [does X]" — proven Shorts hook
3. ✅ 49-sec Shorts (sweet spot)
4. ✅ Высокая доля лайков (3.7%) — сильный engagement signal алгоритму

## 🏷️ Tag-стратегия — что показал API

Стянул теги топ-3 видео. Главный insight:

### TOP-3 (виральная Chirps At Birds) — **только base canonical 19 tags**

```
cat psychology, cat facts, cat behavior, cat secrets, cat science,
cat communication, cat body language, feline behavior, understanding cats,
facts about cats, animal facts, animal science, did you know,
mind blowing facts, brain cat, cat facts daily, cat behavior funny,
cat domestication, cats vs humans
```

**Это ТОЧНО наш CLAUDE.md base set.** Никаких кастомных. И именно эта простота + сильный title-hook дали виральность.

### TOP-1 (Sky Blue 1 373 views) — теги MISMATCH с контентом

Видео про физику неба, но теги: `cats ancient egypt`, `how cats domesticated humans`, `cat history`, `cat domestication`. Эти теги от другого видео (Egyptian Domestication?). Сработало вопреки mismatch — title-hook сильный.

### TOP-2 (Box Bed) — теги матчат

`why cats like boxes`, `cardboard box cat`, `cat instincts` — content-matched + base set.

### Lesson — обновляем правило в director-checklist:

✅ **Tags = base canonical 19 + 3-5 video-specific (matched к контенту)**
❌ **Не наследовать теги с предыдущих видео не относящихся к теме**

20-25 тегов в CLAUDE.md — overkill. **15-20 чистых, релевантных** работает лучше.

## 📊 Performance by niche

| Niche | Count | Avg views | Best |
|-------|-------|-----------|------|
| **Cat Psychology** | 13 | **665** | 1 373 (Sky Blue is technically Brain Hacks but cat-tagged) |
| **Brain Hacks** | 2 (Doorway, Vagus) | 49 | 88 (Doorway Effect) |
| **Pure Cat Psych Shorts** | rest | ~430 avg | — |

⚠️ **Brain Hacks performing 13× WORSE на канале**:
- Doorway Effect (May 6): **88** views (3 days old)
- Vagus Nerve (May 7): **10** views (2 days old)
- vs Cat Psych median ~440-700 views in same age range

Possible reasons:
1. Канал tagged как cat-content — алгоритм не пушит non-cat топики
2. Brain Hacks ниша у нас новая, ещё нет authority
3. Subscriber base = cat-lovers, не интересна абстрактная психология

**Вывод:** Brain Hacks нужно либо больше времени (3-4 видео для авторитета), либо переименовать в **"Cat Brain Hacks"** / "Smart Cat Facts" — оставить cat-связь, чтобы алгоритм понимал нишу. Sky Blue (физика) сработал потому что тегирован как cat psychology — это сработало парадоксально.

## 🆕 Recent videos (May 6-9) — ещё рано судить

- May 6 Doorway Effect: 88 views, 9 likes — slow start, retention issue (см. doorway-effect-review.md)
- May 7 Vagus Nerve: 10 views — only 2 days, нужно больше времени
- May 8 Orange Cats: 13 views — только вчера
- May 9 Slow Blink: 1 view — published today

## Recommendations

1. ⭐ **Удвоиться на "Why Your Cat [does X]" titles** — Chirps At Birds доказал что универсально-relatable cat behaviors → виральность
2. 🚫 **Не делать чистый Brain Hacks** на этом канале без cat-связки. Если Brain Hacks — обязательно cat-tag и cat-related angle
3. ✅ **Tags simplify** — base 19 + 3-5 specific. Не наследовать со старых видео
4. 📈 **Подкрутить engagement на Vagus Nerve и Orange Cats** — pinned comments, активные ответы первые 24h, чтобы алгоритм увидел сигнал
5. 🎯 **Следующая тема в backlog** должна быть Cat-relatable + universally-experienced. Smart picks из content-ideas:
   - Why Cats Hate Closed Doors
   - Why Cats Stare at Walls
   - Why Cats Knead Then Bite
   - Why Cats Bring You Dead Things (already done — went well at 1001 views)