from datetime import date, datetime
from typing import Dict


SCAM_KEYWORDS = {"generator", "unlock", "hack", "free gift card"}


def parse_date(value: str | None):
    if not value:
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        return None


def expiry_valid(expiry: date | None) -> bool:
    return bool(expiry and expiry >= date.today())


def condition_match(conditions: str | None, category: str | None) -> bool:
    if not conditions:
        return True
    if not category:
        return True
    return category.lower() in conditions.lower()


def anti_scam_pass(offer: Dict) -> bool:
    text = " ".join(
        [offer.get("title", ""), offer.get("conditions", ""), offer.get("code", ""), offer.get("url", "")]
    ).lower()
    return not any(keyword in text for keyword in SCAM_KEYWORDS)


def confidence_score(expiry_ok: bool, condition_ok: bool, success_rate: float | None) -> int:
    score = 0
    score += 35 if expiry_ok else 0
    score += 25 if condition_ok else 5
    if success_rate is None:
        score += 20
    else:
        score += int(max(0.0, min(1.0, success_rate)) * 40)
    return max(0, min(100, score))
