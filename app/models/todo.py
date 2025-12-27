from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field


class TodoBase(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    completed: bool = False


class TodoResponse(TodoBase):
    id: UUID
    created_at: datetime
    updated_at: datetime


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
