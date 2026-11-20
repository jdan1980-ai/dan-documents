# StillWave — Motion-graphics Shorts (version B, from 2026-11-19)

A new way to build the samurai-series Shorts: everything is animated in code (free, no Flow credits, every detail editable), instead of three slow crops of a still with three text beats. Pilot: ŌKAMI. Script: `stillwave/assets/okami-short-motion.py`.

**🇺🇦 RU:** Новый способ делать Shorts самурайской серии: всё анимируется кодом (бесплатно, без кредитов Flow, любую деталь можно поправить точечно) вместо трёх медленных кропов неподвижного кадра и трёх текстовых фраз. Пилот — ŌKAMI.

## Why

The template Short (`samurai-short-build.py`, "version A") is a static frame with text, and every Short has the same structure. Two problems: a weak first second (viewers decide to swipe in 1–2 s) and a risk of looking repetitive across the series (the same issue that brought complaints on Seven Lights). Version B opens already in motion and gives every Short its own visual event.

**🇺🇦 RU:** Шаблонный Short (версия A) — неподвижный кадр с текстом, и все Shorts устроены одинаково. Проблемы: слабая первая секунда (решение свайпнуть принимается за 1–2 с) и риск однообразия по серии (как на Seven Lights). Версия B начинается уже в движении, и у каждого Short своё визуальное событие.

## Structure (24 s, 1080×1920, 30 fps)

| Time | Beat | What happens |
|---|---|---|
| 0–8 s | HOOK | Tight on the painted animal's face. Its eyes **already glowing at frame 1**, the hall exposes up from darkness, slow pull-back. Hook words appear one by one (rise + fade). |
| 8–9 s | transition | **Ink bleed**: the next shot soaks through a spreading ink blot with a dark wet rim. |
| 9–16 s | KANJI | The kanji is **written stroke by stroke** with a tapered brush in the correct stroke order (KanjiVG data), dry-brush edge, a wet gold point at the brush tip. Then romaji + gloss. |
| 16–17 s | transition | Ink bleed again. |
| 17–24 s | WIDE | Samurai before the painting, slow push-in. Closing line + "Full 2 hours on the channel". |
| all | depth | Gold dust motes drift up through every shot (2.5D). |

Under everything runs the video's own seamless loop (`<slug>-animate.py` output), so candles, eyes and ink keep living.

**🇺🇦 RU:** 0–8 с хук: крупно морда, глаза уже горят на первом кадре, зал светлеет, камера отъезжает, слова появляются по одному. 8–9 с переход через растекающуюся тушь. 9–16 с иероглиф пишется кистью по чертам в правильном порядке, потом ромадзи и перевод. 16–17 с снова тушь. 17–24 с общий план с самураем, финальная фраза и CTA. Через все кадры летят золотые пылинки. Под всем — живая петля самого видео.

## How to build one

1. **Loop:** render the long-form's local animation at 1920 px:
   `python3 stillwave/assets/<slug>-animate.py <slug>-2h-source.jpg <slug>-loop.mp4 12`
   (for a Flow-animated video, use its Flow loop instead.)
2. **Kanji stroke data:** download the KanjiVG file for the kanji (hex code point, 5 digits) into `stillwave/assets/kanjivg/`:
   `curl -sSf -o stillwave/assets/kanjivg/072fc.svg https://raw.githubusercontent.com/KanjiVG/kanjivg/master/kanji/072fc.svg` (狼 = U+72FC). KanjiVG is CC BY-SA 3.0; the copyright header stays in the file.
3. **Adapt the script** (currently tuned for ŌKAMI — copy it to `<slug>-short-motion.py` or, better, turn it into a per-slug config like `samurai-short-build.py`). Values to set per video:
   - `EYES` — pixel positions of the glowing point for the hook (eyes of the animal; for a video without eyes pick another light: moon, blade, lantern) in the 1920×1080 frame;
   - `shot_face` crop centre / zoom, `shot_clouds` (a dark, calm area for the kanji), `shot_wide` centre (keep both the animal and the samurai inside the 9:16 window);
   - the KanjiVG file name; hook / gloss / closing lines (from the script's §12 essay);
   - ink-blot seed points in `TRANS`.
4. **Render:** `python3 stillwave/assets/okami-short-motion.py <slug>-loop.mp4 <track>.mp3 <slug>-short-B.mp4 40` (~4–5 min on the cloud box). Needs `opencv-python-headless`, `svgpathtools`, `Pillow`, `numpy`, ffmpeg.
5. **Check frames** at 0.1 / 4 / 12 / 21 s: the eye flare must not look like headlights, the samurai must not be cut at the edge, all text inside the Shorts safe zone (x 60–880, y 150–1450).
6. **Music:** a track from the album, not one that drew a Content ID claim; −14 LUFS (the script does it).

**🇺🇦 RU:** 1) Отрендерить петлю видео. 2) Скачать файл черт иероглифа из KanjiVG. 3) Под каждое видео поменять: точку свечения для хука (глаза животного; если глаз нет — луна, клинок, фонарь), центры и зум трёх кадров, файл иероглифа, тексты, точки старта клякс. 4) Рендер ~4–5 минут. 5) Проверить кадры: вспышка не «фары», самурай не обрезан, текст в безопасной зоне. 6) Музыка из альбома, не трек с клеймом.

## Cover rule (user, 2026-11-20)

The Short's cover (the frame picked on upload) must show **the scene with the samurai + the big kanji + the name in Latin letters** (e.g. 武士道 / BUSHIDO over the samurai), as the version A Shorts did. A bare kanji on a dark background (the ŌKAMI B cover) draws less attention in the Shorts grid. So every version B Short gets:
- a **cover beat** in the WIDE shot: for the last ~2 s the kanji + name sit large over the wide scene (samurai + animal in frame), so this frame can be chosen as the cover;
- a separate **cover JPG** 1080×1920 with the same layout, to upload as a custom thumbnail where the app allows it.

**🇺🇦 RU:** На заставке Short — кадр со сценой и самураем, большой иероглиф и название латиницей, как у версии A. Голый иероглиф на тёмном фоне (заставка ŌKAMI B) привлекает меньше внимания. В каждом Short версии B: в конце общего плана ~2 с иероглиф + название крупно поверх сцены (этот кадр выбирать заставкой) + отдельный JPG обложки.

## ~~A/B test (ŌKAMI)~~ — cancelled 2026-11-19

**User decision: no A/B. Version B is the standard Shorts format from now on; version A is retired.** (Original plan kept below for reference.)

**🇺🇦 RU:** Решение пользователя: A/B не делаем. Версия B — стандарт для всех Shorts, версия A больше не используется.


Publish version A (template) and version B 2–3 days apart at the same hour, same title formula, Related video = the long-form. After 7 days compare in Studio: **"Viewed vs swiped away"** and **average view duration**. If B wins, B becomes the standard Shorts format and `samurai-short-build.py` is replaced by a per-slug motion builder.

**🇺🇦 RU:** Опубликовать A и B с разницей 2–3 дня в одно время. Через 7 дней сравнить «смотрели / пролистали» и среднюю длительность просмотра. Если B лучше — он становится стандартом.

## Ideas for the next videos (one unique living event each)

- Crane: the painted crane slowly opens its wings; kanji 鶴.
- Koi: the koi swims across the painted water; kanji 鯉.
- Bear: snow starts falling inside the painting; kanji 熊.
- Moon: the moon's light sweeps across the floor to the samurai; kanji 月.

**🇺🇦 RU:** В каждом новом видео — одно живое событие, которого ещё не было: журавль раскрывает крылья, кои плывёт по нарисованной воде, на медведя в росписи падает снег, лунный свет проходит по полу к самураю.
