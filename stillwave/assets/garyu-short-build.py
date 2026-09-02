#!/usr/bin/env python3
"""
garyu-short-build.py — собирает 32-секундный Short из шести кадров §3c.

  python3 garyu-short-build.py --frames DIR --out garyu-short.mp4

Почему не ffmpeg zoompan (правило канала, локнуто 2026-07-26): zoompan округляет
рамку кропа до целых пикселей, поэтому медленный наезд идёт ступеньками —
картинка замирает на 2–3 кадра, потом прыгает. Здесь каждый кадр рендерится в PIL
из рамки с дробными координатами и ресемплится LANCZOS: округлять нечего, дрожание
невозможно по построению.

Безопасная зона Shorts: интерфейс съедает низ ~24%, правый край ~17%, верх ~7%.
Весь текст обязан лежать в y 150–1450, x 60–880 при 1080×1920. Скрипт замеряет
bounding box непрозрачных пикселей каждого оверлея и печатает числа — на глаз
такое не проверяется.

После сборки печатает проверку плавности по ГОТОВОМУ файлу: средняя разница
соседних кадров внутри одного плана. Норма — замерших кадров 0 и CV < 0.25.
"""

import argparse
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H, FPS = 1080, 1920, 30
CREAM = (245, 234, 210)
LS = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
LSI = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
JP_CANDIDATES = ["/tmp/NotoSerifJP-Bold.otf", "NotoSerifJP-Bold.otf",
                 "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc",
                 "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf"]

SAFE = dict(x0=60, x1=880, y0=150, y1=1450)
TEXT_Y = 0.20                   # центр блока по высоте безопасной зоны: 0 — верх, 1 — низ
XFADE = 0.6                     # секунд, только растворение — сдвиг двигает всю комнату

# кадр, длительность, зум (старт→конец), пан (dx, dy в долях лишнего поля), текст
SHOTS = [
    ("fr1", 4.0, 1.00, 1.06, (0.5, 0.35), []),
    ("fr2", 5.0, 1.06, 1.00, (0.5, 0.50), [("臥龍", "jp", 150), ("GARYŪ", "serif", 78)]),
    ("fr3", 5.0, 1.00, 1.05, (0.45, 0.55), [("The helmet is off.", "serif", 62),
                                            ("The swords are down.", "serif", 62)]),
    ("fr5", 6.0, 1.05, 1.00, (0.5, 0.40), [("A dragon at rest", "italic", 64),
                                           ("is not a dragon diminished.", "italic", 58)]),
    ("fr4", 6.0, 1.00, 1.06, (0.5, 0.45), [("The power is simply", "serif", 62),
                                           ("not in use.", "serif", 62)]),
    ("fr6", 6.0, 1.06, 1.00, (0.5, 0.55), [("2 HOURS", "serif", 84),
                                           ("Japanese Samurai Ambience", "serif", 46),
                                           ("SUBSCRIBE", "serif", 44)]),
]


def jp_font(size):
    for p in JP_CANDIDATES:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    raise SystemExit("нет японского шрифта — см. docstring garyu-compose-thumb.py")


def font(kind, size):
    return {"jp": lambda: jp_font(size),
            "serif": lambda: ImageFont.truetype(LS, size),
            "italic": lambda: ImageFont.truetype(LSI, size)}[kind]()


def cover(img):
    """Вписать кадр в 9:16 с запасом на дрейф, без искажения пропорций."""
    iw, ih = img.size
    s = max(W / iw, H / ih) * 1.10          # 10% запаса, чтобы было куда ехать
    return img.resize((round(iw * s), round(ih * s)), Image.LANCZOS)


def ken_burns(base, t, zs, ze, pan):
    """Кроп с ДРОБНЫМИ координатами -> без округления -> без ступенек."""
    bw, bh = base.size
    z = zs + (ze - zs) * t
    cw, ch = W / z, H / z
    px, py = pan
    x = (bw - cw) * px
    y = (bh - ch) * py
    return base.resize((W, H), Image.LANCZOS, box=(x, y, x + cw, y + ch))


def text_layer(lines):
    """Блок текста по центру безопасной зоны. Возвращает слой и его bbox."""
    if not lines:
        return None, None
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    rendered = [(txt, font(kind, size), size) for txt, kind, size in lines]
    gaps = [int(s * 0.42) for _, _, s in rendered]
    total = sum(s * 1.25 for _, _, s in rendered) + sum(gaps[:-1])
    cy = SAFE["y0"] + (SAFE["y1"] - SAFE["y0"]) * TEXT_Y - total / 2
    cx = (SAFE["x0"] + SAFE["x1"]) / 2
    y = cy
    for i, (txt, f, size) in enumerate(rendered):
        w = d.textlength(txt, font=f)
        d.text((cx - w / 2, y), txt, font=f, fill=CREAM + (255,))
        y += size * 1.25 + (gaps[i] if i < len(gaps) - 1 else 0)
    a = np.asarray(layer)[:, :, 3]
    ys, xs = np.where(a > 200)
    box = (xs.min(), xs.max(), ys.min(), ys.max())

    # мягкий скрим под блоком — на золотой ширме кремовый иначе теряется.
    # Замер безопасной зоны его игнорирует (порог alpha > 200), это по правилу.
    scr = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    pad = 70
    ImageDraw.Draw(scr).rounded_rectangle(
        [box[0] - pad, box[2] - pad, box[1] + pad, box[3] + pad], 90, fill=(0, 0, 0, 105))
    layer = Image.alpha_composite(scr.filter(ImageFilter.GaussianBlur(55)), layer)
    return layer, box


def alpha_curve(t, dur):
    """Появление 0.5 с, уход 0.5 с, между ними держим."""
    fi, fo = 0.5, 0.5
    if t < fi:
        return t / fi
    if t > dur - fo:
        return max(0.0, (dur - t) / fo)
    return 1.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--frames", type=Path, required=True,
                    help="папка с garyu-shorts-fr1.jpg … fr6.jpg")
    ap.add_argument("--out", type=Path, default=Path("garyu-short.mp4"))
    ap.add_argument("--audio", type=Path, default=None,
                    help="mp3/wav под видео; берётся окно с --audio-start, "
                         "выравнивается к -16 LUFS / TP -1.5 и получает фейды")
    ap.add_argument("--audio-start", type=float, default=0.0,
                    help="с какой секунды исходника брать окно")
    ap.add_argument("--ffmpeg", default=None)
    a = ap.parse_args()

    ff = a.ffmpeg
    if not ff:
        import shutil
        ff = shutil.which("ffmpeg")
        if not ff:
            import imageio_ffmpeg
            ff = imageio_ffmpeg.get_ffmpeg_exe()

    bases, layers, boxes = {}, {}, {}
    print("безопасная зона: x {x0}–{x1}, y {y0}–{y1}".format(**SAFE))
    fail = False
    for name, dur, zs, ze, pan, lines in SHOTS:
        p = a.frames / f"garyu-shorts-{name}.jpg"
        if not p.exists():
            raise SystemExit(f"нет файла {p}")
        bases[name] = cover(Image.open(p).convert("RGB"))
        layer, box = text_layer(lines)
        layers[name], boxes[name] = layer, box
        if box:
            x0, x1, y0, y1 = box
            ok = (x0 >= SAFE["x0"] and x1 <= SAFE["x1"]
                  and y0 >= SAFE["y0"] and y1 <= SAFE["y1"])
            fail |= not ok
            print(f"  {name}: текст x {x0}–{x1}, y {y0}–{y1}  {'ok' if ok else 'ВНЕ ЗОНЫ'}")
        else:
            print(f"  {name}: без текста")
    if fail:
        raise SystemExit("текст вышел за безопасную зону — правь SHOTS")

    total = sum(s[1] for s in SHOTS) - XFADE * (len(SHOTS) - 1)
    nframes = int(round(total * FPS))
    print(f"\n{len(SHOTS)} планов, {total:.1f} с, {nframes} кадров @ {FPS} fps")

    starts, t0 = [], 0.0
    for _, dur, *_ in SHOTS:
        starts.append(t0)
        t0 += dur - XFADE

    def render(gt):
        out = None
        for i, (name, dur, zs, ze, pan, _) in enumerate(SHOTS):
            lt = gt - starts[i]
            if lt < 0 or lt > dur:
                continue
            img = ken_burns(bases[name], lt / dur, zs, ze, pan)
            layer = layers[name]
            if layer is not None:
                al = alpha_curve(lt, dur)
                if al > 0:
                    tmp = layer.copy()
                    aa = np.asarray(tmp).copy()
                    aa[:, :, 3] = (aa[:, :, 3] * al).astype(np.uint8)
                    img = Image.alpha_composite(img.convert("RGBA"),
                                                Image.fromarray(aa)).convert("RGB")
            if out is None:
                out = img
            else:
                prev_end = starts[i] + XFADE
                k = min(1.0, max(0.0, (gt - starts[i]) / XFADE))
                out = Image.blend(out, img, k)
        return out

    cmd = [ff, "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
           "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium",
           "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(a.out)]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)
    for n in range(nframes):
        proc.stdin.write(render(n / FPS).tobytes())
    proc.stdin.close()
    proc.wait()
    if a.audio:
        silent = a.out.with_suffix(".silent.mp4")
        a.out.rename(silent)
        fade_out = max(0.0, total - 2.0)
        af = (f"afade=t=in:d=1.5,afade=t=out:st={fade_out:.2f}:d=2.0,"
              f"loudnorm=I=-16:TP=-1.5:LRA=11")
        subprocess.run([ff, "-y", "-v", "error",
                        "-i", str(silent),
                        "-ss", str(a.audio_start), "-t", f"{total:.3f}", "-i", str(a.audio),
                        "-filter:a", af,
                        "-c:v", "copy", "-c:a", "aac", "-b:a", "256k",
                        "-shortest", "-movflags", "+faststart", str(a.out)], check=True)
        silent.unlink()
        print(f"звук: {a.audio.name} с {a.audio_start:.0f} с, "
              f"фейд-ин 1.5 с / фейд-аут 2 с, выровнено к -16 LUFS")

    print(f"готово -> {a.out}  ({a.out.stat().st_size/1e6:.1f} MB)")

    # проверка плавности по ГОТОВОМУ файлу, внутри одного плана без растворения
    probe_at = starts[3] + 2.0
    p = subprocess.run([ff, "-v", "error", "-ss", str(probe_at), "-i", str(a.out),
                        "-frames:v", "25", "-f", "rawvideo", "-pix_fmt", "gray",
                        "-s", f"{W}x{H}", "-"], capture_output=True)
    fr = np.frombuffer(p.stdout, dtype=np.uint8).reshape(-1, H, W).astype(np.float32)
    diffs = np.abs(np.diff(fr, axis=0)).mean(axis=(1, 2))
    frozen = int((diffs < 0.05).sum())
    cv = diffs.std() / diffs.mean() if diffs.mean() else 0
    print(f"плавность на {probe_at:.1f} с: замерших кадров {frozen} (норма 0), "
          f"CV {cv:.3f} (норма < 0.25)  -> {'ok' if frozen == 0 and cv < 0.25 else 'ПРОВАЛ'}")


if __name__ == "__main__":
    main()
