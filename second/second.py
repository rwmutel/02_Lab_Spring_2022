"""
02_2 lab task by Roman Mutel
A simple console application, that let's the user explore .json file
"""

from base64 import encode
from email import header
import json
from textwrap import indent
import requests


def get_friendlist(username):
    BEARER = 'AAAAAAAAAAAAAAAAAAAAAGXFZAEAAAAAFI2aTvd7hEHnawFvGivv4dM6G%2BI%3D27XV4r54LYViuhiI1aa83cacNI2OjLbyWbN5Rn8LP1my82FrPt'
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
        'max_results': 200,
        'user.fields': 'name,username,location'
    }
    search_url = f'{BASE_URL}2/users/{user_id}/following'
    response = requests.get(search_url, search_params, headers=search_headers)
    with open('second/friends.json', 'w', encoding='utf-8') as output:
        json.dump(response.json(), output, indent=4, ensure_ascii=False)

    return response.status_code

def main():
    '''
    Main cycle
    '''

    print()
    print('The default file is the data about 26 twitter friends of',\
        'modern Ukrainian poet and writer Serhiy Zhadan.')
    print('If you want to enter another file, place it in the folder and write its name with ".json"')
    print('If you want to stop, press Enter without entering text')
    print()

    key = '-'
    src = open('second/friends.json', 'r', encoding='utf-8')
    data = json.load(src)
    history = [data]

    while key != '':
        print(f'Current level type: {type(data)}')

        if isinstance(data, dict):
            print('Available keys:')
            for data_key in data.keys(): print(data_key)
            print()
            key = input('Enter key, .json file name or ".." to go up: ')
            if key.endswith('.json'):
                src.close()
                src = open(key, encoding='utf-8')
                data = json.load(src)
                history = [data]
            elif key != '..' and key != '':
                history.append(data)
                data = data[key]

        elif isinstance(data, list):
            print(f'Length: {len(data)}')
            print()
            key = input('Enter index, .json file name or ".." to go up: ')
            if key.endswith('.json'):
                src.close()
                src = open(key, encoding='utf-8')
                data = json.load(src)
                history = [data]
            elif key != '..' and key != '':
                history.append(data)
                data = data[int(key)]

        else:
            print(data)
            print("You've reached end!")
            key = input("Enter '..' to go up, .json file name or press enter empty line to exit: ")
            if key.endswith('.json'):
                src.close()
                src = open(key, encoding='utf-8')
                data = json.load(src)
                history = [data]

        if key == '..':
            data = history.pop()

    print()
    print('Bye!', 'Stopping...', sep='\n')



if __name__ == '__main__':
    get_friendlist('serhiy_zhadan')
    main()
