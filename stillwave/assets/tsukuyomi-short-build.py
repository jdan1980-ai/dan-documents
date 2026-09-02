#!/usr/bin/env python3
"""TSUKUYOMI Short builder — 6 vertical shots, jitter-free Ken Burns (PIL float crop).

fr1 = the long-form THUMBNAIL itself (title already baked in, letterboxed into
9:16 with a blurred cover-fit background) — no text overlay needed on it.
fr2 moon rabbit macro · fr3 moon-god close portrait, lotus + gohei
fr4 moonlight beam over clean night sky · fr5 luminous lotus macro on the water
fr6 extreme wide, tiny monk + tiny distant god across the lake

Per user feedback (2026-09-01): the wisdom phrase 明月清風 (Meigetsu seifu / "a
bright moon, a clear wind") is now broken into ONE PIECE PER FRAME 2-6 instead
of one caption stretched across the whole video — shot 2->明, 3->月, 4->清,
5->風, 6->romaji+gloss (phrase resolves on the last shot).
"""
from PIL import Image
from pathlib import Path
import numpy as np

A = Path("/home/user/dan-documents/stillwave/assets")
SP = Path("/tmp/claude-0/-home-user-dan-documents/48780e4d-ee5f-5a8f-92df-523468e19c72/scratchpad")
OUTDIR = SP / "tsukuyomi_shframes"
W, H = 1080, 1920
FPS = 30
SHOT = 6.5
XF = 0.8

SHOTS = [
    ("tsukuyomi-shorts-fr1.jpg", True),
    ("tsukuyomi-shorts-fr2.jpg", False),
    ("tsukuyomi-shorts-fr3.jpg", True),
    ("tsukuyomi-shorts-fr4.jpg", False),
    ("tsukuyomi-shorts-fr5.jpg", True),
    ("tsukuyomi-shorts-fr6.jpg", False),
]
ZOOM = 0.10

# step = 5.7, total = 5.7*5 + 6.5 = 35.0s. Shot 1 = the thumbnail (no overlay,
# title already baked in). One piece of 明月清風 per remaining shot, each
# timed to its shot's stable (post-crossfade) window so it never collides
# with the crossfade transitions or with another beat.
OVERLAYS = [
    ("tsukv_c1.png", 7.0, 10.9),    # shot 2 -> 明
    ("tsukv_c2.png", 12.7, 16.6),   # shot 3 -> 月
    ("tsukv_c3.png", 18.4, 22.3),   # shot 4 -> 清
    ("tsukv_c4.png", 24.1, 28.0),   # shot 5 -> 風
    ("tsukv_c5.png", 29.8, 34.0),   # shot 6 -> Meigetsu seifu / gloss
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
    return im.resize((W * 2, H * 2), Image.LANCZOS)


def kb_frame(src, prog, zoom_in):
    z = (1.0 + ZOOM * prog) if zoom_in else (1.0 + ZOOM * (1.0 - prog))
    cw, ch = src.width / z, src.height / z
    x0, y0 = (src.width - cw) / 2.0, (src.height - ch) / 2.0
    return src.resize((W, H), Image.LANCZOS, box=(x0, y0, x0 + cw, y0 + ch))


def main():
    OUTDIR.mkdir(parents=True, exist_ok=True)
    for old in OUTDIR.glob("*.jpg"):
        old.unlink()
    srcs = [load_cover(A / f) for f, _ in SHOTS]
    n = len(SHOTS)
    step = SHOT - XF
    total = step * (n - 1) + SHOT
    nframes = int(round(total * FPS))
    ovs = [(Image.open(SP / p).convert("RGBA"), a, b) for p, a, b in OVERLAYS]
    print(f"total {total:.2f}s -> {nframes} frames")
    for i in range(nframes):
        t = i / FPS
        layers = []
        for s in range(n):
            s0 = s * step
            s1 = s0 + SHOT
            if s0 - 1e-6 <= t < s1:
                prog = (t - s0) / SHOT
                w = 1.0
                if s > 0 and t < s0 + XF:
                    w = (t - s0) / XF
                if s < n - 1 and t > s0 + step:
                    w = 1.0 - (t - (s0 + step)) / XF
                layers.append((s, prog, max(0.0, min(1.0, w))))
        if not layers:
            layers = [(n - 1, 1.0, 1.0)]
        if len(layers) == 1:
            s, prog, _ = layers[0]
            frame = kb_frame(srcs[s], prog, SHOTS[s][1])
        else:
            (sa, pa, wa), (sb, pb, wb) = layers[0], layers[1]
            Aa = np.asarray(kb_frame(srcs[sa], pa, SHOTS[sa][1]), dtype=np.float32)
            Bb = np.asarray(kb_frame(srcs[sb], pb, SHOTS[sb][1]), dtype=np.float32)
            f = wb / max(1e-6, wa + wb)
            frame = Image.fromarray(np.clip(Aa * (1 - f) + Bb * f, 0, 255).astype(np.uint8))
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
        if t > total - END_FADE:
            k = 1.0 - (t - (total - END_FADE)) / END_FADE
            frame = Image.fromarray((np.asarray(frame, dtype=np.float32) * max(0.0, k)).astype(np.uint8))
        frame.save(OUTDIR / f"f_{i:05d}.jpg", quality=95)
    print("frames done:", len(list(OUTDIR.glob('*.jpg'))))


if __name__ == "__main__":
    main()
