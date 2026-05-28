from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import SessionLocal, engine
from models import Task, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Home route
@app.get("/")
def home():
    return {"message": "Backend Running 🚀"}

# Get all tasks
@app.get("/tasks")
def get_tasks():
    db = SessionLocal()

    tasks = db.query(Task).all()

    return tasks

# Create task
@app.post("/tasks/{text}")
def add_task(text: str):
    task = {
        "id": len(tasks) + 1,
        "text": text
    }

    tasks.append(task)

    return {"message": "Task added"}