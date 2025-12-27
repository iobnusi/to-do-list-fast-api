from datetime import datetime
from typing import List
from app.db.base import AbstractedDb
from app.exceptions import TodoNotFoundError
from app.models.todo import TodoResponse, TodoUpdate


class InMemoryDb(AbstractedDb):
    def __init__(self):
        self.todos: List[TodoResponse] = []

    def get_all(self):
        return self.todos

    def get_by_id(self, todo_id):
        """Get an existing todo by id"""
        for i, todo in enumerate(self.todos):
            if todo.id == todo_id:
                return todo

        raise TodoNotFoundError(todo_id)

    def create(self, todo_data, todo_id):
        """Create a new todo"""
        new_todo = TodoResponse(
            id=todo_id,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            **todo_data.model_dump(),
        )
        self.todos.append(new_todo)
        return new_todo

    def update(self, todo_data, todo_id):
        """Update an existing todo"""
        for i, todo in enumerate(self.todos):
            if todo.id == todo_id:
                update_data = todo_data.model_dump(exclude_unset=True)

                new_data = TodoResponse(
                    id=todo_id,
                    created_at=todo.created_at,
                    updated_at=datetime.now(),
                    completed=update_data.get("completed", todo.completed),
                    title=update_data.get("title", todo.title),
                    description=update_data.get("description", todo.description),
                )
                self.todos[i] = new_data

                return new_data

        raise TodoNotFoundError(todo_id)

    def delete(self, todo_id) -> bool:
        """Delete a todo"""
        for i, todo in enumerate(self.todos):
            if todo.id == todo_id:
                self.todos.pop(i)
                return True

        raise TodoNotFoundError(todo_id)
