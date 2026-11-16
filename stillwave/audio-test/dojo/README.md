# DOJO — Musicful test run (failed)

- **Date:** 2026-11-16
- **Command:** `python3 sevenlights/tools/musicful_album.py --prompt-file stillwave/scripts/dojo-musicful-prompt.txt --requests 4 --out stillwave/audio-test/dojo/`
- **Balance before:** 196.0
- **Balance after:** 196.0 (nothing was charged)
- **Tracks generated:** none. No track ids, no MP3s, and no `musicful_ids.txt` (the script stopped before writing it).

## Error (identical on the first attempt and the one retry)

The first `/v1/music/generate` call was rejected:

```
RuntimeError: generate: {'status': 400000, 'message': 'Invalid request parameter, description: Lyrics or style is required.', 'data': {}}
```

## Likely cause (not verified)

`stillwave/scripts/dojo-musicful-prompt.txt` is **1021 characters**. The tool sends the whole
prompt as the `style` field. The API probably rejects a `style` over a length limit
(perhaps 1000 characters) and reports it as "style is required". The prompt was left unchanged, as
instructed. Trimming it below about 1000 characters (or below a smaller limit, if the API sets one)
should fix this. Check the length limit in the Musicful docs before spending units.
