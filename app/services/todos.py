from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4
import uuid

from app.db.base import AbstractedDb
from app.models.todo import TodoBase, TodoCreate, TodoResponse, TodoUpdate


class TodoService:
    def __init__(self, db: AbstractedDb):
        self.db = db

    def get_all_todos(self) -> List[TodoResponse]:
        # Returns list of TodoResponse
        return self.db.get_all()

    # def get_todo(self, todo_id: UUID) -> Optional[TodoResponse]:
    #     # Returns TodoResponse or None

    def create_todo(self, todo_data: TodoCreate) -> TodoResponse:
        # todo_data is a Pydantic model which acts as the form
        # Access fields: todo_data.title, todo_data.description
        # returns the created TodoResponse
        new_todo = self.db.create(todo_data, todo_id=uuid4())
        return new_todo

    def update_todo(
        self, todo_id: UUID, todo_data: TodoUpdate
    ) -> Optional[TodoResponse]:
        updated_todo = self.db.update(todo_data=todo_data, todo_id=todo_id)
        return updated_todo


# def delete_todo(self, todo_id: int) -> bool:
#     pass
