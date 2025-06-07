#pip install fastapi uvicorn[standart]
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager

from models import TodoRead

fake_todos_db = [
    TodoRead(id=1, title='Сделать дз', description='', done=True),
    TodoRead(id=2, title='Помыть посуду', description='чисто', done=False)
]

next_todo_id = len(fake_todos_db) + 1

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Приложение запускается')
    yield
    print('Приложение остановилось')

app = FastAPI(title='To Do list', lifespan=lifespan)
app.mount('/static', StaticFiles(directory='static'), name='static_files')

@app.get('/api/hello')
async def hello():
    return {'message': 'Fast Api работает'}

@app.get('/api/todos/',  summary='Получить все задачи')
async def get_all_todos():
    return fake_todos_db

@app.post('/api/todos/', response_model=TodoRead)
async def create_new_todo(todo_data: TodoRead):
    global next_todo_id
    new_todo = TodoRead (
        id = next_todo_id ,
        title = todo_data.title ,
        description = todo_data.description ,
        done = False )
    
    fake_todos_db.append(new_todo) 
    next_todo_id += 1
    return new_todo

@app.get('/', response_class=HTMLResponse)
async def serve_index_html():
    html_data = open('static/index.html', encoding='utf-8')
    return HTMLResponse(content=html_data.read(), status_code=200)

#uvicorn main:app --reload