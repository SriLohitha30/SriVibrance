import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("300x300")
        self.player_turn = "X"
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, text="", command=lambda row=i, column=j: self.click(row, column), height=3, width=6)
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def click(self, row, column):
        if self.buttons[row][column]['text'] == "":
            self.buttons[row][column]['text'] = self.player_turn
            if self.check_win():
                messagebox.showinfo("Game Over", f"Player {self.player_turn} wins!")
                self.window.quit()
            elif self.check_tie():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.window.quit()
            else:
                self.player_turn = "O" if self.player_turn == "X" else "X"
                if self.player_turn == "O":
                    self.computer_move()

    def computer_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j]['text'] == ""]
        if empty_cells:
            row, column = random.choice(empty_cells)
            self.buttons[row][column]['text'] = "O"
            if self.check_win():
                messagebox.showinfo("Game Over", "Computer wins!")
                self.window.quit()
            elif self.check_tie():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.window.quit()
            else:
                self.player_turn = "X"

    def check_win(self):
        for row in self.buttons:
            if row[0]['text'] == row[1]['text'] == row[2]['text'] != "":
                return True
        for column in range(3):
            if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == self.buttons[2][column]['text'] != "":
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return True
        return False

    def check_tie(self):
        return all(self.buttons[i][j]['text'] != "" for i in range(3) for j in range(3))

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()