import os
import wget
import json
import gzip
import sqlite3

from settings import DOWNLOAD_PATH, BULK_FILE_URL
from utils import wind_direction


def insert_data(rows):
    conn = sqlite3.connect('winds.db')
    c = conn.cursor()
    c.execute('DROP TABLE winds')
    c.execute('''CREATE TABLE winds 
                 (city text, speed real, direction text)''')
    c.executemany('''INSERT INTO winds
                     VALUES (?, ?, ?)''', rows)
    conn.commit()
    conn.close()


def sync():
    if not os.path.exists(DOWNLOAD_PATH):
        os.makedirs(DOWNLOAD_PATH)

    filename = wget.download(url=BULK_FILE_URL, out=DOWNLOAD_PATH)

    rows = []
    with gzip.open(filename, 'rb') as file:
        while True:
            line = file.readline()
            if line:
                try:
                    data = json.loads(line.decode('utf-8'))

                    city = data['city']['name']
                    speed = data['wind']['speed']
                    direction = wind_direction(data['wind']['deg'])

                    rows.append((city, speed, direction))
                except json.decoder.JSONDecodeError:
                    pass
            else:
                break

    insert_data(rows)


if __name__ == '__main__':
    sync()
