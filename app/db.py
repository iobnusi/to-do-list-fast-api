from typing import List
from app.models.todo import TodoBase


class InMemoryDb:
    def __init__(self):
        self.todos: List[TodoBase] = []


db = InMemoryDb()
