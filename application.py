from flask import Flask
from flask_apispec import use_kwargs
from webargs import fields


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World 1!"