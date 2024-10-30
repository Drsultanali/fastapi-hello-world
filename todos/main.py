from fastapi import FastAPI, HTTPException
import uvicorn
from sqlmodel import  Session, select
from dotenv import load_dotenv
load_dotenv()

from .config.db import create_table, engine
from .models.todos import Todo, UpdateTodo
app = FastAPI()

@app.get('/')
def home():
    return {"message": "Welcome to FastAPI Todo API"}
@app.get("/get_todos")
def get_todos():
    with Session(engine) as session:
        statement = select(Todo)
        result = session.exec(statement)
        data = result.all()
        print (data)
        return data
# Create Todo
@app.post("/create_todo")
def create_todo(todo: Todo):
    with Session(engine) as session:
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return {"status": 200, "message": "todo created successfully"}

# Update todo
@app.put("/update_todo/{id}")
def update_todo(id: int, todo: UpdateTodo):
   with Session(engine) as session:
        db_todo = session.get(Todo, id)
        if not db_todo:
            raise HTTPException(status_code=404, detail="todo not found")
        todo_data = todo.model_dump(exclude_unset=True)
        db_todo.sqlmodel_update(todo_data)
        session.add(db_todo)
        session.commit()
        session.refresh(db_todo)
        return {"status": 200, "message": "todo updated successfully"}
@app.delete("/delete_todo/{id}")
def delete_todo(id: int):
  with Session(engine) as session:
        db_todo = session.get(Todo, id)
        if not db_todo:
            raise HTTPException(status_code=404, detail="todo not found")
        session.delete(db_todo)
        session.commit()
        return {"status": 200, "message": "todo deleted successfully"}

def start():
    create_table()
    uvicorn.run("todos.main:app", host="127.0.0.1", port=8000, reload= True) 
