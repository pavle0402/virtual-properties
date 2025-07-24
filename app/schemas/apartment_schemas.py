from pydantic import BaseModel, Field, conlist, ConfigDict
from typing import Optional, List
from datetime import datetime
from . import FinancialInfoSchema, LocationSchema, FeaturesSchema


class ApartmentSchemaResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True, from_attributes=True)

    title: str
    description: str
    apartment_featuers: FeaturesSchema
    available_from: datetime
    financial_info: FinancialInfoSchema
    location: LocationSchema
    filters: Optional[dict] = None

class ApartmentSchemaRequest(BaseModel):
    filters: Optional[dict] = None
    apartment_id: Optional[int] = None
