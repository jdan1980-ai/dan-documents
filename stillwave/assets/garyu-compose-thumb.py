#!/usr/bin/env python3
"""
garyu-compose-thumb.py — превью 16:9 и wisdom-оверлей для GARYŪ из кадра-героя.

  python3 garyu-compose-thumb.py hero.jpg [-o outdir]

Кладёт рядом:
  garyu-thumb.jpg            1280x720, превью для загрузки
  garyu-thumb-168.png        то же в ширину ленты — проверка читаемости
  garyu-wisdom-overlay.png   1920x1080 прозрачный PNG, верхняя дорожка в CapCut
  garyu-wisdom-preview.jpg   оверлей поверх героя — только посмотреть

Почему кроп именно такой (§10: «маска — это превью»). В полном кадре шлем
занимает 38% ширины: в ленте на 168 px это 64 px, и оскал менпо превращается
в тёмное пятно. Кроп x900 w1494 поднимает шлем до 61% (102 px) — маска
читается, и при этом в кадре остаётся фигура спиной с хвостом и дымный дракон
силуэтом на золоте. Более тесный кроп (68%) читается ещё лучше, но выбрасывает
человека, а фигура спиной к камере — проверенный сигнал шаблона Kanji-Concept.

Шрифт кандзи — Noto Serif JP Bold (минтё), под латиницу Liberation Serif Bold,
единственный шрифт канала. Если Noto нет в системе, скачать:
  curl -sS "https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@700" \
    | grep -o 'https://fonts.gstatic.com[^)]*' | head -1 | xargs curl -sS -o NotoSerifJP-Bold.otf
"""

import argparse
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

CREAM = (245, 234, 210)
GOLD = (228, 196, 108)
LS = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
LSI = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
JP_CANDIDATES = [
    "/tmp/NotoSerifJP-Bold.otf",
    "NotoSerifJP-Bold.otf",
    "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc",
    "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf",  # запасной, гротеск
]

CROP = None                     # кадр героя не режем — только текст поверх
KANJI, ROMAJI, GLOSS = "臥龍", "Seichū no dō", "MOVEMENT  WITHIN  STILLNESS"
WISDOM_KANJI = "静中動"


def jp_font(size):
    for p in JP_CANDIDATES:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    raise SystemExit("не найден японский шрифт — см. docstring")


def opaque_bbox(img, pct=True):
    a = np.asarray(img)[:, :, 3]
    ys, xs = np.where(a > 200)
    w, h = img.size
    if pct:
        return xs.min() / w * 100, xs.max() / w * 100, ys.min() / h * 100, ys.max() / h * 100
    return xs.min(), xs.max(), ys.min(), ys.max()


def build_thumb(hero, out):
    if CROP:
        x, y, w = CROP
        h = round(w * 9 / 16)
        y = min(y, hero.size[1] - h)
        hero = hero.crop((x, y, x + w, y + h))
    th = hero.resize((1280, 720), Image.LANCZOS)
    TW, TH = th.size
    layer = Image.new("RGBA", (TW, TH), (0, 0, 0, 0))

    # 臥龍 縦書き слева, тёмный ореол — золото по золоту иначе тонет
    # тёмная вертикальная полоса на стыке панелей ширмы: x 20–28%, яркость 22–27
    size = 118
    fk = jp_font(size)
    kx, ky = int(TW * 0.205), int(TH * 0.06)
    halo = Image.new("RGBA", (TW, TH), (0, 0, 0, 0))
    dh = ImageDraw.Draw(halo)
    for i, c in enumerate(KANJI):
        dh.text((kx, ky + i * int(size * 1.18)), c, font=fk, fill=(0, 0, 0, 190))
    layer = Image.alpha_composite(layer, halo.filter(ImageFilter.GaussianBlur(28)))
    dl = ImageDraw.Draw(layer)
    for i, c in enumerate(KANJI):
        dl.text((kx, ky + i * int(size * 1.18)), c, font=fk, fill=GOLD + (255,))

    # GARYŪ низом по тёмному переднему плану, мягкий скрим вместо обводки
    fg = ImageFont.truetype(LS, 76)
    tw = dl.textlength("GARYŪ", font=fg)
    gx, gy = int(TW * 0.055), int(TH * 0.835)
    scr = Image.new("RGBA", (TW, TH), (0, 0, 0, 0))
    ImageDraw.Draw(scr).rounded_rectangle(
        [gx - 30, gy - 20, gx + tw + 30, gy + 92], 28, fill=(0, 0, 0, 115))
    layer = Image.alpha_composite(scr.filter(ImageFilter.GaussianBlur(30)), layer)
    ImageDraw.Draw(layer).text((gx, gy), "GARYŪ", font=fg, fill=GOLD + (255,))

    res = Image.alpha_composite(th.convert("RGBA"), layer).convert("RGB")
    res.save(out / "garyu-thumb.jpg", quality=94)
    res.resize((168, 94), Image.LANCZOS).save(out / "garyu-thumb-168.png")

    g = np.asarray(res.convert("L"), dtype=np.float32)
    corner = g[int(TH * 0.78):, int(TW * 0.80):].mean()
    print(f"thumb   угол логотипа: яркость {corner:.0f} {'ok' if corner < 60 else 'СВЕТЛО'}")
    print("        текст: x {:.1f}–{:.1f}%  y {:.1f}–{:.1f}%".format(*opaque_bbox(layer)))


def build_overlay(hero, out):
    W, H = 1920, 1080
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    x, y = int(W * 0.075), int(H * 0.60)
    d.text((x, y), WISDOM_KANJI, font=jp_font(132), fill=CREAM + (255,))
    y += 132 + 34
    d.text((x, y), ROMAJI, font=ImageFont.truetype(LSI, 54), fill=CREAM + (230,))
    y += 54 + 22
    d.text((x, y), GLOSS, font=ImageFont.truetype(LS, 34), fill=CREAM + (200,))
    ov.save(out / "garyu-wisdom-overlay.png")

    bg = hero.resize((W, H), Image.LANCZOS)
    Image.alpha_composite(bg.convert("RGBA"), ov).convert("RGB").save(
        out / "garyu-wisdom-preview.jpg", quality=92)

    x0, x1, y0, y1 = opaque_bbox(ov, pct=False)
    z = np.asarray(bg.convert("L"), dtype=np.float32)[y0:y1, x0:x1]
    print(f"overlay текст: x {x0/W*100:.1f}–{x1/W*100:.1f}%  y {y0/H*100:.1f}–{y1/H*100:.1f}%")
    print(f"        фон под ним: яркость {z.mean():.0f} {'ok, кремовый читается' if z.mean() < 70 else 'СВЕТЛО'}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("hero", type=Path)
    ap.add_argument("-o", "--out", type=Path, default=Path("."))
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)
    hero = Image.open(a.hero).convert("RGB")
    build_thumb(hero, a.out)
    build_overlay(hero, a.out)


if __name__ == "__main__":
    main()
