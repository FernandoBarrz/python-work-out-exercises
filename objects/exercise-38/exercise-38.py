# Exercise number 38 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1



class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor
    
def create_scoops():
    return [Scoop(flavor) for flavor in ('Chocolate', 'vanilla', 'persimmon')]


for scoop in create_scoops():
    print(scoop.flavor)


