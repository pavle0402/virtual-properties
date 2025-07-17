from app.models.real_estate import Apartment
from fastapi import Depends, HTTPException, APIRouter
from app.utils import *
# from schemas


re_router = APIRouter()

@re_router.get("")
def get_all_apartments(user = Depends(any_authenticated)):
    pass