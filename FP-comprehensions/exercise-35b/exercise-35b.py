# Exercise number 35a - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1

import string
def generateGematria():
    return {x : y 
            for y, x in enumerate(string.ascii_lowercase, 1) }
gematria_values = generateGematria()

def gematria_for(word):
    return sum(gematria_values.get(x, 0) for x in word)



def gematria_equal_words(word):
    one_score = gematria_for(word)
    return [w.strip() 
            for w in open("words.txt")
            if gematria_for(w.lower()) == one_score]

print(gematria_equal_words("cat"))