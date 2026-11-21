#!/usr/bin/env python3
"""One-command album build: master-album.py, then select-album.py.

Usage:
    python build-album.py "<raw-folder>" --slug NAME [--cap 120] [--min-length 2.5]

Runs master-album.py on the raw folder (output: "<raw-folder>-mastered"), then
select-album.py on raw + mastered with the same slug, cap and min-length. If
mastering fails, selection does not run. Both tools must sit next to this file.
"""
import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def run(cmd):
    print("\n>>", " ".join(f'"{c}"' if " " in str(c) else str(c) for c in cmd), flush=True)
    return subprocess.run(cmd).returncode


def main():
    ap = argparse.ArgumentParser(description="Master and select an album in one command.")
    ap.add_argument("raw_folder", type=Path, help="folder with the raw Suno WAVs")
    ap.add_argument("--slug", required=True, help="album slug, e.g. SATORI — used for output folder names")
    ap.add_argument("--cap", type=float, default=120.0, help="max album length in minutes (default 120)")
    ap.add_argument("--min-length", type=float, default=2.5,
                    help="drop tracks shorter than this many minutes (default 2.5)")
    args = ap.parse_args()

    raw = args.raw_folder.resolve()
    mastered = raw.parent / (raw.name + "-mastered")

    rc = run([sys.executable, str(HERE / "master-album.py"), str(raw)])
    if rc != 0:
        print(f"\nmaster-album.py failed (exit {rc}); selection skipped.", file=sys.stderr)
        return rc

    rc = run([sys.executable, str(HERE / "select-album.py"), str(raw), str(mastered),
              "--slug", args.slug, "--cap", str(args.cap), "--min-length", str(args.min_length)])
    if rc != 0:
        print(f"\nselect-album.py failed (exit {rc}).", file=sys.stderr)
    return rc


if __name__ == "__main__":
    sys.exit(main())
