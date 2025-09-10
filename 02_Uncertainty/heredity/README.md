# Project 2: Heredity

## Project Overview

This project uses a Bayesian Network to calculate the probability of individuals within a family having a certain number of genes for a harmful trait, as well as the probability of them exhibiting that trait. Given a data file describing a family tree and the known traits of some members, the AI can infer probabilities for everyone else.



## Key Concepts & Skills Gained

-   **Bayesian Networks:** Gained a practical understanding of how to use Bayesian networks to model probabilistic relationships between variables (in this case, genetics).
-   **Conditional Probability:** The entire project is an application of conditional probability, calculating the likelihood of events given that other events have occurred (e.g., the probability of a child having a gene, given their parents' genes).
-   **Joint Probability:** Implemented a function to compute the joint probability of a set of events occurring together across the entire network, which is the core of inference in this model.
-   **Probabilistic Inference:** Wrote code that can infer unknown information (probabilities of genes/traits) from known evidence.

## A Note on Scaffolding

In accordance with the project specifications for Harvard's CS50 AI course, the function to load and parse the family data from CSV files was provided. My responsibility was to implement the core probabilistic logic, including the `joint_probability` function and its helpers, which perform the calculations based on the principles of Bayesian inference.