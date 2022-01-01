class TicTacToe:
    def __init__(self):
        self.board = [" " for i in range(9)]
        self.current_winner = None

    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("|| " + " || ".join(row)+" ||")
    

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]]
        for row in number_board:
            print("|| " + " || ".join(row)+" ||")

        
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            return True
        return False

def play(self, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    letter = "X"
    while game.empty_squares():
        if letter=="O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)