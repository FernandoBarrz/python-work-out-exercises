# Exercise number 31 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1

def pig_latin(words):
    pig_lating_word = ""
    VOWELS = ('a', 'e', 'i', 'o', 'u')
    for word in words.split():
        
        if word[0] in VOWELS:
            pig_lating_word = word + 'way'
        else:
            temp_first_letter = word[0]
            pig_lating_word = word[1:] + temp_first_letter + 'ay'
    return pig_lating_word



def pig_latin_from_file(file_name) -> str:
    return " ".join(pig_latin(word_inner)
                    for word in open(file_name) # Iterates through each line of filename
                    for word_inner in word.split()) # Iterates through each word in the current line
print(pig_latin_from_file("wcfile.txt"))




