from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()
todos = {
    "task1": "Shower",
    "task2": "Eat Dinner",
    "task3": "Grocery Shopping"

}
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
# get all the todos
@app.get("/get_todos")

def getTodos():
    return {"todos": todos}

# Data model for adding todos

class TodoItem(BaseModel):
    task: str
    message: str
@app.post("/add_todo")

def add_todo(item: TodoItem):
    if item.task in todos:
        return {"Error": "Task already exists"}
    todos[item.task] = item.message
    return { "message": f"Added {item.task} to ", "todos":todos}


@app.put("/update_todo/{task}")

def updateTodo(task:str, message:str):
    if task not in todos:
        return {"Error": "Task not found"}
    todos[task] = message
    return { "message": f"Updated {task} to {message}", "todos": todos}

@app.delete("/delet_todo/{task}")

def deleteTodo(task:str, message:str):
    if task not in todos:
        return {"Error": "Task not found"}
    del todos[task]
    return { "message": f"Deleted {task}", "todos": todos}

def start():    
    uvicorn.run("todos.main:app", host="127.0.0.1", port=8000, reload= True) 
