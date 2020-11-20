import unittest
from app.models.player import Player


class TestPlayer(unittest.TestCase):
    pass
    def setUp(self):
        self.player_1 = Player("Sauron", "rock")
        self.player_2 = Player("Gandalf", "paper")


    #@unittest.skip("Delete this line to run the test")
    def test_create_player(self):
        self.assertEqual(self.player_1.name, "Sauron")
        self.assertEqual(self.player_1.choice, "rock")
        self.assertEqual(self.player_2.name, "Gandalf")
        self.assertEqual(self.player_2.choice, "paper")
        
