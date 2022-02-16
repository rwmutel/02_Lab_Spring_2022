'''
Third task of the second laboratory work of 2022 spring semester
Basically just playing with FastAPI and Twitter API
by Roman Mutel
'''

import requests
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
import folium
import json
from geopy.geocoders import Nominatim
from bearer import BEARER

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get('/')
async def root(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


def get_friendlist(username: str):
    """
    Returns a list of Twitter user followings (first 100)

    Args:
        username (str): user's name on Twitter

    Returns:
        list: list of user friends (as objects with location, id, name and username)
    """

    BASE_URL = 'https://api.twitter.com/'
    search_headers = {
        'Authorization': f'Bearer {BEARER}'
    }
    search_params = {
        'usernames': username,
        'user.fields': 'id,name,username,location,description'
    }
    search_url = f'{BASE_URL}2/users/by'
    response = requests.get(search_url, headers=search_headers, params=search_params)
    user_id = response.json()['data'][0]['id']

    search_params = {
        'max_results': 100,
        'user.fields': 'name,username,location'
    }
    search_url = f'{BASE_URL}2/users/{user_id}/following'
    response = requests.get(search_url, search_params, headers=search_headers)

    return response.json()['data']


@app.get('/map/folium_friends_map.html', response_class=HTMLResponse)
async def return_map(request: Request):
    return templates.TemplateResponse('folium_friends_map.html', {'request': request})


@app.get('/map/{username}', response_class=HTMLResponse)
async def read_item(request: Request, username: str):
    friends = get_friendlist(username)
    # friends = json.load(open('friends.json', 'r', encoding='utf-8'))['data']
    gc = Nominatim(user_agent='02_Lab_3_Mutel')
    friends_map = folium.Map(location=(49.4871968, 31.2718321), zoom_start=3)
    mapped_locations = {}

    for friend in friends:
        if 'location' not in friend.keys():
            continue
        location = friend['location']
        coordinates = gc.geocode(location)
        if coordinates == None:
            continue
        if (coordinates.latitude, coordinates.longitude) not in mapped_locations:
            mapped_locations[(coordinates.latitude,coordinates.longitude)] = (location, [f'{friend["name"]} (@{friend["username"]})'])
        else:
            mapped_locations[(coordinates.latitude,coordinates.longitude)][1].append(f'{friend["name"]} (@{friend["username"]})')

    # print(mapped_locations)
    for coordinate in mapped_locations:
        friends_map.add_child(folium.Marker(location=coordinate, popup=
        f'<b>{mapped_locations[coordinate][0]}</b><hr>' + '<br><br>'.join(mapped_locations[coordinate][1])))

    friends_map.save('templates/folium_friends_map.html')

    return templates.TemplateResponse('map.html', {'request': request, 'name': username, 'friends': friends})
