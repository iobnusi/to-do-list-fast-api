from typing import Optional
from uuid import UUID
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.config import get_db
from app.models.user import UserModel
from app.services.auth import AuthService
from app.services.todos import TodoService
from app.utils.auth import oauth2_scheme, verify_access_token


def get_todo_service(db: Session = Depends(get_db)) -> TodoService:
    """Get TodoService with SQLAlchemy database"""
    return TodoService(db)


def get_auth_service(db: Session = Depends(get_db)) -> AuthService:
    """Get AuthService with SQLAlchemy database"""
    return AuthService(db)


def get_current_user(
    token: str = Depends(oauth2_scheme), auth_service=Depends(get_auth_service)
) -> Optional[UserModel]:
    """Gets the current logged in user"""
    # Get the user id by verifying access token
    user_id = verify_access_token(token)

    # Find the user by id
    user = auth_service.get_user_by_id(user_id=UUID(user_id))

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user
