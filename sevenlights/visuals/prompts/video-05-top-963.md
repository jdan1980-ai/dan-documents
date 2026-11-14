# Видео 5 — «963 Hz: Spiritual Awakening» (Nano Banana)

Поза №5 в цикле канала: сидит (1) → на спине (2) → на боку (3) → на животе (4) → **вид сверху, голова к зрителю (5)**.
Референс конкурента: Healing Quiet Tonight b5RWjJgxKGc (501K, вид сверху, над телом световая волна).
Акцент: фиолетовая коронная чакра над головой — самая яркая, от неё вверх в космос уходит мягкий луч / ореол.

## 16:9 (основная — видео, луп, обложка)

```
Cinematic digital art, 16:9. View from above and slightly behind the head: a translucent glass-like male human body lying peacefully on its back in deep space, the top of the head closest to the viewer in the lower right of the frame, the body stretching away diagonally toward the upper middle, arms relaxed at the sides, resting on a soft dark-blue glowing cloud. The body is semi-transparent pale blue with a softly glowing outline; a luminous golden spine and fine golden nerve network shine through, the brain glows warm gold. Exactly seven glowing chakra orbs along the center line of the body: red at the pelvis, orange, yellow, green at the heart, sky blue at the throat, indigo at the forehead, and violet just above the top of the head. The violet crown chakra is the brightest, with a soft violet-white halo and a gentle beam of light rising from it into the cosmos. Faint concentric golden rings around the body. Background: deep navy starfield with soft violet and blue nebula clouds and a distant galaxy, calm and dark. Upper-left area dark and empty for a title. Serene, spiritual, soft glow, high detail, no text, no letters, no logo, no watermark, no extra limbs, anatomically correct hands and feet.
```

## 9:16 (Shorts / вертикальная версия)

```
Cinematic digital art, vertical 9:16. View from directly above: a translucent glass-like male human body lying peacefully on its back in deep space, head at the bottom of the frame closest to the viewer, body stretching upward, arms relaxed at the sides, on a soft dark-blue glowing cloud. Semi-transparent pale blue body with glowing outline, luminous golden spine and nerve network, warm golden glowing brain. Exactly seven glowing chakra orbs along the center line: red, orange, yellow, green, sky blue, indigo, violet. The violet crown chakra above the head is the brightest, with a soft violet-white halo and a gentle beam of light. Deep navy starfield with violet nebula. Upper third dark and empty. Serene, spiritual, soft glow, high detail, no text, no letters, no logo, no watermark, no extra limbs, anatomically correct hands and feet.
```

## Вариант v2 — фигура по центру (просьба пользователя 14.11.2026)

Первая картинка: 7 чакр и луч хорошие, но фигура в правом углу и тело перекручено. Новый промпт (заново, не правка):

```
Cinematic digital art, 16:9. Symmetrical top-down view from directly above: a translucent glass-like male human body lying peacefully and naturally flat on its back in deep space, perfectly centered in the frame, the head at the bottom center closest to the viewer, the body stretching straight up toward the top center, legs straight and together, arms relaxed along the sides, palms up. The whole figure fits in the middle and lower part of the frame, with dark empty space at the top for a title. Semi-transparent pale blue male body (broad shoulders, straight torso, short hair) with a softly glowing outline; a straight luminous golden spine runs exactly under the center line, fine golden nerve network, warm golden glowing brain. Exactly seven glowing chakra orbs on the center line of the body: red at the pelvis, orange, yellow, green at the heart, sky blue at the throat, indigo at the forehead, violet just beyond the top of the head. The violet crown chakra is the brightest with a soft violet-white halo and a gentle beam of light. Faint concentric golden rings centered on the heart. The body rests on soft violet-blue glowing clouds; deep navy starfield with violet nebula and a distant galaxy. Calm, serene, spiritual, soft glow, high detail, no text, no letters, no logo, no watermark, no extra limbs, anatomically correct hands and feet.
```

## Если что-то пошло не так (доп. фразы в конец промпта)

| Проблема | Добавить |
|---|---|
| Чакр больше или меньше 7 | `exactly 7 chakra orbs, no more, no less: red, orange, yellow, green, blue, indigo, violet` |
| Обычный вид сбоку | `strictly a top-down view from above the head, the head nearest to the camera` |
| Женская фигура | `clearly male body: broad shoulders, straight torso, narrow hips, short hair` |
| Луч слишком яркий, режет глаза | `the crown light is soft and gentle, not a laser, calm violet glow` |
| Мало космоса | `rich cosmos: soft violet nebula, distant spiral galaxy, dense stars` |
| Фигура в центре, тексту некуда | `subject on the right half, empty dark space in the upper left for a title` |

Правило: пересчитать чакры — ровно 7. Скачивать оригинал (⋮ → Download), не скриншот.

## Дальше
1. Картинка → `sevenlights/visuals/base_top_963.jpg`.
2. Обложка: `python tools/make_thumb.py --image visuals/base_top_963.jpg --hz "963 HZ" --sub "SPIRITUAL AWAKENING" --out visuals/thumbs/thumb_963_awakening.jpg`.
3. Луп 8 с: `make_loop.py` с координатами чакр (снимаю по картинке).
