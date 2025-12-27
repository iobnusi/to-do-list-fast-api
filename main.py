from typing import Union

from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from app.exceptions import TodoNotFoundError
from app.routers import todos

app = FastAPI()

app.include_router(todos.router)


@app.exception_handler(TodoNotFoundError)
async def todo_not_found_handler(request: Request, exc: TodoNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"message": f"{exc.message}"},
    )


@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(status_code=400, content={"message": str(exc)})


@app.get("/")
def read_root():
    return {"Hello": "World"}
