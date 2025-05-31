#pip install fastapi uvicorn[standart]
from fastapi import FastAPI
from contextlib import asynccontextmanager

from models import TodoRead

fake_todos_db = [
    TodoRead(id=1, title='Сделать дз', description='', done=False),
    TodoRead(id=2, title='Помыть посуду', description='чисто', done=True)
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Приложение запускается')
    yield
    print('Приложение остановилось')

app = FastAPI(title='To Do list', lifespan=lifespan)

@app.get('/api/hello')
async def hello():
    return {'message': 'Fast Api работает'}

@app.get('/api/todos/',  summary='Получить все задачи')
async def get_all_todos():
    return fake_todos_db

#uvicorn main:app --reload
