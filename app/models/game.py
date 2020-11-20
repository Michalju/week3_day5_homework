class Game():
    def __init__(self, name, player_1, player_2):
        self.name = name
        self.player_1 = player_1
        self.player_2 = player_2
        self._result = ''

    def play(self):
        # Rock Paper Scissor rules
        # Rock (1) beats Scissors(2)
        # Scissors(2) beat Paper (3)
        # Paper (3) beat Rock(1)
        
        # Below is when there is a tie 
        if self.player_1.choice == self.player_2.choice:
            self._result = "None won the game"            

        # Below is when Player 1 has rock and wins    
        elif(self.player_1.choice == "rock" and self.player_2.choice == "scissors") or \
            (self.player_1.choice == "scissors" and self.player_2.choice == "paper") or \
            (self.player_1.choice == "paper" and self.player_2.choice == "rock"):
            self._result =  f"{self.player_1.name} won the game"

        # otherwise Player 2 wins
        else:         
            self._result =  f"{self.player_2.name} won the game"