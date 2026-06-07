# Keyword Research Cache

Покрывает гипотезу: **vidIQ-данные для кошачьей ниши стабильны 30-60 дней** → дёргаем платный vidIQ MCP **редко**, кэшируем результат в `vidiq-cache.json`, переиспользуем сколько данные релевантны.

## Структура файла `vidiq-cache.json`

```json
{
  "meta": { "total_credits_spent": N, "credits_saved_so_far": N },
  "queries": [
    {
      "keyword": "seed query string",
      "fetched": "YYYY-MM-DD",
      "credits_spent": 5,
      "seed": {volume, competition, overall, monthly},
      "top_related": [{keyword, score, monthly, competition, verdict}],
      "verdict": "USED/BLOCKED/AVAILABLE — context",
      "notes": "..."
    }
  ],
  "candidates_not_yet_researched": [...]
}
```

## Workflow для Claude (правило)

**Перед тем как тратить vidIQ MCP credits:**

1. Открой `vidiq-cache.json` → ищи keyword (или близкий синоним)
2. Если найден + `fetched` < 60 дней назад → **используй кэш**, не вызывай vidIQ MCP
3. Если найден + старее 60 дней → можно re-fetch (cat-niche keywords могут смещаться)
4. Если **не найден** → спроси юзера разрешения потратить credits → **fetch + сразу добавь в кэш**
5. После каждого нового vidIQ-вызова → **обнови `vidiq-cache.json`** с полным результатом + увеличь `total_credits_spent`

## Workflow для юзера

**Если хочешь сам пополнить кэш:** запусти бот → `/keywords` → введи запрос → скопируй JSON-ответ → добавь в `vidiq-cache.json` как новую запись в `queries[]`. Так канал имеет богатую "library" без credit-burn.

## Verdict legend

- `GREEN` — score >65 + monthly >5k → стоит снимать
- `YELLOW` — 50-65 или monthly 2-5k → снимать с осторожностью / поискать сильнее
- `RED` — <50 или monthly <2k → не тратить production-слот
- `USED` — уже опубликовано, не предлагать
- `BLOCKED` — каннибализация существующего видео

## Credit-saving math

- Каждый vidIQ MCP call = **5 credits**
- Кэш-хит = **0 credits**
- Каждый раз когда ты находишь нужную инфу в кэше вместо нового запроса → запиши +5 в `credits_saved_so_far`
- Цель: к концу мая 2026 cache_hit_rate > 70% → 50+ credits экономии в месяц
