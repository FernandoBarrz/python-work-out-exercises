# Exercise number 18 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1


def get_final_line(file_name):
    with open(file_name, "r") as file:

        
        last_line = file.readlines()
    print(last_line)

    return last_line[-1]


print(get_final_line('README.md'))
    





