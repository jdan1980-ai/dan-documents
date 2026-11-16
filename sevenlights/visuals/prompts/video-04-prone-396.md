# Видео 4 — «396 Hz: Release Fear» (Nano Banana)

Поза №4 в цикле канала: сидит (1) → на спине (2) → на боку (3) → **на животе (4)**.
Референс конкурента: Healing Quiet Tonight awOq7m7-81I и TLWxyq30cK4 (лежит на животе, голова на руках).
Акцент: тёплый красно-золотой свет корневой чакры, «тьма и тревога уходят вниз в космос».

## 16:9 (основная — видео, луп, обложка)

```
Cinematic digital art, 16:9. A translucent glass-like human body lying peacefully face down on its stomach in deep space, head turned to the side and resting on folded arms on a soft dark-blue glowing cloud pillow, legs straight and relaxed, seen from a gentle high three-quarter angle so the whole back and spine are visible. The body is semi-transparent pale blue with a softly glowing outline; a luminous golden spine and fine golden nerve network shine through the back, the brain glows warm gold. Exactly seven glowing chakra orbs along the spine from tailbone to crown: red, orange, yellow, green, sky blue, indigo, violet, evenly spaced, each with a soft halo. The red root chakra at the base of the spine glows strongest, with a warm red-gold light flowing gently down from it like roots into the space below. Faint concentric golden rings radiate around the body. Background: deep navy starfield with subtle warm red-violet nebula at the bottom, calm and dark. Figure in the lower-right two thirds of the frame, upper-left area dark and empty. Serene, safe, soft glow, high detail, no text, no letters, no logo, no watermark, no extra limbs, anatomically correct hands and feet.
```

## 9:16 (Shorts / вертикальная версия)

```
Cinematic digital art, vertical 9:16. A translucent glass-like human body lying peacefully face down on its stomach, head resting on folded arms on a soft dark-blue glowing cloud pillow, seen from above at a gentle angle so the body runs diagonally through the lower two thirds of the frame. Semi-transparent pale blue body with glowing outline, luminous golden spine and nerve network visible through the back, warm golden glowing brain. Exactly seven glowing chakra orbs along the spine: red, orange, yellow, green, sky blue, indigo, violet. The red root chakra glows strongest, with warm red-gold light flowing down from it like roots. Faint golden concentric rings. Deep navy starfield with subtle warm red-violet nebula. Upper third of the frame dark and empty. Serene, safe, soft glow, high detail, no text, no letters, no logo, no watermark, no extra limbs, anatomically correct hands and feet.
```

## Если что-то пошло не так (доп. фразы в конец промпта)

| Проблема | Добавить |
|---|---|
| Чакр больше или меньше 7 | `exactly 7 chakra orbs, no more, no less: red, orange, yellow, green, blue, indigo, violet` |
| Лежит на спине или на боку | `strictly lying face down on the stomach, back facing the viewer` |
| Позвоночник не виден | `the glowing spine is clearly visible along the back from neck to tailbone` |
| Красный свет слишком тревожный / как кровь | `the red light is soft, warm and golden-red, like sunset, calm and safe` |
| Слишком ярко / пёстро | `low-key lighting, mostly dark image, glow only on body, chakras and roots` |
| Лишние пальцы/руки | `exactly two arms, two legs, five fingers per hand` |
| Фигура в центре, тексту некуда | `subject in the lower right, empty dark space in the upper left for a title` |

Правило: перед работой пересчитать чакры — ровно 7. Скачивать оригинал (⋮ → Download), не скриншот.

## Правка v1 (первая картинка: женская фигура, мало космоса)

Первая картинка удачная по позе и чакрам (ровно 7, красные корни), но фигура женская и фон пустой. Правка той же картинки:

```
Edit this image. Keep the pose, the seven chakra orbs and their colors and positions, the golden spine and nerves, the red-gold roots, the golden rings, the pillow and the composition exactly the same. Make the body clearly MALE: broader shoulders, a straight masculine torso without a waist curve, narrow hips, flat chest, muscular back and calves, short-haired or shaved head silhouette. Add much more cosmos to the background: a large soft spiral galaxy and blue-violet nebula clouds in the upper right and behind the head, denser bright stars across the whole sky, a warm red-violet nebula glowing below the body under the roots, faint star dust. Keep the upper-left area darker for a title. Still exactly seven chakra orbs. High resolution 16:9, no text.
```

Если поза или чакры «уехали» — добавить: `keep exactly seven chakra orbs: red, orange, yellow, green, blue, indigo, violet` и `same pose, lying face down`.

## Дальше
1. Положить картинку в `sevenlights/visuals/base_prone_396.jpg` (или прислать в чат).
2. Обложка: `python tools/make_thumb.py --image visuals/base_prone_396.jpg --hz "396 HZ" --sub "RELEASE FEAR & SLEEP" --out visuals/thumbs/thumb_396_release_fear.jpg`.
3. Луп 8 с: `make_loop.py` с новыми координатами чакр (снимаю по картинке).
