import pandas as pd
import numpy as np

## importing matches,

ipl_matches = pd.read_csv('ipl-matches.csv')

def teamsAPI():
    ipl_teams = list(set(list(ipl_matches['Team1']) + list(ipl_matches['Team2'])))
    teams_dict = {
        "teams":ipl_teams
    }
    return teams_dict

def teams_vs_teamsAPI():
    team1 = 'Royal Challengers Bangalore'
    team2 = 'Sunrisers Hyderabad'

    matches_played = (ipl_matches['Team1'] == team1) & (ipl_matches['Team2']==team2) | (ipl_matches['Team1'] == team2) & (ipl_matches['Team2']==team1)
    total_matches = matches_played.shape[0]

    match_won_team1 = matches_played['WinningTeam'].value_counts()[team1]
    match_won_team2 = matches_played['WinningTeam'].value_counts()[team2]

    drawn = total_matches - (match_won_team1 + match_won_team2)

    response = {
        "Number of Matches played": total_matches,
        "Matches Won by Team1": match_won_team1,
        "Matches Won by Team2": match_won_team2,
        "Matches Drawn": drawn
    }
    return response