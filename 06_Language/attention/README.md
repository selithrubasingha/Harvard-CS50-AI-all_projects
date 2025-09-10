# Project 6: Masker (Attention)

## Project Overview

This project utilizes a state-of-the-art **Transformer** model (like BERT) to perform a "fill-in-the-blank" task. The AI is given a sentence with a single masked word and must predict which word most likely belongs in that blank. This project serves as a practical introduction to the powerful **attention mechanism**, which allows models to understand context by weighing the importance of different words in a sentence. 🧠

## Key Concepts & Skills Gained

-   **Transformers:** Gained hands-on experience using a modern, pre-trained Transformer model, which is the foundation for models like ChatGPT and BERT.
-   **Attention Mechanism:** Developed an intuition for how the attention mechanism allows a model to understand complex contextual relationships between words in a sentence.
-   **Natural Language Processing (NLP):** Applied a cutting-edge technique to a common language understanding task.
-   **Pre-trained Models:** Learned how to load and use a massive, pre-trained model (`bert-base-uncased`) from a library like Hugging Face's `transformers`.
-   **Tokenization:** Understood the process of converting human-readable text into a format (tokens) that a neural network can process.

## A Note on Scaffolding

In accordance with the project specifications for Harvard's CS50 AI course, the powerful `transformers` library and the pre-trained BERT model itself were the primary provided components. My task was to write the Python script that loads the model and tokenizer, processes an input sentence with a mask, and then queries the model to predict the most likely words to complete the sentence.