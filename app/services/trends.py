"""Google Trends via pytrends (unofficial, scrapes trends.google.com)."""
from __future__ import annotations

import logging
from typing import Any

from ..db import cache_get, cache_set


logger = logging.getLogger(__name__)


def trends_for_keyword(keyword: str, geo: str = "", timeframe: str = "today 12-m") -> dict[str, Any]:
    """Get Google Trends interest-over-time + related queries.

    geo: '' (worldwide), 'US', 'RU', etc.
    timeframe: 'today 12-m', 'today 5-y', 'today 3-m', 'now 7-d'.
    """
    cache_key = f"trends:{keyword}:{geo}:{timeframe}"
    cached = cache_get(cache_key)
    if cached is not None:
        return cached

    try:
        from pytrends.request import TrendReq
    except ImportError:
        return {"error": "pytrends не установлен"}

    try:
        pyt = TrendReq(hl="en-US", tz=0, timeout=(5, 15))
        pyt.build_payload([keyword], timeframe=timeframe, geo=geo)

        iot_df = pyt.interest_over_time()
        series: list[dict[str, Any]] = []
        if iot_df is not None and not iot_df.empty:
            for ts, row in iot_df.iterrows():
                series.append({"date": ts.strftime("%Y-%m-%d"), "value": int(row[keyword])})

        rising: list[dict[str, Any]] = []
        top: list[dict[str, Any]] = []
        try:
            related = pyt.related_queries()
            if related and keyword in related:
                r = related[keyword]
                if r.get("rising") is not None:
                    for _, row in r["rising"].head(15).iterrows():
                        rising.append({"query": row["query"], "value": int(row["value"]) if row["value"] != "Breakout" else -1})
                if r.get("top") is not None:
                    for _, row in r["top"].head(15).iterrows():
                        top.append({"query": row["query"], "value": int(row["value"])})
        except Exception as e:
            logger.warning("related_queries failed (likely 429 rate limit): %s", e)

        avg = int(sum(p["value"] for p in series) / len(series)) if series else 0
        recent = int(sum(p["value"] for p in series[-12:]) / max(min(12, len(series)), 1)) if series else 0
        trend = "up" if recent > avg * 1.15 else "down" if recent < avg * 0.85 else "stable"

        result = {
            "keyword": keyword,
            "geo": geo or "Worldwide",
            "timeframe": timeframe,
            "series": series,
            "avg_interest": avg,
            "recent_interest": recent,
            "trend": trend,
            "rising": rising,
            "top": top,
        }
        cache_set(cache_key, result)
        return result
    except Exception as e:
        logger.exception("pytrends failed")
        return {"error": f"Google Trends недоступен: {e}"}
