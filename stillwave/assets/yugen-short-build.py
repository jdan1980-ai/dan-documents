#!/usr/bin/env python3
"""YUGEN Short builder — jitter-free Ken Burns rendered in PIL with FLOAT crop boxes.

Also respects the locked SHORTS SAFE ZONE (glyphs inside y 150-1450, x 60-880 of
1080x1920) — the YouTube Shorts player hides the bottom ~24% and right ~17%.

Why not ffmpeg zoompan: zoompan rounds its crop rectangle to whole pixels, so a slow
zoom advances in 1-px steps -> visible stutter. Here every frame is resampled
(LANCZOS) from a float-precision crop of the full-res source, so motion is smooth by
construction. Crossfades and text-overlay fades are blended in PIL too.

Output: raw frames -> ffmpeg (h264 + AAC music).
"""
from PIL import Image
from pathlib import Path
import numpy as np
import sys

U = Path("/root/.claude/uploads/48780e4d-ee5f-5a8f-92df-523468e19c72")
SP = Path("/tmp/claude-0/-home-user-dan-documents/48780e4d-ee5f-5a8f-92df-523468e19c72/scratchpad")
OUTDIR = SP / "yframes"
W, H = 1080, 1920
FPS = 30
SHOT = 6.5          # seconds per shot (including the outgoing crossfade)
XF = 0.8            # crossfade duration

# shot list: (image, zoom-in?)  order = hook -> ridges -> empty(kanji) -> moon -> samurai -> dissolve
SHOTS = [
    ("5efe0d4a-1000204368.jpg", True),
    ("5960dc19-1000204372.jpg", False),
    ("4853d1c3-1000204370.jpg", True),
    ("24c95133-1000204371.jpg", False),
    ("c601bf36-1000204369.jpg", True),
    ("799d329e-1000204373.jpg", True),
]
ZOOM = 0.10         # 10% travel

# text overlays: (png, fade-in start, fade-out end)  ~1s fades
OVERLAYS = [
    ("yov_hook.png", 3.5, 9.5),
    ("yov_concept.png", 12.4, 17.6),
    ("yov_wisdom.png", 29.4, 33.2),   # on the final dissolving shot — samurai reveal stays text-free
]
FADE = 0.9
END_FADE = 0.9      # fade to black at the tail for a clean loop


def load_cover(p):
    """load source, centre-crop to exactly 9:16 so no stretching is needed"""
    im = Image.open(p).convert("RGB")
    tw = im.height * W / H
    if im.width > tw:                       # too wide -> crop sides
        x = (im.width - tw) / 2
        im = im.crop((int(x), 0, int(x + tw), im.height))
    else:                                   # too tall -> crop top/bottom
        th = im.width * H / W
        y = (im.height - th) / 2
        im = im.crop((0, int(y), im.width, int(y + th)))
    return im


def kb_frame(src, prog, zoom_in):
    """one Ken Burns frame at progress 0..1 — FLOAT crop box, centred"""
    z = (1.0 + ZOOM * prog) if zoom_in else (1.0 + ZOOM * (1.0 - prog))
    cw, ch = src.width / z, src.height / z
    x0, y0 = (src.width - cw) / 2.0, (src.height - ch) / 2.0
    return src.resize((W, H), Image.LANCZOS, box=(x0, y0, x0 + cw, y0 + ch))


def main():
    OUTDIR.mkdir(parents=True, exist_ok=True)
    for old in OUTDIR.glob("*.jpg"):
        old.unlink()

    srcs = [load_cover(U / f) for f, _ in SHOTS]
    n = len(SHOTS)
    step = SHOT - XF                          # 5.7s between shot starts
    total = step * (n - 1) + SHOT             # 35.0s
    nframes = int(round(total * FPS))
    ovs = [(Image.open(SP / p).convert("RGBA"), a, b) for p, a, b in OVERLAYS]

    print(f"total {total:.2f}s -> {nframes} frames")
    for i in range(nframes):
        t = i / FPS
        # active shots + blend weight
        layers = []
        for s in range(n):
            s0 = s * step
            s1 = s0 + SHOT
            if s0 - 1e-6 <= t < s1:
                prog = (t - s0) / SHOT
                w = 1.0
                if s > 0 and t < s0 + XF:                    # incoming half of a crossfade
                    w = (t - s0) / XF
                if s < n - 1 and t > s0 + step:              # outgoing half
                    w = 1.0 - (t - (s0 + step)) / XF
                layers.append((s, prog, max(0.0, min(1.0, w))))
        if not layers:
            layers = [(n - 1, 1.0, 1.0)]

        if len(layers) == 1:
            s, prog, _ = layers[0]
            frame = kb_frame(srcs[s], prog, SHOTS[s][1])
        else:
            (sa, pa, wa), (sb, pb, wb) = layers[0], layers[1]
            A = np.asarray(kb_frame(srcs[sa], pa, SHOTS[sa][1]), dtype=np.float32)
            B = np.asarray(kb_frame(srcs[sb], pb, SHOTS[sb][1]), dtype=np.float32)
            f = wb / max(1e-6, wa + wb)
            frame = Image.fromarray(np.clip(A * (1 - f) + B * f, 0, 255).astype(np.uint8))

        # text overlays with smooth alpha fades
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

        # tail fade to black
        if t > total - END_FADE:
            k = 1.0 - (t - (total - END_FADE)) / END_FADE
            frame = Image.fromarray((np.asarray(frame, dtype=np.float32) * max(0.0, k)).astype(np.uint8))

        frame.save(OUTDIR / f"f_{i:05d}.jpg", quality=95)
        if i % 150 == 0:
            print(f"  {i}/{nframes}", flush=True)

    print("frames done:", len(list(OUTDIR.glob('*.jpg'))))


if __name__ == "__main__":
    main()
