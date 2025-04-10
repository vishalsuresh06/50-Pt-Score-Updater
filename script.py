from nba_api.live.nba.endpoints import scoreboard
from nba_api.live.nba.endpoints import boxscore
from datetime import datetime
import requests
import os
from dotenv import load_dotenv

# Get game IDs
games = scoreboard.ScoreBoard().games.get_dict()
gameIds = [game['gameId'] for game in games]

playersWithX = []
scoreThreshold = 45  # Changed threshold to 50

# Loop through games
for game_id in gameIds:
    box = boxscore.BoxScore(game_id)
    awayPlayers = box.away_team.get_dict()['players']
    homePlayers = box.home_team.get_dict()['players']

    # Check away players
    for player in awayPlayers:
        if player['statistics']['points'] >= scoreThreshold:
            playersWithX.append((player['name'], player['statistics']['points']))

    # Check home players
    for player in homePlayers:
        if player['statistics']['points'] >= scoreThreshold:
            playersWithX.append((player['name'], player['statistics']['points']))

# If there are players with 50+ points
if playersWithX:
    # Sort the players list by points in descending order
    playersWithX = sorted(playersWithX, key=lambda x: x[1], reverse=True)

    API_KEY = "password"
    SERVER_URL = "http://localhost:5000/send"

    load_dotenv()
    numbers = os.getenv("PHONE_NUMBERS", "")
    numbers = numbers.split(",") if numbers else []
    
    msg = f"Players who dropped {scoreThreshold}+ points ({datetime.now().strftime('%Y-%m-%d')}):\n--------------------------------------\n\n"

    # Add players and their scores to the message
    for player, score in playersWithX:
        msg += f"{player}: {score} points\n"
    
    # Remove the last newline
    msg = msg.rstrip('\n')

    for num in numbers:
        payload = {
            "recipient": "+12147333570",
            "message": msg
        }

        headers = {
            "Api-Key": API_KEY,
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(SERVER_URL, headers=headers, json=payload)
            print("Status Code:", response.status_code)
            print("Response:", response.json())
        except requests.exceptions.RequestException as e:
            print("Failed to send message:", e)
