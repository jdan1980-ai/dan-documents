"""Тексты интерфейса. Ответы самой Mira генерирует модель, здесь только служебное."""

STRINGS: dict[str, dict[str, str]] = {
    "en": {
        "choose_lang": "Hi, I'm Mira. Pick a language:",
        "age": "I'm an AI coach for people who want to drink less. I'm not a doctor or therapist, "
               "and I'm not a replacement for medical care.\n\nAre you 18 or older?",
        "age_yes": "Yes, I'm 18+",
        "age_no": "No",
        "age_blocked": "Mira is built for adults. Please talk to a parent or a school counselor. Take care.",
        "q_name": "What should I call you?",
        "q_goal": "Nice to meet you, {name}. What are you aiming for?",
        "goal_cut_back": "Cut back",
        "goal_break": "30-day break",
        "goal_quit": "Quit for good",
        "q_baseline": "Roughly how many drinks do you have in a typical week? (just a number)",
        "q_baseline_bad": "Just a number please, like 14. A rough guess is fine.",
        "q_drink": "What do you mostly drink?",
        "q_triggers": "When does the pull show up most? (stress, evenings, social stuff, boredom... in your own words)",
        "q_tried": "Have you tried cutting back before? What happened?",
        "q_motivation": "Last one: why does this matter to you right now?",
        "heavy_warning": "One important thing: if you drink heavily every day, stopping suddenly can be dangerous. "
                         "Please talk to a doctor before you quit abruptly.",
        "help": "I'm here any time, just write.\n\n"
                "/sos - a craving right now\n"
                "/log 2 wine - log drinks\n"
                "/stats - your last 7 days\n"
                "/lang - change language\n"
                "/timezone Asia/Jerusalem - set your timezone\n"
                "/delete - delete all your data",
        "sos_start": "I'm here. What's happening right now?",
        "sos_ok": "I'm okay now",
        "sos_done_ask": "How did it go?",
        "out_resisted": "Rode it out",
        "out_drank": "I drank",
        "out_unclear": "Not sure",
        "sos_closed": "Noted. Write me any time.",
        "log_usage": "Usage: /log 2 wine (the type is optional)",
        "logged": "Logged: {count:g} {drink}. Today: {today:g}.",
        "stats": "Last 7 days: {total:g} drinks.\nYour typical week before: {baseline}.\n{delta}",
        "delta_less": "That is {pct}% less.",
        "delta_more": "That is {pct}% more. No judgment, it's just data.",
        "delta_same": "About the same so far.",
        "delta_unknown": "",
        "tz_set": "Timezone set to {tz}.",
        "tz_bad": "I don't know that timezone. Example: /timezone Asia/Jerusalem",
        "lang_set": "Language set to English.",
        "delete_confirm": "This permanently deletes your profile, chats and logs. Sure?",
        "delete_yes": "Delete everything",
        "delete_no": "Cancel",
        "deleted": "Done. Everything is deleted. /start if you ever want to begin again.",
        "cancelled": "Cancelled.",
        "rate_limited": "That's a lot of messages today. Let's pick this up tomorrow. If it's urgent, use /sos.",
        "expired": "Your free trial has ended. To keep going with Mira, subscribe: {link}",
        "error": "Sorry, I had a technical hiccup. Try again in a minute.",
        "need_start": "Send /start first.",
        "crisis": "I'm an AI and I'm not equipped to support you through this. Please reach out to a person right now.\n\n"
                  "Israel: ERAN 1201\nUSA: call or text 988\nIn immediate danger: 101 (Israel ambulance), 100 (Israel police), 911 (USA), 112 (EU).\n\n"
                  "I'll stay here with you too.",
        "withdrawal": "What you're describing can be dangerous: alcohol withdrawal can cause seizures. "
                      "Please get medical help now: 101 (Israel), 911 (USA), 112 (EU), or go to the nearest ER.",
        "report_title": "Your week",
    },
    "ru": {
        "choose_lang": "Привет, я Mira. Выбери язык:",
        "age": "Я AI-коуч для тех, кто хочет пить меньше. Я не врач и не психотерапевт и не заменяю медицинскую помощь.\n\n"
               "Тебе есть 18 лет?",
        "age_yes": "Да, мне 18+",
        "age_no": "Нет",
        "age_blocked": "Mira создана для взрослых. Поговори с родителями или школьным психологом. Береги себя.",
        "q_name": "Как к тебе обращаться?",
        "q_goal": "Рада знакомству, {name}. К чему ты стремишься?",
        "goal_cut_back": "Сократить",
        "goal_break": "Перерыв 30 дней",
        "goal_quit": "Бросить совсем",
        "q_baseline": "Сколько примерно порций алкоголя в обычную неделю? (просто число)",
        "q_baseline_bad": "Напиши просто число, например 14. Примерно тоже подойдёт.",
        "q_drink": "Что ты пьёшь чаще всего?",
        "q_triggers": "Когда тянет сильнее всего? (стресс, вечера, компании, скука... своими словами)",
        "q_tried": "Пробовал(а) сокращать раньше? Что получилось?",
        "q_motivation": "Последний вопрос: почему это важно для тебя сейчас?",
        "heavy_warning": "Важно: если ты пьёшь много каждый день, резко бросать может быть опасно. "
                         "Сначала поговори с врачом.",
        "help": "Я на связи в любое время, просто пиши.\n\n"
                "/sos - тяга прямо сейчас\n"
                "/log 2 вино - записать выпитое\n"
                "/stats - последние 7 дней\n"
                "/lang - сменить язык\n"
                "/timezone Asia/Jerusalem - часовой пояс\n"
                "/delete - удалить все мои данные",
        "sos_start": "Я здесь. Что происходит прямо сейчас?",
        "sos_ok": "Мне лучше",
        "sos_done_ask": "Чем закончилось?",
        "out_resisted": "Пережил(а)",
        "out_drank": "Выпил(а)",
        "out_unclear": "Не уверен(а)",
        "sos_closed": "Записала. Пиши в любой момент.",
        "log_usage": "Пример: /log 2 вино (тип можно не указывать)",
        "logged": "Записала: {count:g} {drink}. Сегодня: {today:g}.",
        "stats": "Последние 7 дней: {total:g} порций.\nОбычная неделя раньше: {baseline}.\n{delta}",
        "delta_less": "Это на {pct}% меньше.",
        "delta_more": "Это на {pct}% больше. Без осуждения, это просто данные.",
        "delta_same": "Пока примерно так же.",
        "delta_unknown": "",
        "tz_set": "Часовой пояс: {tz}.",
        "tz_bad": "Не знаю такой пояс. Пример: /timezone Asia/Jerusalem",
        "lang_set": "Язык: русский.",
        "delete_confirm": "Это навсегда удалит профиль, переписку и записи. Уверен(а)?",
        "delete_yes": "Удалить всё",
        "delete_no": "Отмена",
        "deleted": "Готово, всё удалено. Если захочешь начать заново, /start.",
        "cancelled": "Отменено.",
        "rate_limited": "Сегодня очень много сообщений. Продолжим завтра. Если срочно, жми /sos.",
        "expired": "Пробный период закончился. Чтобы продолжить с Mira, оформи подписку: {link}",
        "error": "Извини, технический сбой. Попробуй через минуту.",
        "need_start": "Сначала отправь /start.",
        "crisis": "Я искусственный интеллект и не могу помочь с этим так, как нужно. Пожалуйста, обратись к человеку прямо сейчас.\n\n"
                  "Израиль: ЭРАН 1201 (есть русскоязычная линия)\nСША: 988\nНепосредственная опасность: 101 (скорая, Израиль), 100 (полиция, Израиль), 112 (ЕС и Россия), 911 (США).\n\n"
                  "Я останусь с тобой в этом чате.",
        "withdrawal": "То, что ты описываешь, может быть опасно: при алкогольной абстиненции бывают судороги. "
                      "Пожалуйста, срочно обратись за медицинской помощью: 101 (Израиль), 112 (ЕС и Россия), 911 (США), или поезжай в ближайшее приёмное отделение.",
        "report_title": "Твоя неделя",
    },
}

LANG_NAMES = {"en": "English", "ru": "Russian"}


def t(lang: str, key: str, **kw) -> str:
    text = STRINGS.get(lang, STRINGS["en"])[key]
    return text.format(**kw) if kw else text
