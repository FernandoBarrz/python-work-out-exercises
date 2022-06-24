# Exercise number 16 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1



def dictdiff(first, second):
    output = {}
    all_keys = first.keys() | second.keys()

    for key in all_keys:
        first_val = first.get(key, None)
        second_val = second.get(key, None)
        if first_val != second_val:
            output[key] = [first_val, second_val]

    return output


a = {'a': 1, 'b': 2, 'c': 3}
b = {'a': 1, 'b': 2, 'c': 4}

print(dictdiff(a, b))
    





