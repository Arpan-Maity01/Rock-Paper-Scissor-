# Rock-Paper-Scissor-
The game is implemented using a combination of the tkinter library for the graphical user interface (GUI) and the pygame library for handling sounds.

First, we import the necessary libraries and initialize pygame.

Then, we create a tkinter window called root and set its title to "Rock, Paper, Scissors".

Next, we set up the game window using a tkinter.Canvas object. We also create a tkinter.Label object to display the result of the game, a tkinter.OptionMenu object to allow the user to choose their move, and a tkinter.Button object to initiate the game.

The play_game function is responsible for running each game. It first retrieves the user's choice from the dropdown menu and generates a random choice for the computer. Then, it determines the winner based on the rules of Rock, Paper, Scissors. Finally, it updates the text of the result_label to display the choices made by the user and the computer, as well as the outcome of the game.

When the "Play" button is clicked, the play_game function is executed. This allows the user to choose their move, start the game, and view the results.

Finally, we run the tkinter main loop to keep the GUI running and listening for user input.



