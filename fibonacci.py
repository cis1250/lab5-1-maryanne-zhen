#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

# --- Validates and returns user input
def user_input():
    # Validity of user input
    valid = False

    # Loop to get input until the given input is valid
    while not valid:
        try:
            # Asking user for the number of terms they want
            num_terms = int(input("Number of terms to print: "))

            # Checking if the number is positive
            if num_terms > 0:
                valid = True
            else:
                print("Please enter a positive integer.")
        # Error message if the input is not an integer
        except:
            print("Please enter a positive integer.")
    
    # Return the valid input
    return num_terms

# --- Generates fibonacci sequence with given number of terms
def fib_seq(num_terms):
    # Initialize empty list
    sequence = []

    a = 0 # Current term
    b = 1 # Next term

    # Loop for each term up to the given amount
    for i in range(num_terms):
        # Add the current term to the list
        sequence.append(a)
        # Update the values of the current and next term
        a, b = b, a+b
    
    # Return the finished sequence as a list
    return sequence

# --- Prints a given fibonacci sequence
def print_seq(sequence):
    # Loop for each item in the given list
    for i in range(len(sequence)):
        # Print each item in the list with a space after
        print(sequence[i], end=" ")

# ----- MAIN PROGRAM -----
# Taking user input
user_terms = user_input()
# Generating fibonacci sequence
user_sequence = fib_seq(user_terms)
# Printing fibonacci sequence
print_seq(user_sequence)
