from fastapi import Request, Depends, HTTPException
from jose import JWTError, jwt
from datetime import datetime
from app.config import settings
from app.enums.roles import RoleEnum
from typing import Union, List


def get_current_user(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer"):
        raise HTTPException(status_code=401, detail="Invalid authorization header.")
    
    token = auth_header.split(" ")[1]

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
    except JWTError as e:
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

def require_roles(allowed_roles: Union[RoleEnum, List[RoleEnum]]):
    """
    Used to create endpoint dependency that requires one or more roles in order for endpoint to be accessed.
    
    params: allowed_roles -> single RoleEnum or list or RoleEnum(s)
    
    example usage: user = Depends(require_roles([RoleEnum.ADMIN, RoleEnum.OWNER]))
    """
    if isinstance(allowed_roles, RoleEnum):
        allowed_roles = [allowed_roles]

    def role_checker(user = Depends(get_current_user)):
        user_role = user.get("role")

        if user_role not in allowed_roles:
            role_names = [role.value for role in allowed_roles]
            raise HTTPException(
                status_code=403,
                detail={f"Insufficient permissions. Required role/s for this endpoint: {', '.join(role_names)}"}
                )
        return user
    
    return role_checker


# Pre-created convenience dependencies
admin_required = require_roles(RoleEnum.ADMIN)
owner_required = require_roles(RoleEnum.OWNER)
agent_required = require_roles(RoleEnum.AGENT)
investor_required = require_roles(RoleEnum.INVESTOR)

# Common combinations
admin_or_owner = require_roles([RoleEnum.ADMIN, RoleEnum.OWNER])
any_authenticated = require_roles([RoleEnum.ADMIN, RoleEnum.OWNER, RoleEnum.AGENT, RoleEnum.INVESTOR])
crud_real_estate = require_roles([RoleEnum.ADMIN, RoleEnum.AGENT, RoleEnum.INVESTOR, RoleEnum.OWNER])