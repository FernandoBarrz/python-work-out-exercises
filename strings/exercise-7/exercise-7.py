# Exercise number 7 - Python Workout Book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1


def ubbi_dubbi(word_to_translate: str) -> str:
    '''
        Assuming that word_to_translate is an English word with no capital letters or punctuation.
    '''
    
    VOWELS = ('a', 'e', 'i', 'o', 'u')

    ub_word = []

    for word in list(word_to_translate):
        if word in VOWELS:
            ub_word.append(f'ub{word}')
        else:
            ub_word.append(word)
    return "".join(ub_word)

print(ubbi_dubbi('elephant'))


