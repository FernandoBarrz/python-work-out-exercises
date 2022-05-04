# Exercise number 8 - Python Workout Book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1


def strsort(word_to_sort: str) -> str:
    '''
        the sorted() function will sort the characters in Unicode order.
     '''


    return "".join(sorted(word_to_sort)) 

    # highest_unicode_value = 0
    # str_sorted = 
    # for char in word_to_sort:
    #     unicode_char_value = 
    #     if unicode_char_value > highest_unicode_value:
    #         str_sorted
    #         highest_unicode_value = unicode_char_value

    


print(strsort('cba'))


