"""Legal source adapters (stubbed for MVP).
Replace these with official APIs/affiliate partners/public platforms.
"""

from typing import Dict, List


class SourceClient:
    def fetch_offers(self, brand: str, category: str | None = None) -> List[Dict]:
        # Stub data simulating legal/public deal platform responses.
        sample = [
            {
                "code": f"{brand[:4].upper()}10",
                "discount": "10% OFF",
                "expiry": "2099-12-31",
                "conditions": "Min purchase $50",
                "source": "public_deal_platform",
                "success_rate": 0.78,
                "title": f"{brand} 10% off orders above $50",
                "url": f"https://deals.example/{brand}",
            },
            {
                "code": "SAVE20",
                "discount": "20% OFF",
                "expiry": "2020-01-01",
                "conditions": "First-time users",
                "source": "affiliate_api",
                "success_rate": 0.31,
                "title": f"{brand} first-time coupon",
                "url": f"https://affiliate.example/{brand}",
            },
            {
                "code": "GENERATOR-UNLOCK",
                "discount": "50% OFF",
                "expiry": "2099-12-31",
                "conditions": "Use coupon generator",
                "source": "unknown_blog",
                "success_rate": 0.05,
                "title": f"{brand} coupon generator",
                "url": f"https://spam.example/{brand}",
            },
        ]
        return sample
