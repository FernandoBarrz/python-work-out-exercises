# Exercise number 3 - Python WorkOut
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.8.2 64-bit

def run_timing():
    """Asks the user repeatedly for numeric input. Prints the average time an
d number of runs."""
    number_of_runs = 0
    total_time = 0
    while True:
        one_run = input('Enter 10 km run time: ')
        if not one_run:
            break
        number_of_runs += 1
        total_time += float(one_run)
        
    average_time = total_time / number_of_runs

    print(f'Average of {average_time}, over {number_of_runs} runs')
run_timing()
