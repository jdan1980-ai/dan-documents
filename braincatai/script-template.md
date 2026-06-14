# Script Template — BrainCatAI Short

**Pipeline:** 7 scenes → image in Nano Banana 2 → animation in Veo 3 → CapCut overlays → Google Vids TTS.
**Total runtime (DEFAULT, locked 14 июн 2026):** **~33 sec** — short loop format (hook 4s + 5 beats × ~5s + CTA 4s). Each Veo clip cut to 4-5s in CapCut. Music written for ~60s but edited to loop seamlessly under ~33s. Validated by pain (12 июн) + choose-human (14 июн); niche winners run 9-30s, looping drives retention (DOESN'T Love 489%). Only go to 56s/8-scene if a topic genuinely needs the extra room — short is the default.

> ⚠️ **Before you start, read [`director-checklist.md`](./director-checklist.md)** — the master playbook with mantras, per-stage checklists, troubleshooting, and analytics-based learnings. Reading the 5 mantras (top of that file) is non-optional for every new video.

Copy this file to `scripts/<slug>.md` and fill in the fields.
Every prompt and voiceover line is in its own code block — click the copy icon and paste straight into the tool.

---

## Meta

- **Title (working):**
- **Slug:** (e.g. `why-sky-blue`)
- **Category:** Science / Biology / Math / Psychology / AI / History / Trivia
- **Series:** Cat Asks Why / What If / TIL / standalone
- **Status:** idea | script | images | animation | edited | published
- **Date created:**
- **Publish date:**

## Audience Promise — что зритель получит

Одна фраза — что зритель узнаёт или чувствует. Используем для проверки каждой сцены: помогает ли она этому обещанию?

> 

## ✍️ Правило для Voiceover

Каждая строка должна быть понятна **9-летнему И 40-летнему одновременно**. Пиши как другу за чаем рассказываешь, не как из учебника. Никакого жаргона, страшных слов, "хм/в общем/типа". Таблица замены сложных слов — в [style-guide.md §9](./style-guide.md#9-editorial-voice-writing-style).

**Двуязычный канал-стрим:** к каждой сцене делаем EN-озвучку для основного канала `@braincatai` + RU-перевод для возможного RU-зеркала (в русскоязычном сегменте кошатников больше — это потенциально вторая монетизация без новой продакшен-нагрузки).

---

## 🔒 Locked Brain Prompt (always prepend)

Paste this at the **start of every Nano Banana image prompt** to lock Brain's look. Only Brain is locked — the background is chosen per-video below.

```
Cute orange tabby kitten named Brain, big round Pixar-style eyes — each eye has a LARGE PURE WHITE sclera (white of the eye clearly visible all around) surrounding a medium round EMERALD-GREEN iris (#3DDC84) with a black pupil in the center; ONLY the small iris is colored green, the white of the eye stays pure white, NEVER a fully-green eyeball, NEVER green sclera (iris NOT brown, NOT amber, NOT yellow, NOT hazel), small thin round gold-framed glasses (ALWAYS on, every shot), a plain smooth brown leather collar (smooth band, NO studs, NO spikes, NO metal plates, NO front buckle) with EXACTLY ONE gold HEART-SHAPED tag engraved "Brain" (heart shape — NOT round, NOT blank; identical every scene), soft fluffy orange fur with darker tabby stripes, ALL 4 PAWS — both FRONT and both BACK — the SAME orange ginger tabby color as the body (NO white paws, NO white socks, NO white mittens, NO white toes, NO white BACK paws), tail orange ginger tabby to the very tip (NO white tail tip), pink nose, long white whiskers, Pixar/Disney 3D ANIMATED CARTOON style (stylized smooth cartoon shading, big cartoon eyes — like a Pixar movie frame, NOT photorealistic, NOT a real cat, NOT realistic fur), soft cartoon lighting, vertical 9:16 composition.
```

> ⚠️ **Eye color trap:** Warm lighting often pushes the AI to render brown/amber eyes even though "green" is in the prompt. Always include the hex `#3DDC84`, repeat the emerald-green note in per-shot descriptions, and add the `EYE COLOR RULE (strict)` block in Veo 3 prompts.

**Negative prompts (Nano Banana):**

```
2D, flat, anime, cel-shaded, photorealistic cat, realistic cat, real cat, photoreal, hyperrealistic, realistic fur, photograph, live action, lifelike, 3D realism, multiple cats, low quality, blurry, distorted face, extra limbs, extra paws, five legs, six legs, both front paws raised, two paws raised together, white paws, white socks, white mittens, white toes, white feet, white-tipped paws, white back paws, white hind paws, white back feet, white socks on back legs, white tail tip, white-tipped tail, round tag, circular tag, blank tag, bone-shaped tag, two tags, studded collar, spiked collar, collar with holes, collar buckle, missing glasses, no glasses, missing collar, missing heart tag, watermark, text in image, logo, ugly, scary, aggressive expression, mouth open as if talking, lip-sync, talking cat, mouth movement, chattering, brown eyes, amber eyes, yellow eyes, hazel eyes, golden eyes, dark eyes, brown iris, amber iris, wrong eye color, eye color tinted by lighting, warm-tinted eyes, green sclera, green eye-whites, fully green eyes, green-tinted eyeballs, whole eye green
```

## ⚠️ Veo 3 animation rules — anti-drift (вставлять в каждый animation-промт)

> 🛠️ Усилено 21 мая 2026 после регресса Veo (после молчаливого апдейта 10-кредитной версии): очки пропадали, глаза синели, появлялся второй кот, уход в реализм. Эти правила бьют точечно по тем сбоям. Канонический блок — в [`style-guide.md`](./style-guide.md).

Every `🎬 Animation prompt` block must include these strict rule blocks before STYLE:

```
EYE COLOR RULE (strict): Each eye is a LARGE PURE WHITE sclera (white of the eye clearly visible all around) with a medium round EMERALD-GREEN iris (#3DDC84) and a black pupil in the center. ONLY the small iris is green — the white of the eye/sclera stays PURE WHITE, NEVER tinted green, NEVER a fully-green eyeball. Iris NEVER brown, NEVER amber, NEVER yellow, NEVER hazel, NEVER BLUE, NEVER CYAN, NEVER grey. Warm OR cool lighting must NOT tint the iris or sclera. Stays emerald green even half-closed or dilated.

GLASSES RULE (strict): Brain ALWAYS wears his small round gold-framed glasses — they stay ON his face the entire clip. NEVER remove the glasses, NEVER let them fade out, NEVER animate them off his face.

SINGLE-CHARACTER RULE (strict): EXACTLY ONE cat in frame at all times — Brain. NEVER add a second cat, NEVER spawn another kitten, NEVER add a wild cat or any other animal. If a hologram appears it is a GLOWING TRANSLUCENT BLUE hologram (clearly see-through, NOT a real solid cat). Only Brain is a real solid cat.

STYLE RULE (strict): Pixar 3D animated CARTOON style throughout — NEVER photorealistic, NEVER a real/photographic cat, NEVER documentary realism. Brain's identity stays IDENTICAL to the input image.

ANATOMY RULE (strict): Brain has exactly 4 paws — 2 front, 2 back — AND exactly 2 EARS (NO third ear, NO phantom ear, NO ear-shaped artifact). Body stays slender 8-week-old kitten proportions — NEVER morphing chubby. Keep the brown collar with the gold heart tag visible.

MOUTH RULE (strict): Mouth stays closed throughout, no lip-sync, no talking motion. Expressions through eyes, ears, whiskers, and body. (State any exception explicitly, e.g. a single soft meow/yawn.)

MOTION RULE (strict — anti-drift): Keep motion modest and controlled. ONLY the described action moves; the character's look stays locked. Large/fast motion increases drift — prefer a subtle camera push-in plus contained action. If a beat needs big motion, split it and keep each clip ≤5 seconds.
```

Exceptions to MOUTH RULE (state explicitly when used): brief held jaw-drop for shock, single yawn, one soft meow on CTA.

---

## 🏠 Локации (Scene Settings — залочить для ЭТОГО видео)

Берём 1–3 локации максимум на видео. Каждая = единый описательный параграф, **вставляется дословно** в каждую сцену которая её использует. CTA-сцена (Scene 8) должна быть в одной из этих локаций — никогда generic outro-фон. См. [style-guide.md §8b](./style-guide.md#8b-scene-continuity-per-video-world-locks).

### Location A — `INT. / EXT. NAME — TIME OF DAY`

```

```

### Location B — `INT. / EXT. NAME — TIME OF DAY` (delete if not used)

```

```

### Location C — `INT. / EXT. NAME — TIME OF DAY` (delete if not used)

```

```

### Scene → location map

| Scene | Location | Notes |
|-------|----------|-------|
| 1 | A | |
| 2 | A | |
| 3 | | |
| 4 | | |
| 5 | | |
| 6 | | |
| 7 | | |
| 8 (CTA) | **must match one above** | |

---

## Полный VO (целиком на всё видео — для общего обзора)

Целевой объём **80–120 слов EN** ≈ 50 сек при 130 wpm. RU должен влезать в те же тайминги (русский короче по слогам — обычно влезает).

**🇬🇧 English (основной канал @braincatai):**

```

```

**🇷🇺 Русская версия (для возможного RU-зеркала канала):**

```

```

---

# 🖼️ ТУМБНЕЙЛ ПЕРВЫМ — STOP, сделай обложку ДО генерации сцен

> ⛔ **Не начинай генерить сцены, пока не готова обложка.** Это правило стоит здесь, прямо перед сценами, специально — чтобы про тумбу не забыть (раньше она была в конце файла и терялась).
>
> 1. Заполни концепт + промт в секции **`## 🖼️ ТУМБНЕЙЛ`** ниже (SEO Pack).
> 2. Сгенерь её СНАЧАЛА. Free generation → гоняй до идеала, эмоция лица = главный CTR-рычаг.
> 3. Только потом приступай к Scene 1.

---

# Scenes

---

## Scene 1 — HOOK (0–7 sec)

**Что зритель видит:** перехватить внимание за первые 2 секунды. Контр-интуитивное или шокирующее утверждение. Визуальный удар идёт ДО слов.
**Локация:** A / B / C (выбрать из карты выше)

**🎨 Image-промт для Nano Banana** (копи-паст в Nano Banana как промт сцены):

> Format: `[Locked Brain prompt] + [exact location block from above] + [per-shot action]`

```

```

**🎬 Animation-промт для Veo 3** (копи-паст в Veo 3 чтобы оживить картинку из Nano Banana):

```
Camera motion + Brain's action + facial expression + duration ~7s
```

**🎙️ Voiceover для этой сцены** (озвучка через Google Vids TTS):

🇬🇧 EN:
```

```

🇷🇺 RU:
```

```

---

## Scene 2 — Curiosity gap (7–14 sec)

**Что зритель видит:** пообещать ответ, заставить смотреть дальше. Curiosity-gap — viewer должен почувствовать что НЕ узнать ответ нельзя.

**🎨 Image-промт для Nano Banana** (копи-паст в Nano Banana как промт сцены):

```

```

**🎬 Animation-промт для Veo 3** (копи-паст в Veo 3 чтобы оживить картинку из Nano Banana):

```

```

**🎙️ Voiceover для этой сцены** (озвучка через Google Vids TTS):

🇬🇧 EN:
```

```

🇷🇺 RU:
```

```

---

## Scene 3 — Setup (14–21 sec)

**Что зритель видит:** ввести концепт / контекст. Часто здесь scientist-Brain в лабе с диаграммой — даёт авторитет утверждению.

**🎨 Image-промт для Nano Banana** (копи-паст в Nano Banana как промт сцены):

```

```

**🎬 Animation-промт для Veo 3** (копи-паст в Veo 3 чтобы оживить картинку из Nano Banana):

```

```

**🎙️ Voiceover для этой сцены** (озвучка через Google Vids TTS):

🇬🇧 EN:
```

```

🇷🇺 RU:
```

```

---

## Scene 4 — Build-up (21–28 sec)

**Что зритель видит:** добавить первую часть объяснения. Часто extreme close-up на детали (ухо, глаз, лапа) — визуально иллюстрирует механизм.

**🎨 Image-промт для Nano Banana** (копи-паст в Nano Banana как промт сцены):

```

```

**🎬 Animation-промт для Veo 3** (копи-паст в Veo 3 чтобы оживить картинку из Nano Banana):

```

```

**🎙️ Voiceover для этой сцены** (озвучка через Google Vids TTS):

🇬🇧 EN:
```

```

🇷🇺 RU:
```

```

---

## Scene 5 — Core explanation (28–35 sec)

**Что зритель видит:** доставить ключевое озарение визуально. Triptych / диаграмма / split-screen — то ради чего зритель и пришёл.

**🎨 Image-промт для Nano Banana** (копи-паст в Nano Banana как промт сцены):

```

```

**🎬 Animation-промт для Veo 3** (копи-паст в Veo 3 чтобы оживить картинку из Nano Banana):

```

```

**🎙️ Voiceover для этой сцены** (озвучка через Google Vids TTS):

🇬🇧 EN:
```

```

🇷🇺 RU:
```

```

---

## Scene 6 — Twist / aha moment (35–42 sec)

**Что зритель видит:** "вау"-пэйофф. Pattern interrupt — slo-mo, dramatic zoom, или Brain в реакции jaw-drop / dilated eyes. Эмоциональный пик видео.

**🎨 Image-промт для Nano Banana** (копи-паст в Nano Banana как промт сцены):

```

```

**🎬 Animation-промт для Veo 3** (копи-паст в Veo 3 чтобы оживить картинку из Nano Banana):

```

```

**🎙️ Voiceover для этой сцены** (озвучка через Google Vids TTS):

🇬🇧 EN:
```

```

🇷🇺 RU:
```

```

---

## Scene 7 — Bonus fact / contrast (42–49 sec)

**Что зритель видит:** один дополнительный удивительный факт усиливающий тему. Контраст / bonus / эволюционный или биологический "why" в виде thought-bubble или contemplative pose.

**🎨 Image-промт для Nano Banana** (копи-паст в Nano Banana как промт сцены):

```

```

**🎬 Animation-промт для Veo 3** (копи-паст в Veo 3 чтобы оживить картинку из Nano Banana):

```

```

**🎙️ Voiceover для этой сцены** (озвучка через Google Vids TTS):

🇬🇧 EN:
```

```

🇷🇺 RU:
```

```

---

## Scene 8 — CTA / outro (49–56 sec)

**Что зритель видит:** подмигивание в камеру, CTA на подписку. ≤ 6 сек. Обычно используется универсальный Sc 8 клип (slow blink + meow) — генерится один раз и переиспользуется.

> **End card:** after Scene 8, append the reusable Brain end card (Thanks For Watching + Like + Subscribe). See [end-card.md](./end-card.md) for the prompts. Use **Short variant (3 sec)** by default to keep total runtime under 60 sec.

**🎨 Image-промт для Nano Banana** (копи-паст в Nano Banana как промт сцены):

```

```

**🎬 Animation-промт для Veo 3** (копи-паст в Veo 3 чтобы оживить картинку из Nano Banana):

```

```

**🎙️ Voiceover для этой сцены** (озвучка через Google Vids TTS):

🇬🇧 EN:
```

```

🇷🇺 RU:
```

```

---

## 🎵 Промт для музыки (Suno / Udio / Mubert)

**Логика трека** — опиши как музыка должна развиваться по таймлайну: открытие → нарастание → пэйофф → resolve. Это даст Suno чёткую структуру вместо плоского лупа.

> ⏱️ **Правило (locked 28 мая 2026): промт пишем на 1 минуту (~60s), НЕ 56s** — буфер, чтобы трек покрыл всё видео + энд-карту и не оборвался. Тайм-коды растягиваем до ~60s (напр. close 52-60s).

**Полный промт** (копи-паст в Suno, английский — модель лучше понимает EN):

```

```

**Альт-промт** (если Suno просит покороче):

```

```

## Сборка в Google Vids

1. Загрузить все 8 анимированных клипов по порядку (Scene 1 → Scene 8)
2. Добавить VO-трек из TTS (один цельный файл проще — но при нужде делить под клипы)
3. Музыка на -18 LUFS, голос на -12 LUFS (~6 dB голос над музыкой)
4. Burn-in субтитры, верхняя треть, максимум 4 слова на экране за раз
5. Добавить SFX-cues по заметкам монтажа ниже

## Заметки по монтажу — общие

- Резать сцены хард-cut'ами или whip-pan'ами
- Burn-in субтитры (макс 4 слова за раз, верхняя треть)
- Голос -12 LUFS, музыка -18 LUFS
- SFX: whoosh на переходах, ding на момент-озарение, meow на CTA

## SEO Pack (для загрузки на YouTube — копи-паст)

> **Правила vidIQ-оптимизации (целимся в 80+/100):**
> - **Title:** 40–70 символов, главный ключ внутри (`cat psychology` для этого канала всегда), через `|` ниша-тег, заканчиваем 🐱. **БЕЗ хэштегов в title по правилу Карены — они убивают retention Shorts.**
> - **Description:** ≥ 250 символов, главный ключ повторить 2–3 раза, включить 5+ supporting keywords, emoji, в конце блок хэштегов + CTA на подписку
> - **Tags:** 20–25 тегов, микс broad (1 слово) + medium (2 слова) + long-tail (3–5 слов), заполнять до 500 символов
> - Всегда базовый набор: `cat psychology, cat facts, cat behavior, brain cat, did you know, mind blowing facts`
> - Обязательные channel-wide (Карена): `braincatai, cat facts mind blowing, cat behavior explained`

**Финальный title** (40–70 символов, заканчивается `🐱 | Cat Psychology`):

```

```

**Hashtags for title bar** (top 3 — paste at the end of the title field, `#shorts` always first):

```
#shorts #catpsychology #catfacts
```

Альт-титлы для A/B-теста:

```


```

**Description** (≥ 250 символов, главный ключ повторить 2–3×, копи-паст в YouTube):

```


🐱 Follow Brain for more cat psychology, cat facts, and cat secrets every week.

#shorts #catpsychology #catfacts #catbehavior #braincatai #didyouknow #petfacts
```

**Tags** (через запятую в поле тегов YouTube — базовый набор + 5–10 видео-специфичных):

Базовый набор (всегда включать):

```
cat psychology, cat facts, cat behavior, cat secrets, cat science, cat communication, cat body language, feline behavior, understanding cats, facts about cats, animal facts, animal science, did you know, mind blowing facts, brain cat, cat facts daily, cat behavior funny, cat domestication, cats vs humans
```

Video-specific (5–10 long-tail тегов под именно это видео):

```

```

**Расширенный набор хэштегов** (только в тело описания — НИКОГДА в title по правилу Карены):

```
#shorts #catpsychology #catfacts #catbehavior #braincatai #didyouknow #petfacts
```

---

## 🖼️ ТУМБНЕЙЛ (ОБЯЗАТЕЛЬНО — отдельная секция в каждом скрипте)

> **Правило (locked 28 мая 2026, обновлено 7 июн 2026):** тумбнейл-промт ВСЕГДА живёт в собственной видной секции `## 🖼️ ТУМБНЕЙЛ` — НЕ закопан внутри SEO Pack. **И генерируется ПЕРВЫМ — до сцен** (см. якорь «🖼️ ТУМБНЕЙЛ ПЕРВЫМ» перед `# Scenes`). Применяет «5 Signs» формулу (текущий лучший CTR): крупный план лица 60% + dilated глаза в зрителя + ОДИН hook-объект + желтая плита + короткий броский текст (≤3-4 слова/строка) + emoji.

**Концепт тумбнейла (1 строкой):**

> 

**🖼️ Промт для тумбнейла** (Nano Banana 2 — применяет **«5 Signs» формулу** = текущий лучший CTR на канале):

> **Формула 5 Signs (locked 27 мая 2026):** лицо 60% кадра + dilated emerald глаза в зрителя + ОДИН видимый hook-объект + желтая plate (2 строки caps) + emoji-маркер эмоции + слабый tilt 2-4°. Эмоция меняется под тему (cold/awe/wow/confused/warm-smug), всё остальное — постоянно.

```
EXTREME CLOSE-UP of cute Pixar/Disney 3D ANIMATED CARTOON orange tabby kitten Brain — face fills ~60% of frame, slight 2-4° tilt for energy. Big round Pixar-style eyes — each eye has a LARGE PURE WHITE sclera (white of the eye clearly visible all around) surrounding a medium round EMERALD-GREEN iris (#3DDC84) with a black pupil; ONLY the small iris is green, the white of the eye stays pure white, NEVER a fully-green eyeball, NEVER green sclera. EYES WIDE AND DILATED locked DIRECTLY into the viewer with [EMOTION — pick one: COLD INTENSE GLARE / WIDE AWE / SHOCKED "WHAT?!" / SMUG KNOWING / WARM LOVING SLOW-BLINK]. Ears [POSE — pick one: perked sharply UP and forward / slammed flat backward / relaxed neutral]. Mouth closed in [tense flat line / soft smile / confused frown]. Small thin round gold-framed glasses ALWAYS on. Plain smooth brown leather collar with EXACTLY ONE gold HEART-SHAPED tag engraved "Brain". Soft fluffy orange tabby fur with darker stripes, ALL 4 paws ginger (NO white socks), tail ginger to the tip, EXACTLY 2 ears, EXACTLY 4 paws. Pixar/Disney 3D ANIMATED CARTOON style (stylized smooth cartoon shading, NOT photorealistic, NOT a real cat). Vertical 9:16.

HOOK ELEMENT (~20-25% of frame, lower-RIGHT or upper-LEFT, NOT covering face): [ONE concrete object that visualizes the hook — e.g. broken TV showing strobe / human hand recoiling / giant number "38" / cartoon thought-bubble / glowing icon / sparking lightbulb]. The hook element should READ in 0.5s at thumbnail size.

BACKGROUND: cozy living room HEAVILY BLURRED with warm honey-amber bokeh (sage rug + cream armchair faintly visible but heavy DOF). Brain is rim-lit so he POPS off the background. High contrast.

TEXT PLATE (BIG and BOLD, positioned in the LOWER-MIDDLE of the frame at roughly 55-70% height — raised well CLEAR of the very bottom edge so it is NOT cut off by the phone UI / duration badge. Text is LARGE, filling ~85-90% of the frame width, easily readable on a small phone screen. 2 lines, ALL CAPS, slight 2-3° tilt, BOLD ROUNDED GEOMETRIC SANS-SERIF Fredoka One / Nunito Bold, Electric Yellow #FFD23F fill, solid charcoal #2B2B2B outline 6px, soft black drop-shadow). Lines:
LINE 1: "[HOOK WORD / NUMBER]"
LINE 2: "[PAYOFF + EMOJI 💔/🤯/💚/❓]"

TYPOGRAPHY LOCK (strict — same font on every BrainCatAI thumbnail): single font family, soft rounded terminals, NO serifs, NO brush-script, NO Comic Sans, NO Papyrus, NO Impact.

EYE COLOR RULE (strict): Each eye = LARGE PURE WHITE sclera with medium round EMERALD-GREEN iris (#3DDC84) and black pupil — only the small iris is green, sclera stays pure white, NEVER a fully-green eyeball, NEVER green sclera.
ANATOMY RULE (strict): EXACTLY 4 paws AND EXACTLY 2 EARS. NO 5th paw, NO phantom 3rd ear, NO extra fur tuft.
STYLE RULE (strict): Pixar/Disney 3D ANIMATED CARTOON. NOT photorealistic, NOT a real cat.
LANGUAGE RULE (strict): All on-screen text in ENGLISH only. NO Russian text, NO Cyrillic.
```

> **Шпаргалка по эмоции под тип темы:**
> - **Негатив-зеркало** (Signs You're Not Loved, 5 Worst Things You Do) → COLD INTENSE GLARE + ears flat back + 💔
> - **Mind-blow факт** (Oldest Cat, TV Broken) → SHOCKED "WHAT?!" wide eyes + ears UP + 🤯
> - **Predator/record** (Killing Machine) → SMUG KNOWING + ears UP + small fang/shadow hook
> - **Тёплый reveal** (Stretch = Trust) → WARM LOVING SLOW-BLINK + ears relaxed + 💚
> - **Спук/загадка** (Stares at Nothing) → WIDE STARING OFF-FRAME + dilated pupils + ❓

**Negative prompts (Nano Banana — thumbnail):**

```
2D flat, anime, photorealistic cat, real cat, photoreal, hyperrealistic, multiple cats, second cat, low quality, blurry, cluttered background, busy background, distorted face, extra limbs, extra paws, five legs, three ears, extra ear, phantom ear, missing glasses, missing collar, missing heart tag, brown eyes, amber eyes, yellow eyes, hazel eyes, green sclera, green eye-whites, fully green eyes, green-tinted eyeballs, white paws, white socks, white tail tip, round tag, blank tag, mouth open as if talking, talking cat, serif font, hand-drawn text, brush-script font, Comic Sans, Papyrus, Impact font, gradient text, neon text, metallic text, multiple fonts, mixed typography, sharp serifs on text, calligraphy, Russian text, Cyrillic letters, ugly, scary, watermark, logo
```

---

## 📌 Закрепляемый комментарий (Pinned comment)

Постится от имени канала под видео сразу после публикации → ⋮ → Pin. Отвечать на первые 10-20 ответов в первый час чтобы удвоить engagement. Каждый закреп заканчивается вопросом / эмодзи-кнопкой / интерактивом который легко ответить с телефона. **Также добавить в [`pinned-comments.md`](../pinned-comments.md)** как очередную пронумерованную запись.

🇬🇧 EN:
```

```

🇷🇺 RU (для RU-зеркала):
```

```

---

## Метрики после публикации

| Метрика | 48ч | 7 дней | 30 дней |
|---------|-----|--------|---------|
| Просмотры |   |        |         |
| Средняя продолжительность просмотра |  |  |  |
| Retention % |   |        |         |
| Лайки |       |        |         |
| Шеры |        |        |         |
| Комментарии | |        |         |
| Подписчики прибавилось | |     |    |

### Заметки — что сработало / что нет
