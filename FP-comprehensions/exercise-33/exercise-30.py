# Exercise number 30 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1

def flatten(complex_list):
    return [ele 
            for lst in complex_list
            for ele in lst]


print(flatten([[1, 2], [3, 4]]))




