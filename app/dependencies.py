from app.db.base import AbstractedDb
from app.db.memory import InMemoryDb
from app.services.todos import TodoService

# Create instance of db
db: AbstractedDb = InMemoryDb()

# Create instance of service
todo_service = TodoService(db)


def get_todo_service() -> TodoService:
    return todo_service
