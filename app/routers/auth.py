from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import strategy_options
from starlette import status

from app.dependencies import get_auth_service
from app.models.user import Token, UserCreate, UserLogin
from app.services.auth import AuthService
from app.utils.auth import create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/register", response_model=bool)
def register_user(
    user_create: UserCreate, auth_service: AuthService = Depends(get_auth_service)
):
    return auth_service.create_user(user=user_create)


@router.post("/login", response_model=Token)
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(get_auth_service),
):
    user = auth_service.authenticate_user(
        name=form_data.username, password=form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            # headers={"WWW-Authenticate": "Bearer"},
        )

    # create the access token
    access_token = create_access_token(
        name=form_data.username, user_id=str(user.id), expire_delta=None
    )

    # Return in OAuth2 format that Swagger UI expects
    return {"access_token": access_token, "token_type": "bearer"}
