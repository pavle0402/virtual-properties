from fastapi import APIRouter, Depends, Request, HTTPException
from app.schemas.auth_schemas import (
                                    RegisterUserRequest,
                                    RegisterUserResponse,
                                    LoginUserRequest
                                    )
from app.controllers.auth import register_controller, login_controller
from app.db.db_config import get_db
from app.utils import *

auth_router = APIRouter()

@auth_router.post("/register", response_model=RegisterUserResponse)
def register_user(
    request: RegisterUserRequest,
    db = Depends(get_db)
):
    return register_controller(request, db)


@auth_router.post("/login")
def login(request: LoginUserRequest,
          db = Depends(get_db)):
    return login_controller(request, db)

#test endpoint for permission
@auth_router.get("/test")
def test_endpoint(user = Depends(admin_required)):
    if not user:
        raise HTTPException(status_code=403, detail="Unauthorized access.")
    return {"message":f"Welcome admin!"}