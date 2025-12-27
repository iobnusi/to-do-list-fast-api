from uuid import UUID


class TodoNotFoundError(Exception):
    """Raised when a todo item is not found"""

    def __init__(self, todo_id: UUID):
        self.todo_id = todo_id
        self.message = f"Todo with id {todo_id} not found"
        super().__init__(self.message)
