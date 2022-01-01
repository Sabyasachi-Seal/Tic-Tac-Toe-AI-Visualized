import math # for mathematical uses
import random # for randomly choosing a value

class Player:
    def __init__(self, letter):
        # lettter tells us the player. It can have X or O
        self.letter = letter
    

    def get_move(self, game):
        # returns the move of the player in a game 
        pass

class RandomComputerPlayer(Player):
    def init(self, letter):
        super().__init__(self, letter)
    
    
    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(self, letter)
    

    def get_move(self, game):
        pass