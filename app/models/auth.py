from sqlalchemy import Column, ForeignKey, DateTime, Enum
from datetime import datetime
from sqlalchemy.types import (
    Integer,
    String,
    DateTime,
    Boolean
)
from sqlalchemy.dialects.postgresql import ENUM
from app.enums.roles import RoleEnum
from sqlalchemy.orm import relationship
from ..db.db_config import Base

#*************Authentication and users*****************
class User(Base):   
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(150))
    created_at = Column(DateTime, default=datetime.now())
    role_id = Column(Integer, ForeignKey("role.id"))

    role = relationship("Role", back_populates="user")
    #real estate relationships - related to people who create real estate(owners/agencies).
    owned_apartments = relationship("Apartment", back_populates="owner")
    rentals = relationship("RentalInfo", back_populates="user")

    @property
    def is_admin(self):
        return self.role.role_type == RoleEnum.ADMIN
    
class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, autoincrement=True)
    role_type = Column(
        Enum(RoleEnum, name="role_enum", native_enum=False),
        nullable=False
    )
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.now())
    
    user = relationship("User", back_populates="role")


class RentalInfo(Base):
    __tablename__ = "rental_info"


    #This object can be added after signing a contract
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey("user.id"), nullable=False)
    apartment_id = Column(ForeignKey("apartment.id"), nullable=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=True)
    active = Column(Boolean, nullable=False)
    deposit_amount = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now())

    user = relationship("User", back_populates="rentals")
    apartment = relationship("Apartment", back_populates="rentals") 

    @property
    def rent_monthly_price(self):
        return self.apartment.price