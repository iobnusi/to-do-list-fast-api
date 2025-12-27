from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.config import get_db
from app.services.todos import TodoService


def get_todo_service(db: Session = Depends(get_db)) -> TodoService:
    """Get TodoService with SQLAlchemy database"""
    return TodoService(db)
