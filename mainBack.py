from fastapi import FastAPI
from shema import Task , Create_task, taskId 

app = FastAPI()

Tasks = [
    {"id": 1, "title" : "jsp", "etat" : "ok"} 
]

@app.get("/")
async def root():
    return {"task": f"{Tasks}"}

################################## ADD #########################################

@app.get("/add")
async def task():
    return {"task": f"{Tasks}"}


@app.post("/add")
async def add_task(task_data : Create_task) -> taskId:
    id = Tasks[-1]['id'] + 1
    task = taskId(id = id , **task_data.model_dump()).model_dump()
    Tasks.append(task)
    print(Tasks)
    return task

################################# DELETE #########################################

# @app.delete("/delete/{task_id}")
# async def Delete_task(task_id : int ,task_data : Create_task) -> taskId:
    
  
