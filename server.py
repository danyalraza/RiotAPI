from flask import Flask
from flask import render_template
from riot_client import Client

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('layout.html', name=name)

if __name__ == "__main__":
    app.run()