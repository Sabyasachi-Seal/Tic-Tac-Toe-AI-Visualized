import math
import time
from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
from tkinter import *
from functools import partial
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [" " for _ in range(9)]
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("|| " + " || ".join(row)+" ||")
    

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
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
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        #checking row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3: (row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True

        #check Column
        col_ind = square % 3
        column = [self.board[col_ind+i*3]for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #check diagonal
        if square%2==0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

    def gameboard_pc(self, game_board):
        global button
        button = []
        o_player = GeniusComputerPlayer("O")
        for i in range(3):
            button.append(i)
            button[i] = []
            for j in range(3):
                button[i].append(j)
                get_t = o_player.get_move(game_board)
                button[i][j] = Button(
                    game_board, bd=5, command=get_t, height=4, width=8)
                button[i][j].grid(row=m, column=n)
        game_board.mainloop()

    def withpc(self, game_board):
        game_board.destroy()
        game_board = Tk()
        game_board.title("Tic Tac Toe")
        self.gameboard_pc(game_board)
    
    def play(self):
        menu = Tk()
        menu.geometry("250x250")
        menu.title("Tic Tac Toe")
        self.withpc(menu)
        menu.mainloop()

    # if print_game:
    #     game.print_board_nums()

    # letter = 'X'
    # while game.empty_squares():
    #     if letter=="O":
    #         square = o_player.get_move(game)
    #     else:
    #         square = x_player.get_move(game)

    #     if game.make_move(square, letter):
    #         if print_game:
    #             print(letter+ f" makes a move to square {square}")
    #             game.print_board()
    #             print("")

    #         if game.current_winner:
    #             if print_game:
    #                 print(letter + " wins!")
    #             return letter


    #         letter = "O" if letter == "X" else "X"
    #     time.sleep(1)
    # if print_game:
    #     print("It\'s a tie!")



if __name__ == '__main__':
    game = TicTacToe()
    game.play()