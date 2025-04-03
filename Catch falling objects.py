import tkinter as tk
import random

class CatchGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Catch the Falling Objects")
        
        self.canvas = tk.Canvas(master, width=400, height=400, bg="lightblue")
        self.canvas.pack()
        
        self.basket_width = 60
        self.basket = self.canvas.create_rectangle(170, 350, 170 + self.basket_width, 370, fill="brown")
        
        self.score = 0
        self.score_label = tk.Label(master, text="Score: 0")
        self.score_label.pack()

        self.falling_item = None
        self.falling_item_speed = 5
        self.start_game()

        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)

    def start_game(self):
        self.create_falling_item()
        self.update_game()

    def create_falling_item(self):
        x = random.randint(0, 380)
        self.falling_item = self.canvas.create_oval(x, 0, x + 20, 20, fill="red")

    def update_game(self):
        if self.falling_item:
            self.canvas.move(self.falling_item, 0, self.falling_item_speed)
            pos = self.canvas.coords(self.falling_item)

            if pos[3] >= 400:  # If item falls below the screen
                self.canvas.delete(self.falling_item)
                self.create_falling_item()
            elif self.check_collision(pos):
                self.canvas.delete(self.falling_item)
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")
                self.create_falling_item()

        self.master.after(100, self.update_game)

    def check_collision(self, pos):
        basket_pos = self.canvas.coords(self.basket)
        return (pos[2] > basket_pos[0] and pos[0] < basket_pos[2] and pos[3] >= basket_pos[1])

    def move_left(self, event):
        self.canvas.move(self.basket, -20, 0)

    def move_right(self, event):
        self.canvas.move(self.basket, 20, 0)

if __name__ == "__main__":
    root = tk.Tk()
    game = CatchGame(root)
    root.mainloop()