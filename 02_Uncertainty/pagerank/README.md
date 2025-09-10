# Project 2: PageRank

## Project Overview

This project is an implementation of Google's famous PageRank algorithm. The AI ranks a corpus of web pages by importance based on their link structure. Pages with more, high-quality incoming links are considered more important. The program calculates these ranks by iteratively distributing "rank" from each page to the pages it links to until the values converge.

## Key Concepts & Skills Gained

-   **PageRank Algorithm:** Implemented the core logic of PageRank, including the concept of a "damping factor" to model a user randomly surfing to any page.
-   **Iterative Algorithms:** Wrote an algorithm that repeatedly refines its results until they converge to a stable solution within a defined tolerance.
-   **Markov Chains:** Understood, at a high level, how the PageRank model can be interpreted as a Markov chain, where each page is a state and links are transition probabilities.
-   **Data Structures:** Used dictionaries to represent the corpus of web pages, their links, and their calculated PageRank values efficiently.

## A Note on Scaffolding

In accordance with the project specifications for Harvard's CS50 AI course, the corpus of web pages and the main program loop were provided. My primary task was to implement the two main versions of the PageRank algorithm: one based on random sampling (a sampling model) and one based on iterative formula calculations (an iteration model).