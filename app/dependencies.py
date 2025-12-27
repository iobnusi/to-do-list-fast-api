from app.services.todos import TodoService

# Create instance of service
todo_service = TodoService()


def get_todo_service() -> TodoService:
    return todo_service
