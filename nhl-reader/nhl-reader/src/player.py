from dataclasses import dataclass

@dataclass
class Player:
    name: str
    nationality: str
    assists: int
    goals: int
    penalties: int
    team: str
    games: int

    def get_score(self):
        return self.goals + self.assists
    
    def __str__(self): 
        return f"{self.name:21} {self.team} {str(self.goals):2} + {str(self.assists):2} = {self.get_score()}"
