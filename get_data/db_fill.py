import sqlite3
from urllib.request import urlopen
import json

def get_data():
    db = sqlite3.connect('../db.sqlite3')
    cursor = db.cursor()
    link = 'https://jsonplaceholder.typicode.com/photos'
    response = urlopen(link)
    data_json = json.loads(response.read())
    for i in data_json:
        print(i['albumId'])
        print(i['id'])
        print(i['title'])
        print(i['url'])
        print(i['thumbnailUrl'])
        print('=================')
