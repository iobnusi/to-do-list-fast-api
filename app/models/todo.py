from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class TodoBase(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    completed: bool = False
    created_at: datetime
    updated_at: datetime
