from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
import uuid
from sqlalchemy.dialects.postgresql import UUID as UUIDPSG
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import Column
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Boolean, DateTime, String

from app.db.config import Base


class UserBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr = Field(max_length=50)


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[EmailStr] = mapped_column(String(50), nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())
