from fastapi import APIRouter, Depends

from app.dependencies import get_todo_service
from app.models.todo import TodoCreate, TodoResponse
from app.services.todos import TodoService

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
)


@router.get("/")
def get_all_todos(todo_service: TodoService = Depends(get_todo_service)):
    return todo_service.get_all_todos()


@router.post("/create", response_model=TodoResponse)
def create_todo(
    todo: TodoCreate, todo_service: TodoService = Depends(get_todo_service)
):
    return todo_service.create_todo(todo)
