# Exercise number 26 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1

"""
Uses the technique "dispatch table" and the operator module
"""

import operator


    
def calc(to_solve):
    op, a, b= to_solve.split(" ", maxsplit=2)
    a = int(a)
    b = int(b)
    operations = {
        "+": operator.add(a, b),
        "-": operator.sub(a, b),
        "*": operator.mul(a, b),
        "/": operator.truediv(a, b),
        "%": operator.mod(a, b)
    }
    return operations[op]

print(calc("+ 99 1"))       
            
            








