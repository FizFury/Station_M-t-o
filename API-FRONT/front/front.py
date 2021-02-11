# coding: utf-8
from flask import Flask, render_template
from flask_restx import Resource, Api, fields, reqparse
import requests, json
import pymysql
import datetime

# Config Flask App Definition
app = Flask(__name__)

db_host = "localhost"

db = pymysql.connect(
    host=db_host,
    user="admin",
    passwd="toor",
    db="station_meteo"
)


@app.route("/affichage")
def index():
    response = requests.get(url="http://192.168.8.248:5000/print_data")
    data = response.text
    data = json.loads(data)

    response = requests.get(url="http://192.168.8.248:5000/print_last_data")
    lastdata = response.text
    lastdata = json.loads(lastdata)

    response = requests.get(url="http://192.168.8.248:5000/print_10last_data")
    last10data = response.text
    last10data = json.loads(last10data)

    response = requests.get(url="http://192.168.8.248:5000/print_graph_data")
    graphdata = response.text
    graphdata = json.loads(graphdata)

    return render_template("index.html", data=data, lastData=lastdata, last10Data=last10data, lastGraphData=graphdata)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001', debug=False)
