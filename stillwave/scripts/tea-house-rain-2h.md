# Tea House Rain — 2H Deep Focus

## Meta

- **Title:** Quiet Focus Music — Japanese Tea House Rain | 2H Deep Work for Coding, Writing & Late Night Study
- **Slug:** `tea-house-rain-2h`
- **Format:** Long-form
- **Length:** 2H (7 200 sec)
- **Phase:** 1 (soft intro — most Japanese-leaning of the 3 hybrid videos)
- **Aesthetic:** Hybrid — engawa veranda + closed MacBook + Japanese tea cup
- **Status:** script ready — awaiting Suno + NanoBanana generation
- **Upload date:** TBD (week of May 13–19)

---

## 1. 🎵 Suno Prompt A — Style field

```
Slow ambient lo-fi soundscape with rain falling on shoji paper screens, distant koto plucks every 30 seconds, soft warm analog synth pad, deep wooden creak undertones from a traditional Japanese tea house, occasional shakuhachi breath note, water dripping from eaves into a stone basin. 60 BPM. Rain dominates the texture, music is delicate background. Loopable for 2 hours, no buildup, no climax, sustained meditative atmosphere. instrumental only, no vocals, no singing, no chanting, no spoken word, pure instrumental
```

## 2. 🎵 Suno Prompt B — Lyrics field

```
[no lyrics, no vocals, instrumental only]
[opening: a single distant temple bell rings once, rain begins falling on shoji paper screens]
[section A: koto plucks slowly every 30 seconds, water dripping from eaves into a stone tsukubai basin, deep wood creak]
[section B: shakuhachi breath note enters far away, mist rolling over a bamboo grove outside]
[section C: brief silence held for 8 seconds, then rain swells and koto returns more intimately]
[loop point: rain texture remains constant throughout, instruments fade in and out around it, no audible break in audio]
[mood: monk alone in a quiet tea house at dusk, brush in hand, time forgotten]
[texture: wet wood floors, paper screens, distant water on stone, soft brushstroke on rice paper]
```

---

## 3. 🎨 NanoBanana prompt 16:9 (thumbnail + video visual)

```
Photorealistic cinematic interior scene, traditional Japanese tea house engawa veranda at dusk during light rain. Low cedar wood writing desk in the foreground with a closed silver MacBook laptop centered, a traditional Japanese ceramic tea cup with steam gently rising on the right of the laptop, a small bamboo tea whisk and an ink stone with a calligraphy brush. Beyond the desk, traditional shoji paper screens slightly slid open showing a wet bamboo grove and gentle rain falling onto a stone tsukubai basin. Warm amber glow from a single paper andon lantern on the left of the frame casting soft shadows. Muted natural palette: deep forest greens, wet cedar wood browns, soft misty grays, single warm amber lantern accent. Atmospheric depth across three planes: foreground desk and tea cup, mid-ground shoji screens with falling rain, background bamboo silhouettes fading into mist. Soft rainy late-afternoon daylight combined with interior lantern glow. Wide cinematic 16:9 framing slightly asymmetric, shallow depth of field on the laptop and tea cup, bamboo and rain softly out of focus. Wet wood textures, condensation on cup, subtle steam rising. NO text in image. NO logos. NO watermarks. 4K detail, photorealistic rendering, high cinematic quality, contemplative quiet mood.
```

## 4. 🎨 NanoBanana prompt 9:16 (vertical Shorts version)

```
Photorealistic cinematic vertical 9:16 scene, traditional Japanese tea house engawa veranda at dusk during light rain. Low cedar wood writing desk centered with a closed silver MacBook laptop and a traditional Japanese ceramic tea cup with steam rising. Above the desk: shoji paper screens slightly open showing wet bamboo grove and rain falling beyond, mist rolling. To the lower-foreground: small bamboo tea whisk and ink stone. Warm amber glow from a paper andon lantern at the upper-left. Muted natural palette: forest greens, wet cedar wood browns, soft misty grays, single amber accent. Vertical depth: bottom = desk and tea cup foreground, middle = shoji and rain, top = bamboo silhouettes in mist. NO text in image. NO logos. NO watermarks. 4K, photorealistic, contemplative.
```

---

## 5. 🛠️ ffmpeg encode command (2H = 7 200 sec)

```bash
ffmpeg -loop 1 -i tea-house-rain-2h.jpg -i tea-house-rain-2h.mp3 \
  -c:v libx264 -tune stillimage -pix_fmt yuv420p -r 1 \
  -c:a aac -b:a 192k -shortest -t 7200 tea-house-rain-2h.mp4
```

---

## 6. 📝 YouTube Title (Phase 1 format)

```
Quiet Focus Music — Japanese Tea House Rain | 2H Deep Work for Coding, Writing & Late Night Study
```

## 7. 📝 YouTube Description

```
🍵 Step into a quiet Japanese tea house at dusk. Rain on shoji screens, mist over the bamboo, your MacBook open, the world finally still.

This 2-hour deep focus session is built for sustained concentration — slow ambient music layered under real rainfall on paper screens. Distant koto plucks and a single shakuhachi breath every few minutes. No buildups, no drops, no distractions. Just the sound of rain and quiet attention.

Perfect for:
• Deep coding & programming
• Late-night writing
• Studying & reading
• Trading & analysis
• Creative flow
• Quiet contemplation

Put on your headphones, pour yourself something warm, and step into the Tea House.

▶ Subscribe for daily deep focus sessions — new tea house, lantern, and quiet city soundscapes every week.

#deepfocus #studymusic #japaneseambient #rainmusic #focusmusic
```

## 8. 🏷️ Tags (18 tags — primary keywords first)

```
deep focus music, focus music, study music, coding music, work music, productivity music, japanese ambient, rain on shoji, lo-fi study, late night focus, deep work, concentration music, no distractions, ambient rain, tea house ambient, koto rain music, shakuhachi rain, calm focus
```

## 9. # Hashtags

```
#deepfocus #studymusic #japaneseambient #rainmusic #focusmusic
```

## 10. 📌 Pinned comment

```
🍵 If this rain helps you focus — what are you working on right now? Drop one word below (coding, writing, studying, trading...) — and subscribe for a new tea-house session every week 🌧️
```

## 11. 🔁 A/B title variant

```
Rain on Shoji Screens — Japanese Tea House Focus | 2H Deep Work Music for Coding & Studying
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