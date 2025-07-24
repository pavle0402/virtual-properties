from pydantic import BaseModel, ConfigDict
from typing import TypeVar, Optional, Generic, List
from app.enums.apartment_enums import (
    CurrencyEnum,
    ListingTypeEnum,
    ConditionEnum,
    HeatingTypeEnum,
    OwnershipTypeEnum
)

#abstract response schema for whole project
ResponseData = TypeVar("ResponseData")

class DetailResponse(BaseModel, Generic[ResponseData]):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    data: Optional[ResponseData] = None
    status: Optional[str] = None
    err_msg: Optional[str] = None


class FinancialInfoSchema(BaseModel):
    price: int
    currency: CurrencyEnum
    listing_type: ListingTypeEnum
    deposit_required: bool = True
    utilities_included: bool = False
    monthly_utilities_cost: Optional[int] = None

class LocationSchema(BaseModel):
    address: Optional[str] = None
    city: str
    muncipality: Optional[str] = None
    postal_code: Optional[str] = None
    latitude: Optional[str] = None
    longtitude: Optional[str] = None
    orientation: List[str]

class InteriorSchema(BaseModel):
    total_area_measured: Optional[float] = None
    bedroom_count: Optional[int] = 1
    bathroom_count: Optional[int] = 1
    floor_number: Optional[int] = None
    total_floors: Optional[int] = None
    condition: Optional[ConditionEnum] = None
    furnished: Optional[bool] = True

class AdditionalInfoSchema(BaseModel):
    heating_type: Optional[HeatingTypeEnum] = None
    air_conditioning: Optional[bool] = None
    has_elevator: Optional[bool] = None
    has_terrace: Optional[bool] = None
    private_parking: Optional[bool] = False
    basement: Optional[bool] = None
    pets_allowed: Optional[bool] = None
    ownership_type: OwnershipTypeEnum
    smoking_allowed: Optional[bool] = None

class FeaturesSchema(BaseModel):
    interior: Optional[InteriorSchema] = None
    additional_info: Optional[AdditionalInfoSchema] = None