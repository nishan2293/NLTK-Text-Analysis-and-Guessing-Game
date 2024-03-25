# NLTK-Based Text Analysis and Word Guessing Game

## Overview
This Python script provides functionality for text analysis and a word guessing game using the Natural Language Toolkit (NLTK). It includes features like lexical diversity calculation, text preprocessing, and a simple word guessing game based on the most frequent nouns in a given text.

## Features
1. **Lexical Diversity Calculation**: Computes the lexical diversity of a given text.
2. **Text Preprocessing**: Tokenizes the text, removes stopwords and non-alphabetic tokens, lemmatizes, and identifies nouns.
3. **Word Guessing Game**: A game using the most common nouns from the preprocessed text.

## Requirements
- Python 3
- NLTK library


## Installation
Ensure you have NLTK installed and the required NLTK packages downloaded:

```python
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('omw-1.4')
```

## Deployment

To deploy this project run

```bash
 python your_script.py your_text_file.txt
```





## Authors

- [@nishan2293](https://github.com/nishan2293)