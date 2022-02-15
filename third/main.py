'''
Third task of the second laboratory work of 2022 spring semester
Basically just playing with FastAPI and Twitter API
by Roman Mutel
'''

from urllib import request
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
import folium
from geopy.geocoders import Nominatim

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get('/')
async def root(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.get('/map/{twitter_username}', response_class=HTMLResponse)
async def read_item(request: Request, twitter_username: str):
    # gc = Nominatim(user_agent='02_Lab_3_Mutel')



    return templates.TemplateResponse('map.html', {'request': request, 'name': twitter_username})