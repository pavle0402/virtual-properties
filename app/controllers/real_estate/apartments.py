from fastapi import HTTPException
from app.data_access import apartment_dao
from pydantic.type_adapter import TypeAdapter

class ApartmentService:
    @staticmethod
    def get_all(db, request):
        filters = request.filters
        return apartment_dao.get_all(db, filters)

    @staticmethod
    def get_by_id(db, request):
        apartment_id = request.apartment_id
        return apartment_dao.get_by_id(db, apartment_id)