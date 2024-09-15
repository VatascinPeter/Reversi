# Reversi
A player of Reversi developed in Python

My player (player.py) is given the colour of it's stones and the colour of the opponent's stones (0 or 1) in initialization (__init__)

The "select_move" method has an imput parameter of the board state (nxn matrix, the number -1 signifies an empty space, 0 or 1 signify a player's stone). The method returns the coordinate of my player's next move, if there is any possible.

The player first evaluates the board and finds all possible moves, then it uses the minimax algorithm to find the most optimal move. the minimax runs until there is still time to evaluate and keeps a static game value for each game state.

I also created a greedy player for testing.
