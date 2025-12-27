from typing import List
from app.models.todo import TodoResponse


class InMemoryDb:
    def __init__(self):
        self.todos: List[TodoResponse] = []


db = InMemoryDb()
