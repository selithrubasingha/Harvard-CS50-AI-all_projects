# Project 4: Nim

## Project Overview

This project involves building an AI that learns to play the mathematical game of Nim. What makes this project unique is that the AI is not programmed with the game's optimal strategy. Instead, it uses **reinforcement learning**—specifically Q-learning—to discover the winning strategy on its own. It achieves this by playing against itself thousands of times, learning from the outcomes of its actions through trial and error. 🤖

![Project Demo](path/to/your/nim_demo.gif)

## Key Concepts & Skills Gained

-   **Reinforcement Learning (RL):** This was a hands-on introduction to RL, a major branch of machine learning where an agent learns to make optimal decisions by interacting with an environment and receiving rewards or punishments.
-   **Q-Learning:** Implemented the Q-learning algorithm to train the agent. This involved creating a Q-table to store values for every possible state-action pair and using an update rule to iteratively improve those values.
-   **Exploration vs. Exploitation:** Implemented an **epsilon-greedy** policy. This strategy allows the agent to balance making random moves to discover new strategies (**exploration**) with choosing the best-known move to win (**exploitation**).
-   **Model-Free Learning:** The AI learns how to play the game perfectly without ever being given the rules or a model of the game's dynamics. It learns purely from the feedback of its actions.

## A Note on Scaffolding

In accordance with the project specifications for Harvard's CS50 AI course, the `nim.py` file containing the game engine (the `Nim` class and its methods for handling moves and game state) was provided. My primary responsibility was to implement the `train` function, which contains the entire Q-learning algorithm, and to write the main code that facilitates a game between a human player and the trained AI.