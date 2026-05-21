# Google Flow — `@Brain` Character setup + direct-gen тест

**Цель:** проверить можно ли генерить видео НАПРЯМУЮ (text→video) через Flow-агента с сохранённым персонажем `@Brain`, минуя шаг Nano Banana (картинка→видео). Если консистентность держится — экономим целый шаг продакшена.

> ⚠️ **Это эксперимент, пайплайн пока НЕ меняем.** Сначала A/B-тест на одной сцене (ниже). Меняем `CLAUDE.md` / `director-checklist.md` / `style-guide.md` только если `@Brain` держит строгий спек.

> 🚨 **НЕ включать у Brain «character voice / talking dialogue» Veo 3.1.** У нас locked-правило: рот закрыт, без lip-sync. Озвучка ВСЕГДА отдельно через Google Vids TTS. Native-audio Veo можно использовать только для эмбиента/SFX, не для речи кота.

---

## Шаг A — создать канонический референс Brain (один раз)

Сначала сгенерь ОДИН чистый эталонный кадр Brain в Nano Banana — нейтральная поза, все черты видны. Он станет image-якорем для `@Brain` (image-якорь надёжнее текста).

**Nano Banana — character-sheet референс:**

```
Character reference sheet of a cute orange tabby kitten named Brain. Centered, facing camera in a neutral friendly seated pose, full body visible, even soft studio lighting, plain light neutral background. 8-10 week old kitten, NOT adult, NOT chubby, NOT pudgy — slender petite kitten body with small chest, slim torso, delicate proportions, small paws. Big round sparkling VIVID EMERALD GREEN eyes (bright pure emerald green iris #3DDC84 — NOT brown, NOT amber, NOT yellow, NOT hazel, NOT golden). Small thin round gold-framed glasses. Brown leather collar with a gold heart-shaped tag engraved "Brain". Soft fluffy orange fur with darker tabby stripes, pink nose, long white whiskers. EXACTLY 2 EARS (one left, one right — both pointed perky triangle kitten ears, perfectly symmetric, NO third ear, NO extra fur tuft, NO ear-shaped artifact on head). EXACTLY 4 paws (2 front + 2 back). Mouth closed, soft friendly expression. Pixar 3D render style, clean, 4K, sharp focus on the character.
```

Negative:
```
multiple cats, extra limbs, extra paws, five legs, three ears, extra ear, phantom ear, missing glasses, missing collar, missing heart tag, brown eyes, amber eyes, yellow eyes, hazel eyes, mouth open, talking, blurry, distorted, watermark, text overlay, logo
```

→ Выбери самый чистый результат (правильные глаза/уши/лапы/очки/ошейник). Сохрани как `assets/brain-character-reference.png`.

---

## Шаг B — создать персонажа `@Brain` в Flow

1. Flow → раздел **Characters / Ingredients** → New Character
2. Загрузить `assets/brain-character-reference.png` как визуальный якорь
3. В описание персонажа вставить (текстовый якорь):

```
Brain — a cute Pixar-style orange tabby KITTEN (8-10 weeks old, slender petite kitten proportions, NOT adult, NOT chubby). Signature locked features that must NEVER change: big round VIVID EMERALD GREEN eyes (iris #3DDC84, never brown/amber/yellow/hazel), small thin round gold-framed glasses, brown leather collar with a gold heart-shaped tag reading "Brain", soft fluffy orange tabby fur with darker stripes, pink nose, long white whiskers, EXACTLY 2 symmetric pointed kitten ears (never a third ear), EXACTLY 4 paws. Mouth stays closed (no talking, no lip-sync). Pixar 3D render style.
```

4. Сохранить. Теперь в любом промте можно звать его `@Brain`.

---

## Шаг C — direct-gen тест-промт (одна сцена)

**Тестируем на:** `why-cats-stretch-at-you` Сцена 1 (приветственное потягивание) — полный кадр Brain + движение + чёткая видимость черт = честный тест консистентности. Это безопасное видео (24 мая), не рискованный killer-прыжок.

**Flow text→video промт (вставить с `@Brain`):**

```
@Brain in a cozy modern living room — cream walls, warm honey-amber wooden floor, a sage-green rug, a cream linen armchair on the right, a tall window with sheer curtains in the background, soft warm afternoon daylight. Medium shot, side 3/4 view, gentle slow push-in over 7 seconds.

Action: @Brain notices his owner entering off-frame to the upper-right, ears perk happily, then flows into a big luxurious GREETING STRETCH — front legs reach far forward and low, chest dips toward the floor, hindquarters rise high, back arches in a deep satisfying stretch, tail curving up. He holds the stretch a beat, then eases up and looks warmly up toward the owner with happy emerald eyes and a content tail sway.

STRICT RULES (must hold the entire clip):
- Eyes BRIGHT EMERALD GREEN #3DDC84 throughout — never brown/amber/yellow. Warm light must not tint the iris.
- EXACTLY 2 ears (never a third/phantom ear), ear shape stays small kitten triangles even during the stretch.
- EXACTLY 4 paws, never a 5th paw, never an extra limb during the stretch motion.
- Body stays slender 8-week kitten proportions even arched in the stretch — never morphs chubby or unnaturally long.
- Keep glasses, brown collar + gold heart tag visible.
- Mouth stays CLOSED (a tiny soft yawn at the stretch peak is OK) — NO talking, NO lip-sync, NO dialogue audio.
Pixar 3D render style, cinematic warm daylight, vertical 9:16, soft depth of field. 7 seconds.
```

---

## Шаг D — A/B сравнение + решение

Сгенери ту же Сцену 1 двумя способами:
- **(старый)** Nano Banana картинка → Veo image-to-video (как в скрипте `why-cats-stretch-at-you.md`)
- **(новый)** этот direct-gen промт через `@Brain`

**Сравни по чек-листу:**

| Критерий | Старый (img→vid) | Новый (@Brain direct) |
|----------|------------------|------------------------|
| Глаза emerald #3DDC84 (не амбер) | | |
| Ровно 2 уха (нет фантомного) | | |
| Ровно 4 лапы в движении | | |
| Очки + ошейник + heart-tag на месте | | |
| Пропорции котёнка (не растолстел) | | |
| Рот закрыт (нет lip-sync) | | |
| Качество движения потягивания | | |
| Сколько ретраев до годного | | |
| Цена (credits) | | |

**Decision gate:**
- ✅ Если `@Brain` держит ВСЕ строгие пункты за ≤2 попытки → переходим на direct-gen, картинку оставляем fallback для рискованных сцен (killer-прыжок). Обновляю пайплайн в `CLAUDE.md` + `director-checklist.md` + `style-guide.md`.
- 🟡 Если держит частично (напр. иногда фантомное ухо) → гибрид: direct-gen для простых сцен, картинка-чекпоинт для близких/экшн-планов.
- 🔴 Если стабильно дрейфит → остаёмся на img→vid (дешёвый QA-чекпоинт важнее экономии шага).

→ Запиши результаты сравнения сюда, чтобы решение было задокументировано.

---

## Заметки

- Image-якорь (`brain-character-reference.png`) почти всегда даёт лучшую консистентность чем только текст — обязательно грузи картинку в Character, не только описание.
- Если Flow-агент позволяет тянуть несколько ассетов в один запрос — можно добавить и `brain-character-reference.png`, и `owner-reference.png` (для сцен с рукой хозяйки) одновременно.
- Directional-правило остаётся: если сцена требует движения в сторону (прыжок/подкрадывание), описывай направление прямо в text-промте (преимущество direct-gen — не надо пред-ориентировать входную картинку).
