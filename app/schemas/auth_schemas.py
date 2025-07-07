from pydantic import BaseModel, field_validator, EmailStr
from typing import Optional
from app.enums.roles import RoleEnum
from fastapi.exceptions import HTTPException

ALLOWED_ROLES = [RoleEnum.AGENT, RoleEnum.CLIENT, RoleEnum.INVESTOR]

class RegisterUserRequest(BaseModel):

    first_name: str 
    last_name: str
    email: EmailStr 
    password: str
    role: RoleEnum 


    @field_validator("role")
    def validate_role(cls, v):
        if v not in ALLOWED_ROLES:
            return HTTPException(status_code=422, detail=f"Role {v} is not allowed.")
        return v