import unittest
from app.models.game import Game
from app.models.player import Player


class TestGame(unittest.TestCase):
    pass

    def setUp(self):
        self.player_1 = Player("Sauron", "rock")
        self.player_2 = Player("Gandalf", "paper")
        self.game = Game("Our first game", self.player_1, self.player_2)

    # @unittest.skip("Delete this line to run the test")
    def test_game_being_created(self):
        self.assertEqual(self.game.name, "Our first game")
        self.assertEqual(self.game.player_1.name, "Sauron")
        self.assertEqual(self.game.player_2.name, "Gandalf")

    def test_game_play(self):
        self.assertEqual(self.game._result, "")
        self.game.play()
        self.assertEqual(self.game._result, "Gandalf won the game")

    def test_game_tie(self):
        self.game1 = Game(
            "Our first game", Player("Sauron", "rock"), Player("Gandalf", "rock")
        )
        self.game1.play()
        self.assertEqual(self.game1._result, "None won the game")

        self.game2 = Game(
            "Our first game", Player("Sauron", "paper"), Player("Gandalf", "paper")
        )
        self.game2.play()
        self.assertEqual(self.game2._result, "None won the game")

        self.game3 = Game(
            "Our first game",
            Player("Sauron", "scissors"),
            Player("Gandalf", "scissors"),
        )
        self.game3.play()
        self.assertEqual(self.game3._result, "None won the game")

    def test_game_player1_win(self):
        pass

    def test_game_player2_win(self):
        pass