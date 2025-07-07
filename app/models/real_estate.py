from sqlalchemy import Column, ForeignKey, DateTime, Enum
from datetime import datetime
from sqlalchemy.types import (
    Integer,
    String,
    DateTime,
    Numeric,
    Boolean,
    Float,
)
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import relationship
from ..db.db_config import Base
from app.enums.apartment_enums import (
                                CurrencyEnum,
                                ListingTypeEnum,
                                ConditionEnum,
                                HeatingTypeEnum,
                                OwnershipTypeEnum
                                )


class Apartment(Base):
    __tablename__ = "apartment"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(150), nullable=False)
    description = Column(String(1500), nullable=False)
    price = Column(Integer, nullable=False)
    currency = Column(
        Enum(CurrencyEnum, name='currency_enum', native_enum=False),
        nullable=False
        )
    listing_type = Column(
        Enum(ListingTypeEnum, name='listing_type_enum', native_enum=False),
        nullable=False
    )
    #location info
    address = Column(String(150))
    city = Column(String(150), nullable=False)
    muncipality = Column(String(150))
    postal_code = Column(String(150))
    latitude = Column(Numeric(9, 6))
    longtitude = Column(Numeric(9, 6))
    #general info
    total_area = Column(Float, nullable=False)
    total_area_measured = Column(Float)
    bedroom_count = Column(Integer, default=1)
    bathroom_count = Column(Integer, default=1)
    floor_number = Column(Integer)
    total_floors = Column(Integer)
    #state of apartment
    condition = Column(
        Enum(ConditionEnum, name='condition_enum', native_enum=False)
    )
    furnished = Column(Boolean, default=True)
    orientation = Column(
        MutableList.as_mutable(ARRAY(String)),
        nullable=False
    )
    #infrastructure
    heating_type = Column(
        Enum(HeatingTypeEnum, name="heating_type_enum", native_enum=False),
        nullable=False, default=HeatingTypeEnum.NONE
    )
    air_conditioning = Column(Boolean, default=None, nullable=False)
    has_elevator = Column(Boolean, default=None, nullable=False)
    has_terrace = Column(Boolean, default=None, nullable=True)
    private_parking = Column(Boolean, default=False, nullable=True)
    basement = Column(Boolean, default=None, nullable=True)
    #financial details
    deposit_required = Column(Boolean, nullable=False, default=True)
    utilities_included = Column(Boolean, default=False, nullable=False)
    monthly_utilities_cost = Column(Integer, nullable=True) #average
    #legal status
    ownership_type = Column(
        Enum(OwnershipTypeEnum, name="ownership_type_enum", native_enum=False),
        nullable=False, default=OwnershipTypeEnum.PRIVATE
    )
    #additional info
    pets_allowed = Column(Boolean, nullable=True)
    smoking_allowed = Column(Boolean, nullable=True)
    available_from = Column(DateTime, nullable=False)
    #status
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)
    is_rented = Column(Boolean, default=False)
    #relationships
    owner_id = Column(Integer, ForeignKey("user.id"), nullable=False)


    owner = relationship("User", back_populates="owned_apartments")
    rentals = relationship("RentalInfo", back_populates="apartment")