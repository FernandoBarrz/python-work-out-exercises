# Exercise number 47 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1


import os

def all_lines(path):
    for filename in os.listdir(path):
        full_filename = os.path.join(path, filename)

        try:
            for line in open(full_filename):
                yield line
        except OSError:
            pass
for one_line in all_lines('/etc/'):
    print(one_line)