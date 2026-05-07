# simple flask webpage skeleton practice
from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the website"

if __name__ == "__main__":
    app.run()