from fastapi import APIRouter, Depends

from app.dependencies import get_todo_service

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
)


@router.get("/")
def get_all_todos(todo_service=Depends(get_todo_service)):
    return todo_service.get_all_todos()
