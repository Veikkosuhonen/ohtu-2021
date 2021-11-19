from typing import List
import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self) -> List[Player]:
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatistics(unittest.TestCase):

    def setUp(self) -> None:
        self.stats = Statistics(PlayerReaderStub())

    def test_nothing(self):
        self.assertTrue(True)
    
    def test_search_with_whole_name(self):
        kurri = self.stats.search("Kurri")
        self.assertEqual(kurri.name, "Kurri")
        self.assertEqual(kurri.team, "EDM")

    def test_search_with_partial_name(self):
        lemieux = self.stats.search("Lem")
        self.assertEqual(lemieux.name, "Lemieux")
        self.assertEqual(lemieux.team, "PIT")
    
    def test_search_not_found(self):
        nobody = self.stats.search("Aho")
        self.assertEqual(nobody, None)
    
    def test_get_many_player_team(self):
        edm = self.stats.team("EDM")
        self.assertEqual(edm[0].name, "Semenko")
        self.assertEqual(edm[1].name, "Kurri")
        self.assertEqual(edm[2].name, "Gretzky")
        self.assertEqual(len(edm), 3)
    
    def test_get_one_player_team(self):
        pit = self.stats.team("PIT")
        self.assertEqual(pit[0].name, "Lemieux")
        self.assertEqual(len(pit), 1)

    def test_empty_team(self):
        not_found = self.stats.team("NJD")
        self.assertEqual(not_found, [])
    
    def test_one_top_scorer(self):
        best = self.stats.top_scorers(0) # <-- Bad implementation wants 0 instead of 1
        self.assertEqual(best[0].name, "Gretzky")
        self.assertEqual(len(best), 1)
    
    def test_all_top_scorers(self):
        all = self.stats.top_scorers(4)
        self.assertEqual(all[0].name, "Gretzky")
        self.assertEqual(all[4].name, "Semenko")
        self.assertEqual(len(all), 5)
    