from flask import Flask
from webargs import fields

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World Adding webargs!"