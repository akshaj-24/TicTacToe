import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.startGame = False
        self.xpos = 0
        self.opos = 0
        self.winner = False
        self.row1 = [" ", " ", " "]
        self.row2 = [" ", " ", " "]
        self.row3 = [" ", " ", " "]
        self.current_player = "X"

    def reset_game(self):
        self.xpos = 0
        self.opos = 0
        self.winner = False
        self.row1 = [" ", " ", " "]
        self.row2 = [" ", " ", " "]
        self.row3 = [" ", " ", " "]
        self.current_player = "X"


    def welcome(self):
        self.startGame = True
        return self.startGame

    def display_grid(self):
        print(self.row1)
        print(self.row2)
        print(self.row3)

    def x_position(self):
        while True:
            try:
                self.xpos = int(input("Enter X position (1-9): "))
                if self.xpos not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    raise ValueError("Position should be between 1 and 9.")
                if self.is_position_taken(self.xpos):
                    raise ValueError("Position already taken. Choose a different position.")
                break
            except ValueError as e:
                print(f"Incorrect choice! {e}")

    def o_position(self):
        while True:
            try:
                self.opos = int(input("Enter O position (1-9): "))
                if self.opos not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    raise ValueError("Position should be between 1 and 9.")
                if self.is_position_taken(self.opos):
                    raise ValueError("Position already taken. Choose a different position.")
                break
            except ValueError as e:
                print(f"Incorrect choice! {e}")
        return self.opos

    def is_position_taken(self, pos):
        if pos in [1, 2, 3] and self.row1[pos - 1] != " ":
            return True
        elif pos in [4, 5, 6] and self.row2[pos - 4] != " ":
            return True
        elif pos in [7, 8, 9] and self.row3[pos - 7] != " ":
            return True
        return False

    def x_placement(self):
        if self.xpos in [1, 2, 3]:
            self.row1[self.xpos - 1] = "X"
            return self.row1
        elif self.xpos in [4, 5, 6]:
            self.row2[self.xpos - 4] = "X"
            return self.row2
        elif self.xpos in [7, 8, 9]:
            self.row3[self.xpos - 7] = "X"
            return self.row3

    def o_placement(self):
        if self.opos in [1, 2, 3]:
            self.row1[self.opos - 1] = "O"
            return self.row1
        elif self.opos in [4, 5, 6]:
            self.row2[self.opos - 4] = "O"
            return self.row2
        elif self.opos in [7, 8, 9]:
            self.row3[self.opos - 7] = "O"
            return self.row3

    def check_winner(self):
        for row in [self.row1, self.row2, self.row3]:
            if all(cell == "X" for cell in row) or all(cell == "O" for cell in row):
                return True

        for col in range(3):
            if all(row[col] == "X" for row in [self.row1, self.row2, self.row3]) or all(
                    row[col] == "O" for row in [self.row1, self.row2, self.row3]):
                return True

        if all(row[i] == "X" for i in range(3)) or all(row[i] == "O" for i in range(3)):
            return True

        if all(row[i] == "X" for i in range(2, -1, -1)) or all(row[i] == "O" for i in range(2, -1, -1)):
            return True

        return False

class TicTacToeGUI:
    def __init__(self, master, game):
        self.master = master
        self.master.title("Tic Tac Toe")

        self.game = game

        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text=" ", font=("Helvetica", 16), width=6, height=3,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def on_button_click(self, row, col):
        index = 3 * row + col
        if self.game.winner or self.game.is_position_taken(index + 1):
            return
        if self.game.current_player == "X":
            self.game.xpos = index + 1
            self.game.x_placement()
            self.update_board()
        elif self.game.current_player == "O":
            self.game.opos = index + 1
            self.game.o_placement()
            self.update_board()

        if self.game.check_winner():
            messagebox.showinfo("Game Over", f"{self.game.current_player} is the winner!")
            self.game.reset_game()
            self.update_board()
        elif " " not in self.game.row1 + self.game.row2 + self.game.row3:
            messagebox.showinfo("Game Over", "It's a tie!")
            self.game.reset_game()
            self.update_board()
        else:
            self.game.current_player = "O" if self.game.current_player == "X" else "X"

    def update_board(self):
        for i in range(3):
            for j in range(3):
                index = 3 * i + j
                self.buttons[index].config(text=self.game.row1[index] if index < 3 else
                self.game.row2[index - 3] if 2 < index < 6 else
                self.game.row3[index - 6])


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe()
    app = TicTacToeGUI(root, game)
    root.mainloop()
