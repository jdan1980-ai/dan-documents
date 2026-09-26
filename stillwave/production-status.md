# StillWave — Production Status

Single source of truth for the StillWave pipeline. Update at every status change.

**Pipeline stages:** 📝 concept → 🎵 suno generated → 🎨 image generated → 🎬 video generated → 🎞️ assembled → ⏰ scheduled → 📤 published

---

## Published

See `published-videos.md` for the full table with metrics.

## Recently published

**🔒 Live-checked via VidIQ 2026-09-25** (this table had gone stale since ~July 8 while dozens of videos shipped in between — RYŪ and KAMI series both fully published without this file being updated; see the two sub-series tables below, now corrected). `published-videos.md`'s deeper analysis (format performance, patterns) still only covers through GAMAN/MUSHIN and needs its own full refresh — flagged separately, ask before doing that bigger pass.

| Slug | Title | Published | Views | Notes |
|------|-------|-----------|-------|-------|
| `raijin-1h` | RAIJIN — 雷神 \| Japanese Zen Music for Calm & Deep Sleep | 2026-09-25 | 2 (just live) | — |
| `fujin-1h` | FUJIN — 風神 \| Japanese Zen Music for Letting Go | 2026-09-22 | 118 | — |
| `kannon-1h` | KANNON — 観音 \| Finding Mercy & Stillness | 2026-09-19 | 133 | — |
| `benzaiten-1h` | BENZAITEN (弁財天) — Deep Focus, the Water Goddess's Flow | 2026-09-16 | 151 | — |
| `hachiman-1h` | HACHIMAN (八幡) — Warrior Focus, the God of War's Silence | 2026-09-13 | 115 | — |
| `amaterasu-2h` | AMATERASU (天照) — Returning to Warmth | 2026-09-10 | 111 | — |
| `inari-1h` | INARI (稲荷) — 1 Hour for Abundance & Stillness | uploaded, private | 0 | **Scheduled 2026-09-28 14:00** — not live yet |

**Older standout performers worth noting** (from the same VidIQ pull, outside the KAMI/RYŪ series): `gaman-2h` GAMAN — 2,456 views, 43 likes, 15 comments — still the channel's clear outlier. `nagomi-2h` NAGOMI — 827 views. `ikigai-2h` IKIGAI — 638 views. `wabi-sabi-2h` WABI-SABI — 560 views (the "45:47 avg / 38%" retention video that prompted this check — genuinely strong for a 2H video). `kokoro-2h` KOKORO — 386 views.

## 🐉 RYŪ (龍) — Samurai Dragon sub-series (Kanji-Concept)

**✅ COMPLETE — all 5 published** (verified live via VidIQ 2026-09-25; this table had gone stale and was still showing 4 of them as unstarted). Five-video sub-series: a lone samurai before a massive painted dragon mural, each video its own element/location/palette.

| Slug | Title | Element / Location | Wisdom overlay | 📝 | 🎵 | 🎨 | 🎬 | 🎞️ | ⏰ | 📤 |
|------|-------|---------------------|-----------------|----|----|----|----|-----|-----|-----|
| `garyu` (untracked slug) | GARYŪ — 臥龍 \| Crouching Dragon | — | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `unryu-2h` | **UNRYŪ — 雲龍** \| Japanese Zen Music for Rising Above, Clarity & Inner Power | Cloud dragon · mountain-peak gate above a cloud sea · cool silver-jade | 雲外蒼天 (Ungai sōten) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `suiryu-2h` | **SUIRYŪ — 水龍** \| Japanese Zen Music for Perseverance, Flow & Quiet Strength | Water dragon · dragon-gate waterfall at dusk · deep teal-black | 柔よく剛を制す (Jū yoku gō o seisu) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `karyu-2h` | **KARYŪ — 火龍** \| Japanese Zen Music for Inner Fire, Focus & Unshakable Resolve | Fire dragon · night shrine courtyard, braziers · ember-gold | 不撓不屈 (Futō fukutsu) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `seiryu-2h` | **SEIRYŪ — 青龍** \| Japanese Zen Music for New Beginnings, Renewal & Inner Clarity | Azure dragon (East guardian) · spring dawn terrace · pale cyan-gold | 一陽来復 (Ichiyō raifuku) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

All five have both long-form and Shorts live (published 2026-08-23 → 2026-09-05).

## ⛩️ KAMI (神) — Gods of Japan sub-series (Kanji-Concept)

Sibling series to RYŪ: each video = one Shinto deity manifesting as a colossal LIVING figure of light (never a statue/mural), own signature light colour + sacred creature, lone samurai/worshipper for scale. **🔬 `hachiman-1h` is the channel's first Google Lyria pilot (locked 2026-09-08)** — Suno's new download caps (Pro 20/mo, Premier 60/mo, no confirmed unlimited workaround) can't cover this channel's volume, so Hachiman tests Lyria (strong reviews on instrumental/ambient fidelity, no download cap, ~$0.04-0.08/track via API) at a shortened **1H** length (channel avg watch time ~30 min; 1H already validated as the format sweet spot). If Lyria's Japanese-instrument timbre holds up over a full album, convert the series default from Suno to Lyria going forward — the original Suno prompts stay in each script as `§1-Suno` fallback either way.

| Slug | Title | Signature colour / creature | Wisdom overlay | Music source | 📝 | 🎵 | 🎨 | 🎬 | 🎞️ | ⏰ | 📤 |
|------|-------|------------------------------|-----------------|---------------|----|----|----|----|-----|-----|-----|
| `tsukuyomi-2h` | TSUKUYOMI — 月読 \| flagship | pale silver-blue · moon rabbits | (see script) | Suno | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `amaterasu-2h` | AMATERASU — 天照 \| Japanese Zen Music for Morning Meditation & Sunrise Calm | warm golden-amber sunrise · sacred roosters | 一陽来復 (Ichiyō raifuku) | Suno | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `hachiman-1h` | HACHIMAN — 八幡 \| Japanese Zen Music for Courage, Protection & Inner Strength | warm white-gold · white doves (perched, not flying) | 質実剛健 (Shitsujitsu gōken) | **Lyria (pilot)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `benzaiten-1h` | BENZAITEN — 弁財天 \| Japanese Zen Music for Deep Focus, Creativity & Flowing Calm | cool aquamarine-teal · white snake | 行雲流水 (Kōun ryūsui) | **Lyria** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `kannon-1h` | KANNON — 観音 \| Japanese Zen Music for Healing, Compassion & Deep Calm | soft rose-pink / pearl-white · white cranes | 一視同仁 (Isshi dōjin) | **Lyria** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `fujin-1h` | FUJIN — 風神 \| Japanese Zen Music for Letting Go, Release & Inner Peace | storm-grey / pale jade-green · hawk | 諸行無常 (Shogyō mujō) | **Lyria** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `raijin-1h` | RAIJIN — 雷神 \| Japanese Zen Music for Inner Strength, Calm Power & Deep Focus | deep indigo-violet / electric white-blue · raiju (wolf) | 泰然自若 (Taizen jijaku) | **Lyria** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `inari-1h` | INARI — 稲荷 \| Japanese Zen Music for Abundance, Gratitude & Inner Prosperity | fire-gold (thumb) / warm amber moonlit (video) · kitsune | 五穀豊穣 (Gokoku hōjō) | **Lyria (user-produced visuals)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ |

**Status (live-checked via VidIQ 2026-09-25):** TSUKUYOMI through RAIJIN are all fully published — this table had gone stale, still showing most of them as mid-pipeline. **INARI is uploaded and scheduled for 2026-09-28 14:00** (currently private) — only remaining open items are confirming the rename script ran cleanly in `INARI-ALBUM/` and whether a standalone Concept Short exists alongside its teaser Short (see `inari-1h.md` §14 open question). Next KAMI entry after Inari: none currently drafted — the sub-series has run TSUKUYOMI/AMATERASU/HACHIMAN/BENZAITEN/KANNON/FUJIN/RAIJIN/INARI (8 gods); decide whether to continue (e.g. Susanoo, Ame-no-Uzume, Ryūjin) or close the arc here.

## In production / next up

> Pipeline для long-form full-album: 📝 script → 🎵 suno generated → 🎨 image generated → 🎬 video loop → 🎞️ assembled in CapCut → ⏰ scheduled → 📤 published.

**🔒 Live-checked via VidIQ 2026-09-25:** GAMAN and MONO NO AWARE are both published (this table still had MONO NO AWARE marked mid-pipeline — it actually went live 2026-07-12, 154 views). Only `bonsai-desk-night-2h` and `lantern-glow-study-3h` are genuinely still unproduced.

| Slug | Title | Length | 📝 | 🎵 | 🎨 | 🎬 | 🎞️ | ⏰ | 📤 |
|------|-------|--------|----|----|----|----|-----|-----|-----|
| `gaman-2h` | **GAMAN — 我慢** \| Japanese Zen Music for Endurance, Deep Focus & Inner Strength | 2H | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `mono-no-aware-2h` | **MONO NO AWARE — 物の哀れ** \| Japanese Zen Music for Healing, Letting Go & Inner Peace | 2H | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `muga-2h` | **MUGA — 無我** \| Japanese Zen Music for Flow State, Deep Focus & Losing the Self | 2H | ✅ | ⏳ | ✅ | ⏳ | ⏳ | ⏳ | ⏳ |
| `bonsai-desk-night-2h` | Deep Focus Music — Bonsai Desk Late Night | 2H | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| `lantern-glow-study-3h` | Quiet Hours Focus Music — Lantern Glow Study | 3H | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |

**MUGA (2026-09-26):** direct thematic sequel to MUSHIN (無心, channel's #1 video, 41.8K views), one concept deeper ("no-self" vs "no-mind"). Deliberately reuses MUSHIN's exact winning formula from `published-videos.md`'s analysis: classic monk+ENSO photoreal template, 2H length. **Music source updated same day: Suno is no longer usable at all (download caps) — Lyria is now the only option channel-wide, KAMI included**, so this doubles as a natural experiment: if MUGA performs near MUSHIN's level on Lyria, KAMI's underperformance is likely the visual template, not Lyria. Visual hook is a giant ENSO circle caught mid-dissolution (ink feathering into mist) rather than MUSHIN's intact circle, to literalize "no-self" distinctly. Full package written (§0-§15, 20 Lyria variants). **Hero image generated (2026-09-26)** — thumbnail (`muga-2h-thumb.jpg`) and wisdom overlay (`muga-butsugaichinyo-overlay.png`) delivered. Note: the delivered enso reads as a fully intact glowing circle rather than the "mid-dissolution, lower arc feathering into mist" spec written in §3 — closer to MUSHIN's own crisp enso than to MUGA's intended differentiator. Flagged for the user; proceeding with this image as-is unless a regenerate is requested. Next: generate the 20 Lyria variants (§1), then the Flow loop (§4) from this hero.

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