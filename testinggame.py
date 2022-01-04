import math
import time
from testingplayer import GeniusComputerPlayer
from tkinter import *
from functools import partial
from tkinter import messagebox
sign = 0
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

    def update_text(self, i, gb):
        global sign
        o_player = GeniusComputerPlayer("O")
        print(i)
        if self.board[i] == ' ':
            if sign % 2 == 0:
                self.board[i] = "X"
            else:
                self.board[i] = "O"
            sign += 1
            # button[i].config(text=board[i])
        x = True
        # if winner(board, "X"):
        #     gb.destroy()
        #     x = False
        #     box = messagebox.showinfo("Winner", "Player won the match")
        # elif winner(board, "O"):
        #     gb.destroy()
        #     x = False
        #     box = messagebox.showinfo("Winner", "Computer won the match")
        # elif(isfull()):
        #     gb.destroy()
        #     x = False
        #     box = messagebox.showinfo("Tie Game", "Tie Game")
        if(x):
            if sign % 2 != 0:
                move = o_player.get_move(self)
                # button[(i+1)*(j+1)-1].config(state=DISABLED)
                # self.update_text(move, gb)

    def gameboard_pc(self, game_board):
        global button
        button = []
        for index in range(len(self.board)):
            # print(index//3, index%3)
            button.append(Button(game_board, bd=5, text=" ", height=4, width=8, command=self.update_text(index, game_board)))
            button[index].grid(row=(index//3), column=(index%3))
        for index in range(len(self.board)):
            for index2 in range(len(self.board)):
                # button[index]['text'] = self.update_text(button[index], index, game_board)
                button[index2].config(text=str(index2))
                # print(button[index2], end="\n")
        

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
    # play(game)
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    game.gameboard_pc(game_board)
    game_board.mainloop()