from pydantic import BaseModel




class Task(BaseModel):
    title: str
    note: str | None = None 
    etat : str

class Create_task(Task):
    pass

class taskId(Task):
    id : int