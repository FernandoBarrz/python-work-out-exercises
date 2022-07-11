# Exercise number 35a - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1

import string


def generateGematria():
    return {x : y 
            for y, x in enumerate(string.ascii_lowercase, 1) }



print(generateGematria())




