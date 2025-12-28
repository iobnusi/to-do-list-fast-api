from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends

from app.dependencies import get_current_user, get_todo_service
from app.models.todo import TodoCreate, TodoResponse, TodoUpdate
from app.models.user import UserModel
from app.services.todos import TodoService

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
)


@router.get("/", response_model=List[TodoResponse])
def get_all_todos(
    todo_service: TodoService = Depends(get_todo_service),
    current_user: UserModel = Depends(get_current_user),
):
    return todo_service.get_all_todos(user_id=current_user.id)


@router.get("/{todo_id}", response_model=TodoResponse)
def get_all_todos(
    todo_id: UUID,
    todo_service: TodoService = Depends(get_todo_service),
    current_user=Depends(get_current_user),
):
    return todo_service.get_todo_by_id(todo_id=todo_id, user_id=current_user.id)


@router.post("/create", response_model=TodoResponse)
def create_todo(
    todo: TodoCreate,
    todo_service: TodoService = Depends(get_todo_service),
    current_user=Depends(get_current_user),
):
    return todo_service.create_todo(todo, user_id=current_user.id)


@router.patch("/update/{todo_id}", response_model=TodoResponse)
def update_todo(
    todo_id: UUID,
    todo: TodoUpdate,
    todo_service: TodoService = Depends(get_todo_service),
    current_user=Depends(get_current_user),
):
    return todo_service.update_todo(
        todo_id=todo_id, todo_data=todo, user_id=current_user.id
    )


@router.delete("/{todo_id}", response_model=bool)
def update_todo(
    todo_id: UUID,
    todo_service: TodoService = Depends(get_todo_service),
    current_user=Depends(get_current_user),
):
    return todo_service.delete_todo(todo_id=todo_id, user_id=current_user.id)
