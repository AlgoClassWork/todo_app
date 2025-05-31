#pip install fastapi uvicorn[standart]
from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Приложение запускается')
    yield
    print('Приложение остановилось')

app = FastAPI(title='To Do list', lifespan=lifespan)

@app.get('/api/hello')
async def hello():
    return {'message': 'Fast Api работает'}

#uvicorn main:app --reload