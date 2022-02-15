'''
Third task of the second laboratory work of 2022 spring semester
Basically just playing with FastAPI and Twitter API
by Roman Mutel
'''

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get('/')
async def root():
    return {'message': 'Hello, world!'}


@app.get('/index/{name}', response_class=HTMLResponse)
async def read_item(request: Request, name: str):
    return templates.TemplateResponse('index.html', {'request': request, 'name': name})