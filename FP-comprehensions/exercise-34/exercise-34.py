# Exercise number 34 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1

def is_supervocalic(word):
    set_word = set(word)
    vowels = {"a", "e", "i", "o", "u"}
    return vowels < set_word

def supervolic_words(file_name):
    return {word.strip() 
            for word in open(file_name)
            if is_supervocalic(word.lower())}

print(supervolic_words("words.txt"))




