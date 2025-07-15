from fastapi import APIRouter, Depends, Response
from app.schemas.auth_schemas import (
                                    RegisterUserRequest,
                                    RegisterUserResponse,
                                    LoginUserRequest,
                                    LoginResponse
                                    )
from app.controllers.auth import register_controller, login_controller
from app.db.db_config import get_db

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