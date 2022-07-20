# Exercise number 44 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1

from Animal import Animal

class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4)
        
class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4)
class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)
class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)

wolf = Wolf('Grey')
sheep = Sheep("White")
snake = Snake("brown")
parrot = Parrot("Green")

class Cage:
    def __init__(self, ID):
        self.ID = ID
        self.animals = []
    def add_animals(self, *animals):
        for animal in animals:
            self.animals.append(animal)
    def __repr__(self) -> str:
        
        return f'ID: {self.ID}\n' + '\t'.join(str(animal) for animal in self.animals)

c1 = Cage(1)
c1.add_animals(wolf, sheep)
c2 = Cage(2)
c2.add_animals(snake, parrot)

print(c1)
print(c2)
