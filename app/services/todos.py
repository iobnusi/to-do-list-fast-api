from typing import List

from app.db import db
from app.models.todo import TodoBase


class TodoService:
    def get_all_todos(self) -> List[TodoBase]:
        # Returns list of TodoResponse
        return db.todos


# def create_todo(self, todo_data: TodoCreate) -> TodoResponse:
#     # todo_data is a Pydantic model
#     # Access fields: todo_data.title, todo_data.description
#     pass


# def get_todo(self, todo_id: int) -> Optional[TodoResponse]:
#     # Returns TodoResponse or None
#     pass


# def update_todo(self, todo_id: int, todo_data: TodoUpdate) -> Optional[TodoResponse]:
#     pass


# def delete_todo(self, todo_id: int) -> bool:
#     pass

todo_service = TodoService()
