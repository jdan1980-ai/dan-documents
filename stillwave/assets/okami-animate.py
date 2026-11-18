#!/usr/bin/env python3
"""ŌKAMI — animate the still frame without Flow (seamless loop, every motion is periodic).

Motions: two candle flames flicker and sway, their warm light trembles on the gold leaf and the
floor, the wolf's gold eyes glimmer, the painted ink clouds on the left doors undulate slowly,
and the painted wolf's body "breathes" (a sub-percent swell of the torso).
Usage: python3 okami-animate.py SRC.jpg OUT.mp4 [seconds=12]
"""
import sys, subprocess
import numpy as np, cv2

src, out = sys.argv[1], sys.argv[2]
T = float(sys.argv[3]) if len(sys.argv) > 3 else 12.0
FPS = 24; N = int(T * FPS)
B = cv2.imread(src).astype(np.float32)  # BGR
H, W = B.shape[:2]
rng = np.random.default_rng(5)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)

def pnoise(t, ks, amp=1.0):
    """smooth periodic noise in [-1,1]-ish, integer cycles per loop -> seamless"""
    ph = rng.uniform(0, 2 * np.pi, len(ks)); w = rng.uniform(0.5, 1, len(ks))
    return lambda t: amp * sum(wi * np.sin(2 * np.pi * k * t / T + p) for k, p, wi in zip(ks, ph, w)) / sum(w)
def gauss(cx, cy, s): return np.exp(-((xx - cx) ** 2 + (yy - cy) ** 2) / (2 * s * s))

FLAMES = [(721, 502, 525), (1733, 502, 525)]   # x, flame centre y, flame base y (frame recropped 2026-11-18)
# flameless background for each flame patch
bg = B.copy()
core = np.zeros((H, W), np.uint8)
for fx, fy, fb in FLAMES:
    cv2.ellipse(core, (fx, fy - 2), (9, 21), 0, 0, 360, 255, -1)
bg = cv2.inpaint(B.astype(np.uint8), cv2.dilate(core, np.ones((5, 5))), 5, cv2.INPAINT_TELEA).astype(np.float32)
lum = B.mean(2)
flame_alpha = np.clip((lum - 120) / 100, 0, 1) * (cv2.GaussianBlur(core.astype(np.float32), (0, 0), 3) / 255 > 0.05)
for fx, fy, fb in FLAMES:   # the wax below the flame is not part of the flame
    flame_alpha[fb - 1:, fx - 30:fx + 30] = 0
flame_alpha = cv2.GaussianBlur(flame_alpha.astype(np.float32), (0, 0), 1.2)

flick = [pnoise(None, [5, 7, 11, 13, 17]), pnoise(None, [6, 9, 12, 15, 19])]
sway = [pnoise(None, [3, 4, 7]), pnoise(None, [2, 5, 8])]
light = [gauss(fx, fy, 367) for fx, fy, _ in FLAMES]

EYES = [(1035, 336), (1091, 334)]
eye_glow = sum(1.0 * gauss(x, y, 5) + 0.55 * gauss(x, y, 14) + 0.22 * gauss(x, y, 34) for x, y in EYES)
eye_pulse = pnoise(None, [1, 2])

# ink clouds on the left doors: soft mask, kept away from the left candle
cloud = np.zeros((H, W), np.float32)
cv2.rectangle(cloud, (0, 60), (650, 680), 1, -1)
cv2.rectangle(cloud, (650, 60), (900, 250), 1, -1)
cloud = cv2.GaussianBlur(cloud, (0, 0), 40)
# the wooden door frames must not bend: no displacement near the vertical rails or the top rail
RAILS = [196, 574, 959, 1336, 1708]
dist = np.min(np.abs(xx[None] - np.array(RAILS, np.float32)[:, None, None]), axis=0)
cloud *= np.clip((dist - 10) / 30, 0, 1) * np.clip((yy - 45) / 30, 0, 1)
# wolf torso for the breath
torso = gauss(1428, 301, 167) * (xx > 1180)
torso = cv2.GaussianBlur(torso.astype(np.float32), (0, 0), 20)

ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}",
                       "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "16", "-preset", "slow",
                       "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
for i in range(N):
    t = i / FPS
    # geometric warps: clouds undulate, torso breathes
    ph = 2 * np.pi * t / T
    dx = cloud * (6 * np.sin(ph + yy / 90) + 3 * np.sin(2 * ph + xx / 140))
    dy = cloud * (2.5 * np.cos(ph + xx / 120))
    br = 0.006 * np.sin(2 * ph)                       # two breaths per loop
    dy += torso * br * (yy - 401)                      # swell up from the belly line
    dx += torso * br * 0.5 * (xx - 1428)
    frame = cv2.remap(bg, xx - dx, yy - dy, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    # flames: scale/sway around their base, then lay over the flameless background
    for k, (fx, fy, fb) in enumerate(FLAMES):
        f = flick[k](t); s = 1 + 0.12 * f; sw = 1.6 * sway[k](t)
        sh = 0.03 * sway[k](t)   # lean around the flame base, not around y=0
        M = np.float32([[1 - 0.04 * f, sh, fx * 0.04 * f + sw - sh * fb], [0, s, fb * (1 - s)]])
        Mf = cv2.warpAffine(B, M, (W, H), flags=cv2.INTER_LINEAR)
        Ma = cv2.warpAffine(flame_alpha, M, (W, H), flags=cv2.INTER_LINEAR)
        Ma = Ma * (np.abs(xx - fx) < 40) * (np.abs(yy - fy) < 60)
        frame = frame * (1 - Ma[..., None]) + Mf * (1 + 0.08 * f) * Ma[..., None]
    # warm light trembles on the gold leaf and floor
    gain = 1 + 0.055 * (flick[0](t) * light[0] + flick[1](t) * light[1])
    frame = frame * gain[..., None]
    # eyes glimmer
    e = 0.65 + 0.35 * (0.5 + 0.5 * eye_pulse(t))
    frame += (eye_glow * e)[..., None] * np.array([45, 150, 240], np.float32) * 0.6
    ff.stdin.write(np.clip(frame, 0, 255).astype(np.uint8).tobytes())
ff.stdin.close(); ff.wait()
print("saved", out, N, "frames")
