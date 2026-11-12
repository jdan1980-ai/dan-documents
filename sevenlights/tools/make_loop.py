"""Бесшовная видеопетля из статичной картинки «тело в космосе с семью чакрами».

Все движения периодичны с периодом петли (по умолчанию 8 с), поэтому последний кадр плавно переходит в первый:
  1. волна света по чакрам снизу вверх (красная → фиолетовая) — «семь огней» поднимаются вдоль позвоночника;
  2. расходящиеся от сердца кольца волн («звук»);
  3. мерцание звёзд, у каждой своя фаза;
  4. лёгкая виньетка: взгляд к центру, края (кисти рук внизу) в тени;
  5. (необязательно, --ribbon) цветная лента над телом колышется бегущей волной и переливается;
  6. (необязательно, --roots) светящиеся «корни» под корневой чакрой: по ним вниз бегут импульсы света
     («страх стекает в землю»), корни мягко «дышат» и чуть покачиваются кончиками.

Нужны Python 3 с numpy и Pillow и ffmpeg в PATH.
Запуск:
  python make_loop.py --image base.png --out loop.mp4
  python make_loop.py --image base.png --out loop.mp4 --chakras "705,415;757,383;822,348;881,318;943,305;1020,236;1060,238"
Координаты чакр — в пикселях исходной картинки (как она есть, с рамкой), от корневой к макушке.
Значения по умолчанию — для картинки sevenlights/visuals/base_chakra_body.webp.
Видео 3 (поза на боку, лента над телом):
  python make_loop.py --image ../visuals/base_side_sleep.jpg --out loop_side.mp4 \
    --chakras "673,504;738,495;820,482;900,456;1028,446;1140,426;1214,391" \
    --ribbon "0,425;600,425;800,360;900,322;1000,318;1100,330;1250,340;1376,320"
--ribbon — ломаная (x,y исходной картинки, слева направо): всё цветное ВЫШЕ неё считается лентой.
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
    ap.add_argument('--ribbon', help='нижняя граница ленты: "x,y;x,y;..." в пикселях исходной картинки')
    ap.add_argument('--roots', help='прямоугольник с корнями под корневой чакрой: "x0,y0,x1,y1" в пикселях исходной картинки')
    ap.add_argument('--ribbon-amp', type=float, default=9, help='размах колыхания ленты, px при 1920x1080')
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

    # 5. Лента: её свет отделяется от тёмного фона и в каждом кадре сдвигается по вертикали бегущей волной
    rib = None
    if args.ribbon:
        bpts = [tuple(map(float, p.split(','))) for p in args.ribbon.split(';')]
        bx = np.array([(x - crop_off[0] - off[0]) * sx for x, _ in bpts])
        by = np.array([(y - crop_off[1] - off[1]) * sy for _, y in bpts])
        yb = np.interp(np.arange(w), bx, by).astype(np.float32)          # граница для каждого столбца
        region = np.clip((yb[None, :] - yy) / (12 * s), 0, 1)              # мягко: 1 выше границы
        sat = base.max(2) - base.min(2)
        cmask = np.clip((sat - 0.10) / 0.15, 0, 1)                         # только цветное
        dark = np.array([0.012, 0.018, 0.045], np.float32)                 # цвет неба
        rib = (np.clip(base - dark, 0, 1) * (region * cmask)[..., None]).astype(np.float32)
        ytop = int(max(0, np.argwhere((region * cmask).max(1) > 0.01)[0][0] - 40)) if (region * cmask).max() > 0.01 else 0
        ybot = int(min(h, yb.max() + 40))
        rib = rib[ytop:ybot]
        rr = np.arange(ybot - ytop, dtype=np.float32)[:, None]
        xs = np.arange(w, dtype=np.float32)
        amp = args.ribbon_amp * (w / 1920)
        lam1, lam2 = w * 0.55, w * 0.9

    # 6. Корни: тонкие тёплые светлые линии ниже корневой чакры (в конусе вниз от неё)
    roots = None
    if args.roots:
        from PIL import ImageFilter as _IF
        q = [float(v) for v in args.roots.split(',')]
        X0, X1 = [int(np.clip((v - crop_off[0] - off[0]) * sx, 0, w)) for v in (q[0], q[2])]
        Y0, Y1 = [int(np.clip((v - crop_off[1] - off[1]) * sy, 0, h)) for v in (q[1], q[3])]
        lumr = base.mean(2)
        blr = np.asarray(Image.fromarray((lumr * 255).astype(np.uint8)).filter(_IF.BoxBlur(max(2, int(round(5 * s))))), float) / 255
        line = np.clip((lumr - blr - 0.02) / 0.06, 0, 1) * np.clip((base[..., 0] - base[..., 2] - 0.02) / 0.10, 0, 1)
        rcx, rcy = pts[0]
        ddx, ddy = xx - rcx, yy - rcy
        dist = np.sqrt(ddx ** 2 + ddy ** 2)
        cone = np.clip((ddy - 0.8 * np.abs(ddx) + 20 * s) / (20 * s), 0, 1)     # только вниз от чакры
        excl = np.clip((dist - 22 * s) / (10 * s), 0, 1)                         # без самого шара чакры
        M = (line * cone * excl)[Y0:Y1, X0:X1].astype(np.float32)
        roots = (base[Y0:Y1, X0:X1] * M[..., None]).astype(np.float32)
        rd = dist[Y0:Y1, X0:X1].astype(np.float32)
        rxl = np.arange(X1 - X0, dtype=np.float32)[None, :]
        rrows = np.arange(Y1 - Y0)[:, None]
        rlam = 110 * s
        rtip = np.clip(rd / (200 * s), 0, 1)                                      # кончики качаются сильнее

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
        if rib is not None:
            dy = amp * np.sin(2 * np.pi * (xs / lam1 - ph))                     # 1 период волны за петлю
            shimmer = 1 + 0.22 * np.sin(2 * np.pi * (xs / lam2 - ph))        # перелив бежит вдоль ленты
            src = rr - dy[None, :]
            i0 = np.clip(np.floor(src).astype(np.int32), 0, rib.shape[0] - 1)
            i1 = np.clip(i0 + 1, 0, rib.shape[0] - 1)
            f = np.clip(src - np.floor(src), 0, 1)[..., None]
            cols = np.arange(w)[None, :]
            moved = rib[i0, cols] * (1 - f) + rib[i1, cols] * f
            fb = base32.copy()
            fb[ytop:ybot] = np.clip(fb[ytop:ybot] - rib + moved * shimmer[None, :, None], 0, 1)
        else:
            fb = base32
        if roots is not None:
            sway = 1.5 * s * np.sin(2 * np.pi * (yy[Y0:Y1, X0:X1] / (300 * s) - ph)) * rtip
            src = rxl - sway
            j0 = np.clip(np.floor(src).astype(np.int32), 0, X1 - X0 - 1)
            j1 = np.clip(j0 + 1, 0, X1 - X0 - 1)
            fr_ = np.clip(src - np.floor(src), 0, 1)[..., None]
            moved = roots[rrows, j0] * (1 - fr_) + roots[rrows, j1] * fr_
            pulse = np.maximum(0, np.cos(2 * np.pi * (rd / rlam - 2 * ph))) ** 6     # 2 волны вниз за петлю
            gain = (1 + 0.15 * np.sin(2 * np.pi * ph)) + 1.6 * pulse
            if fb is base32:
                fb = base32.copy()
            fb[Y0:Y1, X0:X1] = np.clip(fb[Y0:Y1, X0:X1] - roots + moved * gain[..., None], 0, 1)
        frame = fb * (1 + tw[..., None])
        frame = 1 - (1 - frame) * (1 - np.clip(light, 0, 1))   # «экран»: свет только добавляется
        frame = np.clip(frame * vign, 0, 1)
        ff.stdin.write((frame * 255 + 0.5).astype(np.uint8).tobytes())
    ff.stdin.close()
    ff.wait()
    print(f'Готово: {args.out} ({n} кадров, {args.seconds} с, {w}x{h}, звёзд {len(stars)})')


if __name__ == '__main__':
    main()
