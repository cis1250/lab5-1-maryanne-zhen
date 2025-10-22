#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

# -------------------------

# --- Takes and validates sentence input from user
def get_sentence():
    # Validity of user's sentence
    valid = False

    # Loop to get input until given input is a valid sentence
    while not (valid):
        # Prompting user to enter a sentence
        sentence_string = input("Enter a sentence: ")
        # Checking validity of sentence
        valid = is_sentence(sentence_string)

        # Print a message if invalid input
        if not valid:
            print("This does not meet the criteria for a sentence.")

    # Splitting the sentence into a list
    sentence = (sentence_string.lower()).split()

    # Removing punctuation from the sentence
    for word in sentence:
        for character in word:
            if character in '[,.!?]$':
                sentence[sentence.index(word)] = word.replace(character, "")

    # Return the validated sentence as a list
    return sentence

# --- Calculating the frequencies of each word in a given sentence
def calculate_frequencies(sentence):
    # Initializing lists for each word and its frequency
    words = []
    frequencies = []

    # Iterating through each word(item) in the sentence(list)
    for word in sentence:
        # Checking if the word(item) already exists in the words list
        if word in words:
            # Setting index to the spot of the current word
            index = words.index(word)
            # Increasing the corresponding frequency by 1
            frequencies[index] += 1
        else:
            # Add the new word to the words list
            words.append(word)
            # Add a new spot in frequencies and set it to 1
            frequencies.append(1)

    # Return the words and frequencies lists
    return words, frequencies

# --- Printing each word and its frequency in a clear format
def print_frequencies(words, frequencies):
    # Looping for the number of unique words
    for i in range (len(words)):
        # Printing the word and its corresponding frequency
        print(f"{words[i]:10} : {frequencies[i]:5}")

# --- Main function
def main():
    # Getting a sentence from the user
    sentence = get_sentence()

    # Creating two lists to hold the words and frequencies of the sentence
    words, frequencies = calculate_frequencies(sentence)

    # Printing the results
    print_frequencies(words, frequencies)

# ----- MAIN PROGRAM -----
main()
