from app.models.real_estate import Apartment
from fastapi_pagination.ext.sqlalchemy import paginate

class ApartmentDAOService:
    @staticmethod
    def get_all(db, filters):
        query = db.query(Apartment)
        if filters:
            #k-key, v-value
            for k, v in filters.items():
                if hasattr(Apartment, k):
                    query = query.filter(getattr(Apartment, k) == v)
        return paginate(query)

    @staticmethod
    def get_by_id(db, apartment_id):
        pass