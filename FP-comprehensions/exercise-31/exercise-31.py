# Exercise number 31 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1

def pig_latin_from_file(file_name) -> str:
    pig_lating_word: str = ''
    VOWELS = ('a', 'e', 'i', 'o', 'u')
    with open(file_name) as file:
        for line in file.readlines():
            for word in line.split():
                print(word)
                if word[0] in VOWELS:
                    pig_lating_word = word + 'way'
                else:
                    temp_first_letter = word[0]
                    pig_lating_word = word[1:] + temp_first_letter + 'ay'

    return pig_lating_word
print(pig_latin_from_file("wcfile.txt"))




