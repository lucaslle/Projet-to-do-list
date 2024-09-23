from fastapi import FastAPI, Request
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Task(Base):
	__tablename__ = "tasks"
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, index=True)
	description = Column(String, index=True)
	
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
Base.metadata.create_all(bind=engine)



############################################## ADD ########################################
 
@app.post("/tasks/")
async def create_item(name: str, description: str):
	db = SessionLocal()
	db_task = Task(name=name, description=description)
	db.add(db_task)
	db.commit()
	db.refresh(db_task)
	return db_task



@app.get("/tasks/{task_id}")
async def read_item(task_id: int):
	db = SessionLocal()
	task = db.query(Task).filter(Task.id == task_id).first()
	return task


####################################### UPDATE #############################################
@app.put("/tasks/{task_id}")
async def update_item(task_id: int, name: str, description: str):
	db = SessionLocal()
	db_task = db.query(Task).filter(Task.id == task_id).first()
	db_task.name = name
	db_task.description = description
	db.commit()
	return db_task


######################################### DELETE ############################################
@app.delete("/tasks/{task_id}")
async def delete_item(task_id: int):
	db = SessionLocal()
	db_task = db.query(Task).filter(Task.id == task_id).first()
	db.delete(db_task)
	db.commit()
	return {"message": "Task deleted successfully"}

