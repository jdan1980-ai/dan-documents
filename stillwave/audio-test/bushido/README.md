# BUSHIDO — Musicful test batch

- **Date:** 2026-11-13
- **Prompt:** `stillwave/scripts/bushido-musicful-prompt.txt` (unchanged)
- **Command:** `python3 sevenlights/tools/musicful_album.py --prompt-file stillwave/scripts/bushido-musicful-prompt.txt --requests 3 --out stillwave/audio-test/bushido/`
- **Model:** MFV3.0, instrumental=1, action=auto (tool defaults)
- **Balance before:** 262.0
- **Balance after:** 244.0 (18 units spent: 3 requests × 2 tracks × 3 units)

## Tracks

| ID | Duration | Title (as printed by the tool) | File |
|---|---|---|---|
| 1606610 | 225 s (3:45) | Dawn at the Dojo | `1606610.mp3` |
| 1606611 | 206 s (3:26) | Dawn at the Dojo | `1606611.mp3` |
| 1606612 | 194 s (3:14) | 静かな朝 | `1606612.mp3` |
| 1606613 | 204 s (3:24) | 静かな朝 | `1606613.mp3` |
| 1606614 | 193 s (3:13) | 黎明の静寂 | `1606614.mp3` |
| 1606615 | 203 s (3:23) | 遠室の静けさ | `1606615.mp3` |

Total ≈ 20:25. All six generated and downloaded; no errors. IDs are also in `musicful_ids.txt`.

## Track length / duration parameter (docs research)

Source: https://docs.musicful.ai/api-reference/ai-music-generator/v1-generate-music.md

**None found.** `/v1/music/generate` has no parameter that sets a target length, duration, seconds or end time. Body parameters: `action` (`auto`, `custom`, `extend`, `concat`, `upload`, `upload_extend`, `artist_consistency`), `style`, `mv`, `instrumental`, `lyrics`, `title`, `gender`, `continue_at`, `continue_song_id`, `audio_url`, `singer_id`.

Length-related only indirectly:
- `mv` sets a ceiling, not a target: MFV3.0 / MFV2.0 / MFV1.5X / MFV1.5 generate songs up to 8 minutes, MFV1.0 up to 4 minutes.
- `continue_at` (+ `continue_song_id`) with `action=extend` / `upload_extend` sets where a continuation starts in an existing song; `concat` joins segments. The docs do not say how long the added segments are.

The tool was not changed and no new parameter was used.
