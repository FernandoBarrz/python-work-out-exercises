# Exercise number 13 - Python Workout Book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1

from operator import itemgetter

PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)] 


def format_sort_records(sequence=None):
    if not sequence:
        return 'No data available'
    output_str = ''
    for record in sorted(sequence, key=itemgetter(1, 0)):
        first_name, last_name, date_arr = record
        output_str += f'{last_name:10}{first_name:10}{date_arr:5.2f}\n'
    return output_str
    
print(format_sort_records(PEOPLE))

    

    





