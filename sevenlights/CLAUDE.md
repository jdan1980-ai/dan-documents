# Seven Lights — Project Instructions

The user's second YouTube channel, launched 2026-11-06. Healing-frequency (Solfeggio) sleep music
around the seven chakras. Modelled on the fast-growing competitor **Healing Quiet Tonight**
(`UCSJmN2W_LRf8Qa8uK3J1dtg`, teardown in `../stillwave/competitor-tracker.md`). The earlier
`../quiethertz/` folder was the planning draft for this channel under a working name; its music
and visual research still applies, but **Seven Lights is the real channel name**.

## Channel info

- **Name:** Seven Lights — Chakra Healing Music
- **Channel ID:** `UC6z78h-99kMxQscMgICadOg`
- **First video:** `M31WgyzQWQk`, published 2026-11-06 14:00 UTC, 2:58:02
- **Cadence:** 3 videos a week (as stated in the description)
- **Not connected to VidIQ yet** — only StillWave is. Connecting it unlocks analytics for this channel.

## Communication

Same as StillWave: chat replies in Russian only, written once; anything to copy goes in English in its
own code block. Explanatory prose in script files is EN + RU.

## Format (from the first video)

- **Length:** ~3 hours. Album cap **180 min** (`--cap 180`), `--min-length 2.5`.
- **Music:** soft ambient pads, a warm slow drone and gentle, sparse piano. No vocals, no drums,
  no sudden sounds, flat dynamics. One Solfeggio frequency (or combo) per video.
- **No wisdom overlay** (that is StillWave's signature). The text lives on the thumbnail.
- **Thumbnail:** a glowing meditating figure with the seven chakra points lit along the spine, on a
  deep blue starfield; large gold `528 HZ` top-left, white `DEEP HEALING SLEEP` under it.
- **Description:** keep the first video's structure — one-line summary with the main keywords,
  ABOUT THIS VIDEO, HOW TO LISTEN, PERFECT FOR, ABOUT [Hz], SEVEN LIGHTS, then the medical
  disclaimer and hashtags. **Keep the disclaimer**: it says plainly that no frequency is proven to
  heal the body and that this is not medical advice. Do not write health claims as facts.

## Title formula (first video)

```
[Hz] - [hook, e.g. Fall Into Deep Sleep in 5 Minutes] • [chakra/benefit] • [benefit]
```

**Put "Sleep Music" (or "Healing Music") in the first half of the title.** On its first day the video
was classified only as *Health*, while the competitor's videos sit in *Electronic music + Health +
Music*. Categories can settle over the first 48 hours, so re-check before renaming; StillWave lost a
video to the wrong category this way (Pomodoro 50/10). Example:
`528Hz Sleep Music - Fall Into Deep Sleep in 5 Minutes • Unblock All 7 Chakras`

## Tags

Base set from the first video, **minus `meditative mind`** — that is the name of a large separate
channel, and using another channel's name as a tag counts as misleading metadata on YouTube:

```
deep sleep music, sleep music, healing music, healing sleep, healing sleep music, relaxing music, relaxing sleep music, meditation music, sleep meditation, music for sleep, music to sleep, ambient sleep music, insomnia music, calm your mind, stop overthinking, chakra meditation, chakra music, piano relaxing music, mindfulness, seven lights
```
Add the Hz-specific tags per video (`528 hz`, `528 hz healing frequency`, `3 hour sleep music`, ...).

## Publishing time

The competitor publishes daily at **02:00 UTC** (21:00 New York, 04:00 Israel in winter). The first
Seven Lights video went out at 14:00 UTC. Try 02:00 UTC and compare.

## Album workflow

Same tools as StillWave (`../stillwave/tools/master-album.py`, `select-album.py`), cap 180.
Rename the files to `NN - Name.wav` for CapCut ordering; the description does not need a
tracklist (the competitor uses none). Scripts per video go in `scripts/<slug>.md`.
