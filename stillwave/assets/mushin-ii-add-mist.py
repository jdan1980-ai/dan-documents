#!/usr/bin/env python3
"""Adds a thin low mist layer over the pond so the mist is already in the first frame of the Flow loop."""
from PIL import Image, ImageFilter
import numpy as np, sys
src, out, prev = sys.argv[1:4]
rng = np.random.default_rng(3)
im = Image.open(src).convert('RGB'); W, H = im.size
HZ = 1084
base = np.asarray(im).astype(np.float32)
# soft cloudy noise: sum of blurred random fields stretched horizontally
def layer(scale, blur):
    n = rng.random((H // scale + 2, W // (scale * 4) + 2)).astype(np.float32)
    img = Image.fromarray((n * 255).astype(np.uint8)).resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(blur))
    return np.asarray(img).astype(np.float32) / 255
noise = 0.55 * layer(40, 30) + 0.30 * layer(16, 14) + 0.15 * layer(6, 6)
noise = np.clip((noise - 0.42) / 0.35, 0, 1)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
# vertical profile: thickest just above/below the horizon line, thin band over the water
v = np.exp(-((yy - (HZ + 60)) / 170) ** 2) + 0.35 * np.exp(-((yy - (HZ + 420)) / 260) ** 2)
h = np.clip(1.15 - xx / 3600, 0.35, 1)        # a little heavier on the left
mask = np.clip(noise * v * h, 0, 1) * 0.32
# keep the samurai, the stone and the swords clean
lum = base.mean(axis=2)
keep = np.zeros((H, W), np.float32)
keep[1150:, 2300:3650] = 1
keep = np.asarray(Image.fromarray((keep * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(120))).astype(np.float32) / 255
mask *= (1 - keep * 0.85)
mist = np.array([196, 204, 216], np.float32)
outa = base * (1 - mask[..., None]) + mist * mask[..., None]
o = Image.fromarray(np.clip(outa, 0, 255).astype(np.uint8))
o.save(out, quality=95)
o.resize((1920, 1080), Image.LANCZOS).save(prev, quality=92)
