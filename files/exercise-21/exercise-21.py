# Exercise number 21 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1
import os
from pprint import pprint


def find_longest_word(file_name):
    longest_word = ''
    with open(file_name) as file:
        for line in file.readlines():
            for word in line.split():
                if len(longest_word) < len(word):
                    longest_word = word
    return longest_word         


def find_all_longest_words(dir_name):
    """
    Returns a dict with directory names as keys and the longest word in them as values of the dict.
    """
    dirs_list = os.listdir(dir_name)
    return {x: find_longest_word(os.path.join(dir_name, x)) for x in dirs_list if os.path.isfile(os.path.join(dir_name, x))}
    
    


pprint(find_all_longest_words("./books"))

    





