# To-Do List Application

A full-stack to-do list application with FastAPI backend and React frontend.

## Backend Setup

### Prerequisites
- Python 3.8+
- PostgreSQL (optional, can use SQLite)

### Installation

1. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Create database:
```bash
createdb todos_db
```

### Running the Backend

Start the FastAPI server:
```bash
fastapi dev main.py
```

The API will be available at `http://localhost:8000`

API Documentation: `http://localhost:8000/docs`

### Deactivate Environment
```bash
deactivate
```

## Frontend Setup

### Prerequisites
- Node.js 16+
- Yarn

### Installation

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
yarn
```

### Running the Frontend

Start the development server:
```bash
yarn dev
```

The frontend will be available at `http://localhost:5173`

## Running the Full Application

1. Start the backend server in one terminal:
```bash
source .venv/bin/activate
fastapi dev main.py
```

2. Start the frontend in another terminal:
```bash
cd frontend
yarn dev
```

3. Open your browser to `http://localhost:5173`

## Features

- Create new to-do items
- View all to-do items
- Mark items as complete/incomplete
- Delete to-do items
- Persistent storage with database
