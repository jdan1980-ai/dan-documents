# Bonsai Desk Late Night — 2H Coding Focus

## Meta

- **Title:** Deep Focus Music — Bonsai Desk Late Night | 2H Coding, Writing & Hyperfocus
- **Slug:** `bonsai-desk-night-2h`
- **Format:** Long-form
- **Length:** 2H (7 200 sec)
- **Phase:** 1 (soft intro — balanced hybrid: modern dominant + Japanese accent)
- **Aesthetic:** Hybrid — modern minimalist desk at night + small bonsai accent
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
Photorealistic cinematic interior scene, modern minimalist apartment at night, light rain on the large window. Dark walnut writing desk centered in the frame with an open silver MacBook laptop (warm amber screen glow is the dominant light source illuminating the entire scene), a small Japanese black pine bonsai in a clay pot on the corner of the desk, a ceramic coffee mug with subtle steam rising, an open notebook with a leather cover beside the laptop, a brass desk lamp turned off in the background. Beyond the window: blurred night cityscape with soft amber and white light points, gentle rain streaks running down the glass. Muted dark palette: deep charcoal blacks, warm amber laptop glow as the central highlight, distant city lights as small bright accents, soft cool grays in the rain. Atmospheric depth across three planes: foreground desk with bonsai and laptop, mid-ground rain-streaked window, background blurred city skyline bokeh. Wide cinematic 16:9 framing slightly asymmetric, shallow depth of field on the bonsai and laptop. Wet glass textures, the laptop screen glow reflects off the wet window. NO text in image. NO logos. NO watermarks. 4K detail, photorealistic rendering, high cinematic quality, contemplative late-night mood.
```

## 4. 🎨 NanoBanana prompt 9:16 (vertical Shorts version)

```
Photorealistic cinematic vertical 9:16 scene, modern minimalist apartment at night with rain on a large window. Center: dark walnut desk with open silver MacBook laptop (warm amber screen glow as main light), small Japanese black pine bonsai in a clay pot on the corner, ceramic coffee mug with steam, open notebook with leather cover. Above the desk: large window taking up upper half of frame, showing blurred night cityscape with soft amber light points and rain streaks running down the glass. Muted dark palette: charcoal blacks, warm amber laptop glow accent, distant city lights, soft gray rain. Vertical depth: bottom = desk and bonsai, middle = laptop screen, top = rainy window with city bokeh. NO text in image. NO logos. NO watermarks. 4K, photorealistic, contemplative late-night mood.
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