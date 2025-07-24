from app.api.endpoints.auth import auth_router
from app.api.endpoints.real_estate.apartments import ap_router
from fastapi import APIRouter

router = APIRouter()

api_prefix = "/re_api"

router.include_router(auth_router, prefix=api_prefix + "/auth")
router.include_router(ap_router, prefix=api_prefix + "/apartments")