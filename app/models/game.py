class Game():
    def __init__(self, name, player_1, player_2):
        self.name = name
        self.player_1 = player_1
        self.player_2 = player_2

    def play(self):
        return f"{self.player_1.name} won the game"