# StillWave — Power Hour 力 (CHIKARA) Playlist

YouTube playlist for the **Power Hour Focus** series. One sustained hour of deep work — coding, writing, studying, trading. Each entry is a ~1H long-form video using the locked Spacious Tokyo Penthouse aesthetic.

- **Channel:** StillWave ([@stillwavezen](https://www.youtube.com/@stillwavezen)) — `UC188FjOT6tivjPOPfZ69s7Q`
- **Иероглиф:** 力 (chikara — power, strength)
- **Visibility:** Public
- **Ordering:** Manual (newest first); pin the strongest performer to position 1 after 7d review
- **Status:** ⏳ awaiting manual creation in YouTube Studio (no OAuth creds on file for `playlists.insert`)

---

## 1. Playlist title

```
Power Hour 力 — 1H Deep Work Focus Music | Coding, Writing & Studying Sprints
```

> Иероглиф is allowed in playlist titles (see `stillwave/CLAUDE.md` §Title format). Keyword-first "Power Hour" leads for search; the 力 carries channel identity; the tail covers the 3 highest-intent use cases from the Tokyo Apartment Rain Tags table (coding / writing / studying).

### A/B variant

```
力 CHIKARA — Power Hour Focus | 1H Deep Work Sprints for Late-Night Coding & Study
```

---

## 2. Playlist description

```
Power Hour 力 — one sustained hour of deep work.

This is the StillWave Power Hour series: 1-hour focus music sessions designed for a single, uninterrupted sprint of concentration. Each video locks you into the same atmosphere — a quiet luxury apartment high above neon Tokyo, rain or lantern light on the glass, a warm fireplace glow, an open laptop on a cedar desk. No buildup. No climax. No distraction. Just one hour.

Use it for:
• 1-hour Pomodoro-style coding sprints
• Power hour writing sessions and journaling
• Focused study, deep reading, exam prep
• A single trading hour focus block
• Creative flow and ideation
• Late-night deep work after the city sleeps

New Power Hour focus sessions every Tuesday and Friday. Subscribe and tap the bell — one hour at a time, we build the habit.

力 (chikara) — power, strength. The kind that comes from one focused hour, not eight scattered ones.

#powerhour #1hourfocus #deepwork #deepfocusmusic #studymusic #codingmusic #pomodoro #japaneseambient #tokyomusic #flowstate
```

> Length: ~960 chars. YouTube playlist description limit = 5000 chars; this leaves room to append per-video timestamps or a featured-track list once the playlist has 3+ entries.

---

## 3. Initial video list (manual add order)

| Order | Video | Length | YT video ID | Status | Added |
|-------|-------|--------|-------------|--------|-------|
| 1 | Power Hour Focus Music — Tokyo Apartment Rain \| 1H Deep Work Sprint for Coding, Writing & Studying | 1H 04min 48sec | _TBD — pull from `videos.list` after May 10, 14:00 publish_ | 📤 published May 10, 2026 | ⏳ |

### Pipeline for additions

A video joins the playlist when **both** are true:
1. Length is between **58min and 1H 12min** (Power Hour band — fits the 1H Pomodoro / focus-sprint search intent)
2. Aesthetic follows the Spacious Tokyo Penthouse hybrid spec (see `stillwave/CLAUDE.md` §Aesthetic)

### Candidates already in production / backlog

| Slug | Length | Power Hour band? | Action |
|------|--------|------------------|--------|
| `tokyo-apartment-rain-1h` | 1H 04min | ✅ yes | Add to playlist on publish day (May 10) |
| `nervous-system-reset-528hz-1h` | 1H 01min | ✅ yes — borderline (different theme: 528Hz / nervous system, not deep work) | Decide after 7d review — if it lifts on "1 hour focus" search, add; if it lifts on "528 Hz" search, leave out (different audience cluster) |
| `bonsai-desk-night-2h` | 2H | ❌ no — belongs to a future "Deep Work 2H" playlist | Skip |
| `lantern-glow-study-3h` | 3H | ❌ no — belongs to a future "Quiet Hours 3H" playlist | Skip |

### Legacy candidate (decision: SKIP)

- `1 Hour Shakuhachi Flute Meditation • Japanese Zen Music` (2026-03-21, 1H 4M 49S, 228 views) — fits the **length** band but **not the aesthetic** (old иероглиф / sumi-e format, not Spacious Tokyo Penthouse). Including it dilutes the series identity in Phase 1. Reconsider only if we ever rebrand it.

---

## 4. Thumbnail / cover

Use the existing POWER HOUR overlay assets already in the repo:

- `stillwave/assets/power-hour-large.png` — playlist cover (large variant, best contrast at YouTube's playlist-card crop)
- `stillwave/assets/power-hour-overlay.png` — overlay layer if combining with a still from the latest entry

YouTube auto-derives the playlist thumbnail from video #1 by default. **Override** to the large POWER HOUR asset in Studio so the series reads as a coherent unit even before it has multiple videos.

---

## 5. Tags & discovery

Playlists themselves don't have a tags field, but the **description** carries SEO. The hashtags at the bottom of the description (10 above) cover the core keyword cluster: `powerhour`, `1hourfocus`, `deepwork`, `deepfocusmusic`, `studymusic`, `codingmusic`, `pomodoro`, `japaneseambient`, `tokyomusic`, `flowstate`.

These are the same tokens that won attribution for the Tokyo Apartment Rain video (see `stillwave/scripts/tokyo-apartment-rain-1h.md` §Tags audit trail).

---

## 6. How to create the playlist

### Option A — Manual (YouTube Studio) — DO THIS FIRST

1. YouTube Studio → **Content** → **Playlists** → **New playlist**
2. Title: paste from §1 above
3. Visibility: **Public**
4. Save → open the new playlist → **Edit** description: paste from §2
5. Add video: **Tokyo Apartment Rain — Power Hour Focus Music** (after it goes live May 10, 14:00)
6. **Playlist settings** → **Set custom thumbnail** → upload `stillwave/assets/power-hour-large.png`
7. Ordering: **Manual** (so we control the pin order after 7d/30d reviews)
8. Copy the resulting playlist URL (`https://www.youtube.com/playlist?list=PL...`) — paste into §7 below + add to `tokyo-apartment-rain-1h.md` description ("Part of the Power Hour 力 playlist: <URL>")

### Option B — API (when OAuth creds are available)

`playlists.insert` requires OAuth 2.0 with scope `https://www.googleapis.com/auth/youtube` — the read-only API key at `/root/.config/youtube-api-key` (see `stillwave/CLAUDE.md`) is **not** sufficient. Once a desktop or service-account OAuth flow is wired up:

```bash
# 1. Create the playlist (returns the new playlistId)
ACCESS_TOKEN=...  # OAuth2 access token with youtube scope

curl -s -X POST "https://www.googleapis.com/youtube/v3/playlists?part=snippet,status" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON' | jq
{
  "snippet": {
    "title": "Power Hour 力 — 1H Deep Work Focus Music | Coding, Writing & Studying Sprints",
    "description": "Power Hour 力 — one sustained hour of deep work.\n\nThis is the StillWave Power Hour series: 1-hour focus music sessions designed for a single, uninterrupted sprint of concentration. Each video locks you into the same atmosphere — a quiet luxury apartment high above neon Tokyo, rain or lantern light on the glass, a warm fireplace glow, an open laptop on a cedar desk. No buildup. No climax. No distraction. Just one hour.\n\nUse it for:\n• 1-hour Pomodoro-style coding sprints\n• Power hour writing sessions and journaling\n• Focused study, deep reading, exam prep\n• A single trading hour focus block\n• Creative flow and ideation\n• Late-night deep work after the city sleeps\n\nNew Power Hour focus sessions every Tuesday and Friday. Subscribe and tap the bell — one hour at a time, we build the habit.\n\n力 (chikara) — power, strength. The kind that comes from one focused hour, not eight scattered ones.\n\n#powerhour #1hourfocus #deepwork #deepfocusmusic #studymusic #codingmusic #pomodoro #japaneseambient #tokyomusic #flowstate",
    "defaultLanguage": "en"
  },
  "status": { "privacyStatus": "public" }
}
JSON

# 2. Add the Tokyo Apartment Rain video (replace VIDEO_ID + PLAYLIST_ID from step 1)
curl -s -X POST "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "snippet": {
      "playlistId": "PLAYLIST_ID",
      "position": 0,
      "resourceId": { "kind": "youtube#video", "videoId": "VIDEO_ID" }
    }
  }' | jq

# 3. Upload a custom thumbnail for the playlist
# (NOTE: thumbnails.set works only on videos, not playlists; YouTube derives the
#  playlist card from video #1's thumbnail. Override is UI-only in YouTube Studio.)
```

Quota: `playlists.insert` = 50 units, `playlistItems.insert` = 50 units. Both cost is within daily 10k budget.

---

## 7. Playlist record (fill in after creation)

- **Playlist ID:** `_TBD_`
- **Playlist URL:** `_TBD_`
- **Created:** `_TBD_`
- **Created via:** ☐ YouTube Studio (manual) ☐ API
- **First entry added:** `_TBD_` (videoId)

---

## 8. Review cadence

Tie to the Tokyo Apartment Rain review schedule (see `stillwave/production-status.md`):

- **48h after first add (May 12, 14:00)** — log playlist impressions / views via `playlists.list` + `playlistItems.list`; record in `published-videos.md` under a new "Playlist performance" section
- **7d (May 17, 14:00)** — decide whether to add `nervous-system-reset-528hz-1h` based on whether it pulled "1 hour focus" or "528 Hz" search traffic
- **30d (June 9, 14:00)** — decide if Power Hour becomes the locked series template (then we commit to 1 new entry / week minimum)
