# Exercise number 10 - Python Workout Book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1


def my_sum(*args):
    '''
        Generic function that uses the + operator on different data types (numbers, strings, list, and tuples)
    '''
    if not args:
        return args

    output = args[0]

    for arg in args[1:]:
        output = output + arg

    return output

print(my_sum(1,2,32,4,345,45,345,38423), type(my_sum(1,2,32,4,345,45,345,38423)))

