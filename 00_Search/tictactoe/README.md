# Project 0: Tic-Tac-Toe

## Project Overview

This project is an AI that plays Tic-Tac-Toe optimally. The program uses the Minimax algorithm to determine the best possible move at any given state of the game, ensuring that it will never lose. The user can play against the AI and experience firsthand how a game theory algorithm works in a simple, deterministic environment.

![Project Demo](path/to/your/tictactoe.gif)

## Key Concepts & Skills Gained

-   **Game Theory:** Understood the fundamentals of adversarial search in a two-player, zero-sum game.
-   **Minimax Algorithm:** Implemented the recursive Minimax algorithm to explore the game tree, evaluating the utility of each possible move to make the optimal choice.
-   **Recursion:** Utilized recursion to explore all possible future states of the game from the current board.
-   **Algorithm Design:** Defined key functions for the algorithm, such as checking for a winner (`winner`), determining if the game is over (`terminal`), and calculating the board's score (`utility`).

## A Note on Scaffolding

In accordance with the project specifications for Harvard's CS50 AI course, the graphical user interface (GUI) using `pygame` and the main game loop were provided. My core contribution was implementing the AI's "brain"—the `minimax` function and all its helper functions—which decides which move the computer should make.