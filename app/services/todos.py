from datetime import datetime
from typing import List
import uuid

from app.db import db
from app.models.todo import TodoBase, TodoCreate, TodoResponse


class TodoService:
    def get_all_todos(self) -> List[TodoResponse]:
        # Returns list of TodoResponse
        return db.todos

    def create_todo(self, todo_data: TodoCreate) -> TodoResponse:
        # todo_data is a Pydantic model which acts as the form
        # Access fields: todo_data.title, todo_data.description
        # returns the created TodoResponse
        new_todo = TodoResponse(
            id=uuid.uuid4(),
            title=todo_data.title,
            description=todo_data.description,
            completed=todo_data.completed,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        db.todos.append(new_todo)
        return new_todo


# def get_todo(self, todo_id: int) -> Optional[TodoResponse]:
#     # Returns TodoResponse or None
#     pass


# def update_todo(self, todo_id: int, todo_data: TodoUpdate) -> Optional[TodoResponse]:
#     pass


# def delete_todo(self, todo_id: int) -> bool:
#     pass

todo_service = TodoService()
