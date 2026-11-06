---
name: stillwave-album
description: Builds a long-form album video for the user's StillWave YouTube channel (@stillwavezen, 2-hour Japanese zen ambient music) from raw Lyria/Suno tracks to an upload-ready package. Covers the mastering and selection commands, the wisdom overlay PNG, fixing the track order, poetic track names, YouTube timestamps, the PowerShell rename script, and saving everything to the dan-documents repo. Use this whenever the user announces a new album or video ("новый альбом", "делаем альбом X", "муз тут C:\...\Desktop\...", "сделай оверлей"), pastes master-album.py or select-album.py output, asks for a tracklist, timestamps, track names or a rename script, says the album is short of 2 hours, or wants reserve tracks added — even if they never say "album".
---

# StillWave album builder

The user runs the StillWave channel from the `jdan1980-ai/dan-documents` repo and makes a new
long-form album every few days. The steps below are the routine that has worked across
ZAZEN, NARA, SATORI, KARESANSUI, MUSASHI, Autumn Leaves and others. Most of the effort the
user notices is in small things going right every time: the correct font, a sensible track
order, names that fit, timestamps that match, and a rename script that just works.

## Before you start

Read `references/stillwave.md`: it condenses the channel rules this routine depends on. The
repo's own `stillwave/CLAUDE.md` is the source of truth; if they disagree, follow the repo file.

The repo also holds `quiethertz/`, a plan for a possible second channel modelled on a competitor
("Healing Quiet Tonight"). It is not a channel the user runs, so do not apply its rules to
StillWave albums.

## How to talk to the user

- Chat replies are **Russian only, written once** — no English duplicate, no repeated "RU"
  block. The user asked for this explicitly after replies started doubling up.
- Anything to be copied (commands, titles, tags, descriptions, tracklists, PowerShell) goes
  in **English inside its own code block**, one field per block.
- Answer what was asked. When the user asks for one thing (an overlay, a CapCut tip), give
  that thing first and keep side-advice short; they lose patience with detours.
- You cannot see their PC. Paths like `C:\Users\jdan1\OneDrive\Desktop\X` are folders on
  their machine: give them commands to run and wait for the pasted output.

## Step 1 — mastering commands

When the user names an album and its folder, give the two commands (MP3 input is fine —
mastering reads it and writes WAV):

```
python master-album.py "C:\Users\jdan1\OneDrive\Desktop\<FOLDER>"
python select-album.py "C:\Users\jdan1\OneDrive\Desktop\<FOLDER>" "C:\Users\jdan1\OneDrive\Desktop\<FOLDER>-mastered" --slug <slug> --cap <CAP> --min-length 2.5
```

`<CAP>` is 120: the channel cap is 2 hours. `--min-length 2.5` is the
user's rule: tracks shorter than 2:30 never go in. Do not offer to lower it.

If the user adds new tracks to an existing album, they want only the new ones mastered:
`master-album.py` on the new folder, copy the results into `<FOLDER>-mastered` without
overwriting, copy the raw files into `<FOLDER>`, then re-run `select-album.py`. Files with the
same name are not necessarily the same track — when a copy reports `SKIPPED (name exists)`,
compare file sizes before assuming they are duplicates.

## Step 2 — the wisdom overlay

Every StillWave long-form opens with a wisdom phrase: kanji, romaji, short English gloss,
lower-left, cream. Pick a **real** Japanese phrase (yojijukugo, kotowaza or Zen line) that fits
the video, and check it has not been used on the channel:

```bash
grep -rln "<phrase>" stillwave/scripts stillwave/assets/*.py
```

It should not name the album's own concept. Then build it with the bundled script:

```bash
python skills/stillwave-album/scripts/make_overlay.py --kanji 一葉知秋 --romaji "Ichiyō chishū" \
  --gloss "One falling leaf tells of autumn" \
  --out stillwave/assets/<slug>-<phrase-slug>-overlay.png \
  --hero <hero image if you have one> --preview <scratchpad>/preview.jpg
```

The script uses the channel's brush font (YujiBoku, in `stillwave/assets/fonts/`) and refuses to
draw a glyph the font lacks. It prints a note if the brush font is missing; if you see that
note, find out why before shipping — a whole run of overlays once went out in a plain
fallback font because nobody noticed the brush font had arrived in the repo.

Look at the preview yourself: the text must not cover the figure or the focal light, and should
sit on a dark area. If the lower-left is bright, re-run with `--scrim 200`. Send the user **only
the transparent PNG** (a JPG preview looks opaque and reads as a bug). If no hero image was
sent, build it anyway in the standard spot and say you will re-check once the frame arrives.

## Step 3 — reading the selection output

Save the pasted `select-album.py` output to a file in the scratchpad and run:

```bash
python skills/stillwave-album/scripts/plan_album.py --select <file> \
  --album-dir "C:\Users\jdan1\OneDrive\Desktop\<slug>-ALBUM" --cap <CAP> \
  [--extra "Night Forest Meditation (7).wav=3:43"]
```

It prints the order, total, gap to the cap, and how many same-group neighbours it removed.
Why the reorder matters: `select-album.py` only detects variants from `PREFIX_variant`
filenames. Lyria names such as `Breath of the Bamboo (3).mp3` or `5 (1).mp3` all read as
variant 0, so it falls back to alphabetical order and plays every take of one prompt back to
back. The planner groups takes by base name and alternates groups. Tell the user plainly when
you reordered and why, in one or two sentences.

From the output also report:
- **Length.** If the album is short, say exactly how many tracks are needed (the planner's
  "more track(s) still fit" figure) and remember the cap: one too many pushes it over 2 hours.
- **Reserve tracks.** If the user wants to top up from a previous album, use tracks from that
  album's `<slug>-RESERVE` folder — those were never published. Never reuse tracks from a
  published album. Pass each one with `--extra "<file name>=<m:ss>"`; take the length from the
  mastering table of that album.
- **Clipping.** Tracks marked `⚠ clipped input` in the mastering table that ended up in the
  album: list their positions and suggest clean swaps from RESERVE (lowest TP).
- **Duplicates** the selector dropped, if any.

## Step 4 — names, timestamps, rename script

Write one poetic name per track in the planner's order (style in `references/stillwave.md`).
You have not heard the tracks, so say the names come from the theme and invite corrections.
Keep names unique, plain ASCII where possible (no `<>:"/\|?*`), 3–6 words.

Put the names in a file, one per line, and run the planner again with `--names <file>
--out-dir <scratchpad dir>`. It writes `tracklist.txt` and `rename.ps1`. The rename script maps
each current full filename to its new `NN - Name.wav`, so it also applies the new order, is
safe to re-run, and prints `NOT IN LIST` for anything unexpected. If extra reserve tracks are
included, tell the user to copy them into the ALBUM folder before running it.

Timestamps come from the selector's start column, so they can drift by a second or two after a
reorder; say so and suggest spot-checking a couple in CapCut.

## Step 5 — save and push

Save the package to `stillwave/scripts/<slug>.md` (meta, overlay, order note, rename script,
tracklist, and the description once written), add or update the row in
`stillwave/production-status.md`, commit, and push to the working branch:

```bash
git pull --rebase -q origin <branch> && git push -q -u origin <branch>
```

Retry the push on network errors; if the remote has moved on, rebase rather than force.
Copy files the user sent (hero frames) into `stillwave/assets/` before committing.

## Checklist before replying

- Russian-only chat, code blocks for anything to copy.
- Overlay: real phrase, unused, brush font, PNG only, placement checked or flagged.
- Track count and total under the cap; clipping and gaps reported with numbers.
- Same-group neighbours: 0, or explained if unavoidable.
- Names count matches tracks; rename script and tracklist come from the same run.
- Everything committed and pushed; say the commit hash.
