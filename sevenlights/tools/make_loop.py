"""Бесшовная видеопетля из статичной картинки «тело в космосе с семью чакрами».

Все движения периодичны с периодом петли (по умолчанию 8 с), поэтому последний кадр плавно переходит в первый:
  1. волна света по чакрам снизу вверх (красная → фиолетовая) — «семь огней» поднимаются вдоль позвоночника;
  2. расходящиеся от сердца кольца волн («звук»);
  3. мерцание звёзд, у каждой своя фаза;
  4. лёгкая виньетка: взгляд к центру, края (кисти рук внизу) в тени.

Нужны Python 3 с numpy и Pillow и ffmpeg в PATH.
Запуск:
  python make_loop.py --image base.png --out loop.mp4
  python make_loop.py --image base.png --out loop.mp4 --chakras "705,415;757,383;822,348;881,318;943,305;1020,236;1060,238"
Координаты чакр — в пикселях исходной картинки (как она есть, с рамкой), от корневой к макушке.
Значения по умолчанию — для картинки sevenlights/visuals/base_chakra_body.webp.
Для YouTube петля размножается до нужной длины, например:
  ffmpeg -stream_loop -1 -i loop.mp4 -i track.wav -shortest -c:v copy -c:a aac -b:a 320k video.mp4
"""
import argparse
import subprocess
import numpy as np
from PIL import Image

# Цвета чакр от корневой к макушке
COLORS = np.array([
    (255, 55, 35), (255, 135, 30), (255, 215, 60), (60, 230, 110),
    (60, 180, 255), (90, 105, 255), (190, 80, 255)], float) / 255


def autocrop(im, thr=12):
    """Обрезать однотонную рамку (скриншот с полями): рамка — строки и столбцы, где все пиксели цвета угла.
    (Разброс яркости как признак не годится: тёмный космос у краёв почти однотонный и срезался вместе с рамкой.)"""
    a = np.asarray(im, float)
    diff = np.abs(a - a[0, 0]).max(2) > thr
    rows = np.where(diff.any(1))[0]
    cols = np.where(diff.any(0))[0]
    if len(rows) == 0 or len(cols) == 0:
        return im, (0, 0)
    return im.crop((cols[0], rows[0], cols[-1] + 1, rows[-1] + 1)), (cols[0], rows[0])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--image', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--seconds', type=float, default=8)
    ap.add_argument('--fps', type=int, default=30)
    ap.add_argument('--width', type=int, default=1920)
    ap.add_argument('--height', type=int, default=1080)
    ap.add_argument('--chakras', default='705,415;757,383;822,348;881,318;943,305;1020,236;1060,238',
                    help='x,y семи чакр в пикселях исходной картинки (с рамкой), от корневой к макушке, через ;')
    ap.add_argument('--no-autocrop', action='store_true')
    ap.add_argument('--seed', type=int, default=7)
    args = ap.parse_args()

    im = Image.open(args.image).convert('RGB')
    crop_off = (0, 0)
    if not args.no_autocrop:
        im, crop_off = autocrop(im)
    # Кадрирование ровно под 16:9 по центру
    W, H = im.size
    target = args.width / args.height
    if W / H > target:
        nw = int(round(H * target)); x0 = (W - nw) // 2; im = im.crop((x0, 0, x0 + nw, H)); off = (x0, 0)
    else:
        nh = int(round(W / target)); y0 = (H - nh) // 2; im = im.crop((0, y0, W, y0 + nh)); off = (0, y0)
    sx = args.width / im.size[0]; sy = args.height / im.size[1]
    base = np.asarray(im.resize((args.width, args.height), Image.LANCZOS), float) / 255
    h, w = base.shape[:2]
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)

    pts = [tuple(map(float, p.split(','))) for p in args.chakras.split(';')]
    pts = [((x - crop_off[0] - off[0]) * sx, (y - crop_off[1] - off[1]) * sy) for x, y in pts]
    s = (sx + sy) / 2

    # 1. Свечение чакр: ядро + широкий ореол, заранее по одной карте на чакру
    glows = []
    for (cx, cy) in pts:
        d2 = (xx - cx) ** 2 + (yy - cy) ** 2
        core = np.exp(-d2 / (2 * (14 * s) ** 2))
        halo = np.exp(-d2 / (2 * (55 * s) ** 2))
        glows.append((0.9 * core + 0.35 * halo).astype(np.float32))

    # 2. Кольца от сердца (4-я чакра)
    hx, hy = pts[3]
    r = np.sqrt((xx - hx) ** 2 + (yy - hy) ** 2)
    ring_fade = np.clip((r - 120 * s) / (180 * s), 0, 1) * np.clip((1100 * s - r) / (500 * s), 0, 1)
    ring_col = np.array([1.0, 0.78, 0.5], np.float32)
    lam = 90 * s

    # 3. Звёзды: яркие ненасыщенные точки фона, разбитые на группы с разной фазой мерцания
    lum = base.mean(2); sat = base.max(2) - base.min(2)
    loc = lum > 0.62
    loc &= sat < 0.25
    from numpy.lib.stride_tricks import sliding_window_view
    pad = np.pad(lum, 2, mode='edge')
    mx = sliding_window_view(pad, (5, 5)).max(axis=(2, 3))
    # Только звёзды на тёмном фоне: светлые точки контура тела не должны мерцать (контур становился пунктирным)
    from PIL import ImageFilter
    bg = np.asarray(Image.fromarray((lum * 255).astype(np.uint8)).filter(ImageFilter.BoxBlur(10)), float) / 255
    stars = np.argwhere(loc & (lum >= mx) & (bg < 0.16))
    rng = np.random.default_rng(args.seed)
    groups = 8
    star_maps = np.zeros((groups, h, w), np.float32)
    gid = rng.integers(0, groups, len(stars))
    for (y, x), g in zip(stars, gid):
        y0, y1, x0, x1 = max(0, y - 4), min(h, y + 5), max(0, x - 4), min(w, x + 5)
        star_maps[g, y0:y1, x0:x1] += np.exp(-((yy[y0:y1, x0:x1] - y) ** 2 + (xx[y0:y1, x0:x1] - x) ** 2) / (2 * 1.6 ** 2))
    star_phase = rng.random(groups)
    star_cycles = rng.integers(1, 3, groups)   # 1 или 2 мерцания за петлю — целое число, петля бесшовная

    # 4. Виньетка
    vx = (xx - w / 2) / (w / 2); vy = (yy - h / 2) / (h / 2)
    vign = (1 - 0.35 * np.clip(vx ** 2 * 0.7 + vy ** 2, 0, 1.4) ** 1.5)[..., None].astype(np.float32)

    n = int(round(args.seconds * args.fps))
    # Сама анимация бесшовная (без сжатия шов = обычной разнице соседних кадров). После сжатия на шве
    # остаётся скачок ~1 уровень яркости из 255 (опорный кадр против предсказанного) — на глаз не виден;
    # высокое качество (crf 12) делает его ещё меньше.
    ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
                           '-s', f'{w}x{h}', '-r', str(args.fps), '-i', '-', '-c:v', 'libx264', '-preset', 'slow',
                           '-crf', '12', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', args.out],
                          stdin=subprocess.PIPE)
    base32 = base.astype(np.float32)
    for i in range(n):
        ph = i / n   # фаза петли 0..1
        light = np.zeros((h, w, 3), np.float32)
        for k, g in enumerate(glows):
            # Волна поднимается от корневой чакры к макушке за одну петлю
            p = 0.5 + 0.5 * np.cos(2 * np.pi * (ph - k / 7))
            amp = 0.18 + 0.82 * p ** 3
            light += g[..., None] * (COLORS[k] * amp).astype(np.float32)
        # Кольца: два круга волн уходят наружу за петлю
        rings = np.maximum(0, np.cos(2 * np.pi * (r / lam - 2 * ph))) ** 10 * ring_fade * 0.10
        light += rings[..., None] * ring_col
        # Звёзды: множитель яркости вокруг каждой звезды
        tw = np.zeros((h, w), np.float32)
        for g in range(groups):
            tw += star_maps[g] * (0.55 * np.sin(2 * np.pi * (star_cycles[g] * ph + star_phase[g])))
        frame = base32 * (1 + tw[..., None])
        frame = 1 - (1 - frame) * (1 - np.clip(light, 0, 1))   # «экран»: свет только добавляется
        frame = np.clip(frame * vign, 0, 1)
        ff.stdin.write((frame * 255 + 0.5).astype(np.uint8).tobytes())
    ff.stdin.close()
    ff.wait()
    print(f'Готово: {args.out} ({n} кадров, {args.seconds} с, {w}x{h}, звёзд {len(stars)})')


if __name__ == '__main__':
    main()
