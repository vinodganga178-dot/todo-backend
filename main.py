from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tasks = []

# GET all tasks
@app.get("/tasks")
def get_tasks():
    return tasks

# ADD task
@app.post("/tasks/{username}/{text}")
def add_task(username: str, text: str):

    task = {
        "id": len(tasks) + 1,
        "text": text,
        "done": False,
        "user": username
    }

    tasks.append(task)

    return {"message": "Task added"}

# DELETE task
@app.delete("/tasks/{id}")
def delete_task(id: int):

    global tasks

    tasks = [task for task in tasks if task["id"] != id]

    return {"message": "Task deleted"}

# TOGGLE DONE
@app.put("/tasks/{id}")
def update_task(id: int):

    for task in tasks:

        if task["id"] == id:
            task["done"] = not task["done"]

    return {"message": "Task updated"}