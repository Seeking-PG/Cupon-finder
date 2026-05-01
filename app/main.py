from fastapi import FastAPI
from app.models.schemas import CouponSearchRequest, CouponSearchResponse
from app.services.coupon_service import CouponService

app = FastAPI(title="Coupon Finder AI", version="0.1.0")
service = CouponService()


@app.post("/coupons/search", response_model=CouponSearchResponse)
def search_coupons(payload: CouponSearchRequest) -> CouponSearchResponse:
    return service.search(brand=payload.brand, category=payload.category)
