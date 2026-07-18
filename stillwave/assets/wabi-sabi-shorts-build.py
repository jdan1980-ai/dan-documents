#!/usr/bin/env python3
"""
WABI SABI — 侘寂 | Shorts builder (35 sec, 1080x1920).

Storyboard (scripts/wabi-sabi-2h.md §14):
  Frame 1  0-4 s   HOOK   "Why do the Japanese fill cracks with GOLD?"
  Frame 2  4-25 s  REVEAL 侘寂 / WABI SABI -> "Beauty in imperfection" -> "The break becomes..."
  Frame 3  25-35 s CTA    "Full 2-hour session on the channel" + StillWave badge

Inputs (drop next to this script):
  wabi-sabi-shorts-frame1.jpg   NanoBanana 9:16 — broken shards on dark wood (hook)
  wabi-sabi-shorts-frame2.jpg   NanoBanana 9:16 — kintsugi bowl in black void (reveal)
  wabi-sabi-shorts-frame3.jpg   NanoBanana 9:16 — tea ceremony / gold seam macro (CTA)
  wabi-sabi-shorts-audio.mp3    one album track (trimmed to 35 s, fade in/out)
  (any missing frame is rendered as a labeled MOCK so the cut can be previewed)

Usage:
  python3 wabi-sabi-shorts-build.py                     # silent video
  python3 wabi-sabi-shorts-build.py --audio track.mp3   # with soundtrack

Output:
  wabi-sabi-shorts-35s.mp4  (+ overlay PNGs in ./wabi-sabi-shorts-work/)
"""

import argparse
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = Path(__file__).parent
WORK = HERE / "wabi-sabi-shorts-work"
OUT = HERE / "wabi-sabi-shorts-35s.mp4"

W, H = 1080, 1920
FPS = 30
DUR = [4.0, 21.0, 10.0]          # frame durations, total 35 s
XFADE = 0.6

KANJI_FONT = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
GOLD = (228, 186, 92, 255)       # kintsugi gold — matches the covers
SHADOW = (0, 0, 0, 210)

LOGO = HERE / "stillwave-badge-800.png"

FRAMES = [HERE / f"wabi-sabi-shorts-frame{i}.jpg" for i in (1, 2, 3)]

# ---------------------------------------------------------------- overlays

def _font(path, size):
    return ImageFont.truetype(path, size)


def _center(draw, y, text, font, fill=GOLD, spacing=2, shadow=True):
    total = draw.textlength(text, font=font) + spacing * (len(text) - 1)
    x = (W - total) / 2
    for ch in text:
        if shadow:
            draw.text((x + 3, y + 3), ch, font=font, fill=SHADOW)
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + spacing


def _multiline(img, lines, y0, size, gap=20):
    d = ImageDraw.Draw(img)
    f = _font(SERIF_BOLD, size)
    y = y0
    for ln in lines:
        _center(d, y, ln, f)
        y += size + gap


def make_overlays():
    WORK.mkdir(exist_ok=True)
    specs = []

    # T1 — hook (frame 1, over the dark upper half)
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    _multiline(img, ["Why do the Japanese", "fill cracks with GOLD?"], 640, 82, gap=28)
    p = WORK / "t1-hook.png"; img.save(p)
    specs.append((p, 0.5, 3.9))

    # T2a — kanji + romaji over the black void above the bowl
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    kf = _font(KANJI_FONT, 280)
    _center(d, 180, "侘寂", kf, spacing=30)
    rf = _font(SERIF_BOLD, 92)
    _center(d, 560, "WABI SABI", rf, spacing=8)
    p = WORK / "t2a-kanji.png"; img.save(p)
    specs.append((p, 4.6, 11.0))

    # T2b — meaning (over the dark floor below the bowl)
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    _multiline(img, ["Beauty in imperfection"], 1620, 76)
    p = WORK / "t2b-meaning.png"; img.save(p)
    specs.append((p, 11.0, 17.5))

    # T2c — the line
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    _multiline(img, ["The break becomes", "the most beautiful line"], 1560, 72, gap=26)
    p = WORK / "t2c-line.png"; img.save(p)
    specs.append((p, 17.5, 24.4))

    # T3 — CTA + badge
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    _multiline(img, ["Full 2-hour session", "on the channel"], 640, 78, gap=26)
    if LOGO.exists():
        logo = Image.open(LOGO).convert("RGBA")
        lw = 230
        logo = logo.resize((lw, int(logo.height * lw / logo.width)), Image.LANCZOS)
        img.alpha_composite(logo, ((W - lw) // 2, 1420))
    p = WORK / "t3-cta.png"; img.save(p)
    specs.append((p, 25.6, 34.5))

    return specs

# ---------------------------------------------------------------- mock frames

def make_mock(path, variant):
    """Charcoal placeholder with a gold 'crack' so the cut previews before art."""
    img = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(img)
    for y in range(H):
        v = int(10 + 22 * y / H)
        d.line([(0, y), (W, y)], fill=(v, v - 2, v - 4))
    # stylized gold crack
    pts = [(200, 1500), (420, 1180), (560, 1260), (700, 900), (860, 980)]
    if variant == 1:
        pts = [(150, 1600), (400, 1400), (620, 1520), (900, 1350)]
    if variant == 3:
        pts = [(100, 1000), (980, 940)]
    d.line(pts, fill=(228, 186, 92), width=8)
    img = img.filter(ImageFilter.GaussianBlur(0.8))
    d = ImageDraw.Draw(img)
    d.text((30, 30), f"MOCK frame {variant} — replace with NanoBanana",
           font=_font(SERIF_BOLD, 34), fill=(120, 112, 96))
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
    ap.add_argument("--audio", type=Path, default=None)
    args = ap.parse_args()
    if args.audio and not args.audio.exists():
        sys.exit(f"Audio not found: {args.audio}")
    build(args.audio)
