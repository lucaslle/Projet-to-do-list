from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from shema import Create_task, taskId 


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

Tasks = [
    {"id": 1, "title": "to do","note" : "marche zby j'en ai marre", "etat": "arrete"}
    
]


@app.get("/add")
async def read_root(request: Request):
    print(Tasks)
    return templates.TemplateResponse("index.html", {"request": request, "Tasks": Tasks})

@app.post("/add")
async def add_task(task_data : Create_task) -> taskId:
    id = Tasks[-1]['id'] + 1
    task = taskId(id = id , **task_data.model_dump()).model_dump()
    Tasks.append(task)
    print(Tasks)
    return task

@app.delete("/delete/{task_id}")
async def delete_task(task_id: int):
    for index, task in enumerate(Tasks):
        if task['id'] == task_id:
            deleted_task = Tasks.pop(index)
            print(Tasks)
            return {"message": "Task deleted", "task": deleted_task, "Tasks":Tasks }


@app.put("/update/{task_id}")
async def update_task(task_id: int, updated_data: Create_task):
    for index, task in enumerate(Tasks):
        if task['id'] == task_id:
            Tasks[index]['title'] = updated_data.title
            Tasks[index]['note'] = updated_data.note
            Tasks[index]['etat'] = updated_data.etat
            print(Tasks)
            return {"message": "Task updated", "task": Tasks[index]}