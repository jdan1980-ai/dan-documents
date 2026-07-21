#!/usr/bin/env python3
"""
Concept Shorts builder — educational "what does this concept mean" Shorts,
repurposed from the Community-Post essays. Funnels to the long-form session.

Difference from the teaser Shorts: these TEACH the concept (opens search traffic
— "what is wabi sabi", "ikigai meaning" — which our music videos never catch)
and reinforce the "we teach + play music" brand.

White titles top, jitter-free centered Ken Burns (4x supersample), no badge.
Reuses the existing teaser frames (wabi-sabi-shorts-fr*.jpg / mizu-shorts-fr*.jpg).

Usage:  python3 concept-shorts-build.py <slug>   (slug = wabi-sabi | mizu)
Output: <slug>-concept-short-42s.mp4
"""

import sys
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
W, H = 1080, 1920
FPS = 30
XFADE = 0.6

KANJI_FONT = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
WHITE = (255, 255, 255, 255)
SHADOW = (0, 0, 0, 210)

# payload for "lines": (list_of_lines, y0, size) ; for "kanji": (kanji, romaji)
CONFIGS = {
    "wabi-sabi": [
        ("wabi-sabi-shorts-fr1.jpg", 6.0, "lines", (["Why do the Japanese", "mend broken bowls", "with GOLD?"], 150, 74)),
        ("wabi-sabi-shorts-fr4.jpg", 6.0, "kanji", ("侘寂", "WABI SABI")),
        ("wabi-sabi-shorts-fr2.jpg", 6.0, "lines", (["Beauty in imperfection", "and impermanence"], 160, 76)),
        ("wabi-sabi-shorts-fr3.jpg", 6.0, "lines", (["Kintsugi — golden repair.", "The crack is not hidden"], 160, 72)),
        ("wabi-sabi-shorts-fr6.jpg", 6.0, "lines", (["It's honored as part", "of the object's story"], 160, 74)),
        ("wabi-sabi-shorts-fr7.jpg", 6.0, "lines", (["Nothing is perfect.", "And that is beautiful."], 160, 76)),
        ("wabi-sabi-shorts-fr5.jpg", 6.0, "lines", (["Full 2-hour session", "on the channel"], 160, 78)),
    ],
    "zanshin": [
        ("zanshin-shorts-fr1.jpg", 6.5, "lines", (["What calm does a samurai", "keep after the strike?"], 150, 74)),
        ("zanshin-shorts-fr2.jpg", 6.5, "kanji", ("残心", "ZANSHIN")),
        ("zanshin-shorts-fr3.jpg", 6.5, "lines", (["The awareness that stays", "after the moment passes"], 155, 72)),
        ("zanshin-shorts-fr4.jpg", 6.5, "lines", (["Guard never dropped.", "Breath still even."], 155, 76)),
        ("zanshin-shorts-fr5.jpg", 6.5, "lines", (["Off the mat —", "steady after a hard day"], 155, 74)),
        ("zanshin-shorts-fr6.jpg", 6.5, "lines", (["Full 2-hour session", "on the channel"], 155, 76)),
    ],
    "mizu": [
        ("mizu-shorts-fr1.jpg", 6.0, "lines", (["What does WATER mean", "to the Japanese?"], 160, 78)),
        ("mizu-shorts-fr4.jpg", 6.0, "kanji", ("水", "MIZU — water")),
        ("mizu-shorts-fr3.jpg", 6.0, "lines", (["“The highest good", "is like water”"], 160, 78)),
        ("mizu-shorts-fr5.jpg", 6.0, "lines", (["It never argues", "with the stone"], 160, 80)),
        ("mizu-shorts-fr2.jpg", 6.0, "lines", (["and always finds", "its own way"], 160, 80)),
        ("mizu-shorts-fr6.jpg", 6.0, "lines", (["Be like water —", "soft, unstoppable"], 160, 80)),
        ("mizu-shorts-fr1.jpg", 6.0, "lines", (["Full 2-hour session", "on the channel"], 160, 78)),
    ],
}


def _font(path, size):
    return ImageFont.truetype(path, size)


def _center(draw, y, text, font, spacing=2):
    total = draw.textlength(text, font=font) + spacing * (len(text) - 1)
    x = (W - total) / 2
    for ch in text:
        draw.text((x + 3, y + 3), ch, font=font, fill=SHADOW)
        draw.text((x, y), ch, font=font, fill=WHITE)
        x += draw.textlength(ch, font=font) + spacing


def make_overlays(story, work):
    work.mkdir(exist_ok=True)
    specs = []
    t = 0.0
    for i, (_, dur, kind, payload) in enumerate(story):
        img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        if kind == "kanji":
            kanji, romaji = payload
            ksize = 300 if len(kanji) == 1 else 250
            _center(d, 150, kanji, _font(KANJI_FONT, ksize), spacing=24)
            _center(d, 150 + ksize + 40, romaji, _font(SERIF_BOLD, 84), spacing=8)
        else:
            lines, y0, size = payload
            f = _font(SERIF_BOLD, size)
            y = y0
            for ln in lines:
                _center(d, y, ln, f)
                y += size + 24
        p = work / f"txt{i+1}.png"
        img.save(p)
        specs.append((p, max(0.5, t + 0.6), t + dur - 0.4))
        t += dur
    return specs


def build(slug):
    story = CONFIGS[slug]
    work = HERE / f"{slug}-concept-work"
    out = HERE / f"{slug}-concept-short-{int(round(sum(d for _, d, _, _ in CONFIGS[slug])))}s.mp4"
    total = sum(d for _, d, _, _ in story)

    missing = [f for f, *_ in story if not (HERE / f).exists()]
    if missing:
        sys.exit(f"Missing frames: {missing}")

    overlays = make_overlays(story, work)
    inputs, filters = [], []
    n = len(story)
    SS = 4
    for i, (frame, dur, _, _) in enumerate(story):
        fr = int((dur + XFADE) * FPS)
        zexpr = f"min(1.10,1.0+0.10*on/{fr})" if i % 2 == 0 else f"max(1.0,1.10-0.10*on/{fr})"
        inputs += ["-loop", "1", "-t", str(dur + XFADE), "-i", str(HERE / frame)]
        filters.append(
            f"[{i}:v]scale={W*SS}:{H*SS}:force_original_aspect_ratio=increase,"
            f"crop={W*SS}:{H*SS},zoompan=z='{zexpr}':d={fr}"
            f":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},format=yuv420p[v{i}]")

    cur, offset = "v0", 0.0
    for i in range(1, n):
        offset += story[i - 1][1]
        nxt = f"x{i}" if i < n - 1 else "base"
        filters.append(f"[{cur}][v{i}]xfade=transition=fade:duration={XFADE}:offset={offset}[{nxt}]")
        cur = nxt

    for j, (png, t0, t1) in enumerate(overlays):
        idx = n + j
        inputs += ["-loop", "1", "-t", str(total + 1), "-i", str(png)]
        filters.append(
            f"[{idx}:v]format=rgba,fade=t=in:st={t0}:d=0.5:alpha=1,"
            f"fade=t=out:st={t1 - 0.5}:d=0.5:alpha=1[o{j}];"
            f"[{cur}][o{j}]overlay=0:0:enable='between(t,{t0},{t1})'[c{j}]")
        cur = f"c{j}"

    cmd = ["ffmpeg", "-y", *inputs, "-filter_complex", ";".join(filters), "-map", f"[{cur}]",
           "-t", str(total), "-r", str(FPS), "-c:v", "libx264", "-preset", "medium",
           "-crf", "22", "-pix_fmt", "yuv420p", str(out)]
    print(f"[ffmpeg] {slug} concept short — {total:.0f}s…")
    subprocess.run(cmd, check=True, capture_output=True)
    print(f"Saved → {out}  ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in CONFIGS:
        sys.exit(f"Usage: concept-shorts-build.py <{'|'.join(CONFIGS)}>")
    build(sys.argv[1])
