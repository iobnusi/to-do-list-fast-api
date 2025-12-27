from dotenv import load_dotenv

load_dotenv()

from contextlib import asynccontextmanager

from app.db.config import Base, engine

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from app.exceptions import TodoNotFoundError
from app.routers import todos


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan events for the application.
    Code before yield runs on startup.
    Code after yield runs on shutdown.
    """
    # Startup
    print("Starting up...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully")

    yield  # App runs here

    # Shutdown
    print("Shutting down...")
    engine.dispose()
    print("Database connections closed")


# Create FastAPI app with lifespan
app = FastAPI(lifespan=lifespan)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    return {"Server": "Running"}
