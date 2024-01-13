from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "hellooooooo this is AA demo "
