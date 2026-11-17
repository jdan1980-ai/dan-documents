# MUSHIN II — Musicful test batch

- **Date:** 2026-11-17
- **Prompt:** `stillwave/scripts/mushin-ii-musicful-prompt.txt` (unchanged)
- **Command:** `python3 sevenlights/tools/musicful_album.py --prompt-file stillwave/scripts/mushin-ii-musicful-prompt.txt --requests 4 --out stillwave/audio-test/mushin-ii/`
- **Balance before:** 142.0
- **Balance after:** 118.0 (24 units spent, 4 requests × 2 tracks)

## Tracks

| Request | Track id | Duration | Title (as printed by the tool) |
|---|---|---|---|
| 1 | 1621034 | 234 s | Moonlit Pond Still |
| 1 | 1621035 | 228 s | Moonlit Pond Still |
| 2 | 1621036 | 200 s | 静かな呼吸 |
| 2 | 1621037 | 203 s | 静かな呼吸 |
| 3 | 1621038 | 202 s | 静かな坐禅 |
| 3 | 1621039 | 208 s | 静かな坐禅 |
| 4 | 1621040 | 203 s | 呼吸の静けさ |
| 4 | 1621041 | 199 s | 静かな呼吸 |

Total: 1677 s (~28 min). All four requests succeeded; no errors.

Files: `<id>.mp3` in this folder; ids also in `musicful_ids.txt`.
