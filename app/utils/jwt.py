from datetime import timedelta, datetime
from jose import JWTError, jwt
from app.config import settings
from typing import Optional

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_LIFETIME = settings.ACCESS_TOKEN_LIFETIME
REFRESH_TOKEN_LIFETIME = settings.REFRESH_TOKEN_LIFETIME
REFRESH_SECRET_KEY = settings.REFRESH_SECRET_KEY

class JWTAuthManager:
    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None);
        to_encode = data.copy()
        expire = datetime.now() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_LIFETIME))
        to_encode.update({"exp":expire})
        try:
            jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        except JWTError as e:
            raise Exception("Failed to encode JWT token!") from e
        
    @staticmethod
    def create_refresh_token(data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        expire = datetime.now() + (expires_delta or timedelta(days=REFRESH_TOKEN_LIFETIME))
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, REFRESH_SECRET_KEY, algorithm=ALGORITHM)
        
    @staticmethod
    def verify_token(token: str, is_refresh: bool = False):
        key = REFRESH_SECRET_KEY if is_refresh else SECRET_KEY
        try:
            payload = jwt.decode(token, key, algorithm=ALGORITHM)
            return payload
        except JWTError as e:
            raise Exception("Failed to decode JWT token") from e