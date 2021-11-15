import requests
import datetime
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['nationality'],
            player_dict["assists"],
            player_dict["goals"],
            player_dict["penalties"],
            player_dict["team"],
            player_dict["games"]
        )

        players.append(player)

    print("Players from FIN " + str(datetime.datetime.now()))

    finnish_players_by_score = sorted(
        filter(lambda p: p.nationality == "FIN", players),
        key=lambda p: p.get_score(),
        reverse=True
    )

    for player in finnish_players_by_score:
        print(player)


if __name__ == "__main__":
    main()