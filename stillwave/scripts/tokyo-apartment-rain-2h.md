# Tokyo Apartment Rain — 2H Deep Focus

## Meta

- **Title:** Quiet Focus Music — Tokyo Apartment Rain | 2H Deep Work for Coding, Writing & Late Night Study
- **Slug:** `tokyo-apartment-rain-2h`
- **Format:** Long-form
- **Length:** 2H (7 200 sec)
- **Phase:** 1 (soft intro — most rainy/ambient of the 3 hybrid videos)
- **Aesthetic:** Hybrid Tokyo Apartment — high-floor skyscraper apartment + rainy floor-to-ceiling window over neon Tokyo + tea cup + bonsai
- **Status:** script ready — awaiting Suno + NanoBanana generation
- **Upload date:** TBD (week of May 13–19)

---

## 1. 🎵 Suno Prompt A — Style field

```
Slow ambient lo-fi soundscape with heavy rain falling on a high floor floor-to-ceiling glass window, distant koto plucks every 30 seconds, soft warm analog synth pad, deep sub-bass pulse every 16 bars (the city heartbeat), occasional muted city ambient hum (no traffic horns), water dripping from a window frame. 60 BPM. Rain dominates the texture, music is delicate background. Loopable for 2 hours, no buildup, no climax, sustained meditative atmosphere. instrumental only, no vocals, no singing, no chanting, no spoken word, pure instrumental
```

## 2. 🎵 Suno Prompt B — Lyrics field

```
[no lyrics, no vocals, instrumental only]
[opening: a single distant temple bell rings once far below in the city, heavy rain begins falling against a tall glass window]
[section A: koto plucks slowly every 30 seconds, sub-bass pulses softly every 16 bars like the city's heartbeat, muted Tokyo ambient hum below]
[section B: warm synth pad swells gently, condensation forms on the glass, neon glow softens through the rain]
[section C: piano enters with single sustained notes, brief silence held for 8 seconds, then rain swells back]
[loop point: rain texture remains constant throughout, instruments fade in and out around it, no audible break in audio]
[mood: alone in a high apartment, neon Tokyo below, rain on the glass, time forgotten]
[texture: wet glass, condensation, distant city pulse, soft brushstroke on rice paper]
```

---

## 3. 🎨 NanoBanana prompt 16:9 (thumbnail + video visual)

```
Photorealistic cinematic interior scene, modern luxury minimalist Japanese apartment on a high floor of a Tokyo skyscraper at night during heavy rain. Floor-to-ceiling glass windows dominate the right two-thirds of the frame. Beyond the rain-streaked windows: massive Japanese cityscape stretching to horizon — countless neon signs (kanji and katakana characters glowing in pink, electric blue, electric green, warm amber, and magenta through the rainy glass), distant skyscrapers with lit windows in vertical grids, red taillight streaks of cars on highways and streets winding far below, warm yellow street lights creating a sea of urban glow. Rain runs down the glass in long streaks, slightly distorting the neon city behind into soft beautiful bokeh. Foreground inside the apartment (left third of frame): low cedar wood writing kotatsu-style table with a closed silver MacBook laptop centered, a Japanese ceramic tea cup with steam rising, a single small black pine bonsai in a clay pot in the corner. Soft warm interior glow from a single floor lamp creates contrast with the cool neon city outside. Muted dark interior palette (charcoal blacks, deep grays, warm cedar wood browns) contrasted with vibrant but soft neon city accents (pink, cyan, amber, red taillights) bokeh through the rainy glass. Atmospheric depth across three planes: foreground table with tea and laptop, mid-ground rain-streaked floor-to-ceiling window, background neon Tokyo cityscape with red taillight motion blur. Wide cinematic 16:9 framing slightly asymmetric. Shallow depth of field on the laptop and tea cup with city lights as soft glowing bokeh. NO text in image. NO logos. NO watermarks. 4K detail, photorealistic rendering, high cinematic quality, contemplative late-night Tokyo mood with rain.
```

## 4. 🎨 NanoBanana prompt 9:16 (vertical Shorts version)

```
Photorealistic cinematic vertical 9:16 scene, modern luxury minimalist Japanese apartment on a high floor of a Tokyo skyscraper at night during heavy rain. Lower third of frame: low cedar wood kotatsu-style table with a closed silver MacBook, a Japanese ceramic tea cup with steam, a small black pine bonsai. Middle to upper portion of frame: floor-to-ceiling glass window with heavy rain streaks running down, beyond the glass — neon Tokyo cityscape (kanji and katakana neon signs in pink, cyan, electric green, amber), distant skyscrapers with lit windows, red taillight streaks of cars on highways far below. Soft warm interior glow contrasts with cool neon city outside. Muted dark interior palette + vibrant neon bokeh accents through rainy glass. NO text in image. NO logos. NO watermarks. 4K, photorealistic, contemplative late-night Tokyo mood.
```

---

## 5. 🛠️ ffmpeg encode command (2H = 7 200 sec)

```bash
ffmpeg -loop 1 -i tokyo-apartment-rain-2h.jpg -i tokyo-apartment-rain-2h.mp3 \
  -c:v libx264 -tune stillimage -pix_fmt yuv420p -r 1 \
  -c:a aac -b:a 192k -shortest -t 7200 tokyo-apartment-rain-2h.mp4
```

---

## 6. 📝 YouTube Title (Phase 1 format)

```
Quiet Focus Music — Tokyo Apartment Rain | 2H Deep Work for Coding, Writing & Late Night Study
```

## 7. 📝 YouTube Description

```
🌃 High above Tokyo at night. Rain on the glass. Neon below. Just you, your laptop, and the city.

This 2-hour deep focus session is built for sustained concentration. Slow ambient music layered under heavy rain falling on a high apartment window, with the city's soft pulse far below. Distant koto plucks, a sub-bass heartbeat every sixteen bars. No buildups, no drops. Just the rhythm of rain and the glow of neon Tokyo.

Perfect for:
• Deep coding & programming
• Late-night writing
• Studying & reading
• Trading & analysis
• Creative flow
• Quiet contemplation

Pour something warm, dim the room, let the rain handle the rest.

▶ Subscribe for new Tokyo apartment, lantern, and quiet city sessions every week.

#deepfocus #studymusic #tokyo #rainmusic #focusmusic
```

## 8. 🏷️ Tags (18 tags — primary keywords first)

```
deep focus music, focus music, study music, coding music, work music, productivity music, japanese ambient, tokyo rain, tokyo apartment ambient, lo-fi study, late night focus, deep work, concentration music, no distractions, ambient rain, neon tokyo, koto rain, calm focus
```

## 9. # Hashtags

```
#deepfocus #studymusic #tokyo #rainmusic #focusmusic
```

## 10. 📌 Pinned comment

```
🌃 High floor. Rain on the glass. Neon below. What are you working on tonight? Drop one word — coding, writing, studying, trading — and subscribe for a new Tokyo apartment session every week 🌧️
```

## 11. 🔁 A/B title variant

```
Rain on the Glass — Tokyo Apartment Focus Music | 2H Deep Work for Coding & Studying
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