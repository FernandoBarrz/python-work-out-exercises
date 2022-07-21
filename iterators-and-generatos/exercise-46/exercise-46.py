# Exercise number 46 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1


class MyEnumerate:
    def __init__(self, data):
        self.data = data
        self.index = 0


    def __iter__(self):
        return self


    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration

        value = (self.index, self.data[self.index])
        self.index += 1
        return value

for i, v in MyEnumerate("Perro"):
    print(f'{i} - {v}')