from app.models.real_estate import Apartment
from fastapi import Depends, HTTPException, APIRouter
from app.utils import *
from app.schemas.apartment_schemas import ApartmentSchemaResponse, ApartmentSchemaRequest
from app.db.db_config import get_db
from app.controllers import apartment_cs
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate

ap_router = APIRouter()

@ap_router.post("", response_model=Page[ApartmentSchemaResponse])
def get_all_apartments(request: ApartmentSchemaRequest, db = Depends(get_db), _ = Depends(any_authenticated)):
    apartments = apartment_cs.get_all(db, request)
    return apartments

@ap_router.get("/{apartment_id}")
def get_apartment_by_id(request: ApartmentSchemaRequest, db = Depends(get_db), _ = Depends(any_authenticated)):
    return apartment_cs.get_by_id(db, request)

@ap_router.post("/create")
def create_apartment(_ = Depends(crud_real_estate)):
    pass

@ap_router.put("/edit/{apartment_id}")
def edit_apartment(apartment_id: int, db = Depends(get_db), _ = Depends(crud_real_estate)):
    pass

@ap_router.delete("/delete/{apartment_id}")
def delete_apartment(apartment_id: int, db = Depends(get_db), _ = Depends(crud_real_estate)):
    pass