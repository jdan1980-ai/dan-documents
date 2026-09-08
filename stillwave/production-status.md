# StillWave — Production Status

Single source of truth for the StillWave pipeline. Update at every status change.

**Pipeline stages:** 📝 concept → 🎵 suno generated → 🎨 image generated → 🎬 video generated → 🎞️ assembled → ⏰ scheduled → 📤 published

---

## Published

See `published-videos.md` for the full table with metrics.

## Recently published

| Slug | Title | Published | Views (D) | Notes |
|------|-------|-----------|-----------|-------|
| `gaman-2h` | GAMAN — 我慢 \| Japanese Zen Music for Endurance, Deep Focus & Inner Strength | 2026-07-08 | — (D0) | Kanji-Concept — monitor D3/D7/D14 |
| `tokyo-cafe-rain-1h` | Tokyo Rain & Vinyl \| Late Night Café Ambience Music for Productivity | 2026-07-01 | **10** (D4) | Café format — monitor at D14 (Jul 15) |
| `makoto-the-last-samurai` | MAKOTO — 誠 \| Japanese Cinematic Zen for Honor, Bushido & Spirit · 1H | 2026-06-25 | ~43 (D10) | — |
| `satori-sudden-awakening` | SATORI — 悟り \| Zen Japanese Music for Meditation, Healing & Spiritual Enlightenment | 2026-06-21 | ~170 (D14) | — |
| `mushin-no-mind` | MUSHIN — 無心 \| Japanese Zen Music for No-Mind State, Deep Focus & Inner Stillness | 2026-06-16 | **2,198** (D19) 🔥 | VIRAL — 31 VPH on Jul 5, still in algo push |
| `tokyo-apartment-rain-1h` | Power Hour Focus Music — Tokyo Apartment Rain | 2026-05-10 | ~275 (D56) | 3rd all-time, productivity pillar |

## 🐉 RYŪ (龍) — Samurai Dragon sub-series (Kanji-Concept)

Five-video sub-series: a lone samurai (back to camera, daishō sheathed at LEFT hip) before a massive painted dragon mural, each video its own element/location/palette so none repeat. **GARYŪ (臥龍) already produced/ready.** The 4 remaining full packages (10 Suno variants + hero + 6 Shorts frame prompts + Veo3 cinemagraph loop + wisdom overlay + full copy-paste pack) are written and committed — awaiting image/music generation.

| Slug | Title | Element / Location | Wisdom overlay | 📝 | 🎵 | 🎨 | 🎬 | 🎞️ | ⏰ | 📤 |
|------|-------|---------------------|-----------------|----|----|----|----|-----|-----|-----|
| `garyu` (untracked slug) | GARYŪ — 臥龍 \| Crouching Dragon | — | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (per user, ready) |
| `unryu-2h` | **UNRYŪ — 雲龍** \| Japanese Zen Music for Rising Above, Clarity & Inner Power | Cloud dragon · mountain-peak gate above a cloud sea · cool silver-jade | 雲外蒼天 (Ungai sōten) | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| `suiryu-2h` | **SUIRYŪ — 水龍** \| Japanese Zen Music for Perseverance, Flow & Quiet Strength | Water dragon · dragon-gate waterfall at dusk · deep teal-black | 柔よく剛を制す (Jū yoku gō o seisu) | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| `karyu-2h` | **KARYŪ — 火龍** \| Japanese Zen Music for Inner Fire, Focus & Unshakable Resolve | Fire dragon · night shrine courtyard, braziers · ember-gold | 不撓不屈 (Futō fukutsu) | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| `seiryu-2h` | **SEIRYŪ — 青龍** \| Japanese Zen Music for New Beginnings, Renewal & Inner Clarity | Azure dragon (East guardian) · spring dawn terrace · pale cyan-gold | 一陽来復 (Ichiyō raifuku) | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |

**Next step per video:** generate hero image (§3) → thumbnail + wisdom overlay → generate 10 Suno variants (§1) → master → select/order → §8 → generate 6 Shorts frames (§3c) → Short → generate Veo3 loop (§4) → CapCut laydown → publish. Suggested release order: UNRYŪ → SUIRYŪ → KARYŪ → SEIRYŪ (series closer, spring/dawn).

## ⛩️ KAMI (神) — Gods of Japan sub-series (Kanji-Concept)

Sibling series to RYŪ: each video = one Shinto deity manifesting as a colossal LIVING figure of light (never a statue/mural), own signature light colour + sacred creature, lone samurai/worshipper for scale. **🔬 `hachiman-1h` is the channel's first Google Lyria pilot (locked 2026-09-08)** — Suno's new download caps (Pro 20/mo, Premier 60/mo, no confirmed unlimited workaround) can't cover this channel's volume, so Hachiman tests Lyria (strong reviews on instrumental/ambient fidelity, no download cap, ~$0.04-0.08/track via API) at a shortened **1H** length (channel avg watch time ~30 min; 1H already validated as the format sweet spot). If Lyria's Japanese-instrument timbre holds up over a full album, convert the series default from Suno to Lyria going forward — the original Suno prompts stay in each script as `§1-Suno` fallback either way.

| Slug | Title | Signature colour / creature | Wisdom overlay | Music source | 📝 | 🎵 | 🎨 | 🎬 | 🎞️ | ⏰ | 📤 |
|------|-------|------------------------------|-----------------|---------------|----|----|----|----|-----|-----|-----|
| `tsukuyomi-2h` | TSUKUYOMI — 月読 \| flagship | pale silver-blue · moon rabbits | (see script) | Suno | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | ⏳ |
| `amaterasu-2h` | AMATERASU — 天照 \| Japanese Zen Music for Morning Meditation & Sunrise Calm | warm golden-amber sunrise · sacred roosters | 一陽来復 (Ichiyō raifuku) | Suno | ✅ | ⏳ | ✅ | ⏳ | ⏳ | ⏳ | ⏳ |
| `hachiman-1h` | HACHIMAN — 八幡 \| Japanese Zen Music for Courage, Protection & Inner Strength | warm white-gold · white doves | 質実剛健 (Shitsujitsu gōken) | **Lyria (pilot)** | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| — | **BENZAITEN — 弁財天** (proposed 2026-09-08) | goddess of music, water & eloquence — koto/biwa + flowing water motif, "Deep Focus" angle | — | TBD | — | — | — | — | — | — | — |

**Next step:** HACHIMAN — generate hero (§3), then 10 Lyria variants (§1), master with `--cap 60`, select/order → §8. AMATERASU — generate the 10 Suno variants (§1), hero/tracklist already done. BENZAITEN is a proposed next-in-queue after Hachiman, not yet scripted — needs a full package (visual hook, §0-§14) before production.

## In production / next up

> Pipeline для long-form full-album: 📝 script → 🎵 suno generated → 🎨 image generated → 🎬 video loop → 🎞️ assembled in CapCut → ⏰ scheduled → 📤 published.

| Slug | Title | Length | 📝 | 🎵 | 🎨 | 🎬 | 🎞️ | ⏰ | 📤 |
|------|-------|--------|----|----|----|----|-----|-----|-----|
| `gaman-2h` | **GAMAN — 我慢** \| Japanese Zen Music for Endurance, Deep Focus & Inner Strength | 2H | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `mono-no-aware-2h` | **MONO NO AWARE — 物の哀れ** \| Japanese Zen Music for Healing, Letting Go & Inner Peace | 2H | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| `bonsai-desk-night-2h` | Deep Focus Music — Bonsai Desk Late Night | 2H | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| `lantern-glow-study-3h` | Quiet Hours Focus Music — Lantern Glow Study | 3H | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |

> **GAMAN published 2026-07-08.** Monitor D3 (Jul 11) / D7 (Jul 15) / D14 (Jul 22). Tokyo Rain & Vinyl D14 also due Jul 15.

## Phase 1 batch — week of May 13–19

These are the first 3 hybrid-format videos for the gradual transition (Phase 1 = 1 of 4 / week, but we're running 3 as a test batch). Each script file under `scripts/` has the full 11-item `SW:` package: Suno A + Suno B + NanoBanana 16:9 + NanoBanana 9:16 + ffmpeg command + Title + Description + Tags + Hashtags + Pinned comment + A/B variant.

| Date | Slug | Aesthetic-lean | Why |
|------|------|----------------|-----|
| TBD | `tokyo-apartment-rain-1h` | Tokyo apartment + heavy rain on glass + neon city + tea + bonsai. **Power Hour format (1H 04min, 24 Suno tracks, no loop)** | Catches "1 hour focus music" + "power hour" search demand. Lower production overhead than 2H. |
| TBD | `bonsai-desk-night-2h` | Tokyo apartment + open MacBook (warm screen glow) + bonsai + neon city | Most "coding/programming" hook, laptop is the hero |
| TBD | `lantern-glow-study-3h` | Tokyo apartment + paper andon lantern (warm vs neon contrast) + closed laptop + book | Most "scholarly/study" hook, lantern is the hero, longest at 3H |

Mix the 3 with current иероглиф / Hz format videos so the channel doesn't shift too fast.

## Workflow per video

1. Trigger `SW: [theme]` or `SWS: [theme]` in chat — get the 11-item package
2. Generate music in Suno (Prompts A + B)
3. Generate image in NanoBanana (16:9 + 9:16)
4. Generate video loop in Flow / Kling
5. Edit + master in CapCut + ffmpeg
6. Generate thumbnail via `THUMB: [theme]` → Canva
7. Schedule upload in YouTube Studio
8. After publish: update `published-videos.md` with views at 48h / 7d / 30d