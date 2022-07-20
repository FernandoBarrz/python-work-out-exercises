class Cage:
    def __init__(self, ID):
        self.ID = ID
        self.animals = []
    def add_animals(self, *animals):
        for animal in animals:
            self.animals.append(animal)
    def __repr__(self) -> str:
        
        return f'ID: {self.ID}\n' + '\t'.join(str(animal) for animal in self.animals)