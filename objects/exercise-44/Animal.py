class Animal:
    def __init__(self, color, number_of_legs):
        self.color = color
        self.species = self.__class__.__name__
        self.number_of_legs = number_of_legs


    def __repr__(self) -> str:
        return f'{self.color} {self.species}, {self.number_of_legs}'
        
