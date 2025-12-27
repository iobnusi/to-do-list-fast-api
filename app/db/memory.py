from datetime import datetime
from typing import List
from app.db.base import AbstractedDb
from app.models.todo import TodoResponse


class InMemoryDb(AbstractedDb):
    def __init__(self):
        self.todos: List[TodoResponse] = []

    def get_all(self):
        return self.todos

    def create(self, todo_data, todo_id) -> dict:
        """Create a new todo"""
        new_todo = TodoResponse(
            id=todo_id,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            **todo_data.model_dump()
        )
        self.todos.append(new_todo)
        return new_todo
