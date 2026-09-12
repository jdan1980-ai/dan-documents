#!/usr/bin/env python3
"""
StillWave album auto-builder — select the calmest tracks, order them
anti-Content-ID (round-robin across Suno variants), and copy them straight
into a ready `<SLUG>-ALBUM` folder. Leftover good tracks go to a
`<SLUG>-RESERVE` folder for a future Vol. 2 instead of being deleted.

Replaces the old manual flow (paste the master-album.py table into chat,
wait for a hand-built PowerShell rename map). One command does mastering
selection + ordering + folder assembly.

Requires the RAW Suno folder (for pre-mastering loudness/peak measurements —
the calmness score) and the already-MASTERED folder from master-album.py
(for the actual files to copy — same base filenames, .wav extension).

Filename convention expected: `<PREFIX>_<variant>.wav` or
`<PREFIX>_<variant> (<take>).wav`, e.g. `SUIRYU_7 (2).wav` → variant 7.
Variant = the last underscore-separated number before an optional
"(take)" suffix.

Usage:
  python3 select-album.py <raw-folder> <mastered-folder> --slug SUIRYU
      [--cap 120] [--min-per-variant 2] [--out DIR] [--reserve-dir DIR]

Output:
  <SLUG>-ALBUM/     — selected tracks, copied in final round-robin play
                       order as `NN - <original name>.wav`, printed table
                       with cumulative timestamps (paste straight into §8).
  <SLUG>-RESERVE/   — the good tracks that didn't make the cut (for Vol. 2).
  Exact duplicates (same length + LUFS + TP as an earlier file) are
  dropped entirely, not reserved.
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

AUDIO_EXT = {".wav", ".mp3", ".flac", ".m4a", ".ogg"}
VARIANT_RE = re.compile(r"_(\d+)(?:\s*\(\d+\))?$")


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def natural_key(p: Path):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", p.name)]


def probe_duration(path):
    r = run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", str(path)])
    return float(r.stdout.strip())


def hms(sec):
    sec = int(round(sec))
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def measure(path, prefilter):
    af = prefilter + "loudnorm=I=-16:TP=-1.5:LRA=13:print_format=json"
    r = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path),
             "-af", af, "-f", "null", "-"])
    m = re.search(r"\{[^{}]+\}", r.stderr[-2500:], re.S)
    if not m:
        raise RuntimeError(f"loudnorm measurement failed for {path.name}")
    return json.loads(m.group(0))


def variant_of(stem):
    m = VARIANT_RE.search(stem)
    return int(m.group(1)) if m else 0


def main():
    ap = argparse.ArgumentParser(description="Select + round-robin order + assemble a StillWave album")
    ap.add_argument("raw_folder", type=Path, help="original Suno downloads (for calmness scoring)")
    ap.add_argument("mastered_folder", type=Path, help="output of master-album.py (files actually copied)")
    ap.add_argument("--slug", required=True, help="e.g. SUIRYU — used for output folder names")
    ap.add_argument("--cap", type=float, default=120.0, help="max album length in minutes (default 120)")
    ap.add_argument("--min-per-variant", type=int, default=2,
                    help="don't drop a variant below this count while others remain (default 2)")
    ap.add_argument("--out", type=Path, default=None, help="output ALBUM folder (default: <slug>-ALBUM)")
    ap.add_argument("--reserve-dir", type=Path, default=None,
                    help="output RESERVE folder (default: <slug>-RESERVE)")
    ap.add_argument("--no-shelf", action="store_true", help="match master-album.py --no-shelf if you used it")
    args = ap.parse_args()

    if not args.raw_folder.is_dir():
        sys.exit(f"Not a folder: {args.raw_folder}")
    if not args.mastered_folder.is_dir():
        sys.exit(f"Not a folder: {args.mastered_folder}")

    out_dir = args.out or args.mastered_folder.parent / f"{args.slug}-ALBUM"
    reserve_dir = args.reserve_dir or args.mastered_folder.parent / f"{args.slug}-RESERVE"

    prefilter = "highpass=f=28,"
    if not args.no_shelf:
        prefilter += "highshelf=g=-1.5:f=9000,"

    raw_files = sorted((p for p in args.raw_folder.iterdir() if p.suffix.lower() in AUDIO_EXT),
                        key=natural_key)
    if not raw_files:
        sys.exit(f"No audio files in {args.raw_folder}")

    print(f"Measuring {len(raw_files)} raw tracks for calmness score...\n")
    tracks = []
    seen = {}
    for f in raw_files:
        mastered = args.mastered_folder / (f.stem + ".wav")
        if not mastered.exists():
            print(f"  ! skip {f.name} — no matching mastered file ({mastered.name})")
            continue
        try:
            meas = measure(f, prefilter)
            dur = probe_duration(mastered)
            lufs, tp = float(meas["input_i"]), float(meas["input_tp"])
            sig = (round(dur), round(lufs, 1), round(tp, 1))
            is_dup = sig in seen
            if not is_dup:
                seen[sig] = f.name
            tracks.append({
                "name": f.name, "mastered": mastered, "dur": dur,
                "score": lufs + tp, "variant": variant_of(f.stem),
                "dup_of": seen[sig] if is_dup else None,
            })
        except Exception as e:
            print(f"  ! failed to measure {f.name}: {e}")

    dupes = [t for t in tracks if t["dup_of"]]
    kept = [t for t in tracks if not t["dup_of"]]
    if dupes:
        print(f"Dropping {len(dupes)} exact duplicate(s):")
        for t in dupes:
            print(f"   {t['name']}  ==  {t['dup_of']}")
        print()

    # Anchor first, fill second — deterministic, no thrash:
    #   1) unconditionally keep each variant's `min_per_variant` calmest tracks
    #      (guarantees every variant survives — a handful of anchors across
    #      10 variants is a few minutes, never meaningfully threatens the cap)
    #   2) sort everything left over by score and greedily add the calmest
    #      until the cap is filled (mirrors the manual process: cut the worst)
    cap_sec = args.cap * 60.0
    variant_groups = {}
    for t in kept:
        variant_groups.setdefault(t["variant"], []).append(t)
    for v in variant_groups:
        variant_groups[v].sort(key=lambda t: t["score"])  # calmest first

    selected, remainder = [], []
    for group in variant_groups.values():
        n_anchor = min(args.min_per_variant, len(group))
        selected.extend(group[:n_anchor])
        remainder.extend(group[n_anchor:])

    total = sum(t["dur"] for t in selected)
    if total > cap_sec:
        print(f"⚠ guaranteeing {args.min_per_variant} track(s) per variant already needs "
              f"{hms(total)}, over the {args.cap:.0f}-min cap — keeping all anchors anyway; "
              f"lower --min-per-variant or raise --cap for a stricter cut.\n")

    remainder.sort(key=lambda t: t["score"])  # calmest first
    rejected = []
    for t in remainder:
        if total + t["dur"] <= cap_sec:
            selected.append(t)
            total += t["dur"]
        else:
            rejected.append(t)

    dropped_for_length = rejected
    by_variant = {}
    for t in selected:
        by_variant.setdefault(t["variant"], []).append(t)

    # round-robin play order: cycle variants in natural order, skip exhausted ones,
    # never repeat the immediately-preceding variant if an alternative exists
    queues = {v: sorted(tr, key=lambda t: natural_key(Path(t["name"]))) for v, tr in by_variant.items()}
    order = []
    last_variant = None
    remaining = sum(len(q) for q in queues.values())
    variants_cycle = sorted(queues.keys())
    idx = 0
    while remaining > 0:
        progressed = False
        for _ in range(len(variants_cycle)):
            v = variants_cycle[idx % len(variants_cycle)]
            idx += 1
            if v in queues and queues[v]:
                if v == last_variant and any(len(q) for k, q in queues.items() if k != v):
                    continue
                order.append(queues[v].pop(0))
                if not queues[v]:
                    del queues[v]
                last_variant = v
                remaining -= 1
                progressed = True
                break
        if not progressed:
            # only one variant left with stock — forced to repeat it
            v = next(iter(queues))
            order.append(queues[v].pop(0))
            if not queues[v]:
                del queues[v]
            last_variant = v
            remaining -= 1

    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n{'#':<4} {'variant':>7}  {'start':>9}  {'length':>7}  source")
    print("-" * 70)
    cum = 0.0
    for i, t in enumerate(order, 1):
        dest = out_dir / f"{i:02d} - {t['mastered'].stem}.wav"
        shutil.copyfile(t["mastered"], dest)
        print(f"{i:<4} {t['variant']:>7}  {hms(cum):>9}  {hms(t['dur']):>7}  {t['name']}")
        cum += t["dur"]
    print("-" * 70)
    print(f"ALBUM: {len(order)} tracks, {hms(cum)} total → {out_dir}")

    reserve = dropped_for_length
    if reserve:
        reserve_dir.mkdir(parents=True, exist_ok=True)
        for t in reserve:
            shutil.copyfile(t["mastered"], reserve_dir / t["mastered"].name)
        print(f"\nRESERVE (for Vol. 2): {len(reserve)} tracks → {reserve_dir}")
        for t in sorted(reserve, key=lambda t: t["score"]):
            print(f"   {t['name']}  (score {t['score']:.1f})")

    print("\nPaste the numbered list above into §8 timestamps (cumulative 'start' column),")
    print("then write mood-poetic track names to replace the raw filenames in the description.")


if __name__ == "__main__":
    main()
