from flask import Flask,jsonify, request
from ipl import *

app = Flask('__name__')

@app.route('/')
def home():
    return "Hello world"

@app.route('/api/teams')
def teams():
    func = teamsAPI()
    return jsonify(func)

@app.route('/api/teamvteam')
def teams_vs_teams():
   
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    func = teams_vs_teamsAPI(team1,team2)
    
    return jsonify(func)

if __name__ == "__main__":
    app.run(debug=True)