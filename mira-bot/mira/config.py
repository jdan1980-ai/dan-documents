import os
from dataclasses import dataclass, field


def _bool(value: str | None, default: bool) -> bool:
    if value is None or value == "":
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def _ids(value: str | None) -> frozenset[int]:
    if not value:
        return frozenset()
    return frozenset(int(p) for p in value.replace(" ", "").split(",") if p)


@dataclass(frozen=True)
class Settings:
    telegram_token: str
    anthropic_api_key: str
    db_path: str = "mira.db"
    model_chat: str = "claude-haiku-4-5-20251001"
    model_sos: str = "claude-opus-5-5"
    model_report: str = "claude-haiku-4-5-20251001"
    admin_ids: frozenset[int] = field(default_factory=frozenset)
    paywall_enabled: bool = False
    trial_days: int = 7
    daily_message_limit: int = 80
    default_tz: str = "Asia/Jerusalem"
    payment_link: str = ""

    @classmethod
    def from_env(cls) -> "Settings":
        env = os.environ
        token = env.get("TELEGRAM_BOT_TOKEN", "")
        key = env.get("ANTHROPIC_API_KEY", "")
        if not token or not key:
            raise SystemExit("Нужны TELEGRAM_BOT_TOKEN и ANTHROPIC_API_KEY (см. .env.example)")
        return cls(
            telegram_token=token,
            anthropic_api_key=key,
            db_path=env.get("DB_PATH", "mira.db"),
            model_chat=env.get("MODEL_CHAT", cls.model_chat),
            model_sos=env.get("MODEL_SOS", cls.model_sos),
            model_report=env.get("MODEL_REPORT", cls.model_report),
            admin_ids=_ids(env.get("ADMIN_IDS")),
            paywall_enabled=_bool(env.get("PAYWALL_ENABLED"), False),
            trial_days=int(env.get("TRIAL_DAYS", "7")),
            daily_message_limit=int(env.get("DAILY_MESSAGE_LIMIT", "80")),
            default_tz=env.get("DEFAULT_TIMEZONE", "Asia/Jerusalem"),
            payment_link=env.get("PAYMENT_LINK", ""),
        )
