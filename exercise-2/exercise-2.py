# Exercise number 2 - Python WorkOut
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.8.2 64-bit

def my_sum(*numbers): # The "splat" operator is used when we need an arbitrary amount of arguments
    output = numbers[0]
    for i in numbers[1:]: # It returns a tuple
        output += i  
    return output
print(my_sum(4, 6))
    

