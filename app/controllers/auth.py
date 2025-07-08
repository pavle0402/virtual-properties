from fastapi import HTTPException
from app.utils.hash_password import hash_password
from app.schemas.auth_schemas import RegisterUserResponse
from app.data_access.auth import register_new_user
from app.models.auth import Role

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
        register_new_user(user_data, db)
    else:
        raise HTTPException(status_code=403, detail="Invalid request.")
    return RegisterUserResponse(created=True, message=message)
    