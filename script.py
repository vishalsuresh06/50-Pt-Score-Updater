from nba_api.live.nba.endpoints import scoreboard
from nba_api.live.nba.endpoints import boxscore
import requests
import os
from dotenv import load_dotenv

#Get game ids
games = scoreboard.ScoreBoard().games.get_dict()
gameIds = []
for game in games:
    gameIds.append(game['gameId'])

has50 = False

for id in gameIds:
    box = boxscore.BoxScore(id)
    awayPlayers = box.away_team.get_dict()['players']
    homePlayers = box.home_team.get_dict()['players']
    for player in awayPlayers:
        if player['statistics']['points'] >= 50:
            has50 = True
            break

    for player in homePlayers:
        if player['statistics']['points'] >= 50:
            has50 = True
            break
    if has50:
        break

if has50:
    API_KEY = "password"
    SERVER_URL = "http://localhost:5000/send"

    load_dotenv()
    numbers = os.getenv("PHONE_NUMBERS", "")
    numbers = numbers.split(",") if numbers else []

    for num in numbers:
        payload = {
            "recipient": num,
            "message": "Someone dropped 50"
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