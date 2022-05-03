# Exercise number 4 - Python Workout Book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1


def pig_latin(word_to_translate: str) -> str:
    '''
        Assuming that word_to_translate is an English word with no capital letters or punctuation.
    '''
    pig_lating_word: str = ''
    VOWELS = ('a', 'e', 'i', 'o', 'u')

    if word_to_translate[0] in VOWELS:
        pig_lating_word = word_to_translate + 'way'
    else:
        temp_first_letter = word_to_translate[0]
        pig_lating_word = word_to_translate[1:] + temp_first_letter + 'ay'

    return pig_lating_word

print(pig_latin('computer'))


