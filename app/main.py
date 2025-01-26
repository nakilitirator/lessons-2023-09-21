from fastapi import FastAPI
from app.backend.db import engine, Base
from app.models import user
from app.models import task

app = FastAPI()

app.include_router(task.router)
app.include_router(user.router)


# Создаём таблицы в базе данных
Base.metadata.create_all(bind=engine)


@app.get('/')
async def welcome():
    """Главная страница"""
    return {"message": "Welcome to Taskmanager"}




