button.append(Button(game_board, bd=5, text=index, height=4, width=8))
            button[index].grid(row=(index//3), column=(index%3))