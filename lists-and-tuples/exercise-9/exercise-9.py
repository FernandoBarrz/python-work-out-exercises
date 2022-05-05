# Exercise number 9 - Python Workout Book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1


from importlib.util import find_spec


def firstlast(sequence_to_get):
    '''
        Generic function that get a sequence as input and return a short version of in the same type.
    '''
    first_element = sequence_to_get[0]
    last_element = sequence_to_get[-1]
    if type(sequence_to_get) == list:
        return [first_element, last_element]
    elif type(sequence_to_get) == str:
        return f"{first_element}{last_element}"
    elif type(sequence_to_get) == tuple:
        return (first_element, last_element)
    return "Bad input"

#def firstlast(sequence_to_get):
#    return sequence_to_get[:1] + sequence_to_get[-1:]
#print(firstlast('abcd'))  # 'ad'

    


print(firstlast([1, 2, 3, 4]))


