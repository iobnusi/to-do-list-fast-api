from datetime import datetime
from typing import List

from sqlalchemy.orm.session import Session
from app.db.base import AbstractedDb
from app.exceptions import TodoNotFoundError
from app.models.todo import TodoResponse, TodoModel, TodoUpdate


class SQLAlchemyDb(AbstractedDb):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        todos = self.session.query(TodoModel).all()
        return [self._to_response(todo) for todo in todos]

    def get_by_id(self, todo_id):
        """Get an existing todo by id"""
        todo = self.session.query(TodoModel).filter_by(id=todo_id)
        if not todo:
            raise TodoNotFoundError(todo_id)
        return self._to_response(todo)

    def create(self, todo_data, todo_id):
        """Create a new todo"""
        new_todo = TodoModel(
            id=todo_id,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            **todo_data.model_dump(),
        )
        self.session.add(new_todo)
        self.session.commit()
        self.session.refresh(new_todo)
        return self._to_response(new_todo)

    def update(self, todo_data, todo_id):
        """Update an existing todo"""
        existing_todo = self.session.query(TodoModel).filter_by(id=todo_id)
        if not existing_todo:
            raise TodoNotFoundError(todo_id)

        for key, value in todo_data.model_dump(exclude_unset=True):
            setattr(existing_todo, key, value)

        self.session.commit()
        self.session.refresh(existing_todo)
        return self._to_response(existing_todo)

    def delete(self, todo_id) -> bool:
        """Delete a todo"""
        existing_todo = self.session.query(TodoModel).filter_by(id=todo_id)
        if not existing_todo:
            raise TodoNotFoundError(todo_id)

        self.session.delete(existing_todo)
        self.session.commit()
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
