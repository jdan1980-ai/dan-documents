#!/usr/bin/env python3
"""Build a StillWave wisdom overlay: 1920x1080 transparent PNG, channel-standard layout.

Three lines, LEFT-lower: 4 kanji (large, cream, faint warm glow), romaji (Liberation
Serif Bold 54), English gloss (Liberation Serif Bold 34), over a soft blurred dark
scrim so it reads on any background. Same geometry as every overlay since ENSO.

Usage:
  python make_overlay.py --kanji 一葉知秋 --romaji "Ichiyō chishū" \
      --gloss "One falling leaf tells of autumn" --out overlay.png \
      [--hero hero.jpg --preview preview.jpg] [--scrim 165]

With --hero, prints the brightness of the text zones and writes a composited JPG
preview for your own QA. Deliver only the transparent PNG to the user.
"""
import argparse
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageStat

W, H = 1920, 1080
CREAM = (245, 234, 210, 255)
SUB = (231, 224, 205, 255)
X = 96

KANJI_FONTS = [  # brush font first if the repo has it, then system Japanese fonts
    "stillwave/assets/fonts/YujiBoku-Regular.ttf",
    "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf",
    "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
]
SERIF_FONTS = [
    "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
]


def first_font(candidates, repo_root):
    # relative paths are tried against the repo root, then against the folder
    # three levels above this script (skills/stillwave-album/scripts -> repo root)
    roots = [repo_root, Path(__file__).resolve().parents[3]]
    for c in candidates:
        for p in ([Path(c)] if Path(c).is_absolute() else [r / c for r in roots]):
            if p.exists():
                return str(p)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kanji", required=True, help="the phrase, normally 4 kanji")
    ap.add_argument("--romaji", required=True)
    ap.add_argument("--gloss", required=True, help="short English gloss, 2-6 words")
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--hero", type=Path, help="hero frame, for zone brightness + preview")
    ap.add_argument("--preview", type=Path, help="where to write the composited QA preview JPG")
    ap.add_argument("--scrim", type=int, default=165,
                    help="scrim opacity 0-255; raise to ~200 when the lower-left is bright")
    ap.add_argument("--dx", type=int, default=0, help="shift the whole block right (px)")
    ap.add_argument("--dy", type=int, default=0,
                    help="shift the whole block down (px); negative moves it up, e.g. -470 for upper-left "
                         "when the figure stands in the lower-left")
    ap.add_argument("--repo", type=Path, default=Path.cwd(), help="repo root (for the brush font)")
    a = ap.parse_args()

    kfont_path = first_font(KANJI_FONTS, a.repo)
    sfont_path = first_font(SERIF_FONTS, a.repo)
    if not kfont_path or not sfont_path:
        sys.exit("No usable kanji or serif font found.")
    if "YujiBoku" not in kfont_path:
        print(f"note: brush font not found, using {Path(kfont_path).name} for the kanji")

    f = ImageFont.truetype(kfont_path, 108)
    chars = list(a.kanji)
    for ch in chars:  # a missing glyph renders as an empty box: refuse instead
        if f.getmask(ch).getbbox() is None:
            sys.exit(f"Font {Path(kfont_path).name} has no glyph for {ch!r}")

    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    s = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(s).rounded_rectangle((-200 + a.dx, 636 + a.dy, 950 + a.dx, 1060 + a.dy), radius=170,
                                        fill=(8, 6, 4, a.scrim))
    img.alpha_composite(s.filter(ImageFilter.GaussianBlur(100)))

    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    pitch, y0 = 128, 692 + a.dy
    l0, _, r0, _ = f.getbbox(chars[0])
    c0 = X + a.dx + (r0 - l0) / 2
    for i, ch in enumerate(chars):
        l, t, r, b = f.getbbox(ch)
        md.text((c0 + i * pitch - (l + (r - l) / 2), y0), ch, font=f, fill=255)
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    glow.paste((250, 220, 180, 255), (0, 0),
               mask.filter(ImageFilter.GaussianBlur(18)).point(lambda p: int(p * 0.45)))
    img.alpha_composite(glow)
    img.alpha_composite(Image.composite(Image.new("RGBA", (W, H), CREAM),
                                        Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))
    d = ImageDraw.Draw(img)
    d.text((X + 4 + a.dx, 866 + a.dy), a.romaji, font=ImageFont.truetype(sfont_path, 54), fill=CREAM)
    d.text((X + 4 + a.dx, 940 + a.dy), a.gloss, font=ImageFont.truetype(sfont_path, 34), fill=SUB)

    a.out.parent.mkdir(parents=True, exist_ok=True)
    img.save(a.out)
    bbox = img.getchannel("A").point(lambda p: 255 if p > 200 else 0).getbbox()
    print(f"saved {a.out}  text bbox {bbox}")
    if bbox and bbox[2] > 1000:
        print("warning: text runs past x=1000 — shorten the gloss")

    if a.hero:
        hero = Image.open(a.hero).convert("RGB").resize((W, H), Image.LANCZOS)
        g = hero.convert("L")
        for name, box in {"kanji row": (96 + a.dx, 692 + a.dy, 608 + a.dx, 790 + a.dy),
                          "romaji+gloss": (96 + a.dx, 860 + a.dy, 608 + a.dx, 980 + a.dy),
                          "full frame": (0, 0, W, H)}.items():
            print(f"brightness {name}: {ImageStat.Stat(g.crop(box)).mean[0]:.0f}")
        if a.preview:
            bg = hero.convert("RGBA")
            bg.alpha_composite(img)
            bg.convert("RGB").save(a.preview, quality=88)
            print(f"preview {a.preview}")


if __name__ == "__main__":
    main()
