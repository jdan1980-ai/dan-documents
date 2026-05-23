# Focal ML — Brain character preset + тест (no Veo, попытка убить дрейф)

> **Цель:** проверить держит ли Focal внешность Brain (через Character preset + Kling/Seedance вместо Veo) лучше, чем 10-кредитная Veo, которая дрейфит (синие глаза, реализм, белые лапы, очки пропадают).
>
> **Это тест, не миграция.** Сначала 1 сцена. Меняем пайплайн только если держит + есть 9:16.

## 🚨 Проверить ПЕРВЫМ делом
1. **9:16 vertical** есть? (Storyboard Studio нас уже подставил с 16:9 — это must-check)
2. Выбор модели: ставим **Kling или Seedance**, НЕ Veo (Veo нам уже доказала что дрейфит)
3. Озвучку Brain их голосами **НЕ включаем** — рот закрыт, VO отдельно через Google Vids TTS

---

## Шаг 1 — создать Character «Brain»

**Reference image:** загрузи наш эталон `assets/brain-character-reference.png` (чистый: зелёные глаза, очки, рыжие лапы, heart-tag). Image-якорь — главный рычаг консистентности.

**Visual description (вставить в Character):**
```
Brain — a cute Pixar/Disney 3D ANIMATED CARTOON orange tabby KITTEN (8-10 weeks old, slender petite kitten, NOT adult, NOT chubby, NOT photorealistic, NOT a real cat). LOCKED features that must NEVER change between shots:
- Big round bright EMERALD GREEN eyes (#3DDC84) — never blue, never amber, never cyan.
- Small thin round GOLD-framed glasses — ALWAYS on his face, every shot.
- A plain smooth BROWN leather collar with EXACTLY ONE gold HEART-SHAPED tag engraved "Brain" — heart shape (never round, never blank), no studs, no holes, no buckle.
- Soft fluffy orange tabby fur with darker stripes. ALL 4 paws the SAME ginger as the body (NO white socks). Tail ginger to the very tip (NO white tail tip).
- EXACTLY 2 symmetric kitten ears, EXACTLY 4 paws, pink nose, white whiskers.
- Mouth stays CLOSED (he never talks; no lip-sync).
```

**Personality / mannerisms (Focal держит жесты/эмоции):**
```
Smart, curious, gentle. Expresses everything through eyes, ears and whiskers (mouth stays closed). Calm confident posture. Reacts with slow blinks and head tilts.
```

---

## Шаг 2 — тест-сцена (1 штука)

Берём «5 Things» Сцена 1 (Brain сидит, очки+ошейник+кулон+хвост видны — идеально для проверки локов). Формат **9:16**, модель **Kling/Seedance**.

**Scene prompt:**
```
@Brain (the locked orange tabby kitten — emerald eyes, gold round glasses, brown collar with ONE gold heart "Brain" tag, ginger paws, ginger tail to the tip) sits on a sage-green rug in a cozy Pixar-style living room (cream walls, warm afternoon light, soft cartoon look — NOT photorealistic). Medium close-up, gentle slow push-in over 6 seconds. Brain looks up at the camera with a soft hopeful, slightly pleading expression, ears gently up, head tilted a touch, gives one slow blink. Mouth stays closed. A soft pastel thought-bubble with a little heart floats to the upper-right. Keep Brain IDENTICAL to the character reference the whole clip — glasses on, eyes emerald green, paws and tail ginger, one heart-shaped tag.
```

**Negatives (если есть поле):**
```
photorealistic, real cat, blue eyes, cyan eyes, amber eyes, missing glasses, no glasses, white paws, white socks, white tail tip, round tag, blank tag, two cats, second cat, extra hand, mouth open, talking
```

---

## Шаг 3 — A/B чек vs 10-кредитная Veo

| Критерий | Focal (Kling/Seedance) | 10-cr Veo (для сравнения) |
|----------|------------------------|----------------------------|
| Очки на месте весь клип | | |
| Глаза emerald (не синие) | | |
| Лапы рыжие (не белые) | | |
| Кончик хвоста рыжий | | |
| Кулон — heart с «Brain» | | |
| Стиль Pixar (не реализм) | | |
| 9:16 vertical | | |
| Сколько ретраев | | |
| Цена | | |

**Decision gate:**
- ✅ Держит всё + 9:16 → переносим продакшен в Focal (конец войны с дрейфом). Обновляю пайплайн в `CLAUDE.md`.
- 🟡 Держит частично → гибрид (Focal для движения, наши картинки+Ken Burns для статики)
- 🔴 Дрейфит как Veo / нет 9:16 → остаёмся на «картинки + Ken Burns» (no-Veo лист)

→ Запиши результаты сюда.

## Заметки
- Focal под капотом использует те же модели — сила в **слое консистентности (character preset) + выборе модели**. Поэтому обязательно: preset + image-якорь + Kling/Seedance.
- Если Kling не зайдёт — попробуй Seedance, потом Hailuo. У нас 3 модели на выбор, это и есть преимущество Focal над «только Veo».
