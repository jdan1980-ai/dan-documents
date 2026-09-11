# HACHIMAN — 八幡 | Japanese Zen Music for Courage, Protection & Inner Strength

## Meta

- **Series:** Kanji-Concept — **KAMI (神) "Gods of Japan" sub-series (1 of many)** — new series launched 2026-09-01, sibling to the completed RYŪ (5 dragons) sub-series. Each video = one Shinto/Buddhist deity, manifesting as a colossal LIVING figure of light (never a statue, never a painted mural — same lesson as RYŪ), with one signature sacred creature/symbol tied to that god.
- **Slug:** hachiman-1h
- **Concept:** 八幡 (Hachiman) — god of war, archery and divination, guardian of Japan and patron deity of the samurai class and the bushi warrior spirit. Historically syncretized with Emperor Ōjin; principal shrines Usa Jingū, Iwashimizu Hachimangū, and Tsurugaoka Hachimangū (built by the Minamoto shogunate — the historical root of everything "samurai" on this channel). Sacred messenger: the white dove (hato) — Hachiman shrines use dove guardian-statues instead of the usual komainu lion-dogs.
- **Playlist (add to in Studio):** Japanese Zen Music
- **Length target:** ~1H full album — **shortened from the series-standard 2H, deliberate pilot** (locked 2026-09-08): average watch time on the channel runs ~30 min, and CLAUDE.md already validates 1H as the sweet spot for Healing Hour/standard Power Hour, so this cuts unproven extra length rather than cutting quality.
- **Music source — PILOT (locked 2026-09-08):** **Google Lyria** (via Gemini API/Vertex AI), not Suno. Reason: Suno capped downloads (Free 7 lifetime / Pro 20/mo / Premier 60/mo, effective 2026-09-03) — far below what this channel's volume needs, and no confirmed workaround exists. Lyria tested well on instrumental/ambient fidelity (independent reviews rate it the strongest of the major models specifically for instrumental/ambient output) and has no download cap — pay-per-generation via API (~$0.04–0.08/track). §1 below carries both the new Lyria-structured prompts (primary, use these first) and the original Suno prompts (kept as fallback in §1-Suno in case Lyria's Japanese-instrument timbre doesn't hold up over a full album — Stable Audio failed this test, Lyria has not yet been validated at album scale).
- **Status:** 🟡 IN PROGRESS — ✅ 38 Lyria tracks generated, mastered, selected (21 tracks, 59:34) → `HACHIMAN-ALBUM/`, §8 tracklist written. **Next: generate hero (§3), rename the 2 flagged files (see rename script below), then CapCut laydown.** Lyria pilot validated well on volume/no download cap — the real listening-quality verdict is still pending user review of the final album.

---

## §0 — Positioning & pre-production

- **🔒 KAMI series invariants (locked 2026-09-01, decided before this first video):** each god manifests as a colossal figure formed of LIVING LIGHT/MIST — never a statue, never a carved idol, never a painted mural. Only the god's face/torso and one accompanying sacred symbol or creature need to be clearly "made of" light; the rest may dissolve into mist/sky, same living-element logic locked for the RYŪ dragons. A lone samurai or worshipper, back to camera, hair in a simple topknot, NO helmet, anchors human scale — carried over from RYŪ because it already works for this channel. EXACTLY TWO sheathed swords (daishō) worn at the LEFT hip for a standing figure (thrust through the obi, blade edge up, hilts forward-and-up — the historically correct carry, confirmed on SEIRYU), or resting on a low rack for a seated/kneeling figure. Dark tabi socks + straw waraji sandals — never barefoot (SEIRYU lesson, applies series-wide from the start this time). Each god gets its own **signature light colour** (recurring detail, same pattern as the RYŪ eye-glow colours) — **HACHIMAN = warm white-gold**.
- **HACHIMAN (八幡) — visual hook:** a lone samurai kneels or stands in front of an actual Hachiman-zukuri shrine building at dusk (vermillion-lacquered wood, dark cypress-bark roof, curved chidori-hafu gable — the real architectural style of Usa Jingū, the origin shrine of all Hachiman worship, per the reference photo), facing a colossal warrior-spirit that takes shape out of the fading light itself above the shrine's roofline — armored in ghostly light-formed plate, a massive bow of pure white-gold light raised in one hand, its face calm and resolute. Two or three white doves (Hachiman's sacred messengers) circle slowly around the manifestation, their forms faintly luminous. The spirit's visible head, torso and bow are "made of" the light, the rest of its lower body dissolving into the darkening sky.
- **🔒 Shrine architecture reference (locked 2026-09-01, from user-supplied photo of Usa Jingū):** vermillion/orange-red lacquered wood pillars, beams and lattice railings; a dark, thick cypress-bark (hiwada-buki) roof; an ornate curved gabled entrance porch (chidori hafu) jutting forward from the main roofline; dark wood latticework shoji-style windows; wide stone steps leading up to the veranda. This is a REAL, specific architectural style — not a generic "mountain shrine terrace" — carry it into every frame of this video (hero, Shorts, thumbnail).
- **🔒 No falling/floating petals, no random airborne particles — do not mention them even to forbid them** (locked NanoBanana/Veo rule, learned on ICHIGO ICHIE: naming "no X" still generates X). The doves are the one intentional airborne element and must be described as already in slow, graceful, continuous circular flight — not scattered mid-air debris.
- **🔒 Any light source that should stay constant (the spirit's glow, the doves' faint luminescence) must be described as ALREADY THERE from the first frame** — never fading in mid-loop (SUIRYU lesson).
- **Wisdom phrase is NOT 八幡 itself** (overlay ≠ title concept, series rule). Chosen: **質実剛健** (shitsujitsu gōken — "sincere and robust," the ideal of plain, unadorned inner strength prized in the bushi warrior spirit — strength that needs no display). See §6a.
- **🇺🇦** Новая под-серия **KAMI (神) — «Боги Японии»**, идёт следом за завершённой RYŪ. Инварианты серии: бог — ЖИВАЯ фигура из света/тумана (никогда не статуя, не роспись — тот же урок, что у драконов), у каждого бога свой фирменный цвет свечения (Хатиман = тёплый бело-золотой), одинокий самурай/проситель спиной к камере для масштаба, ровно 2 меча (стоя — на поясе, лезвием вверх; сидя — на подставке), таби+варадзи вместо босых ног (закреплено с самого начала). Хатиман (八幡) — бог войны, стрельбы из лука и гадания, покровитель самураев и защитник Японии; его посланник — белый голубь. Мудрость на оверлее — НЕ 八幡, а отдельная фраза (см. §6a).

---

## §1 — Lyria prompts (PRIMARY — 10 copy-paste variants, structured format)

> 🔒 **Pilot format (locked 2026-09-08).** Lyria's prompt structure is different from Suno's Style+Lyrics pair: ONE descriptive prompt + a separate `negative_prompt` field. Google's own docs demonstrate Lyria CAN build to a crescendo if asked — so our flat-dynamics requirement must be stated explicitly in the prompt AND reinforced in `negative_prompt`, not left to inference. Access via Gemini app (30-sec test clips, free/cheap) or the Gemini API / Vertex AI (full length up to ~3 min, ~$0.04–0.08/generation, no download cap). Each variant below keeps the SAME opening-idea/instrument-lead as its Suno counterpart (for anti-Content-ID opening variety once selected into the album) but is reformatted for Lyria's structure.
> **🇺🇦** Формат Lyria отличается от Suno: один описательный промт + отдельное поле `negative_prompt`. Google сама показывает, что Lyria умеет наращивать динамику, если её не остановить — поэтому плоскую динамику нужно прописывать явно и в тексте, и в negative_prompt. Доступ — через приложение Gemini (тест на 30 сек) или через Gemini API/Vertex AI (полная длина ~3 мин, без лимита на скачивание).

**negative_prompt — same for all 10 variants:**
```
drums, percussion, beat, rhythmic pulse, arpeggios, crescendo, build, swell, climax, rising intensity, dramatic change, vocals, singing, chanting, spoken word
```

### Lyria Variant 1 — temple-bell-led
```
Deeply meditative Japanese zen ambient for inner strength and calm resolve, for sleep. Mood: resolute but calm, warm dusk light, quiet inner strength rather than martial drama. Instrumentation: a distant temple bell (bonshō) that tolls once and resonates a long time, warm koto answering softly with single notes and long gaps between them, a low even string pad resting beneath. Tempo & rhythm: extremely slow, free tempo, no fixed beat, completely ametric — every note floats and decays on its own, koto never falls into a repeating pattern. Arrangement: stays at one soft, steady, unchanging level from the first second to the last — no build, no crescendo, no climax; the bell tolls once more near the end at the exact same soft level as the opening. Soundscape: a lone figure kneeling before a shrine at dusk, the last warm light settling, profound resolute stillness.
```

### Lyria Variant 2 — shakuhachi-led
```
Deeply meditative Japanese zen ambient for quiet resolve, for sleep. Mood: settled, unshaken, quiet strength held without needing to be shown. Instrumentation: a breathy shakuhachi flute leading from the start with long steady tones, a warm even drone pad and a distant koto resting beneath in gentle accord. Tempo & rhythm: deeply slow, free tempo, no fixed beat, completely ametric — the flute's tones float and decay on their own. Arrangement: stays at one soft, steady, unchanging level from the first second to the last — no build, no crescendo, no climax; the flute softens near the end to almost nothing while the pad holds exactly as it was. Soundscape: quiet strength held in stillness, warm dusk air over a mountain shrine.
```

### Lyria Variant 3 — drone-pad-opening
```
Deeply meditative Japanese zen ambient, warm and grounded, for sleep. Mood: enveloping, warm, settled, the stillness before a vow. Instrumentation: a warm even drone pad resting at a low level from the very first second with no melody for the first eight seconds, then a soft koto and a distant flute drifting in gently on top, a faint bell shimmer appearing later. Tempo & rhythm: extremely slow, free tempo, no fixed beat, completely ametric. Arrangement: stays at one soft, steady, unchanging level throughout — no build, no crescendo, no climax; koto and flute recede near the end leaving the warm even pad drifting alone. Soundscape: the stillness before a vow, unshaken, a quiet mountain shrine at dusk.
```

### Lyria Variant 4 — koto-led
```
Deeply meditative Japanese zen ambient, clear and steady, for sleep. Mood: a single note ringing out like a quiet, unbroken vow. Instrumentation: sparse warm koto with each note ringing alone and long silence between notes, a soft even drone pad and a distant shakuhachi resting beneath in gentle accord. Tempo & rhythm: slow, free tempo, no fixed beat, completely ametric — the koto never falls into a repeating pattern, notes spread further apart as the piece continues. Arrangement: stays at one soft, steady, unchanging level from the first second to the last — no build, no crescendo, no climax. Soundscape: intimate clear wood tones over blended silence, a mountain shrine at dusk.
```

### Lyria Variant 5 — rin-bell-and-drone-led
```
Deeply meditative Japanese zen ambient, hushed and steadfast, for sleep. Mood: a guardian keeping watch, calm and unmoved. Instrumentation: a small rin bell shimmering softly at the opening, a warm even drone resting beneath it, koto and shakuhachi drifting far away with long gaps between phrases. Tempo & rhythm: extremely slow, free tempo, no fixed beat, completely ametric. Arrangement: stays at one soft, steady, unchanging level throughout — no build, no crescendo, no climax; the rin bell returns once more near the end at the same soft level, then only the clear even drone remains. Soundscape: shimmering and weightless, a guardian spirit watching over a quiet shrine at dusk.
```

### Lyria Variant 6 — dusk-air-led
```
Deeply meditative Japanese zen ambient, for sleep. Mood: a mountain shrine terrace, the last light of day settling, hushed and warm. Instrumentation: several seconds of soft still dusk air with the faintest distant birdsong before any instrument enters, then a warm singing bowl and a soft even drone, a koto answering far away. Tempo & rhythm: extremely slow, free tempo, no fixed beat, completely ametric. Arrangement: stays at one soft, steady, unchanging level throughout — no build, no crescendo, no climax; instruments thin out near the end until only the dusk air and the even drone remain. Soundscape: airy, still, warm, a mountain shrine terrace at the last light of day.
```

### Lyria Variant 7 — harp-led
```
Deeply meditative Japanese zen ambient, for sleep. Mood: steady light settling evenly over a quiet shrine terrace, gentle and resolute. Instrumentation: a soft harp playing single clear notes with long gaps and never a repeating pattern, a warm even string pad resting beneath, a distant flute answering in accord. Tempo & rhythm: slow, free tempo, no fixed beat, completely ametric. Arrangement: stays at one soft, steady, unchanging level throughout — no build, no crescendo, no climax; the harp slows near the end while the even pad holds steady. Soundscape: soft, clear, weightless light over a quiet shrine terrace.
```

### Lyria Variant 8 — soft-strings-led
```
Deeply meditative Japanese zen ambient, for sleep. Mood: resolve that does not need to be loud to be unbreakable. Instrumentation: soft sustained warm strings resting at a low even level from the first second like a long steady held breath, a distant shakuhachi and koto drifting in on top, a faint bell shimmer. Tempo & rhythm: deeply slow, free tempo, no fixed beat, completely ametric. Arrangement: stays at one soft, steady, unchanging level throughout — no build, no crescendo, no climax; shakuhachi and koto fade near the end back into the warm even strings. Soundscape: warm, deep, blended stillness, an unshaken resolve.
```

### Lyria Variant 9 — felt-piano-led
```
Deeply meditative Japanese zen ambient, for sleep. Mood: quiet devotion, a whole vow held without a sound. Instrumentation: a soft felt piano playing single clear notes with long silences and never a repeating pattern, a warm even drone pad and a distant koto resting beneath in gentle accord. Tempo & rhythm: slow, free tempo, no fixed beat, completely ametric. Arrangement: stays at one soft, steady, unchanging level throughout — no build, no crescendo, no climax; piano notes spread further apart near the end while the even pad holds steady. Soundscape: intimate, soft-hammered, clear stillness at a mountain shrine.
```

### Lyria Variant 10 — wind-led
```
Deeply meditative Japanese zen ambient, for sleep. Mood: a mountain shrine at dusk, wind carrying an old vow, deeply grounded. Instrumentation: several seconds of mountain wind through pine and cedar before any instrument enters, then a warm koto entering softly, a low even drone and a distant shakuhachi resting beneath. Tempo & rhythm: deeply slow, free tempo, no fixed beat, completely ametric. Arrangement: stays at one soft, steady, unchanging level throughout — no build, no crescendo, no climax; the wind returns alone for a moment near the end before the even instruments settle back in. Soundscape: airy, grounded, blended wind over a mountain shrine at dusk.
```

---

## §1-Suno — fallback prompts (10 copy-paste variants — deeply meditative, FLAT dynamics, ametric)

> 🔒 ALL variants: **no percussion, no BPM, free time** + the locked length cue AND the locked **flat-dynamics cue** (both in the tail). **🛌 The music must stay MEDITATIVE and NEVER build** — one soft even unchanging level from first second to last, no crescendo, no swell, no climax. Instruments drift in/out and change colour, volume never grows. Tempo in words only. Plucked/струнные — `never a repeating pattern`, long gaps. Each variant a DIFFERENT opening (anti-Content-ID). Tone: resolute but calm, warm dusk light, quiet inner strength rather than martial drama — courage as stillness, not as a battle cry.
> **🇺🇦** Все 10 — глубоко медитативные, ровная динамика без нарастаний. Тон: спокойная решимость, тёплый закатный свет, внутренняя сила как тишина, а не воинственный клич.

### Variant 1 — temple-bell-led
**STYLE**
```
Deeply meditative Japanese zen ambient for inner strength and calm resolve, for sleep. A distant temple bell (bonshō) tolls once and resonates a long time, warm koto answers softly, a low even string pad rests beneath in gentle accord. Slow, spacious, resolute, unchanging. no drums, no percussion, no beat, no rhythmic pulse, no arpeggios, free time with no fixed tempo, stays at one soft even gentle level the whole way through, no crescendo, no swell, no build, no rise in intensity, no climax, no dramatic change, a long slowly drifting piece that stays calm and unchanging for several minutes, unhurried and extended, do not end early, instrumental only, no vocals, no singing, no chanting, no spoken word, pure instrumental
```
**LYRICS**
```
[no lyrics, no vocals, instrumental only]
[no drums, no percussion, no beat, no tempo — free time, every note floats and decays on its own]
[dynamics: perfectly flat and even from the first second to the last — no swell, no build, no crescendo, no climax; every section stays equally soft, calm and unchanging]
[opening: one distant temple bell strike as dusk settles, four seconds of resonance, silence]
[section A: warm koto notes, never a repeating pattern, long gaps between them, all at the same soft level]
[section B: a low even string pad rests softly under the koto, steady, never swelling]
[section C: the bell tolls once more, distant, everything staying calm and level]
[loop point: the last resonance fades into the first bell with no change in volume]
[mood: a lone figure kneeling before a shrine at dusk, calm and resolute]
[texture: clear, blended, patient, hollow reverberation, unchanging]
```

### Variant 2 — shakuhachi-led
**STYLE**
```
Deeply meditative Japanese zen ambient for quiet resolve, for sleep. A breathy shakuhachi flute leads from the start with long steady tones, a warm even drone pad and distant koto resting beneath in gentle accord. Deeply slow, settled, unchanging. no drums, no percussion, no beat, no rhythmic pulse, no arpeggios, free time with no fixed tempo, stays at one soft even gentle level the whole way through, no crescendo, no swell, no build, no rise in intensity, no climax, no dramatic change, a long slowly drifting piece that stays calm and unchanging for several minutes, unhurried and extended, do not end early, instrumental only, no vocals, no singing, no chanting, no spoken word, pure instrumental
```
**LYRICS**
```
[no lyrics, no vocals, instrumental only]
[no drums, no percussion, no beat, no tempo — free time, every note floats and decays on its own]
[dynamics: perfectly flat and even from the first second to the last — no swell, no build, no crescendo, no climax; every section stays equally soft, calm and unchanging]
[opening: a breathy shakuhachi long steady tone from the second second, calm and settled]
[section A: a warm drone pad rests beneath the flute at a low even level]
[section B: a distant koto joins in accord, sparse, everything staying at the same soft level]
[section C: shakuhachi softens to almost nothing, the even pad holds the calm]
[loop point: the flute's last breath returns to the opening tone with no change in volume]
[mood: quiet strength held without needing to be shown]
[texture: airy, clear, breath-like, blended, unchanging]
```

### Variant 3 — drone-pad-only opening
**STYLE**
```
Deeply meditative Japanese zen ambient, warm and grounded, for sleep. A warm even drone pad resting at a low even level from the first second, then a soft koto and distant flute drift in gently on top in accord, nothing building. Enveloping, warm, settled, unchanging. no drums, no percussion, no beat, no rhythmic pulse, no arpeggios, free time with no fixed tempo, stays at one soft even gentle level the whole way through, no crescendo, no swell, no build, no rise in intensity, no climax, no dramatic change, a long slowly drifting piece that stays calm and unchanging for several minutes, unhurried and extended, do not end early, instrumental only, no vocals, no singing, no chanting, no spoken word, pure instrumental
```
**LYRICS**
```
[no lyrics, no vocals, instrumental only]
[no drums, no percussion, no beat, no tempo — free time, every note floats and decays on its own]
[dynamics: perfectly flat and even from the first second to the last — no swell, no build, no crescendo, no climax; every section stays equally soft, calm and unchanging]
[opening: a warm even drone pad already at a low even level, no melody for the first eight seconds]
[section A: a soft koto and a distant flute drift in together on top, long held notes]
[section B: a faint bell shimmer appears, the pad stays exactly as it was, nothing grows]
[section C: koto and flute recede, the warm even pad drifts on alone]
[loop point: the pad returns seamlessly to the start with no change in volume]
[mood: the stillness before a vow, unshaken]
[texture: warm, wide, blended, weightless, unchanging]
```

### Variant 4 — koto-led
**STYLE**
```
Deeply meditative Japanese zen ambient, clear and steady, for sleep. Sparse warm koto, each note ringing alone with long silence between, a soft even drone and distant shakuhachi resting beneath in gentle accord. Slow, resolute, settled, unchanging. no drums, no percussion, no beat, no rhythmic pulse, no arpeggios, free time with no fixed tempo, stays at one soft even gentle level the whole way through, no crescendo, no swell, no build, no rise in intensity, no climax, no dramatic change, a long slowly drifting piece that stays calm and unchanging for several minutes, unhurried and extended, do not end early, instrumental only, no vocals, no singing, no chanting, no spoken word, pure instrumental
```
**LYRICS**
```
[no lyrics, no vocals, instrumental only]
[no drums, no percussion, no beat, no tempo — free time, every note floats and decays on its own]
[dynamics: perfectly flat and even from the first second to the last — no swell, no build, no crescendo, no climax; every section stays equally soft, calm and unchanging]
[opening: three or four sparse warm koto notes, never a repeating pattern, long silences]
[section A: a soft drone pad rests underneath the koto at a low even level, never swelling]
[section B: distant shakuhachi answers the koto tenderly, all at the same soft level]
[section C: the koto slows, notes further apart, the even pad holds them, calm and unchanging]
[loop point: the last koto note decays into the opening silence]
[mood: a single note ringing out like a quiet, unbroken vow]
[texture: intimate, clear wood, blended silence, unchanging]
```

### Variant 5 — rin-bell + drone-led
**STYLE**
```
Deeply meditative Japanese zen ambient, hushed and steadfast, for sleep. A small rin bell shimmers softly, a warm even drone resting beneath, koto and shakuhachi drift far away with long gaps, all in gentle accord at one calm level. Hushed, clear, settled, unchanging. no drums, no percussion, no beat, no rhythmic pulse, no arpeggios, free time with no fixed tempo, stays at one soft even gentle level the whole way through, no crescendo, no swell, no build, no rise in intensity, no climax, no dramatic change, a long slowly drifting piece that stays calm and unchanging for several minutes, unhurried and extended, do not end early, instrumental only, no vocals, no singing, no chanting, no spoken word, pure instrumental
```
**LYRICS**
```
[no lyrics, no vocals, instrumental only]
[no drums, no percussion, no beat, no tempo — free time, every note floats and decays on its own]
[dynamics: perfectly flat and even from the first second to the last — no swell, no build, no crescendo, no climax; every section stays equally soft, calm and unchanging]
[opening: a small rin bell shimmer, a warm even drone already resting beneath it]
[section A: koto and shakuhachi drift far away, never a repeating pattern, long gaps]
[section B: the rin returns once, the even drone stays exactly as it was, all floating in accord]
[section C: the instruments fade, only the clear even drone and a last rin shimmer remain]
[loop point: the rin decay dissolves back into the opening drone with no change in volume]
[mood: a guardian keeping watch, calm and unmoved]
[texture: clear, blended, shimmering, weightless, unchanging]
```

### Variant 6 — dusk-air-led
**STYLE**
```
Deeply meditative Japanese zen ambient, for sleep. Several seconds of soft still dusk air with the faintest distant birdsong, then a warm singing bowl and a soft even drone enter, koto far away in accord, all at one calm level. Hushed, warm, settled, unchanging. no drums, no percussion, no beat, no rhythmic pulse, no arpeggios, free time with no fixed tempo, stays at one soft even gentle level the whole way through, no crescendo, no swell, no build, no rise in intensity, no climax, no dramatic change, a long slowly drifting piece that stays calm and unchanging for several minutes, unhurried and extended, do not end early, instrumental only, no vocals, no singing, no chanting, no spoken word, pure instrumental
```
**LYRICS**
```
[no lyrics, no vocals, instrumental only]
[no drums, no percussion, no beat, no tempo — free time, every note floats and decays on its own]
[dynamics: perfectly flat and even from the first second to the last — no swell, no build, no crescendo, no climax; every section stays equally soft, calm and unchanging]
[opening: five seconds of soft still dusk air, a single faint distant birdsong, no instruments yet]
[section A: a warm singing bowl and a soft drone enter softly at a low even level]
[section B: a koto answers far away, never a repeating pattern, nothing grows louder]
[section C: the instruments thin out, only the dusk air and the even drone remain]
[loop point: the calm level never changes from start to end]
[mood: a mountain shrine terrace, the last light of day settling]
[texture: airy, still, warm, blended, unchanging]
```

### Variant 7 — harp-led
**STYLE**
```
Deeply meditative Japanese zen ambient, for sleep. A soft harp plays single clear notes with long gaps, never a pattern, a warm even string pad resting beneath and a distant flute answering in accord. Slow, gentle, resolute, unchanging. no drums, no percussion, no beat, no rhythmic pulse, no arpeggios, free time with no fixed tempo, stays at one soft even gentle level the whole way through, no crescendo, no swell, no build, no rise in intensity, no climax, no dramatic change, a long slowly drifting piece that stays calm and unchanging for several minutes, unhurried and extended, do not end early, instrumental only, no vocals, no singing, no chanting, no spoken word, pure instrumental
```
**LYRICS**
```
[no lyrics, no vocals, instrumental only]
[no drums, no percussion, no beat, no tempo — free time, every note floats and decays on its own]
[dynamics: perfectly flat and even from the first second to the last — no swell, no build, no crescendo, no climax; every section stays equally soft, calm and unchanging]
[opening: a soft harp, single clear notes with long gaps, never a repeating pattern]
[section A: a warm string pad rests beneath the harp at a low even level, steady, never swelling]
[section B: a distant flute drifts over the top in accord, long held notes at the same soft level]
[section C: the harp slows, the even pad glows warm and calm, holding steady]
[loop point: the last harp note dissolves into the opening pad with no change in volume]
[mood: steady light settling evenly over a quiet shrine terrace]
[texture: soft, clear, blended, weightless, unchanging]
```

### Variant 8 — soft-strings-led
**STYLE**
```
Deeply meditative Japanese zen ambient, for sleep. Soft sustained warm strings resting at a low even level from the first second like a long steady held breath, a distant shakuhachi and koto drift in on top in accord, a faint bell shimmer. Deeply slow, clear, settled, unchanging. no drums, no percussion, no beat, no rhythmic pulse, no arpeggios, free time with no fixed tempo, stays at one soft even gentle level the whole way through, no crescendo, no swell, no build, no rise in intensity, no climax, no dramatic change, a long slowly drifting piece that stays calm and unchanging for several minutes, unhurried and extended, do not end early, instrumental only, no vocals, no singing, no chanting, no spoken word, pure instrumental
```
**LYRICS**
```
[no lyrics, no vocals, instrumental only]
[no drums, no percussion, no beat, no tempo — free time, every note floats and decays on its own]
[dynamics: perfectly flat and even from the first second to the last — no swell, no build, no crescendo, no climax; every section stays equally soft, calm and unchanging]
[opening: soft sustained warm strings already at a low even level, calm and steady, not swelling]
[section A: a distant shakuhachi drifts in over the strings, blending in accord at the same soft level]
[section B: a soft koto and a faint bell shimmer join, all in balance, nothing grows louder]
[section C: the shakuhachi and koto fade into the strings, which stay warm, low and even]
[loop point: the strings return seamlessly to the start with no change in volume]
[mood: resolve that does not need to be loud to be unbreakable]
[texture: warm, deep, blended, slow, unchanging]
```

### Variant 9 — felt-piano-led
**STYLE**
```
Deeply meditative Japanese zen ambient, for sleep. A soft felt piano plays single clear notes with long silences, never a repeating pattern, a warm even drone pad and distant koto resting beneath in gentle accord. Intimate, slow, clear, unchanging. no drums, no percussion, no beat, no rhythmic pulse, no arpeggios, free time with no fixed tempo, stays at one soft even gentle level the whole way through, no crescendo, no swell, no build, no rise in intensity, no climax, no dramatic change, a long slowly drifting piece that stays calm and unchanging for several minutes, unhurried and extended, do not end early, instrumental only, no vocals, no singing, no chanting, no spoken word, pure instrumental
```
**LYRICS**
```
[no lyrics, no vocals, instrumental only]
[no drums, no percussion, no beat, no tempo — free time, every note floats and decays on its own]
[dynamics: perfectly flat and even from the first second to the last — no swell, no build, no crescendo, no climax; every section stays equally soft, calm and unchanging]
[opening: a soft felt piano, single clear notes with long silences between, never a repeating pattern]
[section A: a warm drone pad rests beneath the piano at a low even level, steady and calm]
[section B: a distant koto answers, sparse and slow, in accord, all at the same soft level]
[section C: the piano notes spread further apart, the even pad holds steady]
[loop point: the last piano note decays into the opening silence]
[mood: quiet devotion, a whole vow held without a sound]
[texture: intimate, clear, soft-hammered, blended, unchanging]
```

### Variant 10 — wind-led
**STYLE**
```
Deeply meditative Japanese zen ambient, for sleep. Several seconds of mountain wind through pine and cedar, then a warm koto enters softly, a low even drone and distant shakuhachi resting beneath in gentle accord. Deeply slow, grounded, unchanging. no drums, no percussion, no beat, no rhythmic pulse, no arpeggios, free time with no fixed tempo, stays at one soft even gentle level the whole way through, no crescendo, no swell, no build, no rise in intensity, no climax, no dramatic change, a long slowly drifting piece that stays calm and unchanging for several minutes, unhurried and extended, do not end early, instrumental only, no vocals, no singing, no chanting, no spoken word, pure instrumental
```
**LYRICS**
```
[no lyrics, no vocals, instrumental only]
[no drums, no percussion, no beat, no tempo — free time, every note floats and decays on its own]
[dynamics: perfectly flat and even from the first second to the last — no swell, no build, no crescendo, no climax; every section stays equally soft, calm and unchanging]
[opening: five seconds of mountain wind through pine and cedar, then koto enters softly]
[section A: a low even drone pad rests beneath the koto, steady, never swelling]
[section B: distant shakuhachi answers, never a repeating pattern, all at the same soft level]
[section C: the wind returns alone for a moment, then the even instruments settle back in]
[loop point: the wind's texture returns seamlessly to the opening with no change in volume]
[mood: a mountain shrine at dusk, wind carrying an old vow]
[texture: airy, grounded, blended, unchanging]
```

---

## §2 — Mastering

🔒 **Automated flow, adjusted for the 1H pilot cap (locked 2026-09-08 — was 2:00/120 min):**
```
python3 master-album.py "<HACHIMAN-LYRIA folder>"
python3 select-album.py "<HACHIMAN-LYRIA folder>" "<HACHIMAN-LYRIA folder>-mastered" --slug HACHIMAN --cap 60
```
Name the downloaded Lyria WAVs `HACHIMAN_1.wav` … `HACHIMAN_10.wav` (one per §1 variant; generate a few takes per variant, same as Suno, so `select-album.py` has options to anchor from) before running these. `master-album.py` masters everything (−16 LUFS, TP −1.5, 28 Hz low-cut, 48 kHz/24-bit) and prints the raw table. `select-album.py` reads both folders, anchors the calmest 2 tracks per variant, greedily fills the rest up to the **60-minute cap**, orders round-robin (anti-Content-ID), and copies into `HACHIMAN-ALBUM/` (ready for CapCut) + `HACHIMAN-RESERVE/`. Paste the printed table back here for §8. **🔒 After the album is selected, rename the files inside `HACHIMAN-ALBUM/` to the poetic track names (numeric prefix kept) before importing into CapCut** — mandatory step, see `CLAUDE.md`.
**🇺🇦** 1H пилот — кап уменьшен с 120 до **60 минут** (`--cap 60`). Скачанные WAV с Lyria называть `HACHIMAN_1.wav` … `HACHIMAN_10.wav` по номеру варианта, по несколько дублей на вариант — так же как раньше с Suno. Дальше прогони обе команды, пришли таблицу — допишу §8 и дам скрипт переименования.

### ✅ Mastering result (2026-09-11) — 21 tracks, 59:34 → `HACHIMAN-ALBUM/`

The Lyria/Producer tool named its own exports descriptively (`Dissolving Silence.wav`, `Mountain Shrine at Dusk.wav`, etc.) — no `_<variant>` numeric suffix like Suno, so `select-album.py` treated all 38 raw tracks as one group and picked the 21 calmest by loudness score up to the 60-min cap (anti-Content-ID variant-spreading doesn't apply to this source, which is fine — that protection was specific to Suno's shared-preset opening problem). `select-album.py` already copies files into `HACHIMAN-ALBUM/` as `NN - <original name>.wav`, and most of those names are already usable poetic titles as-is. Only 2 of the 21 needed a fix for thematic consistency — they came out named for dawn/morning even though every HACHIMAN track is a **dusk** scene:
- `04 - First Light Morning Zen.wav` → `04 - Fading Light Zen.wav`
- `06 - Golden Dawn Awakening (1).wav` → `06 - Golden Dusk Awakening.wav`

**PowerShell — run inside `HACHIMAN-ALBUM/`:**
```powershell
cd "C:\Users\jdan1\OneDrive\Desktop\HACHIMAN-ALBUM"
Rename-Item "04 - First Light Morning Zen.wav" "04 - Fading Light Zen.wav"
Rename-Item "06 - Golden Dawn Awakening (1).wav" "06 - Golden Dusk Awakening.wav"
```
The other 19 files need no action — `select-album.py` already saved them with their final poetic names and correct numeric prefix, ready to import into CapCut in filename order.
**🇺🇦** Инструмент сам назвал файлы почти поэтично — переименовать нужно только 2 из 21 (были названы под рассвет/утро, хотя вся тема HACHIMAN — сумерки). Остальные 19 уже готовы, ничего делать не надо.

---

## §3 — NanoBanana 16:9 (PRIMARY — hero) — the Hachiman shrine at dusk

**Direction:** a lone samurai stands or kneels before a real Hachiman-zukuri shrine building (vermillion lacquered wood, dark cypress-bark roof, curved gabled porch — modeled on Usa Jingū) at dusk; above and behind him, a colossal warrior-spirit of white-gold light takes shape above the shrine roofline, bow raised, doves circling — never a statue or mural.

```
Photorealistic cinematic still, 16:9, 4K, restrained and painterly — NOT a video-game key-art poster, NOT a hyper-saturated fantasy illustration, muted and cinematic like a Kurosawa film still. A lone samurai in dark weathered armor stands from behind, hair in a simple topknot, no helmet, back to the camera, centered in the lower third of a stone courtyard before an ancient Hachiman-zukuri shrine building at dusk — vermillion/orange-red lacquered wood pillars, beams and lattice railings, a dark thick cypress-bark roof, an ornate curved gabled entrance porch (chidori hafu) jutting forward from the main roofline, dark wood latticework windows, wide worn stone steps leading up to the veranda, modeled on the real architecture of Usa Jingū. He looks up toward a colossal warrior-spirit taking shape directly out of the fading dusk light above the shrine's roofline. The spirit's armored torso and face are DENSE and VOLUMETRIC, filled throughout with softly drifting warm white-gold light and mist, fully opaque in silhouette — NOT a thin glowing outline, NOT a wireframe or line-art sketch, NOT a transparent contour you can see through; it must read as a solid, massive body made of light, the same dense treatment as a low-lying cloud lit from within. One hand holds a bow sized naturally in proportion to its own body — roughly as long as its torso, held close at its side or drawn at a natural angle — NOT stretched into a wide glowing arc or light-trail spanning the frame. Its expression is calm and resolute — never a carved statue, never a painted mural, a living presence of dense light. The rest of the spirit's lower body trails off and dissolves into the darkening sky. Two or three white doves, faintly luminous, circle slowly and gracefully around the spirit at a steady, unhurried pace. The samurai wears dark tabi socks and traditional straw waraji sandals bound with cord at the ankle — never barefoot. EXACTLY TWO swords — a katana and a shorter wakizashi (the daishō pair) — both fully sheathed at his LEFT hip only, thrust through the obi with the blade edge upward, both hilts angled forward and up across the front of his body toward his right hand — the historically correct daishō carry, not a shoulder-slung baldric. NO third sword. NO sword drawn. NO sword in his hands. Hands hang empty and relaxed at his sides. Warm amber-and-gold dusk palette across the ENTIRE sky, fading into deep blue only at the very top edge of frame — the horizon and mid-sky must stay warm amber/gold, never a cool blue-dominant sky. The vermillion shrine walls glow warm in the last light, profound resolute stillness. Keep the lower-left corner dark and low-detail for a text overlay, keep the bottom-right corner calm and dark (logo). No airborne particles besides the doves, no text, no letters, no watermark, no other people.
```
> **🔧 Revised 2026-09-11:** first batch came back as a thin, flat neon-outline "hologram sketch" (not the dense volumetric light/mist the KAMI series requires — same treatment that worked on AMATERASU's roosters and TSUKUYOMI's rabbits), the bow rendered as an oversized glowing arc spanning the frame instead of a proportionate held weapon, one variant had a cool blue sky instead of warm dusk, and the overall look read as generic fantasy/video-game key art rather than our restrained cinematic style. Prompt above now explicitly demands density/opacity in the spirit, a naturally-proportioned bow, a warm sky end-to-end, and a "not video-game key-art" style anchor.
> **🇺🇦** Первая партия вышла как тонкий неоновый контур-голограмма (не плотный объёмный свет/туман, как у петухов AMATERASU/кроликов TSUKUYOMI), лук — как огромная светящаяся дуга через весь кадр вместо оружия в руке, один вариант — с холодным синим небом вместо тёплых сумерек, а общий вид — как постер видеоигры, а не наш сдержанный кинематографичный стиль. Промт теперь явно требует плотность духа, пропорциональный лук, тёплое небо целиком и запрет на "видеоигровой" вид.
> Chosen generation → save as `hachiman-2h-source.jpg`. 八幡 kanji goes upper-center over the light-spirit (per Kanji-Concept canon), HACHIMAN romaji low on the dark foreground stone courtyard.

## §3b — NanoBanana 9:16 (Shorts)

```
Photorealistic cinematic vertical still 9:16, 4K. A lone samurai in dark weathered armor stands from behind, hair in a simple topknot, no helmet, lower third, in a stone courtyard before an ancient Hachiman-zukuri shrine building at dusk — vermillion lacquered wood, dark cypress-bark roof, curved gabled porch, wide stone steps, modeled on Usa Jingū. Above and behind him a colossal warrior-spirit takes shape out of the fading dusk light above the shrine roofline, its armored torso and face made of dense warm white-gold light, one hand raised holding a massive glowing bow, calm and resolute — a living presence, never a statue or mural. Two or three faintly luminous white doves circle slowly around it. The samurai wears dark tabi socks and straw waraji sandals — never barefoot. EXACTLY TWO swords — a katana and a shorter wakizashi — both fully sheathed at his LEFT hip only, thrust through the obi with the blade edge upward, hilts angled forward and up — never in front of him, never hidden. NO third sword. NO sword drawn. Hands empty at his sides. Warm amber-gold dusk palette fading to deep blue, the vermillion shrine walls glowing warm in the last light. Keep the centre-left band calm and low-detail (a text overlay sits there). No airborne particles besides the doves, no text, no letters, no watermark, no other people.
```

## §3c — Shorts image set (9:16 — 6 frames · FULL standalone prompts)

Save `hachiman-shorts-fr1.jpg … fr6.jpg`. No in-image text; bottom-right calm for logo. Frame 4 = calm zone for the 八幡 kanji overlay. No terrace railing anywhere. No airborne particles besides the doves. Every samurai frame: EXACTLY TWO sheathed swords, thrust through the obi edge-up at the LEFT hip only, hilts forward, tabi + waraji, hands empty.
**🔒 Frame 1 vs frame 6 — deliberately NOT the same shot** (lesson from the RYŪ series): frame 1 = dusk just beginning to fade, spirit newly risen; frame 6 = later, the light fuller/brighter, warmer gold, the spirit's form more fully resolved — a sense of the vow completing, not a repeat of the opener.

**1. HOOK — samurai before the rising spirit**
```
Photorealistic cinematic vertical still, 9:16, 4K, warm amber-gold dusk palette, dramatic scale. A lone samurai in dark weathered armor stands from behind, hair in a simple topknot, no helmet, a calm still silhouette, centered in the lower third of a stone courtyard before an ancient Hachiman-zukuri shrine building at dusk — vermillion lacquered wood, dark cypress-bark roof, curved gabled porch, wide stone steps, modeled on Usa Jingū, nothing beside him. Above and behind him a colossal warrior-spirit is just beginning to take shape out of the fading dusk light above the shrine roofline, its armored torso and face made of dense warm white-gold light, one hand raising a massive glowing bow, calm and resolute — a living presence, never a statue or mural. Two faintly luminous white doves circle slowly nearby. EXACTLY TWO swords — a katana and a shorter wakizashi (the daishō pair) — both fully sheathed at his LEFT hip only, thrust through the obi with the blade edge upward, hilts angled forward and up, clearly visible from behind, never swapped or hidden. NO third sword. NO sword drawn. NO sword in his hands. Hands hang empty at his sides. He wears dark tabi socks and traditional straw waraji sandals bound with cord at the ankle — never barefoot. Profound resolute stillness. No text, no letters, no watermark.
```

**2. Shrine roof-tile and dusk sky macro (breather)**
```
Photorealistic cinematic vertical close-up, 9:16, 4K, high contrast, warm amber-gold palette. A close-up of weathered wooden shrine roof tiles at the edge of a mountain terrace, catching the last warm light of dusk, soft cool background bokeh of the darkening sky beyond. Delicate, clear, serene, intimate — a small sign of the sacred ground below the rising spirit. No text, no letters, no watermark.
```

**3. The light-spirit detail (armored torso, bow, glowing doves)**
```
Photorealistic cinematic vertical close-up, 9:16, 4K, warm dusk light. A close view of a colossal warrior-spirit's armored torso and face, formed directly out of dense warm white-gold light — glowing plate-armor shapes suggested only by light and drifting mist, never a solid carved surface — one hand holding a massive bow of the same glowing light, its expression calm and resolute. Two faintly luminous white doves circle close by. A living presence made of light, holding its form steady like a sculpture. Reverent, atmospheric, timeless. No text, no letters, no watermark.
```

**4. KANJI frame — the shrine terrace at dusk**
```
Photorealistic cinematic vertical still, 9:16, 4K. A calm, open sky over an ancient Hachiman-zukuri shrine at dusk, soft gradient of warm amber-gold fading into deep blue overhead, the upper half quiet and empty (clean space for a large kanji), a faint dark silhouette of the shrine's curved gabled roofline and vermillion pillars at the bottom of frame. Minimal, serene, clear, atmospheric. No text, no letters, no watermark.
```

**5. Weathered stone lantern on the shrine grounds (detail)**
```
Photorealistic cinematic vertical still, 9:16, 4K, warm dusk light. A single weathered stone lantern (ishidōrō) at the edge of the stone courtyard before an ancient Hachiman-zukuri shrine, moss at its base, a hint of vermillion lacquered pillars soft-focused behind it, the last warm light of dusk catching one edge. Quiet, clear, serene, timeless. No text, no letters, no watermark.
```

**6. Samurai before the fully-risen spirit, wide, warmer light (wisdom)**
```
Photorealistic cinematic vertical still, 9:16, 4K, warm amber-gold dusk palette, dramatic scale. A lone samurai in dark weathered armor stands from behind, hair in a simple topknot, no helmet, a calm still silhouette, centered in the lower third of a stone courtyard before an ancient Hachiman-zukuri shrine building at dusk — vermillion lacquered wood, dark cypress-bark roof, curved gabled porch, wide stone steps, modeled on Usa Jingū — only this one figure, no other people. Above and behind him the warrior-spirit's form is now fully resolved, its armored torso and face made of richer, warmer white-gold light than before, its bow fully raised, two or three faintly luminous doves circling steadily — a living presence, never a statue or mural. EXACTLY TWO swords — a katana and a shorter wakizashi — both fully sheathed at his LEFT hip only, thrust through the obi with the blade edge upward, hilts angled forward and up, never in front of him, never hidden. NO third sword. NO sword drawn. Hands empty at his sides. He wears dark tabi socks and traditional straw waraji sandals bound with cord at the ankle — never barefoot. Profound resolute stillness, the sense of a vow completed. No text, no letters, no watermark.
```

---

## §4 — Flow (Veo 3) loop prompt (16:9)

Feed the CLEAN hero (no text). Frame it as a **cinemagraph**. **🔒 Lock the spirit's ENTIRE visible shape — armored torso, face, and bow — like a sculpture, pixel-identical from the first frame to the last** (RYŪ lesson: a real/organic-looking shape drifts or reshapes over 8 sec unless explicitly frozen). Only the doves' wingbeats (positions on a fixed circular path) and the spirit's glow may hold gentle, contained motion — never its outline. **🔒 The glow and the doves' luminescence must be described as ALREADY present from the first frame.**

```
A cinemagraph on a photorealistic warm dusk scene: a lone samurai in dark weathered armor stands from behind, hair in a simple topknot, no helmet, alone in a stone courtyard before an ancient Hachiman-zukuri shrine building — vermillion lacquered wood, dark cypress-bark roof, curved gabled porch, modeled on Usa Jingū — and above him a colossal warrior-spirit made of dense warm white-gold light — its armored torso, face and raised bow already glowing steadily from the very first frame — with two or three faintly luminous white doves already circling it in slow, graceful flight. Treat the samurai, his armor, his swords, the terrace, and the spirit's ENTIRE visible shape — armor, face, and bow — as a completely frozen still photograph: the spirit's full outline and silhouette stay locked like a sculpture, pixel-identical in every single frame, never drifting position or reshaping. The samurai's build, posture and silhouette also stay exactly as in the still throughout. Camera completely locked and static — no pan, no zoom, no push-in, no dolly, no shake; the frame never moves. Animate ONLY these, all extremely subtle: (1) the doves continue their slow, graceful circular flight along the same fixed circular path, wings beating gently, returning to their starting positions by the end of the loop; (2) the spirit's light glows with a soft, continuous, gently pulsing warm white-gold shimmer, never changing the fixed shape of its armor or bow; (3) the dusk sky in the far background — well away from the spirit's own silhouette — deepens by the faintest, barely perceptible degree, as if the very last moment of daylight is stretching out slowly. The air stays completely clear and calm the entire time. Everything solid — the samurai, the terrace floor, the spirit's fixed armored shape — stays a completely frozen photograph. Slow, warm, resolute, meditative. The doves' flight, the light's glow, and the sky's faint deepening move in a smooth continuous cycle so the last frame matches the first frame exactly, pixel-for-pixel in every fixed element including the spirit's full silhouette and the doves' positions, for a perfectly seamless 8-second loop.
```
**🇺🇦** Дух-воин зафиксирован целиком (доспех, лицо, лук) как скульптура. Живут только: (1) голуби летят по одному и тому же кругу и возвращаются в начальную позицию к концу лупа, (2) свечение духа мягко пульсирует, (3) едва заметное углубление сумеречного неба вдалеке. Камера статична, последний кадр = первый.

---

## §6a — Wisdom Overlay

- Line 1 (kanji): **質実剛健**
- Line 2 (romaji): *Shitsujitsu gōken*
- Line 3 (gloss): Sincere and robust — plain, unadorned strength
- Cream `#F5EAD2`, Liberation Serif Bold, LEFT-lower over the dark foreground terrace stone. 0:00–0:03 scene only → fade-in 2s → hold ~5s → fade-out 2s (ends 0:14).
- **🇺🇦** Мудрость: **質実剛健** / *Shitsujitsu gōken* / «Искренность и стойкость — простая, ничем не украшенная сила» — идеал воинского духа бусидо: сила, которой не нужно себя показывать. Не сам 八幡 (оверлей ≠ заголовок). Слева-внизу, кремовым.

---

## §7 — Title

```
HACHIMAN — 八幡 | Japanese Zen Music for Courage, Protection & Inner Strength
```
(`Music` well within the first 50% of chars ✅ · ≤90 ✅ · no hashtags)

**A/B:** `HACHIMAN — 八幡 | Japanese Zen Music for Warriors, Courage & Quiet Resolve`

---

## §8 — Description (Hikari 5-block; tracklist after mastering)

```
japanese zen music, meditation music, zen music, samurai music, courage music, calming music, relaxing music, healing music, sleep music, ambient music, hachiman, japanese god of war music, music for courage and inner strength, koto music, shakuhachi flute, singing bowls — a one-hour Japanese zen session for courage, protection and quiet inner strength.

🌀 HACHIMAN (八幡) is the guardian of warriors —
god of war, archery, and quiet resolve,
strength that never needs to raise its voice.

At the edge of a mountain shrine at dusk, a lone figure kneels as a colossal spirit of light takes shape above the roofline, a bow of gold in one hand, white doves circling in the fading warmth of day. Slow koto, warm shakuhachi, the long decay of a temple bell — one hour to rest in a courage that holds steady, quietly, without needing to be shown.

Tracklist:
0:00 Dissolving Silence
2:54 Dusk Air & Singing Bowl
5:51 Felt Piano & Zen Drone
8:44 Fading Light Zen
11:38 Fog Over Mountain Shrine
14:15 Golden Dusk Awakening
17:07 Intimate Decay
20:00 Mountain Shrine at Dusk
22:58 Patience Before the Shrine
25:58 Pine Terrace Wind
28:53 Resolute Decay
31:47 Resolute Harp & String Pad
34:45 Serene Mind Zen
37:43 Spacious Zen Ambient
40:31 Sparse Koto Silence
43:21 Still Dusk Sanctuary
46:18 Sustained Stillness
49:03 Temple Bell Decay
51:29 Unchanging Bowed Breath
54:01 Unhurried Breath Shrine
56:38 Unmoving Stillness

🌀 Strength does not need to be loud.
🍃 Nothing forced. Only resolve, and the steady light.

Subscribe for more Japanese ambient meditation journeys 🌿
```

---

## §9 — Tags (verify VidIQ scores; < 450 chars)

```
stillwave, japanese zen music, meditation music, zen music, samurai music, calming music, relaxing music, healing music, sleep music, ambient music, hachiman, japanese god of war, music for courage, music for inner strength, koto music, shakuhachi flute music, singing bowl music, japanese meditation music, zen meditation music, a lone samurai before a colossal spirit of light with a bow of gold at a mountain shrine at dusk, joe hisaishi
```

---

## §10 — Thumbnail

- Build from hero via `hachiman-compose-thumb.py` (clone of the SEIRYU/KARYU composer).
- **八幡** — check the hero's background brightness before choosing ink colour: warm dusk gold/amber background → likely needs dark sumi ink with a cream halo for contrast (same lesson as SHOSHIN/ICHIGO/UNRYŪ); if the kanji band lands over a darker patch of sky, gold reads cleanly instead (SEIRYU/KARYU case). Decide after seeing the actual generation. Vertical stack, left corner, matching the RYŪ series treatment.
- **HACHIMAN** — large legible gold Liberation Serif Bold (or DejaVu Serif Bold), low-centre on the dark foreground terrace stone with a soft scrim.
- Bottom-right corner dark → logo in post.
- **New-series opener note:** this is the FIRST video of the KAMI "Gods of Japan" sub-series — establish the placement/treatment here since future gods (Amaterasu, Susanoo, etc.) will match it for a matched-set look in the channel's video grid, the same role SEIRYU played for closing out RYŪ.

---

## §11 — Pinned Comment

```
🌀 HACHIMAN (八幡) — guardian of warriors, god of courage and quiet resolve. Strength that never needs to raise its voice. 🍃 What are you holding steady through right now? Subscribe for more Japanese ambient meditation journeys 🌿
```

---

## §12 — Community Post (day-of; reuse thumbnail)

```
HACHIMAN (八幡) in Japanese Culture: A Concise Overview

八幡 (Hachiman), god of war, archery, and divination, is one of the most widely venerated kami in Japan — more shrines are dedicated to him than to any other deity, with the great sanctuaries of Usa, Iwashimizu, and Tsurugaoka among the most historically significant in the country. Long syncretized with Emperor Ōjin and adopted as the patron deity of the samurai class by the Minamoto shogunate, Hachiman came to embody a very particular kind of strength: resolute, protective, and unshowy. His sacred messenger is the white dove, a detail still preserved in the guardian statues at his shrines today. Here a lone samurai kneels before a mountain shrine at dusk as that same steady strength takes shape above him.
```

---

## §14 — Shorts (concept + teaser)

Built from the 6 frames (§3c) via `hachiman-short-build.py` + `hachiman-short-overlays.py` (Ken Burns float-precision PIL, crossfades, gold beats) — same pipeline as the RYŪ series. Three gold beats, all inside the safe zone (y 150-1450, x 60-880 of 1080×1920):
- **Beat 1 (hook):** `Strength does not need to be loud` (cream)
- **Beat 2 (concept, frame 4):** `八幡` + `HACHIMAN` (gold)
- **Beat 3 (wisdom):** `質実剛健` + `Shitsujitsu gōken` + `Sincere and robust` (gold)

### 📋 Shorts — copy-paste pack

**Title**
```
Hachiman: Japan's Guardian of Warriors and Courage 🏹 #shorts
```
**A/B Title**
```
What Is Hachiman? Japan's God of War and Quiet Strength 🏹 #shorts
```
**Description**
```
八幡 Hachiman — god of war, archery, and divination, guardian of Japan and patron of the samurai. Strength that never needs to raise its voice.

質実剛健 — sincere and robust; plain, unadorned strength.

Full one-hour Japanese zen session on the channel 🌿

#hachiman #japanese #zen #samurai #shorts
```
**Tags**
```
hachiman, japanese god of war, shinto gods, japanese mythology, samurai, bushido, zen, meditation, courage, stillwave
```
**Pinned comment**
```
🌀 八幡 HACHIMAN — guardian of warriors. Full one-hour session on the channel 🌿
```

Settings: **Not for kids** · playlist **StillWave Shorts** · Related video → long-form HACHIMAN.

---

## §15 — Concept Short (standalone, built from §12 — RELOCKED 2026-09-09)

Separate from the teaser Short above — a standalone cultural-education Short teaching 八幡 from the §12 Community Post text, not footage from the long-form. Build via `concept-shorts-build.py` (add a `hachiman` config), reusing the same 6 `hachiman-shorts-fr1..fr6.jpg` frames (§3c), white titles, jitter-free Ken Burns (same pipeline as ZANSHIN/YUGEN/SHINRIN-YOKU).
**🇺🇦** Отдельный от тизера обучающий Short — тема 八幡 из текста §12, не кадры из лонга. Собирается из тех же 6 кадров §3c через `concept-shorts-build.py`.

### On-screen caption script (RELOCKED 2026-09-09 — full teaching text, not sparse hook beats)

> One full sentence per frame (fr1→beat 1 … fr6→beat 6), lifted/adapted from §12 — not the sparse hook+kanji+wisdom pattern used on the teaser (§14). Cream `#F5EAD2` Liberation Serif, safe zone `y 150-1450 / x 60-880`. ~6-8 sec per beat ≈ 40-48s total.
> **🇺🇦** По одной полной фразе из §12 на каждый из 6 кадров — не скупой хук+иероглиф+мудрость, как в тизере §14.

1. `八幡 (Hachiman) — god of war, archery, and divination, one of the most widely venerated kami in Japan.`
2. `More shrines are dedicated to him than to any other deity — Usa, Iwashimizu, and Tsurugaoka among the most historically significant.`
3. `Long syncretized with Emperor Ōjin, he became the patron deity of the samurai class under the Minamoto shogunate.`
4. `His strength is resolute, protective, and unshowy — never needing to be loud.`
5. `His sacred messenger is the white dove, still preserved in the guardian statues at his shrines today.`
6. `質実剛健 (Shitsujitsu gōken) — sincere and robust; strength that needs no display.`

### Concept Short — SEO pack (copy-paste)

**Title (≤60):**
```
What Is Hachiman? Japan's Most Worshipped War God 🏹 #shorts
```
A/B: `八幡 HACHIMAN — Japan's Guardian God of War and Courage #shorts`

**Description:**
```
HACHIMAN (八幡) — more shrines are dedicated to him than to any other kami in Japan. God of war, archery, and divination, patron deity of the samurai, his sacred messenger is the white dove. His strength is resolute, protective, and unshowy.

Full one-hour HACHIMAN zen session on the channel 🌿
▶ [long-form link]

#shorts #hachiman #samurai #japanesemythology #shinto #zen
```

**Tags:**
```
hachiman, what is hachiman, hachiman meaning, japanese god of war, shinto gods, japanese mythology, samurai, bushido, usa jingu, white dove symbolism, japanese culture, zen, meditation, stillwave
```

**Hashtags:** `#shorts #hachiman #samurai #japanesemythology #shinto #zen`

**Pinned:**
```
🌀 八幡 HACHIMAN — more shrines honor him than any other kami in Japan. Strength that never needs to raise its voice. The full one-hour session is on the channel 🌿
```

**Upload:** Related video → long-form HACHIMAN · Playlist **StillWave Shorts — Japanese Zen & Frequencies** · Not for kids.
