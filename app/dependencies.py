from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.base import AbstractedDb
from app.db.config import get_db
from app.db.memory import InMemoryDb
from app.db.sql_alchemy import SQLAlchemyDb
from app.services.todos import TodoService

# Option 1: Use InMemoryDb (current)
# db: AbstractedDb = InMemoryDb()
# todo_service = TodoService(db)
#
# def get_todo_service() -> TodoService:
#     return todo_service


# Option 2: Use SQLAlchemy Database (new)
def get_todo_service(db: Session = Depends(get_db)) -> TodoService:
    """Get TodoService with SQLAlchemy database"""
    sqlalchemy_db = SQLAlchemyDb(db)
    return TodoService(sqlalchemy_db)
