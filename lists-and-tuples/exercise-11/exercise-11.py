# Exercise number 11 - Python Workout Book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1

from importlib.util import find_spec

import operator

PEOPLE = [
            {'first':'Reuven',
                'last':'Lerner',
                'email':'reuven@lerner.co.il'
            },
            {'first':'Donald', 
                'last':'Trump', 
                'email':'president@whitehouse.gov'
            },
            {'first':'Vladimir', 
                'last':'Putin',
                'email':'president@kremvax.ru'
            }
        ] 

def alphabetize_names(sequence_to_sort):
    '''
    Return the list of dicts, but sorted by last name and then by first name.
    '''
    # The "Key" parameter to "sorted" gets a function, whose result indicates how we'll sort.
    return sorted(sequence_to_sort, key= operator.itemgetter('last', 'first'))

for e in alphabetize_names(PEOPLE):
    print(e["last"], e["first"])



    

    





