import random
from datetime import datetime

class Animal:
    def __init__(self, species:str, name:str, birthYear:int, checkupYear:int = 0, energy:int = 100):
        self.species = species
        self.name = name
        self.birthYear = birthYear
        self.chekcupYear = checkupYear
        self.energy = energy
        pass

zviratko = Animal("Pes", "Domestos", 2015)    