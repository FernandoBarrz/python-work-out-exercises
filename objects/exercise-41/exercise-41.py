# Exercise number 41 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1


class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor
    
class Bowl:

    SCOOP_LIMIT = 3

    def __init__(self):
        self.scoops = []


    def add_scoops(self, *args):
        for scoop in args:
            if len(self.scoops) < self.SCOOP_LIMIT:
                self.scoops.append(scoop)

        
    def __repr__(self) -> str:
        return " - ".join(scoop.flavor for scoop in self.scoops)

class BigBowl(Bowl):
    SCOOP_LIMIT = 5



s1 = Scoop("Chocolate")
s2 = Scoop("Vanilla")
s3 = Scoop("Persiumm")
s4 = Scoop("Banana")
s5 = Scoop("Piña")
s6 = Scoop("Blueberry")
s7 = Scoop("Coconut")
s8 = Scoop("Lima")

b = Bowl()
big_bowl = BigBowl()
b.add_scoops(s7, s8, s1, s2, s3, s4, s5, s6, s7, s8)
big_bowl.add_scoops(s7, s8, s1, s2, s3, s4, s5, s6, s7, s8)

print(b)
print(big_bowl)
print("-"*10)
print(Bowl.SCOOP_LIMIT)
print(BigBowl.SCOOP_LIMIT)

