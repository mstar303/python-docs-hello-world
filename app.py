from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello,my 2nd web shashi v1.0 "
