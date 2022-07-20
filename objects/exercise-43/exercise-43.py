# Exercise number 43 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1


class Animal:
    def __init__(self, color, number_of_legs):
        self.color = color
        self.species = self.__class__.__name__
        self.number_of_legs = number_of_legs


    def __repr__(self) -> str:
        return f'{self.color} {self.species}, {self.number_of_legs}'
        


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

print(wolf)
print(sheep)
print(snake)
print(parrot)