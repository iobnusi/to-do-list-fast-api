from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
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
