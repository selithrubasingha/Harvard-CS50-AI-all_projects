# Project 6: Parser

## Project Overview

This project dives into the field of **Natural Language Processing (NLP)** by building a sentence parser. The AI's task is to take a sentence and, using a provided context-free grammar, identify and extract all the noun phrases within it. This is a fundamental step in enabling a computer to understand the grammatical structure of human language. 🌳

## Key Concepts & Skills Gained

-   **Natural Language Processing (NLP):** Gained experience with computational linguistics and how to programmatically analyze text.
-   **Syntactic Parsing:** Understood the process of analyzing a string of symbols (a sentence) to determine its grammatical structure.
-   **Context-Free Grammar (CFG):** Learned how to define and use a set of grammatical rules to break down sentences into their constituent parts (like noun phrases, verb phrases, etc.).
-   **Noun-Phrase Chunking:** Implemented a specific type of parsing focused on identifying simple, non-recursive noun phrases, which is a common and useful NLP task.
-   **Recursion & Tree Structures:** Worked with the tree-like structures that represent a sentence's grammar.

## A Note on Scaffolding

In accordance with the project specifications for Harvard's CS50 AI course, the `nltk` library and some boilerplate code were provided. My core contribution was to implement the `np_chunk` function, which contains the logic for chunking the sentence to identify all noun phrases based on the grammatical rules.