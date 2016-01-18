from flask import Flask
from flask import jsonify
import requests
from flask import render_template
from riot_client import Client
from key import key

app = Flask(__name__)

riotapi = Client(key)

@app.route("/")
def home():
    return '<h1>Using Riot API</h1>'

@app.route("/summoner/<region>/<username>")
def champions(username, region):
    user = username
    summary = riotapi.get_summoner_by_name(username, region)

    return jsonify(summary)

if __name__ == "__main__":
    app.run(debug=True)
