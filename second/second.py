"""
02_2 lab task by Roman Mutel
A simple console application, that let's the user explore .json file
"""

import json

from numpy import isin

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
    main()