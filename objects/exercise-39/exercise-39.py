# Exercise number 39 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1



class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor
    
class Bowl:
    def __init__(self):
        self.scoops = []


    def add_scoops(self, *args):
        self.scoops.extend(args)

        
    def __repr__(self) -> str:
        return " - ".join(scoop.flavor for scoop in self.scoops)

s1 = Scoop("Chocolate")
s2 = Scoop("Vanilla")
s3 = Scoop("Persiumm")

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
print(b)