"""Pre-configured competitor channels and niche-specific scoring tuning.

Edit this file to add your own channels or tune scoring keywords for your niche.
"""
from __future__ import annotations


PRESETS: dict[str, dict] = {
    "brain_cat": {
        "label": "Brain Cat — cat psychology shorts",
        "your_channels": ["UCMKcrIw1l1u_WU0M9Cv-DKw"],
        "competitors": [
            {"id": "UCYE8gWtISb_CJd1RBNLB0CQ", "title": "Pawsome Cat Minds", "subs": 3790},
            {"id": "UCEZj8zvPA7Q4zTn1pmY6Y-Q", "title": "Catnip Chaos", "subs": 2230},
            {"id": "UC668MRYzX03qHDKn61QYsgw", "title": "The Cat Behavior Guide", "subs": 1500},
            {"id": "UCNf1VL18EpE2WVSTGV-0JYw", "title": "Kitty FactZone", "subs": 1480},
            {"id": "UCEYmHqHBusdttX5WtdCxBiQ", "title": "Feline Clues", "subs": 44},
            {"id": "UCTqgfSEQ2_PK9FsLddVJBfw", "title": "Cat Zorro", "subs": 14500},
        ],
        "winning_title_patterns": [
            "What psychology says about your cat",
            "{N} dark truths about your cat — #{n} will stay with you",
            "Why your cat {does X}",
            "Cats vs {Y}",
            "I tested {X} on cats",
        ],
        "keywords": [
            "cat psychology", "cat facts", "cat behavior",
            "why cats", "cat science", "feline behavior",
            "animal psychology", "pet facts",
        ],
    },
    "still_wave": {
        "label": "StillWave — Japanese Zen + healing frequencies",
        "your_channels": ["UC188FjOT6tivjPOPfZ69s7Q"],
        "competitors": [
            {"id": "UCRqoKky6bPNRoTlCUbQ4Gkg", "title": "Yamato Zen Relaxing", "subs": 3030},
            {"id": "UCB_Fb89w5TmpKFLOpEhHGsg", "title": "Inner Calm", "subs": 2490},
            {"id": "UCy4mVeGGXLPXy4V0ORKS8Qw", "title": "Healing Ether", "subs": 7540},
            {"id": "UCSYbSVuiKV73g30BCYfmWWw", "title": "Mystic Tunes", "subs": 4320},
            {"id": "UCOv0RsgLtqRBihSqZsN4b8w", "title": "Lumina Forest", "subs": 7960},
            {"id": "UCgwkoBfFczdO2faqGqRNkkg", "title": "Cosmic Resonance", "subs": 189000},
        ],
        "winning_title_patterns": [
            "{Hz} Hz | {Promise} | {Duration} {Format}",
            "Japanese {Element} | {Promise} | {Duration}",
            "{Frequency} for {physiological benefit}",
            "Drift into deep sleep • {benefit} • {benefit}",
        ],
        "keywords": [
            "528 hz", "432 hz", "639 hz", "852 hz",
            "japanese zen", "shakuhachi", "deep sleep music",
            "healing frequencies", "meditation music", "sleep music",
            "ambient music", "binaural beats",
        ],
    },
}


# Niche-specific positive markers (in addition to base list in analytics.py).
# Used to tune title scoring per niche.
NICHE_POSITIVE_MARKERS = {
    "meditation": [
        "deep sleep", "fall asleep", "insomnia", "anxiety relief",
        "stress relief", "melatonin", "healing", "instant",
        "hours", "deep", "guided",
    ],
    "cat_psychology": [
        "secret", "truth", "scientists", "psychology says",
        "mind-blown", "facts every", "did you know",
    ],
}


# Patterns that hurt CTR in these niches (in addition to base CAPS / etc).
NICHE_NEGATIVE_MARKERS = {
    "meditation": [
        "🔥",  # high-energy emojis don't fit the calm niche
    ],
    "cat_psychology": [],
}
