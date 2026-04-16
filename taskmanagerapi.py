from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Storage
tasks = []

# Data model
class Task(BaseModel):
    title: str

# 🔹 ADD TASK
@app.post("/tasks")
def add_task(task: Task):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "completed": False
    }
    tasks.append(new_task)
    
    return {
        "message": "Task added",
        "task": new_task
    }

# 🔹 GET ALL TASKS
@app.get("/tasks")
def get_tasks():
    return {
        "tasks": tasks
    }

# 🔹 UPDATE TASK (mark complete)
@app.put("/tasks/{task_id}")
def update_task(task_id: int):
    for t in tasks:
        if t["id"] == task_id:
            t["completed"] = True
            return {
                "message": "Task updated",
                "task": t
            }
    
    return {"error": "Task not found"}

# 🔹 DELETE TASK
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i in range(len(tasks)):
        if tasks[i]["id"] == task_id:
            deleted = tasks.pop(i)
            return {
                "message": "Task deleted",
                "task": deleted
            }
    
    return {"error": "Task not found"}