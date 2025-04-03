from tkinter import *  # noqa: F403
from tkinter import messagebox
import random

# Creating the main game class
class NumberGuessingGame:
    def __init__(self, root):
        self.root = root 
        self.root.title("Number Guessing Game")
        self.root.geometry("300x250")
        self.root.config(background="#fff2e6")
        
        self.random_number = random.randint(1, 100)  # Initialize random number
        self.create_game_ui()

    # Creating the game interface
    def create_game_ui(self): 
        # Creating game instruction label
        self.instruction_label = Label(self.root, text="Guess a number between 1 and 100", font=("Arial", 12)) 
        self.instruction_label.pack(pady=10)
        
        # Creating entry field for the user's input
        self.entry = Entry(self.root) 
        self.entry.pack(pady=5)

        # Creating a submit button to check the user's guess
        self.submit_button = Button(self.root, text="Submit", command=self.check_guess) 
        self.submit_button.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())

            if guess < self.random_number:
                messagebox.showinfo("Try Again", "Too low! Try a higher number.")
            elif guess > self.random_number:
                messagebox.showinfo("Try Again", "Too high! Try a lower number.")
            else:
                messagebox.showinfo("Congratulations!", "Correct! You guessed the number.")
                self.reset_game()
        except ValueError: 
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    # Resetting the game with a new number
    def reset_game(self):
        self.random_number = random.randint(1, 100)  # Get a new random number
        self.entry.delete(0, END)  # Clear the entry field

# Run the game
if __name__ == "__main__":
    root = Tk()
    game = NumberGuessingGame(root)  # Create an instance of the game
    root.mainloop()
    
 
  