# MICHI 道 — the samurai's path through the snow (2 Hours)

## Meta
- **Status (2026-11-25):** Flow tracking-shot clip approved by review; loop = Veo's own clip (it already matches step for step; my 16-frame crossfade version was worse and was dropped; ~10% slower walk in the first 0.5 s, user keeps it). Music: `music-bank/yuki` (or any bank theme) after the Content ID check.
- **Concept (user's idea):** a lone samurai walks endlessly across a snowfield toward a distant temple, leaving footprints — the "endless walk" format of the biggest hit in the niche (KUMAMICHI, 1.67M), done with a samurai. The camera follows at a constant distance, so the clip can loop.
- **Frame:** `assets/michi-2h-source.jpg` (first frame of the Flow clip).

**🇺🇦 RU:** Самурай бесконечно идёт по снегу к далёкому храму и оставляет следы. Камера идёт следом, поэтому петля склеивается без рывка.

## Workflow rule
The Flow prompt is written only after the final image is chosen (user, 2026-11-25).

## Short (version B) — `assets/michi-short-motion.py`, track yuki 1635764
Built on a vertical crop of the Veo clip (no new frame, no Flow credits): `ffmpeg -i flow.mp4 -vf "crop=608:1080:656:0,scale=1080:1920:flags=lanczos,unsharp=5:5:0.5"` → `MICHI_loop_916.mp4` (the user kept Veo's own loop: it matches step for step; my crossfade version was dropped). Softer than native 9:16 (1.8× upscale). Cover 道 / MICHI over the samurai's dark robe (user-approved; the bottom is the Shorts UI zone, the top is temple and moon). Hook from the temple light to the walking samurai, "He walks toward the temple. / He never arrives." · 道 emerges · "The path itself / is the destination." No gold dust (the clip has blowing snow).

Title:
```
He Walks Toward the Temple and Never Arrives
```
Description (add the long-form link):
```
Michi (道), the path. For the samurai, the way was never about reaching the end: every step through the snow is the practice itself. The temple stays on the horizon, and that is the point.

Full 2-hour samurai meditation music on the channel: [MICHI link]

#shorts #michi #samurai #samuraimusic #zenmusic #winter
```
Tags:
```
michi, the way, samurai path, samurai walking, samurai in snow, winter samurai, japanese temple, samurai music, samurai meditation music, japanese zen music, meditation music, shorts
```
Pinned:
```
🌀 The path itself is the destination. Which step are you taking today? Full 2 hours of MICHI on the channel 🌿
```

## §2 — Album (music bank: tsuru, all 10 tracks passed)
Order keeps same-request pairs apart, incl. across the loop. Loop 27:51.6 × 4.3 = exactly 2:00:00, seams 3 s, −15.8 LUFS, MP3 320 kbps 4 × 30:00.

| # | Track | Start |
|---|---|---|
| 1 | 1635846 | 0:00 |
| 2 | 1635848 | 2:32 |
| 3 | 1635850 | 5:29 |
| 4 | 1635852 | 8:37 |
| 5 | 1635854 | 11:44 |
| 6 | 1635847 | 14:37 |
| 7 | 1635849 | 16:46 |
| 8 | 1635851 | 19:35 |
| 9 | 1635853 | 22:11 |
| 10 | 1635855 | 25:08 |
