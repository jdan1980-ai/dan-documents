# DOJO — Musicful test run

- **Date:** 2026-11-16
- **Prompt:** `stillwave/scripts/dojo-musicful-prompt.txt` (883 chars, unchanged)
- **Requests:** 4 (8 tracks, 24 units)
- **Balance before:** 178.0
- **Balance after:** 154.0

## Tracks

| Request | ID | Duration | Title (as returned) | File |
|---|---|---|---|---|
| 1 | 1618767 | 194 s | 空の朝 | `1618767.mp3` |
| 1 | 1618768 | 198 s | 空の朝 | `1618768.mp3` |
| 2 | 1618769 | 195 s | 空の静けさ | `1618769.mp3` |
| 2 | 1618770 | 214 s | 空の静けさ | `1618770.mp3` |
| 3 | 1618771 | 209 s | AI Music | `1618771.mp3` |
| 3 | 1618772 | 214 s | 静かな朝 | `1618772.mp3` |
| 4 | 1618773 | 199 s | 空の呼吸 | `1618773.mp3` |
| 4 | 1618774 | 220 s | 空の呼吸 | `1618774.mp3` |

Pairs from the same request: 1618767+1618768, 1618769+1618770, 1618771+1618772, 1618773+1618774.

No API errors.

## Run 2 (user asked for at least 4 more tracks)

- **Requests:** 2 (4 tracks, 12 units) · **Balance:** 154.0 → 142.0

| Request | ID | Duration | Title (as returned) |
|---|---|---|---|
| 5 | 1618775 | 199 s | 空の静けさ |
| 5 | 1618776 | 205 s | 空の静けさ |
| 6 | 1618777 | 180 s | 空の静けさ |
| 6 | 1618778 | 215 s | AI Music |

## One-cycle check video

`dojo_check_1cycle.mp4` — all 12 tracks, 30:44, built with
`make_long_track.py --trim-start 8 --trim-end 6 --check`, order chosen so no two tracks from the same
request sit side by side:

1618767 → 1618769 → 1618771 → 1618773 → 1618775 → 1618777 → 1618768 → 1618770 → 1618772 → 1618774 → 1618776 → 1618778

Picture is a temporary dark frame with the 一意専心 overlay (hero image not generated yet). Upload as
Unlisted and run YouTube's copyright check.
