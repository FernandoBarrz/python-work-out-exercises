# Exercise number 49 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1



import time 

def elapsed_since(data):
    last_time = None
    for item in data:
        current_time = time.perf_counter()
        delta = current_time - (last_time or current_time)

        last_time = time.perf_counter()
        yield (delta, item)

for t in elapsed_since('abcd'):
    print(t)
    time.sleep(2)