from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from shema import Create_task, taskId 


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/add")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "Tasks": Tasks})

@app.post("/add")
async def add_task(task_data : Create_task) -> taskId:
    id = Tasks[-1]['id'] + 1
    task = taskId(id = id , **task_data.model_dump()).model_dump()
    Tasks.append(task)
    print(Tasks)
    return task

Tasks = [
    {"id": 1, "title": "to do","note" : "marche zby j'en ai marre", "etat": "arrete"},
    {"id": 2, "title": "Apprendre FastAPI","note" : "gekgege", "etat": "arrete"},
    {"id": 3, "title": "Apprendre FastAPI","note" : "gekgege", "etat": "stop"},
    {"id": 4, "title": "Apprendre FastAPI","note" : "gekgege", "etat": "stop"},
    {"id": 5, "title": "Apprendre FastAPI","note" : "gekgege", "etat": "stop"},
    {"id": 6, "title": "Apprendre FastAPI","note" : "gekgege", "etat": "stop"},
    {"id": 7, "title": "Apprendre FastAPI","note" : "gekgege", "etat": "stop"},
    {"id": 8, "title": "Apprendre FastAPI","note" : "gekgege", "etat": "stop"},
    {"id": 9, "title": "Apprendre FastAPI","note" : "gekgege", "etat": "stop"},
    {"id": 10, "title": "Apprendre FastAPI","note" : "gekgege", "etat": "stop"}
]