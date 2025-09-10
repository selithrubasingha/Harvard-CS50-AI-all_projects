# Harvard's CS50 Introduction to AI with Python - Projects

## About This Repository

This repository contains my solutions and implementations for the project assignments from Harvard University's **CS50 Introduction to Artificial Intelligence with Python**. Each project is designed to explore and apply fundamental concepts of modern AI, from search algorithms and knowledge representation to machine learning and natural language processing.

The projects are organized into folders based on the course's lecture topics.

---

## Technologies Used
* **Python 3**
* **Key Libraries:** `pygame`, `scikit-learn`, `tensorflow`, `nltk`, `transformers`

---

## Project Showcase

Here is a summary of the projects completed during the course. Each module tackles a different domain of Artificial Intelligence.

### 00_Search
* **Projects:** `maze`, `tictactoe`, `degrees`
* **Concepts:** This module covers foundational graph search algorithms. I implemented **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** to find solutions in a maze, and the adversarial **Minimax algorithm** to create an unbeatable Tic-Tac-Toe AI.

### 01_Knowledge
* **Projects:** `knights`, `minesweeper`
* **Concepts:** These projects focus on representing knowledge logically. I built agents that use **propositional logic** to solve logic puzzles and play Minesweeper by making decisions based on **logical inference**.

### 02_Uncertainty
* **Projects:** `pagerank`, `heredity`
* **Concepts:** Here, I worked with probabilistic models to handle uncertainty. This involved implementing the **PageRank algorithm** using Markov Chains and building a **Bayesian Network** to calculate genetic probabilities.

### 03_Optimization
* **Project:** `crossword`
* **Concepts:** This project explores optimization problems by implementing a **backtracking search** algorithm to solve crossword puzzles, framed as a **Constraint Satisfaction Problem**.

### 04_Learning
* **Projects:** `shopping`, `nim`
* **Concepts:** This module introduces machine learning. I trained a **k-Nearest Neighbors (k-NN)** classifier to predict shopping behavior and implemented a **Q-learning** agent that masters the game of Nim through **reinforcement learning**.

### 05_Neural_Networks
* **Project:** `traffic`
* **Concepts:** A dive into deep learning, this project involved building and training a **Convolutional Neural Network (CNN)** for image classification, teaching it to recognize traffic signs.

### 06_Language
* **Projects:** `parser`, `questions`, `masker`
* **Concepts:** These projects cover **Natural Language Processing (NLP)**. I implemented a **TF-IDF** based question-answering system and used pre-trained **Transformer models** (like BERT) to understand language context.

---

## How to Run the Projects

To run these projects on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run a specific project:**
    ```bash
    cd 00_Search/tictactoe
    python runner.py
    ```

---

## Acknowledgments

A huge thank you to the entire CS50 team, especially **David J. Malan** and **Brian Yu**, for creating this incredible and challenging course.