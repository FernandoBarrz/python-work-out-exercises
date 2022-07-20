# Exercise number 45 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1

from Animal import Animal
from Cage import Cage

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


class Zoo:
    def __init__(self):
        self.cages = []

    def add_cages(self, *cages):
        for cage in cages:
            self.cages.append(cage)
            
    def animals_by_color(self, color):
        return [animal 
                for cage in self.cages
                for animal in cage.animals
                if animal.color == color]

    def animals_by_legs(self, number_legs):
        return [animal 
                for cage in self.cages
                for animal in cage.animals
                if animal.number_of_legs == number_legs]
    def number_of_legs(self):
        return sum(animal.number_of_legs
                    for cage in self.cages
                    for animal in cage.animals)
    
    def __repr__(self) -> str:
        return  '\n'.join(str(cage) for cage in self.cages)

wolf = Wolf('Grey')
sheep = Sheep("White")
snake = Snake("brown")
parrot = Parrot("Green")

c1 = Cage(1)
c1.add_animals(wolf, sheep)
c2 = Cage(2)
c2.add_animals(snake, parrot)

z = Zoo()
z.add_cages(c1, c2)

print(z)
print(z.animals_by_color('white'))
print(z.animals_by_legs(4))
print(z.number_of_legs())
