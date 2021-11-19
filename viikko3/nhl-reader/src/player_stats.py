from player import Player

class PlayerStats:
    def __init__(self, reader) -> None:
        self.player_reader = reader
    
    def top_scorers_by_nationality(self, nationality: str) -> list[Player]:
        players = self.player_reader.get_players()
        players_by_nationality = list(filter(
            lambda p: p.nationality == nationality, 
            players
        ))
        players_by_nationality.sort(
            key=lambda player: player.get_score(),
            reverse=True
        )
        return players_by_nationality
            
        