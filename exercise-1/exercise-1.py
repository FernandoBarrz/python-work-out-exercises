# Exercise number 1 - Python WorkOut
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.8.2 64-bit

# Dependencies 
import random


# Main function with no arguments
def guessing_game():
    """
        This function generates a random number and ask for guessing it
    """
    random_number = random.randint(0, 100)

    while True:

        user_input = int(input('Guess a number!\n'))
        if user_input > random_number:
            print("Too high\n")

        if user_input < random_number:
            print('Too low\n')

        if user_input == random_number:
            print('Just right\n')
            break


guessing_game()
