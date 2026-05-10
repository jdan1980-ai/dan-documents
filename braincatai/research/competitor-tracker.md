# Competitor Channel Tracker

Канонический список каналов, темы которых мы отслеживаем для генерации идей для BrainCatAI. Высокие просмотры на этих каналах = подтверждение спроса.

## Целевые каналы

| # | Канал | URL | Что смотрим |
|---|-------|-----|-------------|
| 1 | catsinsider | https://www.youtube.com/@catsinsider/videos | Cat behavior + science |
| 2 | AskMyCats | https://www.youtube.com/@askmycats/shorts | Cat psychology Shorts |
| 3 | The Curious Cat | https://www.youtube.com/@thecuriouscatt/videos | Cat psychology longform |
| 4 | Cat Behaviour Channel | https://www.youtube.com/@catbehaviourchannel/videos | Cat behavior documentary |
| 5 | Yamato Zen Relaxing | https://www.youtube.com/@YamatoZenRelaxing/videos | **Different niche** — relaxation/zen aesthetic, see comparison below |
| 6 | **Мир Глазами Кошек** (RU) | https://www.youtube.com/@МирГлазамиКошек | **🔥 Top match** — 32.5K subs, 8.77M views, 46 videos. Hit 2.6M views in Feb 2026. Russian-language equivalent of BrainCatAI niche. Channel ID `UCSYBgC5AwWL9MaRj9lsAcgQ` |

## ⚠️ Технический лимит

Прямой автоматический сбор данных (WebFetch на YouTube/SocialBlade) **заблокирован 403**. Чтобы Claude мог анализировать — нужен один из путей:

### Путь 1 — Вручную (быстро, не требует ключей)
Раз в неделю / перед батчем сценариев — открыть каждый канал, скопировать топ-15 видео по просмотрам и вставить сюда (в таблицу в этом файле или в чат). Claude разберёт паттерны и предложит темы.

Что копировать с каждого канала:
- **Заголовок** (точно как написано)
- **Просмотры** (число)
- **Дата публикации** (если видна)
- Желательно: длительность (Short ≤ 60 сек или long-form)

### Путь 2 — vidIQ (доступен с 12 мая 2026)
Когда восстановятся credits — Claude использует:
- `vidiq_channel_videos` — видео канала с метриками
- `vidiq_outliers` — видео с аномально высокими просмотрами
- `vidiq_keyword_research` — спрос на конкретные ключи
- `vidiq_breakout_channels` — растущие конкуренты

### Путь 3 — YouTube Data API v3 (бесплатно, нужен 1 раз настроить)
Если получить API key (Google Cloud Console, бесплатно для базового использования):
1. Сохранить в `~/.config/youtube-api-key` (НЕ коммитить)
2. Claude может вызывать через `curl` для извлечения video lists + view counts

---

## Рабочий процесс «новый батч сценариев»

1. **Сбор данных** — через путь 1, 2 или 3 → вставить топ видео из 4 каналов в раздел "Свежий снимок" ниже
2. **Анализ** — Claude находит:
   - Темы, которые повторяются на нескольких каналах (= подтверждённый спрос)
   - Темы с высокими просмотрами относительно подписчиков (= алгоритм пушит)
   - Темы, которые НЕ покрыты у нас (= открытая ниша)
3. **Выбор 2–4 тем** для следующего батча
4. **Сценарии** — Claude пишет полные сценарии по [script-template.md](../script-template.md)

---

## Свежий снимок (TBD — заполнить вручную или через API)

> Скопируйте сюда топ-15 видео с каждого канала по просмотрам, я проанализирую.

### catsinsider

| Заголовок | Просмотры | Дата | Тип |
|-----------|-----------|------|-----|
| _пусто_ | | | |

### AskMyCats

| Заголовок | Просмотры | Дата | Тип |
|-----------|-----------|------|-----|
| _пусто_ | | | |

### The Curious Cat

| Заголовок | Просмотры | Дата | Тип |
|-----------|-----------|------|-----|
| _пусто_ | | | |

### Cat Behaviour Channel

| Заголовок | Просмотры | Дата | Тип |
|-----------|-----------|------|-----|
| _пусто_ | | | |

### Yamato Zen Relaxing (другая ниша — relaxation, не explainer)

| Заголовок | Просмотры | Дата | Тип |
|-----------|-----------|------|-----|
| _пусто_ | | | |

---

## 🆚 Yamato Zen Relaxing vs BrainCatAI — разные жанры

> Прямой просмотр канала заблокирован 403 из репо. Анализ ниже сделан по сигналам в названии (`Yamato` + `Zen` + `Relaxing`) и общему паттерну ниши. Для точной картины — пришлите скриншот канала или 5–10 заголовков их видео.

### Что (вероятно) на канале Yamato Zen Relaxing

- **Ниша:** relaxation / ambient / sleep content
- **Эстетика:** японский zen (Yamato = старое название Японии, Zen = медитативная философия)
- **Тип контента:** длинные ambient видео с природой/животными/успокаивающими звуками, без активной озвучки
- **Аудитория:** люди ищущие "как заснуть", "как расслабиться", "ASMR"
- **Длительность:** обычно 1–8 часов на видео (не Shorts формат)

### BrainCatAI

- **Ниша:** cat psychology / educational explainer
- **Эстетика:** Pixar 3D персонаж, тёплое освещение, динамичные сцены
- **Тип контента:** короткие 60-сек Shorts с активной озвучкой, mind-blow факты
- **Аудитория:** ищут "почему мой кот делает X", любят kid-friendly facts
- **Длительность:** ≤ 60 сек (Shorts only)

### Структурные различия

| Параметр | Yamato Zen Relaxing | BrainCatAI |
|----------|--------------------|-----------| 
| **Цель зрителя** | Расслабиться, заснуть | Узнать что-то и удивиться |
| **Активность зрителя** | Пассивное, фоновое | Активное смотрение |
| **Озвучка** | Минимальная или без | Каждые 7 сек новая фраза |
| **Темп** | Медитативный, медленный | Быстрые cuts, hook за 2 сек |
| **Формат** | Long-form 1–8 часов | Shorts 60 сек |
| **Монетизация** | RPM от длительности просмотра | Shorts fund + view-based |
| **Алгоритм** | Ambient/sleep sub-niche | Trending Shorts feed |
| **Персонаж** | Без — природа/предметы | Есть — Brain |

### Перекрытия

- **Оба возможно используют котов** в визуале (Zen канал может показывать спящих котов, котов на солнце, etc.)
- **Оба нацелены на cat lovers** в широком смысле
- **Ниже этого** — это **разные продукты для разных моментов дня**: zen-канал смотрят перед сном, BrainCatAI смотрят пока scrollят ленту днём

### Кого считать конкурентом

**Yamato Zen Relaxing — НЕ прямой конкурент** BrainCatAI. Другая ниша, другая аудитория, другой алгоритмический сегмент. Они не "забирают" ваших зрителей и наоборот.

**Однако** канал может быть полезным эталоном по другим причинам:
1. **Visual aesthetics** — если у них красивая Japanese zen эстетика, можно одолжить **цветовые решения** для конкретных видео BrainCatAI про сон/спокойствие (например, потенциальное "Why cats sleep 16 hours" с zen-эстетикой)
2. **Audio mood** — если они используют качественные ambient треки, можно референсить для тихих сцен BrainCatAI
3. **Title/SEO patterns** — посмотреть как они формируют title для cat-релакс контента (ключевые слова "relaxing", "calming", "zen" иногда попадают в смешанный поиск)

### Что лучше отслеживать

Каналы 1–4 в основном списке — **прямые конкуренты** (та же ниша). За ними следить ради идей и SEO.
Yamato Zen Relaxing — **бенчмарк эстетики**, не источник идей контента. Один взгляд раз в месяц на их визуал, не больше.

---

## Что мы УЖЕ знаем работает (без сбора)

На основе вашей аналитики + общеизвестных виральных паттернов в кошачьей психологии:

### Из ваших данных (Apr 22–28, 2026)

| Тема | Просмотры | Формат | Вердикт |
|------|-----------|--------|---------|
| Why Cats Are Afraid of Cucumbers | 954 | Animated | ✅ Виральная |
| How Cats Always Land on Their Feet | 791 | Static | ✅ Тема работает, переснять анимировано |
| Why Cats "Make Biscuits" | 432 (10.34% CTR) | Static | ✅ Тема работает |
| Your Cat Doesn't Know Your Face | 429 (20% retention) | Static | ✅ Тема работает |
| Your Cat's Purr Heals Bones | 270 (11.9% CTR) | Static | ✅ Hook работает, payoff подкрутить |

### Канонические виральные темы кошачьей психологии (2026)

Эти темы стабильно набирают миллионы просмотров на topical каналах. **Помечено сделано/не сделано** для нашего канала.

#### Поведение и общение
- ✅ Why cats are afraid of cucumbers
- ✅ Why cats make biscuits (knead)
- ✅ Why cats bring you dead things (in production)
- 🟡 Why cats slow blink at you (love language) — **высокий приоритет**
- 🟡 Why your cat stares at you for no reason
- 🟡 Why your cat meows ONLY at humans (not other cats)
- 🟡 Why cats follow you to the bathroom
- 🟡 Why cats knock things off tables
- 🟡 Why cats hate closed doors
- 🟡 Why cats roll on their backs (NOT for belly rubs)
- 🟡 Why cats bring their toys to you

#### Восприятие мира
- ✅ Your cat doesn't know your face
- 🟡 Your cat sees you as a giant, weird-looking cat — **высокий приоритет**
- 🟡 Cats can hear you blinking
- 🟡 Why cats can see in the dark (and you can't)
- 🟡 Why cats hate water (it's not what you think)
- 🟡 Why cats love boxes more than expensive beds (animated done)

#### Тело и физиология
- ✅ Why cats sleep 16 hours a day
- 🟡 Why your cat's purr can heal bones (re-make animated) — **высокий приоритет**
- 🟡 Why cats have rough tongues
- 🟡 Why cats can fit through tiny spaces (whiskers science)
- 🟡 Why cats eat grass and throw up
- 🟡 Why cats love warm spots
- 🟡 Why cats land on their feet (re-make animated) — **высокий приоритет**

#### Тёмные/удивительные факты
- 🟡 Your cat remembers every person who's been mean to it
- 🟡 Your cat could kill you if it was bigger (predator instinct)
- 🟡 Cats domesticated themselves — humans didn't tame them
- 🟡 Why cats arch their backs (Halloween cat origins)
- 🟡 Why cats stare at the wall (it's not ghosts, but...)

#### Идеи на отложенный возврат (нужны зрелость канала / специфический угол)

- 🟠 **Street cats: how they survive in cities** — мощная тема, но риски: бренд-конфликт (Brain в переулке/мусорке), тон-риск (легко скатиться в жалость), смешение аудитории (cat psychology vs animal welfare), требует нескольких локаций (нарушает single-location rule). Вернуться когда канал перейдёт 5–10K подписчиков. Альтернативный угол если делать раньше: *"Your house cat couldn't survive ONE day on the street"* — личный крючок остаётся, уличные коты как фон сравнения, можно сделать в одной локации (квартира + взгляд за окно). Возможно превратить в серию "Street Cat Files".
- 🟠 **Boy Cat vs Girl Cat: Key Differences (direct version)** — saturation МАКСИМАЛЬНАЯ (все cat-каналы делали), стереотипы научно слабые, большинство различий исчезает после стерилизации (а 95% домашних котов стерильны), требует двух котов в кадре (нарушает Brain-alone rule). **Заменено на сильный под-угол** "Your Cat's COLOR Tells You Its Gender" → реальная генетика, meta-момент с Brain (он оранжевый → 80% самец), один кот в кадре, чистый mind-blow. Вернуться к прямой версии можно если набрать большой survey/comment-данных от своей аудитории (community-engagement видео).

### Как читать эту таблицу
- ✅ — у нас уже опубликовано
- 🟡 — открыто, ещё не сделано
- 🟢 — в производстве

---

## 🔥 Мир Глазами Кошек — глубокий разбор (2026-05-10, через бот)

**Stats:** 32.5K subs · **8.77M total views** · 46 videos (since 2016 — пробились в 2026) · 3.39 uploads/week · engagement 2.29%
**Median:** 36,208 views · **Avg:** 191,075 · **Max:** **2,605,492**
**Outliers:** 2 видео × 35-72 от медианы — фактически 2 хита затащили канал в 8.77M total views

### Топ-5 хитов (русскоязычные — но паттерны переводятся 1-в-1)

| Views | Title |
|---|---|
| **2,605,492** | Почему Кошки Вдруг ЗАЛЕЗАЮТ На Вас? **(Причина шокирует)** |
| 1,291,214 | Если Ваша Кошка Спит с Вами Каждую Ночь, **ВОТ ЧТО ЭТО ЗНАЧИТ!** |
| 580,077 | Твоя Кошка Ждала ВСЮ ЖИЗНЬ, Когда Ты ЭТО СДЕЛАЕШЬ! |
| 542,591 | **13 СЛОВ**, которые Ваша Кошка РЕАЛЬНО понимает |
| 535,727 | **17 Вещей**, которые Вы ДОЛЖНЫ ПРЕКРАТИТЬ ДЕЛАТЬ с Кошкой! |

### Title-formula (анализ топ-15 через бот)

- **Длина:** 57 ch avg (range 44-70) ← идеально по нашему скорингу 40-70
- **Восклицательный знак `!`** — **11/15** хитов (vs. в наших нет ни одного!)
- **Скобки `()` или `[]`** — 5/15 хитов: `(Причина шокирует)`, `(прекрати)`, `(говорят ветеринары)`
- **Числа в начале** — 4/15: «13 СЛОВ», «17 Вещей», «15 Повседневных», «17 Продуктов»
- **Знак вопроса `?`** — почти не используется (1/15) ← они предпочитают **declarative emotional**
- **CAPS-акцент** — почти каждый title имеет 1-3 слова в CAPS для drama

### Шаблоны заголовков (lift-and-shift на английский для BrainCatAI)

| Шаблон RU | English equivalent для нас | Какой angle |
|---|---|---|
| «Если Ваша Кошка X, ВОТ ЧТО ЭТО ЗНАЧИТ!» | "If Your Cat Does X, THIS Is What It REALLY Means!" | Direct address + reveal |
| «Почему Кошки Вдруг X? (Причина шокирует)» | "Why Cats Suddenly X (The Real Reason)" | Mystery + payoff |
| «Твоя Кошка X — Правда ШОКИРУЕТ!» | "Your Cat Does X — The Truth WILL Shock You!" | Curiosity + emotion |
| «N Вещей, которые Вы ДОЛЖНЫ Прекратить Делать с Кошкой!» | "N Things You MUST Stop Doing to Your Cat!" | Listicle + warning |
| «N СЛОВ, которые Ваша Кошка РЕАЛЬНО Понимает» | "N Words Your Cat REALLY Understands" | Listicle + revelation |

### Что забирать в наши title прямо сейчас

1. ✅ **Добавить `!`** — у нас сейчас 0 хитов с `!`, у них 11/15. Дешёвый score-boost.
2. ✅ **Скобки с эмоциональным reveal** — `(Real Reason)`, `(Vets Say)`, `(Stop Doing This)`. Дотягивает по нашему скорингу +3.
3. ✅ **Прямое обращение «Your Cat...»** — у нас часть видео уже использует, но не все. Топ-каналы делают это в 100% хитов.
4. ✅ **Listicle-числа** — `13 Words Your Cat Knows`, `17 Things You Should Stop Doing`. Это новый формат для нас.

### Что показывает их успех о нише

- **Ниша cat-psychology shorts/lite-explainer = высокая ёмкость** (8.77M views на 46 видео = 190K avg). Это **в 5x больше потолка**, чем сейчас у BrainCatAI (392 median).
- **Канал стрельнул внезапно**: с 2016 года висел тихо, в феврале 2026 пошли хиты. Это значит **алгоритм YouTube активно пушит cat psychology в 2026** — мы в правильной нише в правильное время.
- **3.39 видео/нед** ниже чем у BrainCatAI (7.88) — у них меньше частота, но больше размер каждого видео и виральность. Качество > количество для этой ниши.

---

## Текущие приоритеты (топ-5 для следующих батчей)

Выбраны по комбинации: высокий спрос + не сделано + хорошо ложится на формат Brain:

1. **Why Cats Slow Blink (and how to slow blink back)** — emotional payoff, save-able hack, нет анимированного контента в Shorts
2. **Your Cat Sees You As a Giant Weird-Looking Cat** — relatable mind-blow, новая для нас тема
3. **Why Your Cat's Purr Can Heal Bones (Re-make)** — наш топ-CTR (11.9%), переснять анимированно с лучшим payoff
4. **Cats Hear You Blinking** — absurd-true hook
5. **Why Cats Hate Closed Doors** — universal experience, low Shorts saturation

## Регулярность пересмотра

- Раз в **неделю** — обновить "Свежий снимок" из 4 каналов (вручную или через vidIQ когда credits)
- Раз в **месяц** — пересмотреть приоритеты на основе свежей аналитики собственного канала
- После каждой публикации — отметить ✅/🟡 в таблице
