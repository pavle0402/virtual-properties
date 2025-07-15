from fastapi import HTTPException
from fastapi.responses import JSONResponse
from app.utils.hash_password import hash_password, verify_password
from app.schemas.auth_schemas import RegisterUserResponse
from app.data_access.auth import register_new_user_dao, login_dao
from app.models.auth import Role
from app.utils.jwt import JWTAuthManager
from app.config import settings

def register_controller(request, db) -> bool:
    if request:

        role_obj = db.query(Role).filter(Role.role_type == request.role).first()
        password = hash_password(request.password)
        first_name = request.first_name
        message = f"Welcome {first_name}. We are happy to have you onoboard."
        user_data = {
            "first_name":request.first_name,
            "last_name":request.last_name,
            "password":password,
            "email":request.email,
            "role_id":role_obj.id
        }
        register_new_user_dao(user_data, db)
    else:
        raise HTTPException(status_code=403, detail="Invalid request.")
    return RegisterUserResponse(created=True, message=message)
    
def login_controller(request, db):
    email = request.get("email")
    username = request.get("username")

    user = login_dao(email, username, db)
    if not user or not verify_password(request.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials, please check your spelling.")     
    user_data = {
        "sub": str(user.id),
        "role": user.role.role_type
        }
    
    access_token = JWTAuthManager.create_access_token(user_data)
    refresh_token = JWTAuthManager.create_refresh_token(user_data)
    response = JSONResponse(
        content={
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "Bearer",
        }
    )

    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=60 * 60 * 24 * 7  #this is related to when the browser will delete the cookie, not lifetime of token
    )

    return response