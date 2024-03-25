import sys
import nltk 
from nltk import word_tokenize
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from random import seed
from random import randint
seed(1234)
# nltk.download('averaged_perceptron_tagger')
# nltk.download("stopwords") 
# nltk.download("wordnet") 
# nltk.download("punkt") 
# nltk.download("omw-1.4")

# Import necessary libraries and modules.
# sys for accessing command-line arguments.
# nltk for natural language processing tasks.
# re for regular expressions.
# Set a seed for the random number generator for reproducibility.

# Function to calculate lexical diversity of a given text.
def lexical_diversity(text):
    tokens = word_tokenize(text) # Tokenize the text into words.
    return round(len(set(tokens)) / len(tokens), 2) # Calculate and return lexical diversity.

# Function to preprocess the raw text.
def preprocess(raw_text):

    # Tokenize the text, convert to lowercase, and filter out non-alphabetic tokens.
    tokens = [t.lower() for t in word_tokenize(raw_text) if t.isalpha()] 

    # Remove stopwords and tokens shorter than 6 characters.
    tokens = [t for t in tokens if t not in stopwords.words('english') if len(t) > 5]

    # Lemmatize the tokens and remove duplicates.
    wnl = WordNetLemmatizer()
    lemmatized = set([wnl.lemmatize(t) for t in tokens])

    # Perform POS tagging on the unique lemmas.
    tags = nltk.pos_tag(lemmatized)

    print('\n')
    print("FIRST TWENTY TAGS AND THEIR UNIQUE LEMMAS:")
    print(tags[:20])

    nouns = [] # List to store nouns.
    # Extract and store nouns from the tagged lemmas.
    for lemma, tag in tags:
        if tag == 'NN':
            nouns.append(lemma)

    print('\n')
    print("NUMBER OF TOKENS:", len(tokens))
    print('\n')
    print("NUMBER OF NOUNS:", len(nouns))

    return tokens, nouns
 
def main():
    # Check if a command-line argument (file name) is provided.
    if len(sys.argv) == 1:
        print("Error: No argument passed")
        return  
    
    # Open and read the content of the file specified in the command-line argument.
    with open(sys.argv[1], 'r') as file:
        content = file.read()

    # Calculate and display the lexical diversity of the file content.
    print('\n')
    print("LEXICAL DIVERSITY:", lexical_diversity(content))
        
    # Preprocess the content to get tokens and nouns.
    tokens, nouns = preprocess(content)

    # Create a dictionary of nouns and their frequencies.
    dict_nouns = {}
    for noun in nouns:
        dict_nouns[noun] = tokens.count(noun)

    # Display the fifty most common nouns and their counts.
    print("\n")
    print("FIFTY MOST COMMON WORDS AND THEIR COUNTS:")
    print(dict(sorted(dict_nouns.items(), key=lambda item: item[1], reverse=True)[:50]))

    # Get the list of fifty most common words.
    common_words_dict = dict(sorted(dict_nouns.items(), key=lambda item: item[1], reverse=True)[:50])
    common_words = [word for word in common_words_dict]

    print("\n")
    print("Let's play a word guessing game!")
    
    # Select a random word from the list of common words for the guessing game.
    random_word = common_words[randint(0,len(common_words)-1)]

    # Create a dictionary with characters in the random word and their counts.
    word_dict = {}
    for c in random_word:
        if c not in word_dict:
            word_dict[c] = 1
        else:
            word_dict[c] += 1

    # Initialize the word guess display, points, and a set for already guessed letters.
    word_guess = ['_']*len(random_word)
    points = 5
    alread_guessd = set()
    print(' '.join(word_guess))
    print('\n')

    # Main loop for the guessing game.
    while True:
        
        # Prompt the user to guess a letter.
        guess = input("Guess a letter: ")

        # Check if the user's guess is the '!' character
        if guess == '!':
            print("GAME OVER, '!' is not valid")
            print('\n')
            return  # Exit the function, effectively ending the game.
        
         # Check if the guessed letter has already been guessed before.
        if guess in alread_guessd:
            # Display a message and show the current state of the guessed word.
            print("Already! guessed, try something else. Score is: ", points)
            print(' '.join(word_guess))
            print('\n')

        # If the guessed letter is in the word being guessed.
        elif guess in word_dict:
            points+=1 # Increase the player's points.
            alread_guessd.add(guess) # Add the guessed letter to the set of already guessed letters.
            if guess in word_dict:
                del word_dict[guess] # del the guess from dict if character already guessed
            
            # Check if all letters have been guessed.
            if len(word_dict) == 0:
                # End the game successfully.
                print("You Solved it!")
            else:
                # If there are still letters to guess, display the current score.
                print("Right! Score is:", points)

            # Get the indexes of the guessed letter in the word.
            indexes = []
            for i, c in enumerate(random_word):
                if c == guess:
                    indexes.append(i)

            # Update the display of the guessed word with the newly guessed letter.
            for index in indexes:
                word_guess[index] = guess

            # printing the updated guessed word
            print(' '.join(word_guess))
            print('\n')

            # Check if the game has been solved and end the loop if it has.
            if len(word_dict) == 0:
                return 
        else:
            # If the guess is incorrect.
            points-=1 # Deduct a point for a wrong guess.
            alread_guessd.add(guess) # Add the guessed letter to the set of already guessed letters.

            # Check if the points have fallen below zero.
            if points < 0:
                print("GAME OVER, TRY AGAIN")
                print("Correct word was:", random_word)
                return # End the game as the player has run out of points.
            print("Sorry! wrong guess. Score is:", points) 
            print(' '.join(word_guess))
            print('\n')
            # Display a message for a wrong guess and show the current state of the guessed word.

if __name__ == '__main__':
    main()