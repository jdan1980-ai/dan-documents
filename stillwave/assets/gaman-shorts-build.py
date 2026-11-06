#!/usr/bin/env python3
"""
GAMAN — 我慢 | Shorts builder (35 sec, 1080x1920).

Storyboard (locked in scripts/gaman-2h.md §14):
  Frame 1  0-4 s   HOOK   "Why do the Japanese never give up?"
  Frame 2  4-25 s  REVEAL 我慢 / GAMAN -> "To endure the unbearable..." -> "Samurai..."
  Frame 3  25-35 s CTA    "Full 2-hour session" + StillWave logo lower third

Inputs (drop next to this script):
  gaman-shorts-frame1.jpg   NanoBanana 9:16 — rain on temple courtyard (hook)
  gaman-shorts-frame2.jpg   NanoBanana 9:16 — monk + scroll (§3b of the script)
  gaman-shorts-frame3.jpg   NanoBanana 9:16 — incense smoke close-up (CTA)
  (any missing frame is rendered as a stylized MOCK so the cut can be previewed)

Usage:
  python3 gaman-shorts-build.py                 # silent video
  python3 gaman-shorts-build.py --audio X.mp3   # with album track (trimmed to 35 s)

Output:
  gaman-shorts-35s.mp4  (+ overlay PNGs in ./gaman-shorts-work/)
"""

import argparse
import math
import random
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = Path(__file__).parent
WORK = HERE / "gaman-shorts-work"
OUT = HERE / "gaman-shorts-35s.mp4"

W, H = 1080, 1920
FPS = 30
DUR = [4.0, 21.0, 10.0]          # frame durations, total 35 s
XFADE = 0.6

KANJI_FONT = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
CREAM = (245, 234, 210, 255)     # #F5EAD2 — locked channel cream
INK = (28, 24, 20, 255)          # sumi ink — kanji over the ivory scroll
SHADOW = (0, 0, 0, 200)

LOGO = HERE / "stillwave-badge-800.png"

FRAMES = [HERE / f"gaman-shorts-frame{i}.jpg" for i in (1, 2, 3)]

# ---------------------------------------------------------------- overlays

def _font(path, size):
    return ImageFont.truetype(path, size)


def _center(draw, y, text, font, canvas_w=W, fill=CREAM, spacing=2, shadow=True):
    total = draw.textlength(text, font=font) + spacing * (len(text) - 1)
    x = (canvas_w - total) / 2
    for ch in text:
        if shadow:
            draw.text((x + 3, y + 3), ch, font=font, fill=SHADOW)
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + spacing


def _multiline(img, lines, y0, size, gap=18):
    d = ImageDraw.Draw(img)
    f = _font(SERIF_BOLD, size)
    y = y0
    for ln in lines:
        _center(d, y, ln, f)
        y += size + gap


def make_overlays():
    WORK.mkdir(exist_ok=True)
    specs = []

    # T1 — hook (frame 1)
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    _multiline(img, ["Why do the Japanese", "never give up?"], 700, 78, gap=26)
    p = WORK / "t1-hook.png"; img.save(p)
    specs.append((p, 0.5, 3.9))

    # T2a — kanji + romaji, dark sumi ink over the ivory scroll (frame 2 upper half)
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    kf = _font(KANJI_FONT, 300)
    _center(d, 400, "我慢", kf, fill=INK, spacing=20, shadow=False)
    rf = _font(SERIF_BOLD, 86)
    _center(d, 790, "GAMAN", rf, fill=INK, spacing=10, shadow=False)
    p = WORK / "t2a-kanji.png"; img.save(p)
    specs.append((p, 4.6, 10.5))

    # T2b — meaning (cream, lower dark zone between scroll and monk)
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    _multiline(img, ["To endure the unbearable", "with quiet dignity"], 1180, 72, gap=26)
    p = WORK / "t2b-meaning.png"; img.save(p)
    specs.append((p, 10.5, 17.5))

    # T2c — samurai line (cream, same dark zone)
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    _multiline(img, ["Samurai trained", "their minds with this"], 1180, 72, gap=26)
    p = WORK / "t2c-samurai.png"; img.save(p)
    specs.append((p, 17.5, 24.4))

    # T3 — CTA (frame 3) — YouTube wording, NOT "link in bio"
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    _multiline(img, ["Full 2-hour session", "on the channel"], 760, 76, gap=26)
    if LOGO.exists():
        logo = Image.open(LOGO).convert("RGBA")
        lw = 220
        logo = logo.resize((lw, int(logo.height * lw / logo.width)), Image.LANCZOS)
        img.alpha_composite(logo, ((W - lw) // 2, 1440))
    p = WORK / "t3-cta.png"; img.save(p)
    specs.append((p, 25.6, 34.5))

    return specs

# ---------------------------------------------------------------- mock frames

def make_mock(path, variant):
    """Stylized charcoal placeholder so the cut previews before NanoBanana art."""
    rng = random.Random(variant)
    img = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(img)
    for y in range(H):                              # charcoal gradient
        v = int(18 + 30 * y / H)
        d.line([(0, y), (W, y)], fill=(v, v, v + 4))

    if variant == 2:                                # ivory scroll (kanji overlay lands here)
        d.rectangle([120, 160, 960, 1000], fill=(224, 214, 190))
        d.rectangle([120, 160, 960, 1000], outline=(150, 138, 112), width=6)
    if variant in (1, 3):                           # rain streaks
        for _ in range(220):
            x = rng.randint(0, W); y = rng.randint(0, H)
            d.line([(x, y), (x - 6, y + rng.randint(40, 90))],
                   fill=(70, 72, 78), width=1)
    # monk silhouette
    cx, top = W // 2, 1150
    d.ellipse([cx - 70, top, cx + 70, top + 140], fill=(12, 12, 13))
    d.polygon([(cx - 230, top + 480), (cx + 230, top + 480), (cx + 150, top + 90),
               (cx - 150, top + 90)], fill=(12, 12, 13))
    # incense smoke
    for t in range(0, 600, 4):
        x = cx + int(26 * math.sin(t / 60)); y = top - t
        if y < 0: break
        d.ellipse([x - 3, y - 3, x + 3, y + 3], fill=(120, 120, 122))
    img = img.filter(ImageFilter.GaussianBlur(1.2))
    d = ImageDraw.Draw(img)
    d.text((30, 30), "MOCK — replace with NanoBanana frame",
           font=_font(SERIF_BOLD, 34), fill=(110, 108, 100))
    img.save(path, "JPEG", quality=90)

# ---------------------------------------------------------------- assembly

def build(audio):
    for i, f in enumerate(FRAMES, 1):
        if not f.exists():
            print(f"[mock] {f.name} missing — rendering placeholder")
            make_mock(f, i)

    overlays = make_overlays()

    inputs, filters = [], []
    for i, (frame, dur) in enumerate(zip(FRAMES, DUR)):
        inputs += ["-loop", "1", "-t", str(dur + XFADE), "-i", str(frame)]
        z = 1.0 + 0.06 * (dur + XFADE) / 21          # gentle Ken Burns
        filters.append(
            f"[{i}:v]scale={W}:{H}:force_original_aspect_ratio=increase,"
            f"crop={W}:{H},zoompan=z='min(zoom+0.0004,{1.12})':d={int((dur+XFADE)*FPS)}"
            f":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},"
            f"format=yuv420p[v{i}]")
    filters.append(f"[v0][v1]xfade=transition=fade:duration={XFADE}:offset={DUR[0]}[x1]")
    filters.append(f"[x1][v2]xfade=transition=fade:duration={XFADE}:offset={DUR[0]+DUR[1]}[base]")

    cur = "base"
    for j, (png, t0, t1) in enumerate(overlays):
        idx = len(FRAMES) + j
        inputs += ["-loop", "1", "-t", "36", "-i", str(png)]
        filters.append(
            f"[{idx}:v]format=rgba,fade=t=in:st={t0}:d=0.5:alpha=1,"
            f"fade=t=out:st={t1 - 0.5}:d=0.5:alpha=1[o{j}];"
            f"[{cur}][o{j}]overlay=0:0:enable='between(t,{t0},{t1})'[c{j}]")
        cur = f"c{j}"

    cmd = ["ffmpeg", "-y", *inputs]
    maps = ["-map", f"[{cur}]"]
    if audio:
        cmd += ["-i", str(audio)]
        filters.append(
            f"[{len(FRAMES)+len(overlays)}:a]atrim=0:35,afade=t=in:d=1,"
            f"afade=t=out:st=33:d=2[aud]")
        maps += ["-map", "[aud]", "-c:a", "aac", "-b:a", "192k"]
    cmd += ["-filter_complex", ";".join(filters), *maps,
            "-t", "35", "-r", str(FPS), "-c:v", "libx264", "-preset", "medium",
            "-crf", "20", "-pix_fmt", "yuv420p", str(OUT)]

    print("[ffmpeg] assembling…")
    subprocess.run(cmd, check=True, capture_output=True)
    print(f"Saved → {OUT}  ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--audio", type=Path, default=None,
                    help="album track for the soundtrack (trimmed to 35 s)")
    args = ap.parse_args()
    if args.audio and not args.audio.exists():
        sys.exit(f"Audio not found: {args.audio}")
    build(args.audio)
