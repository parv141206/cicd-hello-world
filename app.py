from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Yo!"

@app.route("/hello")
def hello_world_2():
    return "Hello"