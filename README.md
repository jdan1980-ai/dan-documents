# YouTube Analytics — vidIQ-альтернатива на бесплатных источниках

Веб-инструмент для анализа YouTube-каналов и видео. Заменяет основной функционал vidIQ:

- **Анализ канала** — статистика, частота загрузок, выбросы (outliers), топ-видео, динамика
- **Анализ видео** — заголовок, SEO, транскрипт, ключевые слова, сравнение с медианой канала
- **Исследование ключевых слов** — поиск без квоты YouTube API, оценка конкуренции, связанные слова
- **Скоринг заголовка** — оценка длины, эмоций, кликбейт-маркеров

## Стек

- **Backend:** FastAPI (Python)
- **Frontend:** Jinja2 + HTMX + TailwindCSS (CDN)
- **Графики:** Plotly
- **Хранилище:** SQLite (кеш ответов)
- **Источники данных:** YouTube Data API v3, `yt-dlp`, `youtube-transcript-api`

## Запуск

### 1. Установить Python 3.10+

Проверь:
```bash
python3 --version
```

### 2. Получить API-ключ YouTube Data API v3

1. Открой https://console.cloud.google.com/
2. Создай проект (любое имя)
3. В поиске сверху найди «YouTube Data API v3» → нажми **Enable**
4. Слева: **APIs & Services → Credentials → + CREATE CREDENTIALS → API key**
5. Скопируй ключ (формата `AIzaSy...`)

Бесплатно, лимит 10 000 запросов в день.

### 3. Установка зависимостей

```bash
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Настройка `.env`

```bash
cp .env.example .env
# открой .env и вставь свой YOUTUBE_API_KEY
```

### 5. Запуск сервера

```bash
uvicorn app.main:app --reload
```

Открой http://localhost:8000 в браузере.

## Структура проекта

```
.
├── app/
│   ├── main.py              # точка входа FastAPI
│   ├── config.py            # настройки из .env
│   ├── db.py                # SQLite-кеш
│   ├── routers/
│   │   ├── pages.py         # HTML-страницы
│   │   └── api.py           # HTMX-эндпоинты (возвращают HTML-фрагменты)
│   └── services/
│       ├── youtube.py       # YouTube Data API v3 клиент
│       ├── ytdlp.py         # yt-dlp (без квоты)
│       ├── transcripts.py   # субтитры + ключевики
│       └── analytics.py     # outliers, скоринг, агрегаты
├── templates/               # Jinja2 шаблоны
│   ├── base.html
│   ├── index.html
│   ├── channel.html
│   ├── video.html
│   ├── keywords.html
│   ├── title.html
│   └── partials/            # HTML-фрагменты для HTMX
├── static/
│   └── style.css
├── data/                    # SQLite база (создаётся автоматически)
├── .env.example
├── requirements.txt
└── README.md
```

## Экономия квоты

YouTube API даёт 10 000 units/день бесплатно. Стоимость операций:

| Операция | units |
|---|---|
| `videos.list` | 1 |
| `channels.list` | 1 |
| `playlistItems.list` | 1 |
| `search.list` | **100** |

**Что делает приложение, чтобы экономить квоту:**

- Все ответы кешируются в SQLite на 24 часа (настраивается `CACHE_TTL`)
- Поиск по ключевикам идёт через `yt-dlp` — без квоты вообще
- Транскрипты тянутся через `youtube-transcript-api` — без квоты

## Дальше

- [ ] CV-скоринг превью (яркость, лица, текст)
- [ ] Сравнение двух каналов рядом
- [ ] Поиск похожих/breakout каналов
- [ ] Экспорт отчётов в PDF/CSV
- [ ] Авторизация и сохранённые каналы
