# Project 3: Crossword

## Project Overview

This is an AI that automatically solves crossword puzzles. The program is given the structure of a crossword puzzle (the grid, and where words start) and a dictionary of valid words. It then uses backtracking search and constraint satisfaction techniques to find a valid solution where all words fit correctly.

![Project Demo](path/to/your/crossword.gif)

## Key Concepts & Skills Gained

-   **Constraint Satisfaction Problems (CSPs):** Modeled the crossword puzzle as a CSP, defining variables (word slots), domains (all possible words for that slot), and constraints (letters must match where words overlap).
-   **Backtracking Search:** Implemented the recursive backtracking algorithm, a fundamental technique for solving CSPs.
-   **Arc Consistency (AC-3):** Implemented logic to enforce arc consistency, a powerful technique to prune the domain of variables *before* searching, which dramatically improves performance.
-   **Graph and Set Theory:** Used data structures to represent the puzzle, including the overlaps between word variables, which is essentially a graph problem.

## A Note on Scaffolding

In accordance with the project specifications for Harvard's CS50 AI course, the `generate.py` script to create puzzles and the `util.py` library with data structures were provided. My task was to implement the `Crossword` class in `generate.py` and the core solving logic in `solver.py`, including enforcing consistency and the backtracking search algorithm.