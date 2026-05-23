# OpenART — обучение консистентного Brain (конец дрейфа)

> **Цель:** обучить/залочить Brain как **Consistent Character / LoRA** в OpenArt. Тогда очки/зелёные глаза/рыжие лапы+хвост/heart-кулон зашиты в модель — не «подсказка на лету» (которую Veo игнорил), а часть персонажа. Это сильнейший лок из всех что мы пробовали.

## 🚨 Проверить
1. **9:16 vertical** на генерации/видео — must
2. Стиль = **stylized / Pixar**, НЕ photoreal
3. Kling Omni умеет voice-driven персонажей — **голос НЕ включать** (рот закрыт, VO отдельно через Google Vids TTS)
4. Модель для нашего мультяшного кота: тестируй **Seedream 4.0 / Kling** (стилизация). Nano Banana 2 если доступна — она у нас держала лучше Pro.

---

## Шаг 1 — сгенерить 5 чистых тренировочных картинок Brain

Принцип OpenArt: «что скормишь важнее промта». Нужно **5 картинок ОДНОГО Brain**, разные ракурсы, нейтральное выражение, **простой ровный фон** (чтобы модель училась персонажу, а не комнате), одинаковый свет. Генерь в Nano Banana 2, отбери чистые (все локи на месте), потом скорми в тренировку.

> Каждый промт уже самодостаточный (Locked Brain внутри). Фон намеренно простой — это для ТРЕНИРОВКИ, не для видео.

**Ref 1 — фас, сидит:**
```
Cute Pixar/Disney 3D ANIMATED CARTOON orange tabby kitten named Brain (8-10 week old kitten, slender, NOT adult, NOT chubby, NOT photorealistic), sitting upright facing camera, neutral friendly expression. Big round VIVID EMERALD GREEN eyes (#3DDC84 — never blue/amber). Small thin round gold-framed glasses ON his face. A plain smooth brown leather collar with EXACTLY ONE gold HEART-SHAPED tag engraved "Brain" (heart shape, not round/blank, no studs/holes). Soft fluffy orange tabby fur with darker stripes, ALL 4 paws ginger (NO white socks), tail ginger to the very tip (NO white tip), pink nose, white whiskers, EXACTLY 2 ears, EXACTLY 4 paws, mouth closed. Plain soft light-grey studio background, even soft lighting, full body visible, sharp focus.
```
**Ref 2 — 3/4 слева, сидит:** тот же промт, заменить «sitting upright facing camera» → `sitting, turned 3/4 to the left, head toward camera`
**Ref 3 — 3/4 справа, сидит:** → `sitting, turned 3/4 to the right, head toward camera`
**Ref 4 — профиль, стоит:** → `standing in full side profile, looking ahead`
**Ref 5 — крупный план морды:** → `close-up portrait of his face and shoulders, facing camera` (чётко видно глаза/очки/кулон)

**Negatives (на все):**
```
photorealistic, real cat, photo, blue eyes, cyan eyes, amber eyes, missing glasses, no glasses, white paws, white socks, white tail tip, round tag, blank tag, bone tag, two tags, studded collar, collar holes, two cats, extra ear, third ear, five paws, extra fingers, mouth open, talking, busy background, watermark, text
```

---

## Шаг 2 — обучить Character / LoRA
OpenArt → Characters → Create → **train custom model / consistent character** → загрузить 5 отобранных картинок → назвать **Brain**.

## Шаг 3 — Character description (вставить при создании)
```
Brain — a cute Pixar/Disney 3D ANIMATED CARTOON orange tabby KITTEN (8-10 weeks, slender, not adult, not photorealistic). LOCKED: emerald green eyes (#3DDC84, never blue/amber); gold round glasses always on; plain brown leather collar with ONE gold HEART tag "Brain" (heart, not round/blank, no studs); ginger fur, all 4 paws ginger (no white socks), tail ginger to the tip; 2 ears, 4 paws, pink nose; mouth closed, never talks. Smart, curious, gentle — expresses through eyes/ears/whiskers.
```

## Шаг 4 — генерить сцены
В промте зови `@Brain` + сцена/поза. Ставь **stylized/Pixar + 9:16**. Локацию (нашу гостиную) и действие описываешь, Brain тянется из обученного персонажа.

## Шаг 5 — анимация
Чистая картинка → Kling/motion (или Kling 3.0 Omni). **Без голоса.** Лучше короткие клипы, мягкое движение.

---

## A/B + decision gate

| Критерий | OpenArt (обученный Brain) |
|----------|----------------------------|
| Очки каждый кадр | |
| Глаза emerald (не синие) | |
| Лапы + хвост рыжие | |
| Кулон heart «Brain» | |
| Pixar (не реализм) | |
| 9:16 | |
| Консистентность между сценами | |

- ✅ Держит всё + 9:16 → **переносим продакшен в OpenArt**, дрейф закрыт. Обновляю пайплайн в `CLAUDE.md` + style-guide (image/video модель).
- 🔴 Не держит / нет 9:16 → остаёмся на «картинки + Ken Burns».

→ Запиши результаты сюда.

## Заметки
- Обучение персонажа = разовая работа, дальше каждый ролик берёт готового Brain. Это окупает время кратно (vs война с дрейфом каждый клип).
- Эти 5 ref-картинок заодно сохрани как `assets/brain-reference-*.png` — пригодятся как anchor в любом инструменте.
