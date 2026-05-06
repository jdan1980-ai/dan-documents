"""Fetch full video stats for both channels via yt-dlp and save as Markdown."""
import json
import sys
from datetime import datetime
from pathlib import Path

from yt_dlp import YoutubeDL


CHANNELS = {
    "Brain Cat (@braincatai)": {
        "handle": "@braincatai",
        "url": "https://youtube.com/@braincatai",
    },
    "StillWave (@stillwavezen)": {
        "handle": "@stillwavezen",
        "url": "https://youtube.com/@stillwavezen",
    },
}


def fetch_channel(url: str) -> list[dict]:
    """Fetch all videos for a channel with full stats."""
    opts = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
        "extract_flat": False,
        "playlistend": 200,
        "nocheckcertificate": True,
    }
    with YoutubeDL(opts) as ydl:
        info = ydl.extract_info(f"{url}/videos", download=False)
    entries = info.get("entries") or []
    videos = []
    for e in entries:
        if not e:
            continue
        videos.append(
            {
                "id": e.get("id"),
                "title": e.get("title") or "",
                "views": int(e.get("view_count") or 0),
                "likes": int(e.get("like_count") or 0),
                "comments": int(e.get("comment_count") or 0),
                "duration_s": int(e.get("duration") or 0),
                "upload_date": e.get("upload_date") or "",
                "url": f"https://youtube.com/watch?v={e.get('id')}",
                "tags": e.get("tags") or [],
            }
        )
    return videos


def fmt_dur(s: int) -> str:
    if s <= 0:
        return "—"
    h, rem = divmod(s, 3600)
    m, sec = divmod(rem, 60)
    if h:
        return f"{h}:{m:02d}:{sec:02d}"
    return f"{m}:{sec:02d}"


def fmt_date(d: str) -> str:
    if not d or len(d) != 8:
        return "—"
    return f"{d[:4]}-{d[4:6]}-{d[6:8]}"


def to_markdown(channel_label: str, channel_url: str, videos: list[dict]) -> str:
    if not videos:
        return f"## {channel_label}\n\nНе удалось получить видео.\n"

    sorted_videos = sorted(videos, key=lambda v: v["views"], reverse=True)
    total_views = sum(v["views"] for v in videos)
    total_likes = sum(v["likes"] for v in videos)
    total_comments = sum(v["comments"] for v in videos)
    avg_views = total_views // max(len(videos), 1)
    median_views = sorted([v["views"] for v in videos])[len(videos) // 2]

    lines = [
        f"## {channel_label}",
        f"",
        f"[{channel_url}]({channel_url})",
        f"",
        f"| Метрика | Значение |",
        f"|---|---|",
        f"| Всего видео | {len(videos)} |",
        f"| Сумма просмотров | {total_views:,} |",
        f"| Сумма лайков | {total_likes:,} |",
        f"| Сумма комментов | {total_comments:,} |",
        f"| Среднее на видео | {avg_views:,} |",
        f"| Медиана | {median_views:,} |",
        f"",
        f"### Все видео (по убыванию просмотров)",
        f"",
        f"| # | Видео | 👁 | 👍 | 💬 | ⏱ | Дата |",
        f"|---|---|---:|---:|---:|---:|---|",
    ]
    for i, v in enumerate(sorted_videos, 1):
        title = v["title"].replace("|", "\\|")[:80]
        lines.append(
            f"| {i} | [{title}]({v['url']}) "
            f"| {v['views']:,} | {v['likes']:,} | {v['comments']:,} "
            f"| {fmt_dur(v['duration_s'])} | {fmt_date(v['upload_date'])} |"
        )
    return "\n".join(lines) + "\n"


def main():
    out_dir = Path("data")
    out_dir.mkdir(exist_ok=True)

    all_data = {}
    md_parts = [
        "# Snapshot статистики каналов",
        "",
        f"_Собрано: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')} через yt-dlp_",
        "",
    ]

    for label, info in CHANNELS.items():
        print(f"[*] Fetching {label}...", file=sys.stderr)
        try:
            videos = fetch_channel(info["url"])
        except Exception as e:
            print(f"[!] Failed: {e}", file=sys.stderr)
            videos = []
        all_data[label] = videos
        md_parts.append(to_markdown(label, info["url"], videos))
        md_parts.append("")

    (out_dir / "channels_snapshot.json").write_text(
        json.dumps(all_data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    Path("CHANNELS_SNAPSHOT.md").write_text("\n".join(md_parts), encoding="utf-8")
    print("[+] Saved data/channels_snapshot.json + CHANNELS_SNAPSHOT.md", file=sys.stderr)


if __name__ == "__main__":
    main()
