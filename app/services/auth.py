from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.models.user import UserCreate, UserModel
from app.utils.auth import get_password_hash, verify_access_token, verify_password


class AuthService:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_name(self, name: str) -> Optional[UserModel]:
        """Get user by name"""
        return self.db.query(UserModel).filter(UserModel.name == name).first()

    def get_user_by_id(self, user_id: UUID) -> Optional[UserModel]:
        """Get user by ID"""
        return self.db.query(UserModel).filter(UserModel.id == user_id).first()

    def create_user(self, user: UserCreate) -> UserModel:
        """Create a new user"""
        if self.get_user_by_name(user.name):
            raise ValueError("Name already registered")

        # hash the request password
        hashed_password = get_password_hash(user.password)

        new_user = UserModel(
            id=uuid4(),
            created_at=datetime.now(),
            name=user.name,
            hashed_password=hashed_password,
        )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def authenticate_user(self, name: str, password: str) -> Optional[UserModel]:
        "Authenticate user"
        user = self.get_user_by_name(name)

        if not user:
            return None

        if verify_password(
            plain_password=password, hashed_password=user.hashed_password
        ):
            return user

        return None
