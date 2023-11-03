import tkinter as tk
import pygame
import random

# Initialize pygame
pygame.init()

# Create a tkinter window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Set up game window
game_window = tk.Canvas(root, width=30, height=30)
game_window.pack()

# Define game variables
choices = ["Rock", "Paper", "Scissors"]
user_choice = ""
computer_choice = ""
result = ""


# Function to start a new game
def play_game():
    global user_choice, computer_choice, result
    user_choice = user_choice_var.get()
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Scissors" and computer_choice == "Paper") or
            (user_choice == "Paper" and computer_choice == "Rock")
    ):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
    user_choice_var.set("")


# Create a label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack()

# Create a dropdown for user choice
user_choice_var = tk.StringVar()
user_choice_var.set("Rock")
user_choice_dropdown = tk.OptionMenu(root, user_choice_var, *choices)
user_choice_dropdown.pack()

# Create a play button
play_button = tk.Button(root, text="Play", command=play_game)
play_button.pack()

# Run the tkinter main loop
root.mainloop()
