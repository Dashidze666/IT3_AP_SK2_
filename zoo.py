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

    def __str__(self):
        return f"{self.species} {self.name} ({self.birthYear}) - energie: {self.energy} %"

    def play(self):
        usage = random.randint(5,20)
        if self.energy >= usage:
            self.energy = self.energy - usage
            self.energy -= usage
            return f"{self.species} {self.name} spotřeboval při hře {usage}% energie a zbývá mu {self.energy}%"
        else:
            return f"{self.species} {self.name} je moc unavený. Potřebuje {usage}% enegrie, al má jen {self.energy}%"

    def feed(self):
        filled = 100 - self.energy
        self.energy = 100
        return f"{self.species} {self.name} byl nakrmen a doplnil {filled}% energie"

    def vetCheck(self):
        if self.chekcupYear < datetime.now().year:
            return f"{self.species} {self.name} musí k veterináři - platnost prohlídky skončila v roce {self.chekcupYear}"
        else:
            rozdil = self.chekcupYear - 
            return f""

zviratko = Animal("Pes", "Domestos", 2015) 
print(zviratko)
print(zviratko.play())
print(zviratko.feed())
