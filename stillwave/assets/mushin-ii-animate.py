#!/usr/bin/env python3
"""MUSHIN II — animate the still without Flow (seamless loop, all motion periodic).

Fine ripples shimmer across the pond (the moon's and the stars' reflections tremble in place),
the stars twinkle, the moon's halo breathes. The samurai, the stone and the swords stay still.
Usage: python3 mushin-ii-animate.py SRC.jpg OUT.mp4 [seconds=12] [output width=1920]
"""
import sys, subprocess
import numpy as np, cv2

src, out = sys.argv[1], sys.argv[2]
T = float(sys.argv[3]) if len(sys.argv) > 3 else 12.0
OW = int(sys.argv[4]) if len(sys.argv) > 4 else 1920
FPS = 24; N = int(T * FPS)
B = cv2.resize(cv2.imread(src).astype(np.float32), (OW, OW * 9 // 16), interpolation=cv2.INTER_AREA)
H, W = B.shape[:2]; S = W / 1920.0
Yp, Xp = np.mgrid[0:H, 0:W].astype(np.float32); yy, xx = Yp / S, Xp / S
rng = np.random.default_rng(11)
def gauss(cx, cy, s): return np.exp(-((xx - cx) ** 2 + (yy - cy) ** 2) / (2 * s * s))

HZ = 542                                          # horizon / water line (1920x1080 units)
MOON = (1330, 330, 220)
# water: everything below the horizon except the rock, the samurai and the swords
water = np.clip((yy - HZ - 6) / 20, 0, 1)
keep = np.zeros((1080, 1920), np.float32)
cv2.ellipse(keep, (1325, 760), (150, 330), 0, 0, 360, 1, -1)          # samurai
cv2.rectangle(keep, (590, 900), (1800, 1080), 1, -1)                    # stone + swords
keep = cv2.resize(cv2.GaussianBlur(keep, (0, 0), 25), (W, H))
water = (water * (1 - np.clip(keep * 1.4, 0, 1))).astype(np.float32)
depth = np.clip((yy - HZ) / 400, 0.15, 1)          # ripples grow towards the viewer

# stars: small bright points in the sky, away from the moon
lum = B.mean(2); loc = cv2.GaussianBlur(lum, (0, 0), 4 * S)
sky = (yy < HZ - 8) & (np.hypot(xx - MOON[0], yy - MOON[1]) > MOON[2] + 120)
star = (np.clip((lum - loc - 6) / 30, 0, 1) * sky).astype(np.float32)
star_ref = (np.clip((lum - loc - 4) / 30, 0, 1) * (yy > HZ) * water).astype(np.float32)   # their reflections
phase = cv2.resize(rng.uniform(0, 2 * np.pi, (60, 100)).astype(np.float32), (W, H), interpolation=cv2.INTER_NEAREST)
star_part = (lum - loc)[..., None] * np.stack([star] * 3, -1)
halo = gauss(MOON[0], MOON[1], MOON[2] * 1.25) * (np.hypot(xx - MOON[0], yy - MOON[1]) > MOON[2] * 0.95)

ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(FPS),
    "-i", "-", "-c:v", "libx264", "-crf", "14", "-preset", "slow", "-profile:v", "high", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
for i in range(N):
    t = i / FPS; ph = 2 * np.pi * t / T
    dx = water * depth * (2.2 * np.sin(4 * ph + yy / 6.5 + xx / 260) + 1.2 * np.sin(6 * ph - yy / 3.7 + 0.8))
    dy = water * depth * (0.6 * np.sin(5 * ph + xx / 90))
    fr = cv2.remap(B, Xp - dx * S, Yp - dy * S, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    tw = 0.55 * np.sin(3 * ph + phase)                            # every star on its own phase
    fr += star_part * tw[..., None]
    fr += (star_ref * 18 * np.sin(5 * ph + phase))[..., None]      # reflected stars glint
    fr += (halo * (6 + 4 * np.sin(ph)))[..., None] * np.array([1.0, 1.0, 1.05], np.float32)
    ff.stdin.write(np.clip(fr, 0, 255).astype(np.uint8).tobytes())
ff.stdin.close(); ff.wait()
print("saved", out, N, "frames")
