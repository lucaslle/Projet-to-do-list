from fastapi import FastAPI, Request,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

class Task(BaseModel):
    title: str
    note : str
    Etat : str


Etat = ["Tranquille", 
        "OK",
        "Mid",
        "MERDE!!!!!"]


Tasks = [
    {"id": 1, "status": "En cours", "title": "Apprendre FastAPI","note" : "fyzgzfzfzgfzgfyuzgufgzugfuzgfuzgfzuf", "etat": Etat[1]},
    {"id": 2, "status": "En caca", "title": "Apprendrecaca","note" : "caca", "etat": Etat[2]}

]

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "Etat": Etat, "Tasks": Tasks})

@app.post("/add")
async def add_task(request: Request, title: str = Form(...),note: str = Form(...) ,Etat: str = Form(...)):
    new_id = len(Tasks) + 1 
    new_task = {"id": new_id, "title": title,"note": note, "etat" : Etat}
    Tasks.append(new_task)
    return templates.TemplateResponse("index.html", {"request": request, "Etat": Etat, "Tasks": Tasks})



