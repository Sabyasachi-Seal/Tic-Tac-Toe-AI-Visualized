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
    def __init__(self, letter):
        super().__init__(letter)
    
    
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s Turn. Input (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError()
                valid_square = True
            except ValueError():
                print("Invalid Move. Try Again.")
        return val
