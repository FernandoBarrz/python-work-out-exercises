# Exercise number 50 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1



def mychain(*args):
    for arg in args:
        for item in arg:
            yield item

for one_item in mychain('abc', [1, 2, 3], {'a': 1, 'b': 2}):
    print(one_item)