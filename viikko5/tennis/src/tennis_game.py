
SCORE_NAMES = {
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty"
}

END_GAME_SCORE = 4

DRAW_NAME = "All"
END_GAME_DRAW_NAME = "Deuce"
ADVANTAGE_MSG = "Advantage "
WIN_MSG = "Win for "


class TennisGame:

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.score1 = 0
        self.score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.score1 += 1
        elif player_name == self.player2_name:
            self.score2 += 1

    def get_score(self) -> str:
        if self.score1 == self.score2:
            return self._get_draw_score()
        elif self._is_end_game():
            return self._get_end_game_score() 
        return SCORE_NAMES[self.score1] + "-" + SCORE_NAMES[self.score2]
    
    def _is_end_game(self) -> bool:
        return self.score1 >= END_GAME_SCORE or self.score2 >= END_GAME_SCORE
    
    def _get_end_game_score(self) -> str:
        score_diff = self.score1 - self. score2
        if score_diff == 1:
            return ADVANTAGE_MSG + self.player1_name
        elif score_diff == -1:
            return ADVANTAGE_MSG + self.player2_name
        elif score_diff >= 2:
            return WIN_MSG + self.player1_name
        else:
            return WIN_MSG + self.player2_name

    def _get_draw_score(self) -> str:
        if self._is_end_game():
            return END_GAME_DRAW_NAME
        return SCORE_NAMES[self.score1] + "-" + DRAW_NAME
