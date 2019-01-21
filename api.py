from flask import Flask
from flask_restful import Resource, Api

import sqlite3

from db import sync
from settings import QUERYSET_COUNT

app = Flask(__name__)
api = Api(app)


class Wind(Resource):
    def get(self, direction):
        conn = sqlite3.connect('winds.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM winds 
                     WHERE direction = '{}'
                     ORDER BY speed DESC 
                     LIMIT {}'''.format(direction, QUERYSET_COUNT))
        return c.fetchall()


api.add_resource(Wind, '/<string:direction>')


if __name__ == '__main__':
    sync()
    app.run()
