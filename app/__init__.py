from app.api.endpoints.auth import auth_router
from app.api.endpoints.real_estate import re_router
from fastapi import APIRouter

router = APIRouter()

api_prefix = "/re_api"

router.include_router(auth_router, prefix=api_prefix + "/auth")
router.include_router(re_router, prefix=api_prefix + "/real_estate")