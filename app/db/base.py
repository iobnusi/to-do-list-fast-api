# database/base.py
from abc import ABC, abstractmethod
from uuid import UUID
from typing import List, Optional

from app.models.todo import TodoCreate, TodoResponse, TodoUpdate


class AbstractedDb(ABC):
    """Abstract base class for database implementations"""

    @abstractmethod
    def get_all(self) -> List[TodoResponse]:
        """Get all todos"""
        pass

    @abstractmethod
    def get_by_id(self, todo_id: UUID) -> Optional[TodoResponse]:
        """Get a single todo by ID"""
        pass

    @abstractmethod
    def create(self, todo_data: TodoCreate, todo_id: UUID) -> TodoResponse:
        """Create a new todo"""
        pass

    @abstractmethod
    def update(self, todo_data: TodoUpdate, todo_id: UUID) -> TodoResponse:
        """Update an existing todo"""
        pass

    # @abstractmethod
    # def delete(self, todo_id: UUID) -> bool:
    #     """Delete a todo"""
    #     pass
