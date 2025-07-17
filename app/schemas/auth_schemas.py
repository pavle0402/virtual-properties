from pydantic import BaseModel, field_validator, EmailStr, model_validator
from typing import Optional
from app.enums.roles import RoleEnum
from fastapi.exceptions import HTTPException

ALLOWED_ROLES = [RoleEnum.AGENT, RoleEnum.CLIENT, RoleEnum.INVESTOR, RoleEnum.OWNER]

class RegisterUserRequest(BaseModel):

    first_name: str 
    last_name: str
    email: EmailStr 
    password: str
    role: RoleEnum


    #created so regular users can't create ADMIN users. -> For that there will be special endpoint accessed only by admins.
    @field_validator("role")
    def validate_role(cls, v):
        if v not in ALLOWED_ROLES:
            return HTTPException(status_code=422, detail=f"Role {v} is not allowed.")
        return v

class RegisterUserResponse(BaseModel):
    created: bool
    message: str

class LoginUserRequest(BaseModel):
    email: EmailStr 
    password: str