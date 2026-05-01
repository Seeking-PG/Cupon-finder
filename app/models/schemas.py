from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field


class Coupon(BaseModel):
    code: str
    discount: str
    expiry: Optional[date] = None
    conditions: Optional[str] = None
    source: str
    expiry_valid: bool = False
    condition_match: bool = False
    success_rate: Optional[float] = None
    confidence: int = Field(ge=0, le=100)


class CouponSearchRequest(BaseModel):
    brand: str = Field(min_length=1)
    category: Optional[str] = None


class BestCoupon(BaseModel):
    code: str
    discount: str
    confidence: int


class OtherCoupon(BaseModel):
    code: str
    confidence: int


class CouponSearchResponse(BaseModel):
    brand: str
    best_coupon: Optional[BestCoupon] = None
    other_coupons: List[OtherCoupon] = []
