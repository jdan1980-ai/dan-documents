# YouTube Analytics Bot — self-hosted vidIQ/Social Blade alternative

17 фич для анализа и подготовки YouTube-видео. Работает на бесплатных API: YouTube Data API v3, yt-dlp, youtube-transcript-api, Google Trends (pytrends), Pillow.

## Запуск

### Двойным кликом (рекомендую)

На рабочем столе → **Start Bot** (зелёная иконка). Откроется окно с логами и автоматически браузер на http://127.0.0.1:8000.

Чтобы остановить → **Stop Bot** (красная иконка).

### Из терминала

```cmd
cd C:\Users\jdan1\projects\dan-documents
git checkout claude/create-iqvideo-bot-IwIMt
.\venv\Scripts\activate
uvicorn app.main:app --reload
```

Потом http://127.0.0.1:8000 (НЕ `localhost` — у некоторых фаервол режет).

### Первый запуск

1. Получи YouTube Data API key на https://console.cloud.google.com/ → Enable "YouTube Data API v3" → Credentials → Create API Key
2. `cp .env.example .env` → впиши `YOUTUBE_API_KEY=AIzaSy...`
3. `pip install -r requirements.txt`
4. `uvicorn app.main:app --reload`

## Все 17 функций

### 📊 Анализ (4)

| Страница | Что делает | Стоимость API |
|---|---|---|
| `/channel` | Статистика канала, outliers, топ-видео, частота загрузок | 1 unit + uploads |
| `/video` | Анализ видео: SEO, транскрипт, vs медиана канала | 1 unit |
| `/keywords` | Поиск по запросу (yt-dlp без квоты), конкуренция | 0 units |
| `/compare` | 2 канала side-by-side | 2 units |

### 📝 Pre-publish (4) — до публикации видео

| Страница | Что делает |
|---|---|
| `/seo` | **SEO Scorecard** — title + description + tags на одном экране, общий балл 0-100 + конкретные рекомендации |
| `/title-batch` | До 10 вариантов заголовка → таблица со скорами рядом, выбор за секунду |
| `/tags-suggest` | Майнинг тегов из outliers ниши — выдаёт частотные теги, реально работающие у соседей |
| `/thumbnail` | Загрузка PNG/JPG → контраст, читаемость на 320px (превью в ленте), доминантные цвета, file weight |

### 🔍 Discovery & Insights (4)

| Страница | Что делает |
|---|---|
| `/breakout` | Что взлетело в нише за 7/14/30/90 дней — `search publishedAfter` + outlier detection |
| `/trends` | Google Trends interest-over-time + rising/top related queries (через pytrends) |
| `/upload-time` | Анализ топ vs последние 30% видео канала → лучший день + час публикации |
| `/comments` | Топ-100 комментов → частотные слова, sentiment hints, кол-во вопросов |

### 💰 Forecast & Tracking (4) — Social Blade / VidIQ / TubeBuddy / LiveDune-style

| Страница | Replicates | Что делает |
|---|---|---|
| `/forecast` | Social Blade | Estimated earnings ($/мес — CPM-based), subscriber milestones, channel grade A++..F, velocity (Cooling/Stable/Hot/Breakout) |
| `/velocity` | VidIQ Vision | Views/час, views/день, прогноз 30d, vs медиана канала |
| `/history` | LiveDune | Дельта от последнего снапшота `data/channels_snapshot.json` — топ роста, новые видео |
| `/competitor-score` | TubeBuddy | Gap analysis vs топ-5 outliers ниши: title/desc length, tag count, hashtags, timestamps, duration |

### 🆎 Утилита

| Страница | Что делает |
|---|---|
| `/title` | Скоринг одного заголовка (используется внутри SEO Scorecard) |

## Snapshot system

Скрипт `scripts/fetch_snapshot.py` сохраняет текущее состояние каналов в `data/channels_snapshot.json`. Запускай регулярно (раз в день/неделю) — на каждой следующей сессии `/history` и `/forecast` покажут дельту просмотров с момента снапшота.

```cmd
python scripts/fetch_snapshot.py
```

## Архитектура

```
app/
├── main.py                  # FastAPI entrypoint
├── config.py                # Pydantic settings, читает .env
├── db.py                    # SQLite кеш ответов (24h TTL)
├── routers/
│   ├── pages.py             # GET / для каждой из 17 страниц
│   └── api.py               # POST эндпоинты для HTMX
└── services/
    ├── youtube.py           # YouTube Data API v3 клиент
    ├── ytdlp.py             # yt-dlp без квоты
    ├── transcripts.py       # youtube-transcript-api
    ├── analytics.py         # Все скоринги, гепы, прогнозы
    ├── thumbnail.py         # PIL анализ изображения
    ├── trends.py            # pytrends
    └── snapshots.py         # Чтение data/channels_snapshot.json

templates/
├── base.html                # Layout + nav (17 пунктов)
├── index.html               # Главная — 4 секции, 16 карточек
├── <feature>.html           # Форма ввода для каждой фичи
└── partials/
    └── <feature>_report.html # HTML-фрагмент результата (HTMX swap)
```

## Стоимость API

Лимит **YouTube Data API: 10 000 units/день** (бесплатно).

| Операция | units |
|---|---|
| `videos.list`, `channels.list`, `playlistItems.list`, `commentThreads.list` | 1 |
| `search.list` (используется в `/tags-suggest`, `/breakout`, `/competitor-score`) | **100** |

Все ответы кешируются в SQLite на 24 часа. Поиск по `/keywords` идёт через yt-dlp без квоты.

## Что НЕЛЬЗЯ сделать (честные ограничения)

- **YouTube Analytics API** (CTR, retention, impressions) — нужен OAuth и доступ только владельцу канала
- **Дизлайки** — убраны YouTube в 2021
- **Скрейпинг Social Blade / VidIQ / TubeBuddy** — нарушает их ToS, блокировка по IP. Мы воссоздаём их фичи на своих формулах, точные числа могут отличаться
- **Tubular audience overlap / demographics** — закрытые данные

## Лаунчеры (Windows)

- `start-bot.bat` — запуск с зелёным баннером + авто-открытие браузера
- `stop-bot.vbs` — тихая остановка (без cmd-окна)
- `install-shortcuts.ps1` — создаёт 3 ярлыка на рабочем столе (Start Bot / Stop Bot / Open Bot)

## Stack

- **Backend:** FastAPI, Pydantic v2
- **Frontend:** Jinja2 + HTMX + TailwindCSS (CDN)
- **Charts:** Plotly (CDN)
- **Cache:** SQLite (через `app/db.py`)
- **Image analysis:** Pillow
- **Trends:** pytrends (unofficial Google Trends scraper)
