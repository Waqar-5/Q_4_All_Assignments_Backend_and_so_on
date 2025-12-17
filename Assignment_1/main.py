# ================================
# Todo List API using FastAPI
# Assignment for Class 10
# Author: Waqar Ali (Student)
# ================================

"""
PROJECT OVERVIEW
----------------
This project is a complete Todo List REST API built using:
- FastAPI (for API framework)
- Pydantic (for data validation)

FEATURES
--------
✔ Create a new Todo
✔ Read all Todos
✔ Read a single Todo by ID
✔ Update a Todo
✔ Delete a Todo
✔ Uses proper HTTP methods (CRUD)
✔ Uses Pydantic models
✔ Beginner-friendly & well-commented
"""

# ----------------
# IMPORTS
# ----------------
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

# ----------------
# APP INITIALIZATION
# ----------------
app = FastAPI(
    title="Todo List API",
    description="CRUD Operations API using FastAPI",
    version="1.0.0"
)

# ----------------
# Pydantic MODELS
# ----------------

class TodoBase(BaseModel):
    title: str = Field(..., example="Learn FastAPI")
    description: str = Field(..., example="Study CRUD operations")
    completed: bool = Field(default=False)

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    pass

class Todo(TodoBase):
    id: int

# ----------------
# IN-MEMORY DATABASE
# ----------------

todos: List[Todo] = []

# ----------------
# ROOT ENDPOINT
# ----------------

@app.get("/")
def home():
    return {"message": "Todo List API is running"}

# ----------------
# CREATE TODO (POST)
# ----------------

@app.post("/todos", response_model=Todo)
def create_todo(todo: TodoCreate):
    todo_id = len(todos) + 1
    new_todo = Todo(id=todo_id, **todo.dict())
    todos.append(new_todo)
    return new_todo

# ----------------
# READ ALL TODOS (GET)
# ----------------

@app.get("/todos", response_model=List[Todo])
def get_all_todos():
    return todos

# ----------------
# READ SINGLE TODO (GET)
# ----------------

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# ----------------
# UPDATE TODO (PUT)
# ----------------

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoUpdate):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = Todo(id=todo_id, **updated_todo.dict())
            return todos[index]
    raise HTTPException(status_code=404, detail="Todo not found")

# ----------------
# DELETE TODO (DELETE)
# ----------------

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")

# ----------------
# HOW TO RUN
# ----------------

"""
1. Install dependencies:
   pip install fastapi uvicorn

2. Run server:
   uvicorn main:app --reload

3. Open browser:
   http://127.0.0.1:8000/docs

You will see Swagger UI to test all CRUD APIs.
"""
