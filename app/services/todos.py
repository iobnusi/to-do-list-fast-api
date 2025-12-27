from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4
import uuid

from sqlalchemy.orm import Session

from app.exceptions import TodoNotFoundError
from app.models.todo import TodoBase, TodoCreate, TodoModel, TodoResponse, TodoUpdate


class TodoService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_todos(self) -> List[TodoResponse]:
        # Returns list of TodoResponse
        todos = self.db.query(TodoModel).all()
        return [self._to_response(todo) for todo in todos]

    def get_todo_by_id(self, todo_id: UUID) -> TodoResponse:
        """Get an existing todo by id"""
        todo = self.db.query(TodoModel).filter_by(id=todo_id).first()
        if not todo:
            raise TodoNotFoundError(todo_id)
        return self._to_response(todo)

    def create_todo(self, todo_data: TodoCreate) -> TodoResponse:
        """Create a new todo"""
        new_todo = TodoModel(
            id=uuid4(),
            created_at=datetime.now(),
            updated_at=datetime.now(),
            **todo_data.model_dump(),
        )
        self.db.add(new_todo)
        self.db.commit()
        self.db.refresh(new_todo)
        return self._to_response(new_todo)

    def update_todo(
        self, todo_id: UUID, todo_data: TodoUpdate
    ) -> Optional[TodoResponse]:
        """Update an existing todo"""
        existing_todo = self.db.query(TodoModel).filter_by(id=todo_id).first()
        if not existing_todo:
            raise TodoNotFoundError(todo_id)

        for key, value in todo_data.model_dump(exclude_unset=True):
            setattr(existing_todo, key, value)

        self.db.commit()
        self.db.refresh(existing_todo)
        return self._to_response(existing_todo)

    def delete_todo(self, todo_id: UUID) -> bool:
        """Delete a todo"""
        existing_todo = self.db.query(TodoModel).filter_by(id=todo_id).first()
        if not existing_todo:
            raise TodoNotFoundError(todo_id)

        self.db.delete(existing_todo)
        self.db.commit()
        return True

    @staticmethod
    def _to_response(todo: TodoModel) -> TodoResponse:
        """Convert SQLAlchemy model to Pydantic response model"""
        return TodoResponse(
            id=todo.id,
            title=todo.title,
            description=todo.description,
            completed=todo.completed,
            created_at=todo.created_at,
            updated_at=todo.updated_at,
        )
