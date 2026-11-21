#!/usr/bin/env python3
"""Plan a StillWave album from select-album.py output: order, timestamps, rename script.

Stage 1 (no --names): parse the pasted select-album output, add any reserve tracks,
fix the order so no two neighbours are takes of the same base track, and print the
order with durations, the total, and how far it is from the cap.

Stage 2 (--names FILE, one poetic name per line, in the stage-1 order): also write
the YouTube tracklist (timestamps) and a PowerShell script that renames every file in
the ALBUM folder to "NN - Name.wav" in the new order.

Usage:
  python plan_album.py --select select_output.txt --album-dir "C:\\...\\slug-ALBUM" \
      [--extra "Night Forest Meditation (7).wav=3:43"] [--cap 120] \
      [--names names.txt --out-dir DIR]

Why the reorder exists: select-album.py reads the variant from filenames shaped
PREFIX_variant. Lyria/Suno names such as "Breath of the Bamboo (3).mp3" all parse as
variant 0, so it falls back to alphabetical order and puts every take of one prompt
in a row. That repeats the same opening back to back (dull, and a Content ID risk).
"""
import argparse
import re
import sys
from pathlib import Path

ROW = re.compile(r"^\s*(\d+)\s+\S+\s+(\d+:\d{2}(?::\d{2})?)\s+(\d+:\d{2}(?::\d{2})?)\s+(.+?)\s*$")
TOTAL = re.compile(r"ALBUM:\s*(\d+)\s+tracks?,\s*(\d+:\d{2}(?::\d{2})?)\s+total")
TAKE = re.compile(r"\s*\((?:take\s*)?\d+\)\s*$", re.I)
BAD_CHARS = set('<>:"/\\|?*')


def sec(t):
    s = 0
    for x in t.split(":"):
        s = s * 60 + int(x)
    return s


def fmt(s):
    h, rem = divmod(int(round(s)), 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def base(stem):
    prev = None
    while prev != stem:  # strip stacked suffixes like "X (Take 2) (1)"
        prev, stem = stem, TAKE.sub("", stem)
    return stem.strip().lower()


def interleave(tracks):
    queues = {}
    for t in tracks:
        queues.setdefault(t["group"], []).append(t)
    order, last = [], None
    while any(queues.values()):
        live = [g for g, q in queues.items() if q]
        cands = [g for g in live if g != last] or live
        g = max(cands, key=lambda g: (len(queues[g]), -queues[g][0]["pos"]))
        order.append(queues[g].pop(0))
        last = g
    return order


def adjacent_repeats(order):
    return sum(1 for a, b in zip(order, order[1:]) if a["group"] == b["group"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--select", required=True, type=Path, help="text file with the pasted select-album output")
    ap.add_argument("--album-dir", default=r"C:\Users\jdan1\OneDrive\Desktop\ALBUM",
                    help="Windows path of the slug-ALBUM folder, for the rename script")
    ap.add_argument("--extra", action="append", default=[],
                    help='reserve track copied into the ALBUM folder: "File Name.wav=m:ss" (repeatable)')
    ap.add_argument("--cap", type=float, default=120.0, help="length cap in minutes")
    ap.add_argument("--keep-order", action="store_true", help="never reorder")
    ap.add_argument("--names", type=Path, help="poetic names, one per line, in the printed order")
    ap.add_argument("--out-dir", type=Path, help="where stage 2 writes tracklist.txt and rename.ps1")
    a = ap.parse_args()

    text = a.select.read_text(encoding="utf-8", errors="replace")
    rows = [m for m in (ROW.match(l) for l in text.splitlines()) if m]
    tot = TOTAL.search(text)
    if not rows or not tot:
        sys.exit("Could not find the numbered table and the 'ALBUM: N tracks, H:MM:SS total' line.")
    tracks = []
    for i, m in enumerate(rows):
        src = m.group(4)
        stem = Path(src).stem
        tracks.append({"pos": i, "num": int(m.group(1)), "start": sec(m.group(2)),
                       "src": src, "stem": stem, "group": base(stem),
                       "current": f"{int(m.group(1)):02d} - {stem}.wav"})
    total = sec(tot.group(2))
    for i, t in enumerate(tracks):  # durations from the cumulative start column (exact sums)
        t["dur"] = (tracks[i + 1]["start"] if i + 1 < len(tracks) else total) - t["start"]
    if int(tot.group(1)) != len(tracks):
        print(f"warning: ALBUM line says {tot.group(1)} tracks, table has {len(tracks)}")

    for k, e in enumerate(a.extra):
        name, _, dur = e.rpartition("=")
        if not name or not dur:
            sys.exit(f"--extra must look like \"File.wav=3:43\", got {e!r}")
        cur = name if name.lower().endswith(".wav") else name + ".wav"
        stem = Path(cur).stem
        tracks.append({"pos": len(tracks) + k, "num": None, "start": None, "src": cur, "stem": stem,
                       "group": base(stem) + " [extra]", "current": cur, "dur": sec(dur)})

    before = adjacent_repeats(tracks)
    order = tracks if a.keep_order or (before == 0 and not a.extra) else interleave(tracks)
    after = adjacent_repeats(order)
    full = sum(t["dur"] for t in order)
    cap = a.cap * 60

    print(f"{'#':>3}  {'length':>6}  current file  ->  group")
    for i, t in enumerate(order, 1):
        print(f"{i:>3}  {fmt(t['dur']):>6}  {t['current']}  ->  {t['group']}")
    print(f"\ntracks: {len(order)}   total: {fmt(full)}   cap: {fmt(cap)}")
    print(f"same-group neighbours: {before} in selector order -> {after} in this order")
    if full > cap:
        print(f"OVER the cap by {fmt(full - cap)} — drop a track or use a shorter extra.")
    else:
        gap = cap - full
        avg = full / len(order)
        need = int(gap // avg)
        print(f"under the cap by {fmt(gap)} (average track {fmt(avg)}): "
              f"{need} more track(s) of average length still fit")

    if not a.names:
        return
    names = [n.strip() for n in a.names.read_text(encoding="utf-8").splitlines() if n.strip()]
    if len(names) != len(order):
        sys.exit(f"{len(names)} names for {len(order)} tracks — they must match one to one.")
    bad = [n for n in names if BAD_CHARS & set(n)]
    if bad:
        sys.exit(f"Names with characters Windows forbids in filenames: {bad}")
    if len(set(n.lower() for n in names)) != len(names):
        sys.exit("Duplicate names — every track needs its own.")

    cur, tl = 0, []
    ps = [f'$folder = "{a.album_dir}"', "$map = @{"]
    q = lambda s: s.replace("'", "''")
    for i, (t, n) in enumerate(zip(order, names), 1):
        tl.append(f"{fmt(cur)} {n}")
        cur += t["dur"]
        ps.append(f"  '{q(t['current'])}' = '{q(f'{i:02d} - {n}.wav')}'")
    ps += ["}",
           "$files = @(Get-ChildItem -LiteralPath $folder -Filter '*.wav')",
           "foreach ($f in $files) {",
           "  if ($map.ContainsKey($f.Name)) { Rename-Item -LiteralPath $f.FullName -NewName $map[$f.Name] }",
           '  else { Write-Host "NOT IN LIST: $($f.Name)" }',
           "}",
           'Write-Host "Done."']
    out = a.out_dir or Path(".")
    out.mkdir(parents=True, exist_ok=True)
    (out / "tracklist.txt").write_text("\n".join(tl) + "\n", encoding="utf-8")
    (out / "rename.ps1").write_text("\n".join(ps) + "\n", encoding="utf-8")
    print(f"\nwrote {out / 'tracklist.txt'} and {out / 'rename.ps1'}")


if __name__ == "__main__":
    main()
