#!/usr/bin/env python3
"""
StillWave album mastering — batch-prepare Suno WAVs for CapCut assembly.

Per track (two-pass EBU R128 loudnorm — accurate, dynamics preserved):
  1. low-cut 28 Hz            — removes generative sub-rumble
  2. high-shelf −1.5 dB @ 9k  — tames Suno high-frequency shimmer (--no-shelf to skip)
  3. loudness → one LUFS target across the whole album (default −16 LUFS, TP −1.5 dB)
  4. fade-in / fade-out       — hides abrupt Suno endings (default 1.0 s, --fade 0 to skip)
  5. resample 48 kHz, 24-bit WAV — matches the CapCut/YouTube pipeline

Usage:
  python3 master-album.py <folder-with-suno-wavs> [-o out-folder] [--lufs -16] [--fade 1.0] [--no-shelf]

Output: <folder>-mastered/ with the same file names + a summary table.
Tracks whose input true peak exceeds 0 dB (clipped upstream) are flagged — consider regenerating those.
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

AUDIO_EXT = {".wav", ".mp3", ".flac", ".m4a", ".ogg"}


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def natural_key(p: Path):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", p.name)]


def probe_duration(path):
    r = run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", str(path)])
    return float(r.stdout.strip())


def measure(path, prefilter):
    """Pass 1 — measure loudness after the tonal pre-filters (so pass 2 lands exactly)."""
    af = prefilter + f"loudnorm=I=-16:TP=-1.5:LRA=13:print_format=json"
    r = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path),
             "-af", af, "-f", "null", "-"])
    m = re.search(r"\{[^{}]+\}", r.stderr[-2500:], re.S)
    if not m:
        raise RuntimeError(f"loudnorm measurement failed for {path.name}")
    return json.loads(m.group(0))


def master(path, out, prefilter, lufs, fade, meas):
    ln = (f"loudnorm=I={lufs}:TP=-1.5:LRA=13:linear=true"
          f":measured_I={meas['input_i']}:measured_TP={meas['input_tp']}"
          f":measured_LRA={meas['input_lra']}:measured_thresh={meas['input_thresh']}")
    af = prefilter + ln
    if fade > 0:
        dur = probe_duration(path)
        af += f",afade=t=in:d={fade},afade=t=out:st={max(0, dur - fade):.3f}:d={fade}"
    r = run(["ffmpeg", "-hide_banner", "-nostats", "-y", "-i", str(path),
             "-af", af, "-ar", "48000", "-c:a", "pcm_s24le", str(out)])
    if r.returncode != 0:
        raise RuntimeError(r.stderr[-400:])


def main():
    ap = argparse.ArgumentParser(description="Batch-master a Suno album for CapCut/YouTube")
    ap.add_argument("folder", type=Path, help="folder with Suno downloads (WAV preferred)")
    ap.add_argument("-o", "--out", type=Path, default=None,
                    help="output folder (default: <folder>-mastered)")
    ap.add_argument("--lufs", type=float, default=-16.0,
                    help="integrated loudness target, default -16 (sleep/meditation-safe)")
    ap.add_argument("--fade", type=float, default=1.0,
                    help="fade in/out seconds per track, 0 = off (default 1.0)")
    ap.add_argument("--no-shelf", action="store_true",
                    help="skip the -1.5 dB high-shelf at 9 kHz")
    args = ap.parse_args()

    if not args.folder.is_dir():
        sys.exit(f"Not a folder: {args.folder}")
    files = sorted((p for p in args.folder.iterdir() if p.suffix.lower() in AUDIO_EXT),
                   key=natural_key)
    if not files:
        sys.exit(f"No audio files in {args.folder}")

    out_dir = args.out or args.folder.parent / (args.folder.name + "-mastered")
    out_dir.mkdir(parents=True, exist_ok=True)

    prefilter = "highpass=f=28,"
    if not args.no_shelf:
        prefilter += "highshelf=g=-1.5:f=9000,"

    print(f"{len(files)} tracks → {out_dir}   (target {args.lufs} LUFS, TP -1.5 dB, 48 kHz/24-bit)\n")
    print(f"{'track':<44} {'in LUFS':>8} {'in TP':>7}  note")
    print("-" * 78)

    clipped = []
    for f in files:
        try:
            meas = measure(f, prefilter)
            note = ""
            if float(meas["input_tp"]) > 0:
                note = "⚠ clipped input — consider regenerating"
                clipped.append(f.name)
            master(f, out_dir / (f.stem + ".wav"), prefilter, args.lufs, args.fade, meas)
            print(f"{f.name[:43]:<44} {float(meas['input_i']):>8.1f} {float(meas['input_tp']):>7.1f}  {note}")
        except Exception as e:
            print(f"{f.name[:43]:<44}  FAILED: {e}")

    print("-" * 78)
    print(f"Done → {out_dir}")
    if clipped:
        print(f"\n⚠ {len(clipped)} track(s) had clipped input (TP > 0 dB):")
        for n in clipped:
            print(f"   {n}")
        print("Mastered versions are safe, but clipping happened inside Suno — regenerate if audible.")


if __name__ == "__main__":
    main()
