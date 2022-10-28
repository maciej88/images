import sqlite3
from urllib.request import urlopen
import json

def get_data():
    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS images_app_library (id integer NOT NULL primary key, album_id integer NULL, title varchar(300) NULL, height integer NULL, width integer NULL, link varchar(100))''')
    link = 'https://jsonplaceholder.typicode.com/photos'
    response = urlopen(link)
    data_json = json.loads(response.read())
    for i in data_json:
        id = i['id']
        album_id = i['albumId']
        title = i['title']
        height = ""
        width = ""
        link = i['thumbnailUrl']
        #i['url']
        cursor.execute('INSERT OR REPLACE INTO images_app_library VALUES (?, ?, ?, ?, ?, ?)', (id, album_id, title, height, width, link))
        db.commit()
    db.close()

get_data()
