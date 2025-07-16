from fastapi import Request, status, Depends, HTTPException
from jose import JWTError, jwt
from datetime import datetime
from app.config import settings

def get_current_user(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer"):
        raise HTTPException(status_code=401, detail="Invalid authorization header.")
    
    token = auth_header.split(" ")[1]

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid bearer token received.")
    
    #for now this is where I will be checking if token expired, TODO: move logic elsewhere
    exp = payload.get("exp")
    if exp and datetime.now().timestamp() > exp:
        raise HTTPException(status_code=401, detail="Auth token expired. Please login again.")
    
    data = {
        "user_id": payload.get("sub"),
        "role": payload.get("role"),
        "expires_at": payload.get("exp")
    }

    return data