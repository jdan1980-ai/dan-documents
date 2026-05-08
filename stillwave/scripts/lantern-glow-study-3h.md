# Lantern Glow Study — 3H Quiet Hours

## Meta

- **Title:** Quiet Hours Focus Music — Lantern Glow Study | 3H Late Night Coding, Studying & Writing
- **Slug:** `lantern-glow-study-3h`
- **Format:** Long-form
- **Length:** 3H (10 800 sec)
- **Phase:** 1 (soft intro — modern setting, minimal Japanese accent through paper lantern)
- **Aesthetic:** Hybrid — modern study room + paper andon lantern as primary light + distant Japanese mountain silhouette
- **Status:** script ready — awaiting Suno + NanoBanana generation
- **Upload date:** TBD (week of May 13–19)

---

## 1. 🎵 Suno Prompt A — Style field

```
Ambient drone with delicate piano figures spaced far apart, soft shakuhachi note approximately every 2 minutes, deep cello swells underneath, paper rustle texture, no rhythm — flowing meditation tempo (effective 50 BPM, no measured beat). Quiet study music with a subtle Japanese accent. Loopable for 3 hours, no climax, no resolution, sustained quiet attention. instrumental only, no vocals, no singing, no chanting, no spoken word, pure instrumental
```

## 2. 🎵 Suno Prompt B — Lyrics field

```
[no lyrics, no vocals, instrumental only]
[opening: paper andon lantern flickers softly, a low ambient drone establishes itself in the room]
[section A: piano plays single notes spaced far apart, room tone present, paper softly rustles in unseen draft]
[section B: shakuhachi enters once, breath held in the air, then silence returns]
[section C: deep cello swells slowly under the piano, lantern paper crackles softly, frame of stillness]
[loop point: drone continues seamlessly throughout, instruments cycle without break, no resolution]
[mood: scholar at a desk past midnight, ink brush in hand, single paper lantern as the only light]
[texture: paper, ink, candle wick, warm wood grain, deep night silence]
```

---

## 3. 🎨 NanoBanana prompt 16:9 (thumbnail + video visual)

```
Photorealistic cinematic interior scene, modern study room at night with a traditional Japanese paper andon lantern as the primary light source. Solid oak writing desk centered in the frame with a closed silver MacBook laptop, an open hardcover book with a leather marker tucked between pages, a Japanese ceramic tea cup with steam, a brass fountain pen resting on a small tray. The paper andon lantern sits on the windowsill behind the desk emitting a warm amber glow that dominates the lighting and casts soft elongated shadows across the desk surface. Beyond the lantern, large window shows distant misty mountain silhouettes against a deep midnight sky with a few faint stars. On the wall in the soft background: a single hanging scroll with soft kanji calligraphy (atmospheric only, unreadable, blurred). Muted palette: deep midnight blues in the upper frame, warm amber lantern glow as the central highlight, soft cedar and oak wood browns. Atmospheric depth across three planes: foreground desk and book, mid-ground lantern and window, background mountain silhouette. Wide cinematic 16:9 framing slightly asymmetric, golden lantern as the main light source creates dramatic chiaroscuro shadow play. NO text in image. NO logos. NO watermarks. 4K detail, photorealistic rendering, high cinematic quality, contemplative late-night scholarly mood.
```

## 4. 🎨 NanoBanana prompt 9:16 (vertical Shorts version)

```
Photorealistic cinematic vertical 9:16 scene, modern study room at night with a traditional Japanese paper andon lantern as the primary light source. Center of frame: solid oak writing desk with a closed silver MacBook laptop, an open hardcover book with leather marker, a Japanese ceramic tea cup with steam, a brass fountain pen on a small tray. Above the desk in the upper portion of frame: the paper andon lantern on a windowsill emitting warm amber glow, casting elongated shadows downward. Far background through the window: distant misty mountain silhouette against midnight sky. On the wall: faint blurred kanji scroll. Muted palette: midnight blues, warm amber lantern glow accent, oak wood browns. Vertical depth: bottom = desk and book, middle = lantern light source, top = mountain silhouette. NO text in image. NO logos. NO watermarks. 4K, photorealistic, contemplative scholarly mood.
```

---

## 5. 🛠️ ffmpeg encode command (3H = 10 800 sec)

```bash
ffmpeg -loop 1 -i lantern-glow-study-3h.jpg -i lantern-glow-study-3h.mp3 \
  -c:v libx264 -tune stillimage -pix_fmt yuv420p -r 1 \
  -c:a aac -b:a 192k -shortest -t 10800 lantern-glow-study-3h.mp4
```

---

## 6. 📝 YouTube Title (Phase 1 format)

```
Quiet Hours Focus Music — Lantern Glow Study | 3H Late Night Coding, Studying & Writing
```

## 7. 📝 YouTube Description

```
🏮 A single paper lantern. Distant mountains. Three hours of quiet to think.

This 3-hour focus session is built for slow, sustained study — ambient drone underneath delicate piano notes, with a single shakuhachi breath every two minutes. No rhythm, no buildups. Just the quiet rhythm of paper, ink, and lantern light.

Perfect for:
• Late-night studying & reading
• Long writing sessions
• Coding in quiet hours
• Research & note-taking
• Slow contemplative reading
• Meditation between work blocks

Light a single lamp, dim everything else, settle in. The lantern keeps the watch.

▶ Subscribe for new lantern, tea house, and bonsai-desk sessions every week.

#studywithme #ambientmusic #focusmusic #japaneseaesthetic #deepwork
```

## 8. 🏷️ Tags (18 tags — primary keywords first)

```
focus music, study music, deep focus music, ambient music, work music, productivity music, study with me, late night study, quiet hours, lantern music, japanese ambient, andon glow, slow piano focus, ambient drone study, no distractions, deep work, coding music, scholarly music
```

## 9. # Hashtags

```
#studywithme #ambientmusic #focusmusic #japaneseaesthetic #deepwork
```

## 10. 📌 Pinned comment

```
🏮 Lantern lit. Late hours. What are you studying tonight? Drop the subject below — and subscribe if quiet lantern hours are your kind of evening.
```

## 11. 🔁 A/B title variant

```
Andon Lantern Focus — 3 Hours Quiet Study Music for Coding & Writing
```

---

## Post-publish metrics

| Metric | 48h | 7d | 30d |
|--------|-----|----|----|
| Views  |     |    |    |
| Avg view duration |  |  |  |
| Watch time (h) | | | |
| Likes  |     |    |    |
| Comments |   |    |    |
| Subs gained |       |    |    |

### Notes — what worked / what didn't