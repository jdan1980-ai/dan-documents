# 🎯 Karena Roshaian Playbook — единый свод правил для Shorts

> **Это канонический источник по всем правилам Карены.** Раньше они были разбросаны по `CLAUDE.md` и `production-status.md` — теперь всё здесь, в одном месте.
>
> **Locked 17 мая 2026. Applied channel-wide (BrainCatAI + StillWave Shorts).**
>
> Если ты (Claude) в новом чате готовишь скрипт, SEO, thumbnail или аплоад — **прочитай этот файл первым**. Юзеру НЕ нужно объяснять эти правила заново каждый раз.

---

## 🚫 ЧАСТЬ 1 — Shorts-specific правила (8 заповедей Карены)

Краткий чек-лист. Каждое правило ниже = механика + почему.

### 1. НЕТ хэштегов в поле title
**Правило:** `#shorts` и тематические хэштеги (`#catpsychology` и т.п.) **никогда** не идут в поле заголовка.
**Почему:** хэштеги в title притягивают международную развлекательную аудиторию, которая отваливается за <3 сек → убивает retention → алгоритм перестаёт продвигать. Плюс на Shorts хэштеги в title не дают SEO-профита (трафик идёт из ленты по retention, не из поиска).
**Куда хэштеги МОЖНО:** только в тело описания (см. Часть 2, п.5).

### 2. Теги заполнять до 500 символов
**Правило:** 20–25 тегов, заполнять поле почти под лимит 500 символов.
**Пропорция:** brand 20% + broad 20% + narrow-specific 40-50%.
**Обязательные channel-wide теги** (всегда включать):
```
braincatai, cat facts mind blowing, cat behavior explained
```

### 3. Заливать ТОЛЬКО с телефона
**Правило:** аплоад через мобильное приложение YouTube, не с десктопа.
**Почему:** только мобильное приложение даёт вручную выбрать стоп-кадр для thumbnail. Десктоп берёт случайный уродливый кадр.

### 4. Первая публикация = Unlisted или Scheduled, НИКОГДА сразу Public
**Правило:** не публиковать напрямую в Public.
**Почему:** если опубликовать Public сразу, видео уходит в ленту ДО завершения рендера → зрители видят сжатый мусор → отваливаются → алгоритм душит видео.

### 5. Всегда "Not for kids"
**Правило:** ставить "Not made for kids" на каждом видео.
**Почему:** "For kids" уводит видео в YouTube Kids, где целевая аудитория его никогда не найдёт.

### 6. Линковать Short → long-form через "Related video"
**Правило:** привязывать каждый Short к long-form видео через Related video.
**Почему:** воронка feed → Short → related long-form → ссылка в описании (кликабельные ссылки в описании есть только у long-form).

### 7. Первые 3 секунды = 90% веса retention
**Правило:** хук в первые 3 сек обязан содержать ВСЕ 4 элемента:
- **Интрига** — контр-интуитивное / шокирующее утверждение
- **Выгода** — что зритель получит (число, обещание)
- **Срочность** — open-loop, заставляющий досмотреть ("Sign 5 will hurt")
- **Релатейбл** — зеркало личного опыта зрителя
**Визуальный удар идёт ДО слов.** Никакого спокойного захода.

### 8. Обновлять YT app перед каждым аплоадом
**Правило:** проверять обновления мобильного YouTube + Studio app ПЕРЕД каждой заливкой.
**Почему:** устаревшая версия приложения стабильно ломает аплоад.

---

## 🆕 ЧАСТЬ 1B — Karena дополнения (2 июн 2026, разбор «5 вещей до 1k подписчиков»)

### 9. «Изумруд»-поиск тем (вместо больших каналов смотрим маленькие)
**Правило:** при поиске новых тем НЕ ориентироваться на Furever Stories 44k / Cats Insider 84k. Искать каналы **≤3k подп с одним вирусным хитом 50k+ просм за последние 3 мес** — это и есть «изумруды», воспроизводимые для нашего размера канала.

**Workflow (mandatory перед каждым раундом темо-поиска):**
1. `vidiq_outliers` с фильтрами:
   ```
   keyword: <наш кейворд>
   contentType: short
   maxSubscribers: 3000
   minViews: 50000
   publishedWithin: threeMonths
   sort: breakoutScore
   ```
2. Отсеять funny-compilation / real-cat-candid (off-format для нас)
3. Оставшиеся = настоящие изумруды → анализировать угол → vidIQ keyword research на кейворд

**Почему это лучше:** если канал на 2k subs сделал 200k просмотров — это означает что тема ПОДНЯЛАСЬ за счёт темы, а не за счёт audience-base. Прямое сигнал «формула работает на нашем размере».

**Лимитация в нашей нише:** 90% small-channel-cat-hits = funny-compilation (Nexlev anti-pattern). Educational + listicle изумрудов мало, но они золото. Пример (2 июн 2026): «Unveiling the Secrets to Kitten Mastery» — Little Mouse 2.09k subs / **660k views** = подсказал angle «kitten parenting / new-owner guide», который мы конвертировали в `5-cat-owner-mistakes` 67.18 GREEN.

### 10. NO subscribe-CTA в первые 60с LONG-form видео
**Правило (для long-form ≥3 мин):** не делать CTA на подписку в первые 60с видео. Сначала **польза**, потом подписка.

**Аналогия Karena:** «представь, в ресторан зашёл, тебе ещё еду не принесли, а официант просит отзыв на Яндексе оставить — никто не оставит».

**Для Shorts (≤60с) это правило НЕ применяется** — CTA на 49-56с (предпоследние 7-10с) = индустриальный стандарт, наш текущий паттерн. Применять только в Cat Evolution (15 мин) и других длинных форматах.

### 11. Алгоритм 2026 пушит малые каналы — НЕ останавливаемся в recovery
**Karena подтверждает (новость от CEO YouTube):** алгоритм специально boost'ит каналы <1k subs в 2026. Видео на 50-900 просм видны на главной.

**Что это значит для нас:** наша recovery-стратегия (1/день + GREEN keywords + 5-Signs обложки) выровнена с алгоритмом. Trust 54v / #1 of 10 = доказательство что алгоритм нас пушит. Не сворачивать.

**Когда пересмотреть:** ≥3 видео с 100+ просм ИЛИ Shorts-feed retention >30%. До тех пор — продолжать ежедневно.

### 12. Eyewear-override: контекстная eyewear заменяет круглые очки (locked 2 июн 2026, user-validated)
**Общий принцип:** локед-правило Brain "glasses ALWAYS on" имеет ИСКЛЮЧЕНИЕ — **любая сцена-специфичная eyewear (что-то надетое на ГЛАЗА или ЛИЦО в области глаз) ЗАМЕНЯЕТ обычные круглые золотые очки**. Очки физически уходят (Brain снял перед сценой).

**Почему:** IRL человек/кот не носит очки ПОД маской / ПОД мото-очками / ПОД ski-goggles. Очки + любая другая eyewear одновременно = визуальный мусор + анатомически невозможно.

**Список eyewear которые отменяют круглые очки (НЕ исчерпывающий, расширять по мере появления):**
- 🛏️ **Sleep mask** / dream goggles (dreams thumbnail / sleeping Brain в маске)
- 🏍️ **Motorcycle goggles** (любая мото-сцена)
- 🎿 **Ski goggles / ski mask** (зимняя/горная сцена)
- 🤿 **Scuba goggles** / diving mask (подводная сцена)
- 🏊 **Swim goggles** (бассейн / купание)
- 🥽 **VR headset / VR goggles** (tech/futurism сцена)
- 🔥 **Welding mask** (workshop сцена)
- 🥽 **3D-glasses** (cinema / movie сцена)
- 🕶️ **Sunglasses** (beach / sunny / cool-pose сцена)
- 🥽 **Lab safety goggles** (chemistry сцена — заменяют scientist-coat-glasses)

**В промте конкретно:**
- Убрать `Small thin round gold-framed glasses ALWAYS on` из Locked Brain block
- Описать новую eyewear с деталями (цвет, форма, материал)
- Добавить явно: `NO regular gold-framed glasses in this scene — [sleep mask / ski goggles / etc.] overrides the glasses rule`
- В негативы добавить: `gold-framed round glasses, regular glasses, eyeglasses, spectacles, glasses worn under [eyewear-name]`

**ВАЖНО — что НЕ затрагивает правило:**
- Костюмы где НЕТ замены eyewear (lab coat, detective hat, chef hat, doctor coat) → очки **остаются** (см. §2 style-guide). Правило 12 — только про eyewear-vs-eyewear.
- Обычные «sleeping Brain» сцены БЕЗ маски (просто спит на ковре) → очки **остаются**.

### 13. Thumbnail prop-variety (locked 2 июн 2026, user direction)
**Принцип:** для разнообразия обложек каждая тема может иметь свой **prop / costume / setting**, добавленный поверх Locked Brain. Это лекарство от «обложечного fatigue» (когда все thumb выглядят одинаково).

**Идеи по темам:**
- 🛏️ dreams → nightcap + sleep mask (eyewear-override §12, очки OFF)
- 🏍️ motorcycle / road / vroom-фактоид → moto-goggles + tiny leather jacket (eyewear-override §12)
- 🎿 cold-weather / winter cat → ski goggles + scarf (eyewear-override §12)
- 🤿 swimming / water-related → swim goggles + tiny float-ring (eyewear-override §12)
- 🥽 «virtual reality experiment» / futurism → VR-goggles (eyewear-override §12)
- 🍳 owner-mistakes / cooking metaphor → tiny chef hat / oven mitts (Brain очки остаются)
- 💕 bond / love → small bouquet / heart-shaped chocolates (Brain очки остаются)
- 🐾 fight / aggression-warning → cute mini boxing gloves (Brain очки остаются)
- 🎓 explainer / scientist → lab coat (Brain очки остаются — §2 style-guide)
- 👮 territorial / sit-above → tiny police hat (Brain очки остаются)
- 🎬 movie-night / TV-flicker → tiny popcorn box + 3D-glasses (eyewear-override §12)

**Жёсткое правило вариативности:**
- **face-size в обложке остаётся 55-60% (5-Signs формула)** — не меняем
- **текст-плита в lower-middle, big bold** — не меняем
- **eye-emotion (если глаза открыты) или sleep-emotion (если закрыты)** — главный CTR-сигнал, не размывать
- Меняется только **prop / accessory / immediate background context** — это даёт визуальное разнообразие БЕЗ потери CTR-паттерна.

---

## 📦 ЧАСТЬ 2 — Порядок SEO Pack (строгий)

При создании ИЛИ значимом редактировании скрипта — **всегда** обновлять полный SEO Pack, **никогда не пропускать теги**. Порядок вывода строго такой:

### 1. Title (40–70 символов)
- Главный ключ внутри (`cat psychology` для BrainCatAI всегда)
- Через `|` ниша-тег, заканчивать `🐱 | Cat Psychology`
- **БЕЗ хэштегов** (правило 1 выше)

### 2. Alt titles для A/B-теста (опционально)
Варианты для тестирования.

### 3. Description (≥ 250 символов)
- Главный ключ повторить 2–3×
- Включить 5+ supporting keywords
- Закончить расширенным блоком хэштегов + CTA на подписку
- Для Shorts описание слабо влияет на discovery, но кормит keyword-понимание YouTube — заполнять стоит, но не агонизировать

### 4. Tags (20–25, до 500 символов)
Базовый набор (всегда):
```
cat psychology, cat facts, cat behavior, cat secrets, cat science, cat communication, cat body language, feline behavior, understanding cats, facts about cats, animal facts, animal science, did you know, mind blowing facts, brain cat, cat facts daily, cat behavior funny, cat domestication, cats vs humans
```
Плюс обязательные channel-wide:
```
braincatai, cat facts mind blowing, cat behavior explained
```
Плюс 5–10 long-tail тегов под именно это видео.

### 5. Hashtags ТОЛЬКО для тела описания
```
#shorts #catpsychology #catfacts #catbehavior #braincatai #didyouknow #petfacts
```
**НЕ добавлять в поле title** (правило 1).

### 6. Pinned comment (с вопросом на engagement)
Добавлять также в [`pinned-comments.md`](./pinned-comments.md).

### 7. Thumbnail concept

---

## 🧠 Часть 3 — почему это вообще важно (контекст для нового чата)

Канал BrainCatAI ушёл в recovery mode (с ~700-1300 v/day до 10-44) из-за нарушения нишевых/алгоритмических правил. Правила Карены — часть восстановления. Не нарушать без явного подтверждения юзера.

Связанные локи в `CLAUDE.md`:
- **Cats-only** — каждое видео про кошек (нарушение = демоушн за audience confusion)
- **Один Short в день** — никогда не публиковать два в один день
- **Pre-scripting vidIQ check** — перед любым скриптом проверить ключ (cache-first)
- **Veo 3 pre-flight** — проверять каждый Veo-промт по чек-листу до траты credits

---

## 📍 Где это используется

- Каждый новый скрипт наследует SEO Pack из `script-template.md` — он уже построен по этим правилам
- Краткая 8-пунктовая сводка продублирована в шапке `production-status.md`
- Полный свод (этот файл) — канонический. При расхождении верить этому файлу.
