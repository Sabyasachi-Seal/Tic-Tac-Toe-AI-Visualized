import math # for mathematical uses
import random # for randomly choosing a value
class Player:
    def __init__(self, letter):
        # lettter tells us the player. It can have X or O
        self.letter = letter
    

    def get_move(self, game):
        # returns the move of the player in a game 
        pass


class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self,game):
        if len(game.available_moves())==9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square


    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'
        if state.current_winner == other_player:
            return {'position': None,
                    'score': (1 if other_player==max_player else -1)*(state.num_empty_squares()+1)
            }
        elif not state.empty_squares():
            return {'position': None,
                    'score': 0
                    }
        
        if player==max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)
            state.board[possible_move] = " "
            state.current_winner = None
            sim_score['position'] = possible_move
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best

