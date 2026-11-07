# Видео 3 — «Сон на боку» (Nano Banana)

Поза №3 в цикле канала: сидит (видео 1) → на спине (видео 2) → **на боку (видео 3)**.
Референс конкурента: Healing Quiet Tonight WR4HK9XB7IU (1.37M, поза на боку) + b5RWjJgxKGc (501K, цветная волна).

## 16:9 (основная — видео, луп, обложка)

```
Cinematic digital art, 16:9. A translucent glass-like human body sleeping peacefully on its side in deep space, knees slightly bent, one hand resting under the cheek, head on a soft dark-blue glowing cloud pillow. The body is semi-transparent pale blue with a softly glowing outline; inside it a luminous golden spine and fine golden nerve network are visible, the brain glows warm gold. Seven glowing chakra orbs along the spine from tailbone to crown: red, orange, yellow, green, sky blue, indigo, violet, each with a soft halo. Above the body flows one smooth silky ribbon wave made of the same seven chakra colors, red on the left fading through to violet on the right, like a gentle sound wave. Faint concentric golden rings radiate from the heart area. Background: deep navy starfield with subtle blue nebula, calm and dark. Figure placed in the lower-right two thirds of the frame, the upper-left area kept dark and empty. Serene, dreamy, soft glow, high detail, no text, no letters, no logo, no watermark, no extra limbs, anatomically correct hands and feet.
```

## 9:16 (Shorts / вертикальная версия)

```
Cinematic digital art, vertical 9:16. A translucent glass-like human body sleeping peacefully on its side, curled slightly, head on a soft dark-blue glowing cloud pillow, seen from a gentle three-quarter angle so the whole body fits in the lower half of the frame. Semi-transparent pale blue body with glowing outline, luminous golden spine and nerve network, warm golden glowing brain. Seven glowing chakra orbs along the spine: red, orange, yellow, green, sky blue, indigo, violet. Above the body a smooth silky ribbon wave of the seven chakra colors rises upward in a gentle S-curve. Faint golden concentric rings from the heart. Deep navy starfield with subtle blue nebula. Upper third of the frame dark and empty. Serene, dreamy, soft glow, high detail, no text, no letters, no logo, no watermark, no extra limbs, anatomically correct hands and feet.
```

## Если что-то пошло не так (доп. фразы в конец промпта)

| Проблема | Добавить |
|---|---|
| Тело лежит на спине | `strictly lying on the side, side view, fetal-like relaxed pose` |
| Волна радугой-аркой | `the ribbon is a horizontal flowing wave, not a rainbow arc` |
| Цвета чакр перепутаны | `chakra order from bottom of spine to top of head: red, orange, yellow, green, blue, indigo, violet` |
| Слишком ярко / пёстро | `low-key lighting, mostly dark image, glow only on body, chakras and ribbon` |
| Лишние пальцы/руки | `exactly two arms, two legs, five fingers per hand` |
| Фигура в центре, текст некуда | `subject in the lower right, empty dark space in the upper left for a title` |

## Дальше
1. Положить картинку в `sevenlights/visuals/base_side_sleep.png` (или прислать в чат).
2. Обложка: `python tools/make_thumb.py --image visuals/base_side_sleep.png --hz "..." --out visuals/thumbs/thumb_video03.jpg`.
3. Луп 8 с: `make_loop.py` с новыми координатами чакр (снимаю по картинке) + анимация волны.
