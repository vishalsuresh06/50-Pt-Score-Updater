from nba_api.live.nba.endpoints import scoreboard
from nba_api.live.nba.endpoints import boxscore

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

print(has50)