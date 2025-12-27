from typing import Union

from fastapi import FastAPI

from app.routers import todos

app = FastAPI()

app.include_router(todos.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
