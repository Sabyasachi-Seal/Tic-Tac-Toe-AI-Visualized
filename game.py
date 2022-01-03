import math
import time
from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Unbeatable Tic-Tac-Toe')


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

def play(game):
    my_menu = Menu(root)
    root.config(menu=my_menu)
    options_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Options", menu=options_menu)
    options_menu.add_command(label="Reset Game", command=reset)
    reset()
    root.mainloop()


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

def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def checkifwon():
    global winner
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"]  == "X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"]  == "X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"]  == "X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"]  == "X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"]  == "X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"]  == "X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"]  == "X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"]  == "X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()

    #### CHECK FOR O's Win
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"]  == "O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"]  == "O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"]  == "O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"]  == "O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"]  == "O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"]  == "O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"]  == "O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"]  == "O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()

    # Check if tie
    if count == 10 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "It's A Tie!\n No One Wins!")
        disable_all_buttons()

def b_click(b, game):
    global count
    square = o_player.get_move(game)
    if count>1:
        print(square)
        print(((b.grid_info()['column']+1)*(b.grid_info()['row']+1)-1))
    if b["text"] == " "  and count%2!=0:
        b["text"] = "X"
        clicked = False
        square = ((b.grid_info()['column']+1)*(b.grid_info()['row']+1)-1)
        game.make_move(square, "X")

    elif b["text"] == " " and count%2==0:
        square = o_player.get_move(game)
        if  ((b.grid_info()['column']+1)*(b.grid_info()['row']+1)) == square:
            b["text"] = "O"
        clicked = True
        game.make_move(square, "O")
    else:
        messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected\nPick Another Box..." )
    count += 1
    checkifwon()

def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9

    global clicked, count
    clicked = True
    count = 1
    if count%2==0:
        b_click(b1, game)
        b_click(b2, game)
        b_click(b3, game)
        b_click(b4, game)
        b_click(b5, game)
        b_click(b6, game)
        b_click(b7, game)
        b_click(b8, game)
        b_click(b9, game)

    else:
        b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1, game))
        b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2, game))
        b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3, game))

        b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4, game))
        b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5, game))
        b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6, game))

        b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7, game))
        b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8, game))
        b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9, game))

    # Grid our buttons to the screen
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)



if __name__ == '__main__':
    x_player = HumanPlayer("X")
    o_player = GeniusComputerPlayer("O")
    game = TicTacToe()
    play(game)
