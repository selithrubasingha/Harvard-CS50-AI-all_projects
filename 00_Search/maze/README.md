# Project 0: Maze Solver

## Project Overview

This project is a fundamental introduction to AI search algorithms. The program's goal is to find a solution to a maze, navigating from a starting point to an end point. It reads a maze layout from a text file and visually outputs the correct path. This project demonstrates how different search strategies can explore a problem space to find a solution. 🗺️

![Project Demo](path/to/your/maze_solution.gif)

## Key Concepts & Skills Gained

-   **Search Algorithms:** Implemented foundational AI search strategies to solve the maze.
-   **Graph Traversal:** Understood how a maze can be represented as a graph and how to traverse it.
-   **Depth-First Search (DFS):** Wrote a solver that explores as far as possible down one branch before backtracking.
-   **Breadth-First Search (BFS):** Wrote a solver that explores all neighbors at the present depth before moving on to the next level, guaranteeing the shortest path.
-   **Data Structures:** Gained practical experience using a **Stack** (for DFS) and a **Queue** (for BFS) to manage the "frontier" of nodes to explore.

## A Note on Scaffolding

In accordance with the project specifications for Harvard's CS50 AI course, the `maze.py` file containing the `Maze` class was provided. This class handles reading the maze from a `.txt` file, identifying key locations (start, end, walls), and drawing the solution. My task was to implement the core `solve` method, which contains the logic for the search algorithms.