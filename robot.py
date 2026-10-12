class Robot:
    def __init__(self, oznaceni:str, baterie:int, ukol:str = "Skače"):
        self.oznaceni = oznaceni
        self.baterie = baterie
        self.ukol = ukol
    def zvuk(self):
        return "bzi bzi"
    
    def diagnostika(self):
        return f"Označení {self.oznaceni}, Baterie {self.baterie}"
    
    def aktivacni_ukol(self):
        return f"Ted {self.ukol}"
    
    def zadej_ukol(self, nUkol:str):
        self.ukol = nUkol
        return f"Mám ted nové zadání, {self.nUkol}"    

robot = Robot("RoboSport", 55)
print(self.zvuk())  