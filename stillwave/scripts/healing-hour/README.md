# 🌿 Healing Hour — StillWave Series

Параллельная серия для **healing / sleep / anxiety / nervous system reset** видео на канале StillWave (@stillwavezen).

Существует **отдельно** от Power Hour series (productivity / focus / deep work) — чтобы YouTube алгоритм не путал две разные аудитории.

---

## 🎯 Когда видео идёт в эту серию

| Признак | Healing Hour ✅ | Power Hour ❌ |
|---|---|---|
| **Intent зрителя** | Замедлиться, расслабиться, заснуть | Работать, сфокусироваться, написать |
| **Тематика** | Hz frequencies, sound bath, meditation, anxiety relief, sleep | Coding, writing, studying, productivity, deep work |
| **Темп воспроизведения** | Медитативный, ниже 60 BPM | Spacious focus, 60-70 BPM |
| **Инструменты** | Singing bowls, shakuhachi, suzu, koto | Rain, ambient pad, lo-fi, soft piano |
| **Поисковые ключевики** | "528 Hz", "nervous system reset", "anxiety relief", "sleep music" | "focus music", "deep work", "productivity", "study music" |
| **Цель видео** | Parasympathetic activation (опустить сердечный ритм) | Sustained attention (1+ часа концентрации) |

**Правило:** если у тебя возникает сомнение, в какой папке хранить — спрашивай "зритель будет работать или расслабляться?". Если расслабляться → `healing-hour/`.

---

## 📝 Title формула

```
Best [keyword] [setting/theme] Healing Hour [1H Top X]
```

**Обязательные элементы:**
- `Best` — positive marker (бот любит, +4 score)
- Hz / 528 / 432 / частоту указывать **числом** в title — для search (бот любит цифры, +8)
- `Healing Hour` — series brand (фирменная фраза)
- `[1H Top X]` в скобках — длина + descriptor (бот любит скобки +3, число +8, positive `top` +4)
- Длина title: **40-70 ch** (sweet spot для бота, +15)
- Финальный score через `/title-batch` должен быть **≥ 80/100**

**Подтверждённый пример** (84/100):
```
Best 528 Hz Japanese Zen Healing Hour [1H Top Nervous System Reset]
```

**Шаблоны под разные темы:**

| Тема | Title template |
|---|---|
| Nervous System Reset | `Best [Hz] [aesthetic] Healing Hour [1H Top Nervous System Reset]` |
| Anxiety Relief | `Best [Hz] [aesthetic] Healing Hour [1H Top Anxiety Relief]` |
| Sleep Wind-Down | `Best [Hz] [aesthetic] Healing Hour [1H Top Deep Sleep]` |
| Vagus Nerve Activation | `Best [Hz] Healing Hour [1H Top Vagus Nerve Reset]` |
| Sound Bath | `Best [Hz] Sound Bath Healing Hour [1H Top Calm]` |

---

## 🎨 Визуальная эстетика

**Локированный baseline:** Spacious Tokyo Penthouse (тот же что Power Hour) — для единства бренда канала.

**Отличие от Power Hour:**

| Элемент | Power Hour | Healing Hour |
|---|---|---|
| **Foreground prop** | Open MacBook + tea cup + bonsai | Low altar + rin singing bowls + incense burner + candle |
| **Освещение** | Balanced 3-source (city + laptop + fireplace) | Dim intimate candlelit (fireplace primary, neon subdued) |
| **Mood** | Active focus | Parasympathetic calm |
| **Window** | Sharp neon, rain ok | Soft bokeh neon, clear or misty (rare rain) |
| **Composition** | Wide dynamic angle | **Frontal symmetric**, eye-level, no ceiling |

См. `nervous-system-reset-528hz-1h.md` для эталонного NanoBanana prompt секции 3/4.

---

## 🎵 Suno spec (audio)

**Locked tail:**
```
instrumental only, no vocals, no singing, no chanting, no spoken word, pure instrumental
```

**Healing Hour текстура:**
- Hz drone foundation (528 / 432 / 963 / 174 / любая Solfeggio)
- Optional secondary Hz overlay каждые 8 минут
- **Rin-dō Buddhist singing bowls** (НЕ Tibetan — Japanese!) с long sustained hum (30+ sec)
- Shakuhachi bamboo flute — soft sustained mono notes раз в 60 сек
- Suzu hand bell shimmer в высоком регистре
- Mokugyo wooden fish-block tap раз в 90 сек (опционально)
- Sub-bass pulse каждые 16 тактов (body heartbeat)
- Fireplace crackle (warm ambient texture)
- **60 BPM** (медитативный темп)
- **No melody, no chord progression** — pure tonal frequency bath
- No buildup, no climax — sustained meditative

**16 треков × ~3:30-4:30 = ~1:01:00 общая длина** (стандарт серии). При необходимости 8 или 24 трека.

---

## 🎬 Pipeline (статичная картинка вместо AI loop)

Для Healing Hour видео **НЕ генерим Flow/Kling motion loop** — AI всегда даёт drift на 1+ часа. Используем:

```bash
# Static image + audio = clean 1-hour video
ffmpeg -loop 1 -i nanobanana-thumbnail.jpg -i audio.mp3 \
  -c:v libx264 -tune stillimage -pix_fmt yuv420p -r 24 \
  -c:a aac -b:a 192k -shortest -t 3660 final.mp4
```

Если хочется лёгкого движения (candle/fireplace) — overlay в CapCut на статичный base layer, чтобы база не дрейфила.

---

## 📋 Pinned comment template

Адаптируется под тему. Пример:

```
🌃 A quiet Tokyo penthouse. Clear calm night. Bronze rin bowls humming. Fireplace crackling. [Hz] Hz holding steady. One hour for your nervous system to remember what calm feels like. Comment one word — what your body needs to release tonight. Subscribe for more Healing Hour sessions 🌸
```

---

## 🏷️ Tags стратегия

24 тега, total **300-480 chars** (sweet spot бота), баланс 3+ short + 5+ medium + 2+ long. Title keywords должны быть в exact match минимум 3-4 тегов.

Базовый набор Healing Hour (адаптируется под Hz/тему):
```
[Hz] hz [theme] healing hour, [theme] healing hour, [Hz] hz [theme] healing,
nervous system reset music, [Hz] hz nervous system reset, 1 hour nervous system reset,
parasympathetic nervous system, vagus nerve activation, anxiety relief music,
japanese sound bath, rin singing bowls, japanese healing music,
frequency healing, meditation music, sleep music, japanese zen, healing music,
zen music, [Hz] hz, japanese ambient, binaural beats, mindfulness, stress relief
```

---

## 🆚 Healing Hour vs Power Hour — quick decision tree

```
Видео про работу, продуктивность, фокус?
   └─ ДА → Power Hour series (root scripts/)
   └─ НЕТ ↓

Видео про сон, исцеление, тревогу, медитацию, Hz-частоты?
   └─ ДА → Healing Hour series (scripts/healing-hour/)
   └─ НЕТ ↓

Видео про деньги, инвестирование?
   └─ ⚠️ Это **не текущая ниша StillWave**. Не делать.

Видео в стиле legacy Hz / иероглиф / sumi-e (старый формат до hybrid pivot)?
   └─ Остаётся в root scripts/ как legacy. С мая 2026 переходим на Power/Healing Hour брендинг.
```

---

## 📂 Файлы в этой папке

| Файл | Title | Status |
|---|---|---|
| `nervous-system-reset-528hz-1h.md` | Best 528 Hz Japanese Zen Healing Hour [1H Top Nervous System Reset] | ✅ Ready to upload (90/100 SEO, music done, image done) |

---

## 🔄 Будущее расширение series

Если Healing Hour видео покажут good performance (24h: > 80 views; 7d: > 200 views; CTR > 4%), можно создать дополнительные параллельные series:

- **Sleep Hour** (`scripts/sleep-hour/`) — узкая ниша sleep music, 3-8 часов
- **Meditation Hour** (`scripts/meditation-hour/`) — guided meditation / breathwork
- **Study Hour** (`scripts/study-hour/`) — отдельно от Power Hour для студентов

Каждая новая series = новый папка с README по этому шаблону.
