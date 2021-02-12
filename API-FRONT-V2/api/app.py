# coding: utf-8
from flask import Flask, render_template
from flask_restx import Resource, Api, fields, reqparse
import requests, json
import pymysql
import datetime

# Config Flask App Definition
app = Flask(__name__)
api = Api(app=app, version="0.1", doc="/api", title="Mon API", description="ceci est une description de l'api de test",
          default="mon api", default_label='ceci est une api de test', validate=True)

db_host = "localhost"

db = pymysql.connect(
    host=db_host,
    user="admin",
    passwd="toor",
    db="station_meteo"
)

@api.route("/print_data")
class PrintData(Resource):
    def get(self):
        sql_query = " select id, temperature, humidity, DATE_FORMAT(date, '%Y-%m-%d %T') as date, id_sonde from data;"
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql_query)
        records = cursor.fetchall()
        return records

@api.route("/print_last_data")
class PrintLastData(Resource):
    def get(self):
        sql_query = " select id, temperature, humidity, DATE_FORMAT(date, '%Y-%m-%d %T') as date, id_sonde from data ORDER BY date DESC LIMIT 1;"
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql_query)
        lastRecord = cursor.fetchone()
        return lastRecord

@api.route("/print_10last_data")
class PrintLastData(Resource):
    def get(self):
        sql_query = " select id, temperature, humidity, DATE_FORMAT(date, '%Y-%m-%d %T') as date, id_sonde from data ORDER BY date DESC LIMIT 10;"
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql_query)
        last10Record = cursor.fetchall()
        return last10Record

@api.route("/print_listsonde") #A TEST
class PrintListSonde(Resource):
    def get(self):
        sql_query = " select id, name from sonde;"
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql_query)
        listSonde = cursor.fetchall()
        return listSonde

@api.route("/print_graph_data")
class PrintLastData(Resource):
    def get(self):
        sql_query = " select id, temperature, humidity, DATE_FORMAT(date, '%Y-%m-%d %T') as date, id_sonde from data ORDER BY date DESC LIMIT 144;"
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql_query)
        graphRecord = cursor.fetchall()
        return graphRecord, 200, {"Access-Control-Allow-Origin": "*"}



        # print("test")

@api.route("/insert_data")
class InsertData(Resource):
    def post(self):
        sql_query = "INSERT INTO data VALUES (null, %s, %s, now(), %s)"
        with db.cursor() as cursor:
            cursor.execute(sql_query, (api.payload['temperature'], api.payload['humidite'], api.payload['sonde_id']))
            db.commit()
        return 200

### DEMO with simple api function via HTTP GET in default namespace
@api.route("/api/v1/ping")
class Ping(Resource):
    @api.response(200, 'API Ping : Success')
    @api.response(400, 'API Ping: Error')
    @api.response(403, 'API Ping: Ceci n\'est pas autorisé')
    def get(self):
        """
        Test de l'API avec un simple ping
        """
        return {'response': 'pong'}, 200

    @api.response(400, 'API Ping: This is a custom 400 error code')
    def delete(self):
        """
        Test de l'API avec erreur 400
        """
        return {'response': 'bad pong'}, 400

    def post(self):
        """
        Test de l'API avec erreur 403
        """
        return {'response': 'pong'}, 403


@api.route("/api/v1/time")
class Time(Resource):
    @api.response(200, 'Flask Time : Success')
    @api.response(400, 'Flask DateTime: Error')
    def get(self):
        """
        Renvoi la date actuelle et le timestamp
        """
        current_timestamp = datetime.datetime.now().timestamp()
        current_date = datetime.datetime.now()
        return {'response': {
            'current_date': str(current_date),
            'current_timestamp': str(current_timestamp)}
               }, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=False)
