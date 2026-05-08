# Bonsai Desk Late Night — 2H Coding Focus

## Meta

- **Title:** Deep Focus Music — Bonsai Desk Late Night | 2H Coding, Writing & Hyperfocus
- **Slug:** `bonsai-desk-night-2h`
- **Format:** Long-form
- **Length:** 2H (7 200 sec)
- **Phase:** 1 (soft intro — balanced hybrid: modern dominant + Japanese accent)
- **Aesthetic:** Hybrid Tokyo Apartment — high-floor skyscraper desk + open MacBook + bonsai + neon Tokyo skyline through floor-to-ceiling window
- **Status:** script ready — awaiting Suno + NanoBanana generation
- **Upload date:** TBD (week of May 13–19)

---

## 1. 🎵 Suno Prompt A — Style field

```
Lo-fi minimal piano figure with deep sub-bass pulse every 8 bars, soft rain ambient on glass window, distant city night hum (no traffic horns), occasional vinyl crackle, gentle warm analog synth pad in the background. 65 BPM. Modern lo-fi study beats with Japanese minimalism — slower than typical lo-fi, more atmospheric, no drums, no hi-hats. Loopable for 2 hours, no climax, sustained focused atmosphere. instrumental only, no vocals, no singing, no chanting, no spoken word, pure instrumental
```

## 2. 🎵 Suno Prompt B — Lyrics field

```
[no lyrics, no vocals, instrumental only]
[opening: soft city night ambient, distant traffic in the distance, light rain begins falling on a glass window]
[section A: minimal piano figure repeats slowly, sub-bass pulses every 8 bars like a heartbeat]
[section B: warm synth pad swells gently, vinyl crackle subtle in the background, rain stays constant on glass]
[section C: piano drops to single sustained notes, sub-bass holds, breath of silence in the texture]
[loop point: rain and city ambient remain throughout, piano cycles without resolution, no audible break]
[mood: programmer awake at 3 AM, bonsai watching from the corner of the desk, code on screen]
[texture: glass condensation, warm laptop glow, soft fabric, distant city pulse]
```

---

## 3. 🎨 NanoBanana prompt 16:9 (thumbnail + video visual)

```
Photorealistic cinematic interior scene, modern luxury minimalist Japanese apartment on a high floor of a Tokyo skyscraper at night, light rain on the floor-to-ceiling window. Floor-to-ceiling glass windows dominate the right two-thirds of the frame. Beyond the windows: massive Japanese cityscape stretching to horizon — countless neon signs (kanji and katakana characters glowing in pink, cyan, electric green, warm amber, magenta), distant skyscrapers with lit windows in vertical grids, red taillight streaks of cars on highways and streets winding far below, warm yellow street lights of Tokyo creating a sea of urban glow. Light rain streaks on the glass, neon city visible but slightly distorted into beautiful bokeh. Foreground inside the apartment (left third of frame): dark walnut writing desk perpendicular to the window with an open silver MacBook laptop (warm amber screen glow as the dominant interior light source), a small Japanese black pine bonsai in a clay pot on the corner of the desk catching the city neon glow, a ceramic coffee mug with subtle steam rising, an open notebook with leather cover. Muted dark interior palette (charcoal blacks, walnut browns, warm amber laptop glow as the central highlight) contrasted with vibrant but soft neon city accents (pink, cyan, amber, red taillights) bokeh through the glass. Atmospheric depth across three planes: foreground desk with bonsai and laptop, mid-ground rain-streaked floor-to-ceiling window, background neon Tokyo skyline with red taillight motion blur. Wide cinematic 16:9 framing slightly asymmetric. Shallow depth of field on the bonsai and laptop with city neon as soft glowing bokeh. The laptop screen glow reflects subtly off the wet window. NO text in image. NO logos. NO watermarks. 4K detail, photorealistic rendering, high cinematic quality, late-night Tokyo apartment mood.
```

## 4. 🎨 NanoBanana prompt 9:16 (vertical Shorts version)

```
Photorealistic cinematic vertical 9:16 scene, modern luxury minimalist Japanese apartment on a high floor of a Tokyo skyscraper at night with light rain on the floor-to-ceiling window. Lower portion of frame: dark walnut desk with an open silver MacBook (warm amber screen glow as main light), a small Japanese black pine bonsai in a clay pot on the corner, a ceramic coffee mug with steam, an open notebook with leather cover. Upper two-thirds of frame: floor-to-ceiling glass window with light rain streaks, beyond the glass — neon Tokyo cityscape (kanji and katakana signs in pink, cyan, electric green, amber), distant skyscrapers with lit windows, red taillight streaks of cars on highways far below. Muted dark interior palette + vibrant neon city bokeh through the rainy glass. Vertical depth: bottom = desk and bonsai, middle = laptop screen + window edge, top = rainy window with neon Tokyo bokeh. NO text in image. NO logos. NO watermarks. 4K, photorealistic, late-night Tokyo apartment mood.
```

---

## 5. 🛠️ ffmpeg encode command (2H = 7 200 sec)

```bash
ffmpeg -loop 1 -i bonsai-desk-night-2h.jpg -i bonsai-desk-night-2h.mp3 \
  -c:v libx264 -tune stillimage -pix_fmt yuv420p -r 1 \
  -c:a aac -b:a 192k -shortest -t 7200 bonsai-desk-night-2h.mp4
```

---

## 6. 📝 YouTube Title (Phase 1 format)

```
Deep Focus Music — Bonsai Desk Late Night | 2H Coding, Writing & Hyperfocus
```

## 7. 📝 YouTube Description

```
🌃 It's 3 AM. The city is asleep. Your bonsai is the only one watching you work.

This 2-hour deep focus session is built for late-night developers, writers, and night-owl creators. Slow lo-fi piano with a sub-bass pulse like a quiet heartbeat. Soft rain on the window. Distant city hum. No drums, no buildups — just the sustained focus of being awake when no one else is.

Perfect for:
• Late-night coding & debugging
• Writing & journaling
• Trading the global markets
• Hyperfocus deep work sessions
• Creative flow at quiet hours
• Studying past midnight

Pour yourself a coffee, dim the room, let your bonsai keep watch.

▶ Subscribe for daily late-night focus sessions — new bonsai, lantern, tea house and city-rain soundscapes every week.

#deepwork #lofistudy #latenightmusic #codingmusic #focusmusic
```

## 8. 🏷️ Tags (18 tags — primary keywords first)

```
deep focus music, deep work music, focus music, late night music, coding music, programming music, study music, work music, productivity music, lo-fi study, lofi night, hyperfocus music, no distractions, ambient lofi, bonsai music, 3am focus, japanese minimal, concentration music
```

## 9. # Hashtags

```
#deepwork #lofistudy #latenightmusic #codingmusic #focusmusic
```

## 10. 📌 Pinned comment

```
🌃 It's late and you're still working. What's the project? Drop a 💻 if coding, ✍️ if writing, 📊 if studying, ☕ if just thinking — and subscribe for more late-night sessions every week.
```

## 11. 🔁 A/B title variant

```
Lo-Fi Focus Music — Bonsai & Rain at 3 AM | 2H Late Night Coding & Writing
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