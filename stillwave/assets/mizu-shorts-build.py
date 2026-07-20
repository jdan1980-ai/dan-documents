#!/usr/bin/env python3
"""
MIZU — 水 | Shorts builder (44 sec, 1080x1920, 6 frames).

All titles GOLD, placed in the UPPER third (Shorts UI covers the bottom).
No badge/logo. Ken Burns slow zoom + fade crossfades. Adapted from wabi-sabi-shorts-build.py.

Storyboard:
  1  0-7    hero macro pour   "This sound has calmed / Japan for centuries"
  2  7-14   koi pond misty    "The tsukubai — / a garden water basin"
  3  14-21  wide rock garden  "Water never argues / with the stone"
  4  21-29  tsukubai pour     水 + MIZU + water   (kanji frame)
  5  29-36  mossy basin macro "Be like water — / soft, unstoppable"
  6  36-44  autumn temple     "2 hours of garden calm / on the channel"

Inputs: mizu-shorts-fr1.jpg … fr6.jpg (+ optional --audio track.mp3)
Output: mizu-shorts-44s.mp4
"""

import argparse
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
WORK = HERE / "mizu-shorts-work"
OUT = HERE / "mizu-shorts-44s.mp4"

W, H = 1080, 1920
FPS = 30
XFADE = 0.6

KANJI_FONT = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
GOLD = (228, 196, 108, 255)          # #E4C46C
SHADOW = (0, 0, 0, 210)

# (file, duration, kind, payload)
#   kind "lines": payload = (list of lines, y0, size)
#   kind "kanji": payload = None  (水 + MIZU block)
STORY = [
    ("mizu-shorts-fr1.jpg", 7.0, "lines", (["This sound has calmed", "Japan for centuries"], 165, 78)),
    ("mizu-shorts-fr2.jpg", 7.0, "lines", (["The tsukubai —", "a garden water basin"], 165, 78)),
    ("mizu-shorts-fr3.jpg", 7.0, "lines", (["Water never argues", "with the stone"], 165, 80)),
    ("mizu-shorts-fr4.jpg", 8.0, "kanji", None),
    ("mizu-shorts-fr5.jpg", 7.0, "lines", (["Be like water —", "soft, unstoppable"], 165, 80)),
    ("mizu-shorts-fr6.jpg", 8.0, "lines", (["2 hours of garden calm", "on the channel"], 165, 78)),
]
TOTAL = sum(d for _, d, _, _ in STORY)


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


def make_overlays():
    WORK.mkdir(exist_ok=True)
    specs = []
    t = 0.0
    for i, (_, dur, kind, payload) in enumerate(STORY):
        img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        if kind == "kanji":
            _center(d, 150, "水", _font(KANJI_FONT, 300), spacing=0)
            _center(d, 500, "MIZU", _font(SERIF_BOLD, 96), spacing=10)
            _center(d, 610, "water", _font(SERIF_BOLD, 56), spacing=4)
        else:
            lines, y0, size = payload
            f = _font(SERIF_BOLD, size)
            y = y0
            for ln in lines:
                _center(d, y, ln, f)
                y += size + 26
        p = WORK / f"txt{i+1}.png"
        img.save(p)
        t0 = max(0.5, t + 0.6)
        t1 = t + dur - 0.4
        specs.append((p, t0, t1))
        t += dur
    return specs


def build(audio):
    missing = [f for f, *_ in STORY if not (HERE / f).exists()]
    if missing:
        sys.exit(f"Missing frames: {missing}")

    overlays = make_overlays()

    inputs, filters = [], []
    n = len(STORY)
    for i, (frame, dur, _, _) in enumerate(STORY):
        inputs += ["-loop", "1", "-t", str(dur + XFADE), "-i", str(HERE / frame)]
        filters.append(
            f"[{i}:v]scale={W}:{H}:force_original_aspect_ratio=increase,"
            f"crop={W}:{H},zoompan=z='min(zoom+0.0004,1.12)':d={int((dur+XFADE)*FPS)}"
            f":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},"
            f"format=yuv420p[v{i}]")

    cur = "v0"
    offset = 0.0
    for i in range(1, n):
        offset += STORY[i - 1][1]
        nxt = f"x{i}" if i < n - 1 else "base"
        filters.append(f"[{cur}][v{i}]xfade=transition=fade:duration={XFADE}:offset={offset}[{nxt}]")
        cur = nxt

    for j, (png, t0, t1) in enumerate(overlays):
        idx = n + j
        inputs += ["-loop", "1", "-t", str(TOTAL + 1), "-i", str(png)]
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
            f"[{n+len(overlays)}:a]atrim=0:{TOTAL},afade=t=in:d=1,"
            f"afade=t=out:st={TOTAL-2}:d=2[aud]")
        maps += ["-map", "[aud]", "-c:a", "aac", "-b:a", "192k"]
    cmd += ["-filter_complex", ";".join(filters), *maps,
            "-t", str(TOTAL), "-r", str(FPS), "-c:v", "libx264", "-preset", "medium",
            "-crf", "20", "-pix_fmt", "yuv420p", str(OUT)]

    print(f"[ffmpeg] assembling {TOTAL:.0f}s…")
    subprocess.run(cmd, check=True, capture_output=True)
    print(f"Saved → {OUT}  ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--audio", type=Path, default=None)
    args = ap.parse_args()
    if args.audio and not args.audio.exists():
        sys.exit(f"Audio not found: {args.audio}")
    build(args.audio)
