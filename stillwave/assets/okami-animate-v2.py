#!/usr/bin/env python3
"""ŌKAMI v2 frame (incense, floor candles; 2026-11-19) — animate the still frame without Flow (seamless loop, every motion is periodic).

Motions: the incense smoke rises and wavers (smoke layer separated from the painting, so the ink behind it stays still); the painted wolf's tail sways; the dark band above the doors fades to shadow; gold dust motes drift up through the hall; two candle flames flicker and sway, their warm light trembles on the gold leaf and the
floor, the wolf's gold eyes glimmer, the painted ink clouds on the left doors undulate slowly,
and the painted wolf's body "breathes" (a sub-percent swell of the torso).
Usage: python3 okami-animate.py SRC.jpg OUT.mp4 [seconds=12] [output width, e.g. 3840]
"""
import sys, subprocess
import numpy as np, cv2

src, out = sys.argv[1], sys.argv[2]
T = float(sys.argv[3]) if len(sys.argv) > 3 else 12.0
FPS = 24; N = int(T * FPS)
B = cv2.imread(src).astype(np.float32)  # BGR
if len(sys.argv) > 4:                      # optional output width, e.g. 3840 for 4K
    ow = int(sys.argv[4]); B = cv2.resize(B, (ow, ow * 9 // 16), interpolation=cv2.INTER_LANCZOS4)   # exact 16:9, even height
    B = np.clip(B, 0, 255)   # Lanczos overshoot would wrap around in the uint8 inpaint step
H, W = B.shape[:2]
S = W / 1920.0                             # all positions below are given for a 1920x1080 frame
rng = np.random.default_rng(5)
Yp, Xp = np.mgrid[0:H, 0:W].astype(np.float32)   # pixel grid
yy, xx = Yp / S, Xp / S                            # design grid (1920x1080 units)

def pnoise(t, ks, amp=1.0):
    """smooth periodic noise in [-1,1]-ish, integer cycles per loop -> seamless"""
    ph = rng.uniform(0, 2 * np.pi, len(ks)); w = rng.uniform(0.5, 1, len(ks))
    return lambda t: amp * sum(wi * np.sin(2 * np.pi * k * t / T + p) for k, p, wi in zip(ks, ph, w)) / sum(w)
def gauss(cx, cy, s): return np.exp(-((xx - cx) ** 2 + (yy - cy) ** 2) / (2 * s * s))

FLAMES = [(45, 760, 780), (1876, 760, 780)]     # x, flame centre y, flame base y (v2 frame, floor candles)
# flameless background for each flame patch
bg = B.copy()
core = np.zeros((H, W), np.uint8)
for fx, fy, fb in FLAMES:
    cv2.ellipse(core, (round(fx * S), round((fy - 1) * S)), (round(9 * S), round(19 * S)), 0, 0, 360, 255, -1)
bg = cv2.inpaint(B.astype(np.uint8), cv2.dilate(core, np.ones((round(5 * S), round(5 * S)))), 5, cv2.INPAINT_TELEA).astype(np.float32)
lum = B.mean(2)
flame_alpha = np.clip((lum - 120) / 100, 0, 1) * (cv2.GaussianBlur(core.astype(np.float32), (0, 0), 3 * S) / 255 > 0.05)
for fx, fy, fb in FLAMES:   # the wax below the flame is not part of the flame
    flame_alpha[round((fb - 1) * S):, round((fx - 30) * S):round((fx + 30) * S)] = 0
flame_alpha = cv2.GaussianBlur(flame_alpha.astype(np.float32), (0, 0), 1.2 * S)

# --- incense smoke layer ---
smoke_box = np.zeros((H, W), np.float32)
cv2.rectangle(smoke_box, (round(740 * S), round(520 * S)), (round(890 * S), round(872 * S)), 1, -1)   # starts below the wolf's muzzle (nose at ~845,488)
loc = cv2.GaussianBlur(B.mean(2), (0, 0), 14 * S)
smask = (np.clip((B.mean(2) - loc - 3) / 18, 0, 1) * smoke_box).astype(np.float32)
smask = cv2.GaussianBlur(smask, (0, 0), 1.5 * S)
bg = cv2.inpaint(np.clip(bg, 0, 255).astype(np.uint8), (cv2.dilate((smask > 0.05).astype(np.uint8), np.ones((round(7 * S), round(7 * S)))) * 255), 6, cv2.INPAINT_TELEA).astype(np.float32)
smoke = np.clip(B - bg, 0, None) * cv2.GaussianBlur(smoke_box, (0, 0), 10 * S)[..., None]
smoke_h = np.clip((872 - yy) / 350, 0, 1)                 # 0 at the burner, 1 at the top of the plume

flick = [pnoise(None, [5, 7, 11, 13, 17]), pnoise(None, [6, 9, 12, 15, 19])]
sway = [pnoise(None, [3, 4, 7]), pnoise(None, [2, 5, 8])]
light = [gauss(fx, fy, 420) for fx, fy, _ in FLAMES]

EYES = [(910, 379, 1.0), (846, 383, 0.6)]        # near eye, far eye (half hidden) with its own strength
eye_glow = sum(k * (1.0 * gauss(x, y, 5) + 0.6 * gauss(x, y, 13) + 0.28 * gauss(x, y, 32) + 0.10 * gauss(x, y, 70)) for x, y, k in EYES)
eye_pulse = pnoise(None, [1, 2])

# ink clouds on the left doors: soft mask, kept away from the left candle
cloud = np.zeros((1080, 1920), np.float32)
cv2.rectangle(cloud, (0, 300), (960, 640), 1, -1)                 # the ink clouds band on the left doors
cloud = cv2.resize(cv2.GaussianBlur(cloud, (0, 0), 40), (W, H), interpolation=cv2.INTER_LINEAR)
# the wooden door frames must not bend: no displacement near the vertical rails or the top rail
RAILS = [293, 633, 965, 1299, 1628]
dist = np.min(np.abs(xx[None] - np.array(RAILS, np.float32)[:, None, None]), axis=0)
cloud *= np.clip((dist - 10) / 30, 0, 1) * np.clip((yy - 95) / 30, 0, 1)
cloud *= 1 - gauss(830, 690, 120)                     # keep the smoke column out of the cloud warp
# the wolf's tail (right doors): sways from its root, more towards the tip
tail = np.clip((xx - 1640) / 250, 0, 1) ** 1.4 * np.exp(-((yy - 360) / 150) ** 2) * np.clip((dist - 10) / 30, 0, 1)
# dark band above the doors fades into shadow
top_shade = (0.25 + 0.75 * np.clip((yy - 10) / 75, 0, 1)).astype(np.float32)
# wolf torso for the breath
torso = gauss(1330, 330, 190) * (xx > 1060) * np.clip((dist - 10) / 30, 0, 1)
torso = cv2.GaussianBlur(torso.astype(np.float32), (0, 0), 20 * S)

# gold dust motes drifting up through the hall (seamless: each mote rises k full heights per loop)
NM = 55
m_x = rng.uniform(0, 1920, NM); m_y = rng.uniform(0, 1080, NM)
m_k = rng.choice([1, 1, 2], NM)                    # loop-heights per loop (slow / a bit faster)
m_r = rng.uniform(1.4, 4.2, NM) * np.where(m_k == 2, 1.25, 1.0)
m_ph = rng.uniform(0, 2 * np.pi, NM); m_sw = rng.integers(1, 3, NM)
m_a = rng.uniform(0.35, 0.9, NM)
GOLD = np.array([80, 178, 236], np.float32)        # BGR
def add_dust(frame, t):
    for i in range(NM):
        x = (m_x[i] + 22 * np.sin(2 * np.pi * m_sw[i] * t / T + m_ph[i])) % 1920
        y = (m_y[i] - 1080 * m_k[i] * t / T) % 1080
        b = m_a[i] * (0.55 + 0.45 * np.sin(2 * np.pi * 3 * t / T + 3 * m_ph[i]))
        r = m_r[i] * S; X, Y = x * S, y * S; R = int(r * 3) + 2
        x0, x1, y0, y1 = max(int(X) - R, 0), min(int(X) + R + 1, W), max(int(Y) - R, 0), min(int(Y) + R + 1, H)
        if x0 >= x1 or y0 >= y1: continue
        g = np.exp(-((Xp[y0:y1, x0:x1] - X) ** 2 + (Yp[y0:y1, x0:x1] - Y) ** 2) / (2 * r * r)) * b
        frame[y0:y1, x0:x1] += g[..., None] * GOLD
    return frame

ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}",
                       "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "12", "-preset", "slow", "-profile:v", "high", "-tune", "film",
                       "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
for i in range(N):
    t = i / FPS
    # geometric warps: clouds undulate, torso breathes
    ph = 2 * np.pi * t / T
    dx = cloud * (6 * np.sin(ph + yy / 90) + 3 * np.sin(2 * ph + xx / 140))
    dy = cloud * (2.5 * np.cos(ph + xx / 120))
    br = 0.006 * np.sin(2 * ph)                       # two breaths per loop
    dy += torso * br * (yy - 480)                      # swell up from the belly line
    dx += torso * br * 0.5 * (xx - 1330)
    tw = np.sin(ph + 0.6) * 7 + np.sin(2 * ph) * 2       # tail sway (px at the tip)
    dx += tail * tw; dy += tail * 0.35 * tw
    frame = cv2.remap(bg, Xp - dx * S, Yp - dy * S, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    # smoke: an upward-travelling sideways wave, stronger higher up; brightness breathes a little
    sx = smoke_h ** 1.3 * (9 * np.sin(2 * np.pi * (2 * t / T) - yy / 38) + 4 * np.sin(2 * np.pi * (3 * t / T) - yy / 17 + 1.3))
    sy = -smoke_h * 3 * (0.5 + 0.5 * np.sin(2 * np.pi * (2 * t / T) - yy / 50))
    sm = cv2.remap(smoke, Xp - sx * S, Yp - sy * S, cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    frame += sm * (0.9 + 0.1 * np.sin(2 * np.pi * t / T))
    # flames: scale/sway around their base, then lay over the flameless background
    for k, (fx, fy, fb) in enumerate(FLAMES):
        f = flick[k](t); s = 1 + 0.12 * f; sw = 1.6 * sway[k](t)
        sh = 0.03 * sway[k](t)   # lean around the flame base, not around y=0
        X0, Y0 = fx * S, fb * S
        M = np.float32([[1 - 0.04 * f, sh, X0 * 0.04 * f + sw * S - sh * Y0], [0, s, Y0 * (1 - s)]])
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
    frame = frame * top_shade[..., None]
    frame = add_dust(frame, t)
    ff.stdin.write(np.clip(frame, 0, 255).astype(np.uint8).tobytes())
ff.stdin.close(); ff.wait()
print("saved", out, N, "frames")
