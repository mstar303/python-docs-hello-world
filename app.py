from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello,simplylearn day06 World!"
