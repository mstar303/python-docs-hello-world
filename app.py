from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello this is new web aws restart "
