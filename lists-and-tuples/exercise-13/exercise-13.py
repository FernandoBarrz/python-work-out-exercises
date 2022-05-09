# Exercise number 13 - Python Workout Book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1

from collections import Counter


def most_repeating_word(sequence_to_count):
    '''
    Return the string that contains the greatest number of repeated letters.
    '''
    most_rpt_word = []
    for element in sequence_to_count:
        most_rpt_word.append(Counter(element).most_common(1)[0][0])

    return most_rpt_word


words = ['this', 'is', 'an', 'elementary', 'test', 'example']

print(most_repeating_word(words))

    

    





