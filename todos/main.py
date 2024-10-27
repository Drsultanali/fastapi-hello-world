from fastapi import FastAPI

app = FastAPI()
import uvicorn

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
@app.get("/gettodos")

def getTodos():
    return {"message": "Getting Todos!"}

@app.post("/addTodo")

def addTodo():
    return {"message": "Adding Todo!"}

@app.put("/updatetodo")

def updateTodo():
    return {"message": f"Updating Todo!"}

@app.delete("/deleteTodo")

def deleteTodo():

    return {"message": f"Deleting Todo!"}

def start():    
    uvicorn.run("todos.main:app", host="127.0.0.1", port=8000, reload= True) 
