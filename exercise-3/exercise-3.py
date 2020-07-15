# Exercise number 3 - Python WorkOut
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.8.2 64-bit

def run_timing():
    """Asks the user repeatedly for numeric input. Prints the average time an
d number of runs."""
    total_time = 0
    total_runs = 0
    while(True):
        try:
            time_to_run = float(input("Enter 10 km run time:  "))
            total_time += time_to_run
        except ValueError as e:
            break
            print(f'You entered a especial character or string: {e}')
        total_runs += 1
        average_time = total_time / total_runs
    return f'Average of {average_time:.1f}, over {total_runs} runs'

run_timing()
