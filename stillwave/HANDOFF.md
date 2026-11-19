# StillWave — handoff between chats

**Read this first in any new or parallel chat about StillWave.** Updated at the end of each working session. Full rules: `stillwave/CLAUDE.md`. One file per video: `stillwave/scripts/<slug>.md`.

## How a video is made now (samurai series, from 2026-11)

1. **Theme** from VidIQ data. Main keyword `samurai music` (~80K/month, low competition), also `samurai meditation music`, `empty mind`. What wins: one huge icon + a small samurai (tiger / dragon / wolf painted on fusuma, giant moon, katana).
2. **Frame**: NanoBanana prompt (photoreal, "a frame from a Kurosawa film", samurai back to camera, exactly two sheathed swords, no text). Crop black bars, exact 16:9, 4K.
3. **Animation**: Flow (camera locked, first frame = last frame, wind/mist stated for the whole clip, never name what must not appear) **or** a local script with no Flow credits (`stillwave/assets/okami-animate.py`: candle flicker, light, glowing eyes, mist/ink drift, breathing; seamless 12 s loop, native 4K).
4. **Music**: Musicful API, one prompt under 1000 characters (quiet, no percussion, nothing that builds). 4 requests = 8 tracks = 24 units, run in a helper cloud session in the "dan-documents" environment; tracks arrive on a git branch `claude/<album>-musicful`.
5. **Copyright check**: one video of all 8 tracks → user uploads Unlisted → YouTube check.
6. **Album**: pick 6 of 8 (one key, even loudness, tracks from the same request never adjacent, incl. across the loop), `sevenlights/tools/make_long_track.py`, loop to exactly 2:00:00, deliver WAV in four 30-min parts. **Sound on trial**: "universal" master for headphones + TV (high-pass 40 Hz, −2 dB at 250 Hz, +2.5 dB shelf from 3.5 kHz, −14 LUFS) — see `stillwave/scripts/okami-2h.md` §2b.
7. **Overlay**: Japanese phrase (kanji + romaji + gloss), transparent PNG via `skills/stillwave-album/scripts/make_overlay.py`, CapCut 0:03–0:14.
8. **Thumbnail v2**: big white brush kanji on the left, tracked name, thin rule with a circle, "SAMURAI MEDITATION MUSIC" (`stillwave/assets/<slug>-compose-thumb-v2.py`).
9. **SEO**: title with Music in the first half and no hashtags; description with poetic tracklist + "(the cycle repeats until 2:00:00)" + links to other series videos; ~24 tags under 500 chars; pinned comment with a question.
10. **Upload**: user assembles in CapCut, schedules, Not for kids, playlists "Japanese Zen Music" + "Samurai Meditation Music — Japanese Zen for Focus & Sleep".
11. **Shorts**: one per published long-form, 24 s vertical (`stillwave/assets/samurai-short-build.py`), published the day after the long-form, Related video = the long-form. Copy in `stillwave/scripts/samurai-shorts-2026-11.md`.
12. **NEW (2026-11-19) — motion-graphics Shorts, version B**: everything animated in code, no Flow — eyes already glowing at frame 1, kinetic words, the kanji written stroke by stroke with a brush (KanjiVG order), ink-bleed transitions, gold dust, the video's own loop underneath. Full method: **`stillwave/motion-shorts.md`**. Script: `stillwave/assets/okami-short-motion.py` (tuned for ŌKAMI; adapt per slug). ŌKAMI is the A/B pilot: version A (template, `samurai-short-build.py okami ...`) vs version B, published 2–3 days apart; compare "viewed vs swiped" and average view duration after 7 days. The user liked B.

## Current state (2026-11-19)

| Video | Status | Link |
|---|---|---|
| MUSHIN | published (the engine, ~54% of channel views) | https://youtu.be/CamT9sohYQM |
| BUSHIDO | published | https://youtu.be/pxjc2GIyvBY |
| DOJO | published (sounded muddy on the user's TV → TV master trial) | https://youtu.be/sV1xoJKKIw0 |
| RONIN | published | https://youtu.be/GNe88uwbsFg |
| Miyamoto Musashi | published | https://youtu.be/mJ3RMn3J4B8 |
| MUSHIN II | scheduled 2026-11-20 16:00 | https://youtu.be/aleEGL01VO4 |
| KATANA | scheduled 2026-11-22 16:00 | https://youtu.be/_fDIyyxtpWQ |
| ŌKAMI | everything ready (4K animation, overlay, thumbnail, SEO, 2 h in normal + TV master); user is checking the TV master on headphones | — |

Shorts ready: BUSHIDO, DOJO, RONIN, MUSHIN II, KATANA (plan: 2 a day, 5–6 h apart, never before their long-form). ŌKAMI Short: after its link and date.

Musicful balance: 70 units (~2 more albums). Next album: decide after the 2026-11-29 review (CTR of the thumbnails, end-screen clicks from MUSHIN, subscribers from Shorts). Candidates: another animal on fusuma (crane, bear, koi); SHOGUN has almost no search demand.

## Agreed for the next videos (2026-11-19)
- Every hero prompt comes as a pair: 16:9 for the long-form + 9:16 for the Shorts (generated with the approved 16:9 as reference, at the highest resolution NanoBanana offers). Shorts are then built from the native vertical frame, not from a crop of the 16:9 one.
- Frame the 16:9 so nothing has to be cropped later (e.g. start at the top edge of the painted doors), so all the pixels go into the 4K render.
- ŌKAMI: no 9:16 frame this time (user is saving credits); its Shorts use crops of the 16:9 loop.

## Open decisions
- TV master: if the user approves ŌKAMI's on headphones, it becomes the standard for every album.
- DOJO: keep, or re-upload with the TV master.
