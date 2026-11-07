"""Оверлей для первых секунд видео: прозрачный PNG 1920x1080 с благодарностью зрителям.

Стиль как у обложек: первая строка золотая со свечением, вторая белая, левый верхний угол (там тёмный космос, тело не закрыто).
  python make_overlay.py --out overlay_intro.png --preview preview.jpg
  python make_overlay.py --title "Thank you for being here" --sub "Sweet dreams, and subscribe for more nights like this" --out o.png

В CapCut: положить PNG на дорожку 0:02–0:11, появление 1.5 с, исчезновение 2 с.
Через ffmpeg (видео перекодируется):
  ffmpeg -i video.mp4 -loop 1 -t 11 -i overlay_intro.png -filter_complex "[1:v]format=rgba,fade=t=in:st=2:d=1.5:alpha=1,fade=t=out:st=8.5:d=2:alpha=1[o];[0:v][o]overlay=0:0:eof_action=pass" -c:a copy out.mp4
"""
import argparse
import os
import sys

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_thumb import text_layer, DEFAULT_IMAGE  # noqa: E402
from make_loop import autocrop  # noqa: E402

W, H = 1920, 1080
FONT = '/usr/share/fonts/opentype/inter/Inter-Black.otf'
FONT_SUB = '/usr/share/fonts/opentype/inter/Inter-SemiBold.otf'


def crescent(size, color):
    """Полумесяц: круг минус смещённый круг, со свечением."""
    s = size * 3
    m = Image.new('L', (s, s), 0)
    d = ImageDraw.Draw(m)
    d.ellipse((s // 2 - size // 2, s // 2 - size // 2, s // 2 + size // 2, s // 2 + size // 2), fill=255)
    off = int(size * 0.32)
    d.ellipse((s // 2 - size // 2 + off, s // 2 - size // 2 - off // 2, s // 2 + size // 2 + off, s // 2 + size // 2 - off // 2), fill=0)
    from PIL import ImageFilter
    glow = m.filter(ImageFilter.GaussianBlur(size * 0.35))
    lay = Image.new('RGBA', (s, s), (0, 0, 0, 0))
    lay.paste(Image.new('RGBA', (s, s), (255, 170, 40, 0)), mask=glow.point(lambda v: int(v * 0.8)))
    lay.paste(Image.new('RGBA', (s, s), color + (255,)), mask=m)
    return lay


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--title', default='Thank you for being here')
    ap.add_argument('--sub', default='Sweet dreams, and subscribe for more nights like this')
    ap.add_argument('--out', required=True)
    ap.add_argument('--preview', help='jpg с оверлеем поверх кадра сцены (для проверки)')
    ap.add_argument('--x', type=int, default=80)
    ap.add_argument('--y', type=int, default=64)
    ap.add_argument('--size-title', type=int, default=92)
    ap.add_argument('--size-sub', type=int, default=46)
    args = ap.parse_args()

    canvas = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    f1 = ImageFont.truetype(FONT, args.size_title)
    f2 = ImageFont.truetype(FONT_SUB, args.size_sub)
    lay, _ = text_layer(args.title, f1, (255, 246, 150), (255, 176, 20), (110, 40, 0), (255, 150, 20), 4)
    canvas.alpha_composite(lay, (args.x - 90, args.y - 90))
    title_w = lay.size[0] - 180
    title_h = lay.size[1] - 180
    moon = crescent(int(args.size_title * 0.62), (255, 226, 120))
    canvas.alpha_composite(moon, (args.x + title_w + 14 - moon.size[0] // 3, args.y + title_h // 2 - moon.size[1] // 2 + 4))
    lay2, _ = text_layer(args.sub, f2, (255, 255, 255), (214, 228, 255), (10, 18, 60), (90, 120, 230), 3)
    canvas.alpha_composite(lay2, (args.x - 90, args.y + title_h + 22 - 90))
    canvas.save(args.out)
    print(f'Готово: {args.out} ({W}x{H}, прозрачный)')

    if args.preview:
        im, _ = autocrop(Image.open(DEFAULT_IMAGE).convert('RGB'))
        iw, ih = im.size
        if iw / ih > W / H:
            nw = int(round(ih * W / H)); x0 = (iw - nw) // 2; im = im.crop((x0, 0, x0 + nw, ih))
        else:
            nh = int(round(iw * H / W)); y0 = (ih - nh) // 2; im = im.crop((0, y0, iw, y0 + nh))
        bg = im.resize((W, H), Image.LANCZOS).convert('RGBA')
        bg.alpha_composite(canvas)
        bg.convert('RGB').save(args.preview, quality=92)
        print(f'Превью: {args.preview}')


if __name__ == '__main__':
    main()
