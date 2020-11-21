class Player():
    def __init__ (self, name, choice):
        self.name = name
        self.choice = choice
    
    def computer(self):
        import random
        self.choice = random.choice(["rock", "scissors", "paper"])