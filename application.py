from flask import Flask
from flask_apispec import use_kwargs

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World Adding flask-apispec!"