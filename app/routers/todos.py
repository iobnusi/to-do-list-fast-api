from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends

from app.dependencies import get_todo_service
from app.models.todo import TodoCreate, TodoResponse, TodoUpdate
from app.services.todos import TodoService

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
)


@router.get("/", response_model=List[TodoResponse])
def get_all_todos(todo_service: TodoService = Depends(get_todo_service)):
    return todo_service.get_all_todos()


@router.get("/{todo_id}", response_model=TodoResponse)
def get_all_todos(todo_id: UUID, todo_service: TodoService = Depends(get_todo_service)):
    return todo_service.get_todo_by_id(todo_id=todo_id)


@router.post("/create", response_model=TodoResponse)
def create_todo(
    todo: TodoCreate, todo_service: TodoService = Depends(get_todo_service)
):
    return todo_service.create_todo(todo)


@router.patch("/update/{todo_id}", response_model=TodoResponse)
def update_todo(
    todo_id: UUID,
    todo: TodoUpdate,
    todo_service: TodoService = Depends(get_todo_service),
):
    return todo_service.update_todo(todo_id=todo_id, todo_data=todo)


@router.delete("/{todo_id}", response_model=bool)
def update_todo(
    todo_id: UUID,
    todo_service: TodoService = Depends(get_todo_service),
):
    return todo_service.delete_todo(todo_id=todo_id)
