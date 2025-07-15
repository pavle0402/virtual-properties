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


    @field_validator("role")
    def validate_role(cls, v):
        if v not in ALLOWED_ROLES:
            return HTTPException(status_code=422, detail=f"Role {v} is not allowed.")
        return v

class RegisterUserResponse(BaseModel):
    created: bool
    message: str

class LoginUserRequest(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None 
    password: str

    @model_validator
    def validate_username_email(values):
        email = values.get("email")
        username = values.get("username")
        
        if not username and not email:
            raise HTTPException(status_code=422, detail=f"Role {v} is not allowed.")