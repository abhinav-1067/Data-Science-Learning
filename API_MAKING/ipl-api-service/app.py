from flask import Flask,jsonify
from ipl import *

app = Flask('__name__')

@app.route('/')
def home():
    return "Hello world"

@app.route('/api/teams')
def teams():
    func = teamsAPI()
    return jsonify(func)

@app.route('/api/teams_vs_teams')
def teams_vs_teams():
    func = teams_vs_teamsAPI()
    t = func('Royal Challengers Bangalore','Lucknow Super Giants')
    return jsonify(t)

if __name__ == "__main__":
    app.run(debug=True)