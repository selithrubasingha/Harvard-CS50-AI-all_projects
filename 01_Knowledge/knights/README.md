# Project 1: Knights and Knaves

## Project Overview

This project involves building an AI that can solve logic puzzles. Based on the classic puzzles of knights (who always tell the truth) and knaves (who always lie), the program uses model checking to determine which characters are knights and which are knaves based on a set of statements they make.

## Key Concepts & Skills Gained

-   **Propositional Logic:** Represented complex English sentences as logical statements using connectives like `And`, `Or`, `Not`, and `Implication`.
-   **Knowledge Representation:** Created a knowledge base that encapsulates all the rules of the puzzle world (e.g., a character must be either a knight or a knave, but not both).
-   **Model Checking:** Implemented a model-checking algorithm that iterates through all possible assignments of roles (models) and checks if the knowledge base holds true for each model, thereby finding the solution.
-   **Logical Inference:** The AI deduces facts that are not explicitly stated by evaluating the truth values of the provided sentences under different models.

## A Note on Scaffolding

In accordance with the project specifications for Harvard's CS50 AI course, the `logic.py` library containing the logical sentence structures (`And`, `Symbol`, etc.) and the puzzle files were provided. My task was to implement the core logic in `puzzle.py`, where I constructed the knowledge bases for each puzzle and used the provided tools to perform model checking and find the solution.