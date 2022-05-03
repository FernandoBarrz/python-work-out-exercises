# Exercise number 6 - Python Workout Book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1


def pl_sentence(sentence_to_translate: str) -> str:
    '''
        Assuming that sentenceto_translate is an English sentence with no capital letters or punctuation.
    '''
    pig_lating_sentence: list = sentence_to_translate.split()
    VOWELS = ('a', 'e', 'i', 'o', 'u')
    pl_sentence = []
    for word in pig_lating_sentence:
        if word[0] in VOWELS:
            word = word + 'way'
            pl_sentence.append(word)
        else:
            temp_first_letter = word[0]
            word = word[1:] + temp_first_letter + 'ay'
            pl_sentence.append(word)

    return " ".join(pl_sentence)

print(pl_sentence('this is a test translation'))


