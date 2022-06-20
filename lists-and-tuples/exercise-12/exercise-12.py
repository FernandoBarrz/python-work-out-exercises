# Exercise number 12 - Python Workout Book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1

from collections import Counter


def most_repeating_word(sequence_to_count):
    '''
    Return the string that contains the greatest number of repeated letters.
    '''
    output = ''
    max_count = 1
    for element in sequence_to_count:
        temp_var = Counter(element).most_common(1)[0][1]
        if temp_var >= max_count:
            max_count = temp_var
            output = element
    return output



words = ['this', 'is', 'an', 'elementary', 'testtt', 'example', 'abbba']

print(most_repeating_word(words))

    

    





