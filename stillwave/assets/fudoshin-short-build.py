#!/usr/bin/env python3
"""FUDOSHIN Short builder — single hero, jitter-free Ken Burns in PIL (float crop).

The 6 vertical §3c frames were not generated, so the Short is built from the 16:9
hero (`fudoshin-2h-source.jpg`) centre-cropped to 9:16 — the samurai + waterfall
sit centred, so the vertical crop keeps the whole composition. One slow zoom-in
across the clip, rendered from float-precision crop boxes (never ffmpeg zoompan),
text beats composited with alpha fades, tail fade to black for a clean loop.
"""
from PIL import Image
from pathlib import Path
import numpy as np

A = Path("/home/user/dan-documents/stillwave/assets")
SP = Path("/tmp/claude-0/-home-user-dan-documents/48780e4d-ee5f-5a8f-92df-523468e19c72/scratchpad")
OUTDIR = SP / "fframes"
SRC = A / "fudoshin-2h-source.jpg"
W, H = 1080, 1920
FPS = 30
TOTAL = 34.0
ZOOM = 0.10          # 10% slow zoom-in across the whole clip

OVERLAYS = [
    ("fov_hook.png", 3.0, 9.5),
    ("fov_concept.png", 12.5, 19.5),
    ("fov_wisdom.png", 24.0, 31.5),
]
FADE = 0.9
END_FADE = 1.0


def load_cover(p):
    im = Image.open(p).convert("RGB")
    tw = im.height * W / H
    if im.width > tw:
        x = (im.width - tw) / 2
        im = im.crop((int(x), 0, int(x + tw), im.height))
    else:
        th = im.width * H / W
        y = (im.height - th) / 2
        im = im.crop((0, int(y), im.width, int(y + th)))
    return im


def kb_frame(src, prog):
    z = 1.0 + ZOOM * prog
    cw, ch = src.width / z, src.height / z
    x0, y0 = (src.width - cw) / 2.0, (src.height - ch) / 2.0
    return src.resize((W, H), Image.LANCZOS, box=(x0, y0, x0 + cw, y0 + ch))


def main():
    OUTDIR.mkdir(parents=True, exist_ok=True)
    for old in OUTDIR.glob("*.jpg"):
        old.unlink()
    src = load_cover(SRC)
    nframes = int(round(TOTAL * FPS))
    ovs = [(Image.open(SP / p).convert("RGBA"), a, b) for p, a, b in OVERLAYS]
    print(f"total {TOTAL}s -> {nframes} frames")
    for i in range(nframes):
        t = i / FPS
        frame = kb_frame(src, t / TOTAL)
        for ov, a, b in ovs:
            if a - FADE <= t <= b + FADE:
                if t < a:
                    al = (t - (a - FADE)) / FADE
                elif t > b:
                    al = 1.0 - (t - b) / FADE
                else:
                    al = 1.0
                al = max(0.0, min(1.0, al))
                if al > 0.003:
                    layer = ov if al >= 0.999 else Image.fromarray(
                        np.dstack([np.asarray(ov)[:, :, :3],
                                   (np.asarray(ov)[:, :, 3] * al).astype(np.uint8)]))
                    frame = Image.alpha_composite(frame.convert("RGBA"), layer).convert("RGB")
        if t > TOTAL - END_FADE:
            k = 1.0 - (t - (TOTAL - END_FADE)) / END_FADE
            frame = Image.fromarray((np.asarray(frame, dtype=np.float32) * max(0.0, k)).astype(np.uint8))
        frame.save(OUTDIR / f"f_{i:05d}.jpg", quality=95)
        if i % 150 == 0:
            print(f"  {i}/{nframes}", flush=True)
    print("frames done:", len(list(OUTDIR.glob('*.jpg'))))


if __name__ == "__main__":
    main()
