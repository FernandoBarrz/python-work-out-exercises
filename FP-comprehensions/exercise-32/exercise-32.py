# Exercise number 32 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1



d = {'a':1, 'b':2, 'c':3}

def flip_dict(data):
    return {y: x for x, y in data.items()}


print(flip_dict(d))




