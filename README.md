# Coupon Finder AI

FastAPI backend for finding likely-valid coupon codes from legal/public sources and filtering fake/expired offers.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API

### POST `/coupons/search`

Request:

```json
{
  "brand": "nike",
  "category": "shoes"
}
```

Example response:

```json
{
  "brand": "nike",
  "best_coupon": {
    "code": "NIKE10",
    "discount": "10% OFF",
    "confidence": 91
  },
  "other_coupons": []
}
```

## Notes

- Sources are intentionally adapter-based and currently stubbed for a legally compliant MVP.
- No scraping bypasses/captcha circumvention are implemented.
- Confidence scoring uses expiry validity, condition match, and success rate.
