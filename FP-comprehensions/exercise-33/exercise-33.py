# Exercise number 33 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1

d = {'a':1, 'b':2, 'c':3}

def transform_values(func, dict_value):
    return {key: func(val) for key, val in dict_value.items()}


print(transform_values(lambda x: x * x, d))




