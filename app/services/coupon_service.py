from app.models.schemas import BestCoupon, CouponSearchResponse, OtherCoupon
from app.services.sources import SourceClient
from app.services.validation import anti_scam_pass, condition_match, confidence_score, expiry_valid, parse_date


class CouponService:
    def __init__(self) -> None:
        self.source_client = SourceClient()

    def search(self, brand: str, category: str | None = None) -> CouponSearchResponse:
        offers = self.source_client.fetch_offers(brand=brand, category=category)
        valid = []

        for offer in offers:
            if not anti_scam_pass(offer):
                continue

            expiry = parse_date(offer.get("expiry"))
            is_expiry_valid = expiry_valid(expiry)
            is_condition_match = condition_match(offer.get("conditions"), category)
            score = confidence_score(is_expiry_valid, is_condition_match, offer.get("success_rate"))

            if score < 60:
                continue

            valid.append(
                {
                    "code": offer["code"],
                    "discount": offer["discount"],
                    "confidence": score,
                }
            )

        valid.sort(key=lambda x: x["confidence"], reverse=True)

        best = valid[0] if valid else None
        others = valid[1:] if len(valid) > 1 else []

        return CouponSearchResponse(
            brand=brand,
            best_coupon=BestCoupon(**best) if best else None,
            other_coupons=[OtherCoupon(code=o["code"], confidence=o["confidence"]) for o in others],
        )
