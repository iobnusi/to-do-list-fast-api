from datetime import datetime, timedelta
from typing import Optional
from fastapi import HTTPException, status
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

# Configuration
SECRET_KEY = "your-secret-key-here-change-this-in-production"  # Change this!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10


# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against a hash"""
    return pwd_context.verify(plain_password[:72].encode("utf-8"), hashed_password)


def get_password_hash(password: str) -> str:
    """Hash a password"""
    return pwd_context.hash(password[:72].encode("utf-8"))


def create_access_token(name: str, user_id: str, expire_delta: Optional[timedelta]):
    token_data = {"sub": name, "id": user_id}

    if expire_delta is None:
        expiration = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    else:
        expiration = datetime.now() + expire_delta

    token_data.update({"exp": expiration})

    return jwt.encode(token_data, SECRET_KEY, ALGORITHM)


def verify_access_token(access_token: str) -> str:
    try:
        # Decode the token
        payload = jwt.decode(access_token, SECRET_KEY, algorithms=ALGORITHM)

        user_id = payload["id"]

        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User ID not found",
            )

        return user_id

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token",
        )
