"""Обложка 1280x720 для видео Seven Lights: базовая картинка «тело с семью чакрами» + текст.

Базовая картинка одна для всех видео (sevenlights/visuals/base_chakra_body.webp), меняется только текст:
  python make_thumb.py --hz "432 HZ" --out thumb_432.jpg
  python make_thumb.py --hz "528 · 432 · 396 HZ" --size-hz 110 --out thumb_descent.jpg
  python make_thumb.py --hz "396 HZ" --sub "ROOT CHAKRA" --out thumb_root.jpg

Сборка детерминированная (без нейросети): анатомия и семь огней остаются как в исходной картинке.
Нужны Python 3, Pillow, numpy и шрифт Inter (путь через --font).
"""
import argparse
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_loop import autocrop  # noqa: E402

W, H = 1280, 720
HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_IMAGE = os.path.join(HERE, '..', 'visuals', 'base_chakra_body.webp')
DEFAULT_FONT = '/usr/share/fonts/opentype/inter/Inter-Black.otf'


def text_layer(text, font, fill_top, fill_bottom, outline, glow, stroke):
    """Слой RGBA с градиентным текстом, обводкой и свечением; возвращает (слой, bbox)."""
    probe = Image.new('L', (4, 4))
    l, t, r, b = ImageDraw.Draw(probe).textbbox((0, 0), text, font=font, stroke_width=stroke)
    pad = 90
    w, h = r - l + 2 * pad, b - t + 2 * pad
    mask = Image.new('L', (w, h), 0)
    ImageDraw.Draw(mask).text((pad - l, pad - t), text, font=font, fill=255)
    outl = Image.new('L', (w, h), 0)
    ImageDraw.Draw(outl).text((pad - l, pad - t), text, font=font, fill=255, stroke_width=stroke)

    layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    # свечение
    g = outl.filter(ImageFilter.GaussianBlur(22))
    layer.paste(Image.new('RGBA', (w, h), glow + (0,)), mask=g.point(lambda v: int(v * 0.9)))
    # обводка
    layer.paste(Image.new('RGBA', (w, h), outline + (255,)), mask=outl)
    # градиентная заливка: сверху светлее, снизу насыщеннее
    ys = np.linspace(0, 1, h)[:, None, None]
    top, bot = np.array(fill_top, float), np.array(fill_bottom, float)
    grad = (top * (1 - ys) + bot * ys) * np.ones((1, w, 1))
    layer.paste(Image.fromarray(grad.astype(np.uint8), 'RGB'), mask=mask)
    return layer, (pad - l, pad - t)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--image', default=DEFAULT_IMAGE)
    ap.add_argument('--out', required=True)
    ap.add_argument('--hz', required=True, help='большая надпись, например "432 HZ"')
    ap.add_argument('--sub', default='DEEP HEALING SLEEP', help='вторая строка (белая)')
    ap.add_argument('--brand', default='SEVEN LIGHTS', help='подпись внизу слева')
    ap.add_argument('--font', default=DEFAULT_FONT)
    ap.add_argument('--size-hz', type=int, default=170)
    ap.add_argument('--size-sub', type=int, default=64)
    ap.add_argument('--boost', type=float, default=1.5, help='яркость/насыщенность/свечение картинки (1 = как есть)')
    ap.add_argument('--fig-scale', type=float, default=1.0, help='размер картинки в кадре (меньше 1 — больше места под текст)')
    ap.add_argument('--text-x', type=int, default=42)
    ap.add_argument('--text-y', type=int, default=18)
    args = ap.parse_args()

    im = Image.open(args.image).convert('RGB')
    im, _ = autocrop(im)
    # Подгонка к 16:9 по центру
    iw, ih = im.size
    if iw / ih > W / H:
        nw = int(round(ih * W / H)); x0 = (iw - nw) // 2; im = im.crop((x0, 0, x0 + nw, ih))
    else:
        nh = int(round(iw * H / W)); y0 = (ih - nh) // 2; im = im.crop((0, y0, iw, y0 + nh))

    # Яркость, насыщенность и свечение (bloom): в ленте обложку видят очень маленькой, тусклое тело теряется
    if args.boost != 1.0:
        k = args.boost
        im = ImageEnhance.Brightness(im).enhance(1 + 0.30 * (k - 1) / 0.5 * 0.5)
        im = ImageEnhance.Color(im).enhance(1 + 0.35 * (k - 1) / 0.5 * 0.5)
        im = ImageEnhance.Contrast(im).enhance(1 + 0.15 * (k - 1) / 0.5 * 0.5)
        arr = np.asarray(im, np.float32) / 255
        bright = np.clip((arr.max(2) - 0.55) / 0.45, 0, 1)[..., None] * arr
        bloom = np.asarray(Image.fromarray((bright * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(14)), np.float32) / 255
        arr = 1 - (1 - arr) * (1 - np.clip(bloom * 0.9 * (k - 1) / 0.5 + bloom * 0.0, 0, 1))
        im = Image.fromarray((np.clip(arr, 0, 1) * 255).astype(np.uint8))

    # Фон: та же картинка, растянутая, размытая и затемнённая; поверх — уменьшенная картинка в правом нижнем углу
    bg = im.resize((W, H), Image.LANCZOS).filter(ImageFilter.GaussianBlur(26))
    bg = Image.fromarray((np.asarray(bg, float) * 0.55).astype(np.uint8))
    fw, fh = int(W * args.fig_scale), int(H * args.fig_scale)
    fig = im.resize((fw, fh), Image.LANCZOS)
    # Мягкие края картинки, чтобы шов с фоном не был виден
    m = np.ones((fh, fw), np.float32)
    ramp = np.clip(np.arange(fw) / 60, 0, 1) * np.clip((fw - 1 - np.arange(fw)) / 60, 0, 1)
    rampy = np.clip(np.arange(fh) / 60, 0, 1) * np.clip((fh - 1 - np.arange(fh)) / 60, 0, 1)
    m = (ramp[None, :] * rampy[:, None] * 255).astype(np.uint8)
    canvas = bg.copy()
    canvas.paste(fig, (W - fw, H - fh), Image.fromarray(m))

    # Тёмная подложка под текстом слева сверху — для читаемости
    shade = Image.new('L', (W, H), 0)
    ImageDraw.Draw(shade).ellipse((-380, -260, 900, 360), fill=150)
    shade = shade.filter(ImageFilter.GaussianBlur(70))
    canvas.paste(Image.new('RGB', (W, H), (3, 6, 22)), mask=shade)

    f_hz = ImageFont.truetype(args.font, args.size_hz)
    f_sub = ImageFont.truetype(args.font, args.size_sub)
    f_brand = ImageFont.truetype(args.font, 26)

    canvas = canvas.convert('RGBA')
    lay, (ox, oy) = text_layer(args.hz, f_hz, (255, 246, 150), (255, 176, 20), (120, 40, 0), (255, 150, 20), 6)
    canvas.alpha_composite(lay, (args.text_x - 90 + 0, args.text_y - 90 + 0))
    hz_bottom = args.text_y + (lay.size[1] - 180)
    lay2, _ = text_layer(args.sub, f_sub, (255, 255, 255), (214, 228, 255), (10, 18, 60), (110, 150, 255), 4)
    canvas.alpha_composite(lay2, (args.text_x - 90, hz_bottom + 4 - 90 + 10))

    d = ImageDraw.Draw(canvas)
    d.text((42, H - 56), args.brand, font=f_brand, fill=(230, 236, 255, 235), stroke_width=2, stroke_fill=(5, 8, 30, 255))
    canvas = canvas.convert('RGB')
    q = 94
    canvas.save(args.out, quality=q, subsampling=0) if args.out.lower().endswith(('.jpg', '.jpeg')) else canvas.save(args.out)
    print(f'Готово: {args.out} ({W}x{H}, {os.path.getsize(args.out) // 1024} КБ)')


if __name__ == '__main__':
    main()
