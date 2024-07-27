import tkinter as tk
from random import shuffle

class MemoryPuzzleGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Memory Puzzle Game")
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.cards = list(range(8)) * 2
        shuffle(self.cards)

        self.buttons = []
        for i in range(16):
            button = tk.Button(self.frame, text="", command=lambda i=i: self.click(i), height=3, width=6)
            button.grid(row=i//4, column=i%4)
            self.buttons.append(button)

        self.clicked = []
        self.matches = 0
        self.time_limit = 60  # in seconds
        self.time_left = self.time_limit
        self.time_label = tk.Label(self.root, text=f"Time left: {self.time_left} seconds")
        self.time_label.pack()

        self.update_timer()

    def click(self, i):
        if len(self.clicked) < 2 and self.buttons[i]['text'] == "":
            self.buttons[i]['text'] = str(self.cards[i])
            self.clicked.append(i)
            if len(self.clicked) == 2:
                self.root.after(500, self.check_match)

    def check_match(self):
        if self.cards[self.clicked[0]] == self.cards[self.clicked[1]]:
            self.matches += 1
            self.buttons[self.clicked[0]]['state'] = 'disabled'
            self.buttons[self.clicked[1]]['state'] = 'disabled'
        else:
            self.buttons[self.clicked[0]]['text'] = ""
            self.buttons[self.clicked[1]]['text'] = ""
        self.clicked = []

        if self.matches == 8:
            self.time_label['text'] = "Congratulations! You won!"
            self.root.after(2000, self.root.destroy)

    def update_timer(self):
        self.time_left -= 1
        self.time_label['text'] = f"Time left: {self.time_left} seconds"
        if self.time_left > 0:
            self.root.after(1000, self.update_timer)
        else:
            self.time_label['text'] = "Time's up! Game over."
            self.root.after(2000, self.root.destroy)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = MemoryPuzzleGame()
    game.run()