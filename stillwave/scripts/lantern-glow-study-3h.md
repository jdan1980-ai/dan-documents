# Lantern Glow Study — 3H Quiet Hours

## Meta

- **Title:** Quiet Hours Focus Music — Lantern Glow Study | 3H Late Night Coding, Studying & Writing
- **Slug:** `lantern-glow-study-3h`
- **Format:** Long-form
- **Length:** 3H (10 800 sec)
- **Phase:** 1 (soft intro — modern setting, minimal Japanese accent through paper lantern)
- **Aesthetic:** Hybrid Tokyo Apartment — high-floor skyscraper study + paper andon lantern as primary interior light + neon Tokyo skyline through floor-to-ceiling window + closed MacBook + book + tea cup
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
Photorealistic cinematic interior scene, modern luxury minimalist Japanese apartment on a high floor of a Tokyo skyscraper at night, traditional Japanese paper andon lantern as the primary interior light source. Floor-to-ceiling glass windows dominate the right two-thirds of the frame. Beyond the windows: massive Japanese cityscape stretching to horizon — countless neon signs (kanji and katakana characters glowing softly in pink, cyan, electric green, warm amber, magenta), distant skyscrapers with lit windows in vertical grids, red taillight streaks of cars on highways and streets winding far below, warm yellow street lights of Tokyo creating a sea of urban glow. Foreground inside the apartment (left third of frame): solid oak writing desk parallel to the window with a closed silver MacBook laptop, an open hardcover book with a leather marker tucked between pages, a Japanese ceramic tea cup with steam, a brass fountain pen resting on a small tray. A traditional Japanese paper andon lantern sits on the desk emitting a warm amber glow that dominates the interior lighting and casts soft elongated shadows across the desk surface. The warm interior lantern glow creates striking chiaroscuro contrast against the cool neon city outside. On the wall behind the desk: a single hanging scroll with soft kanji calligraphy (atmospheric only, unreadable, blurred). Muted palette: deep midnight blacks of the apartment interior, warm amber lantern glow as the central interior highlight, soft cyan/pink/amber neon accents from the city through the glass, red taillight streaks far below, soft oak wood browns. Atmospheric depth across three planes: foreground desk + lantern + book, mid-ground floor-to-ceiling window, background neon Tokyo skyline with red taillight motion blur. Wide cinematic 16:9 framing slightly asymmetric. Shallow depth of field on the lantern and desk with city neon as soft glowing bokeh through the glass. NO text in image. NO logos. NO watermarks. 4K detail, photorealistic rendering, high cinematic quality, contemplative late-night Tokyo scholarly mood with warm lantern + cool neon contrast.
```

## 4. 🎨 NanoBanana prompt 9:16 (vertical Shorts version)

```
Photorealistic cinematic vertical 9:16 scene, modern luxury minimalist Japanese apartment on a high floor of a Tokyo skyscraper at night, traditional Japanese paper andon lantern as the primary interior light source. Lower portion of frame: solid oak writing desk with a closed silver MacBook laptop, an open hardcover book with leather marker, a Japanese ceramic tea cup with steam, a brass fountain pen on a small tray. Middle of frame: paper andon lantern on the desk emitting warm amber glow, casting elongated shadows. Upper two-thirds of frame: floor-to-ceiling glass window, beyond the glass — neon Tokyo cityscape (kanji and katakana neon signs in pink, cyan, electric green, amber), distant skyscrapers with lit windows, red taillight streaks of cars on highways far below. Faint blurred kanji scroll on the wall behind. Muted palette: midnight blacks of the interior, warm amber lantern glow as central interior highlight, vibrant neon city accents through the glass, red taillight streaks. Vertical depth: bottom = desk and book, middle = lantern + window edge, top = neon Tokyo skyline. NO text in image. NO logos. NO watermarks. 4K, photorealistic, contemplative late-night Tokyo scholarly mood with warm lantern + cool neon contrast.
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