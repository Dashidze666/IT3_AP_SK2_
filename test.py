import random
class VesmirnaLod:
    def __init__(self, nazev:str, palivo:int):
        self.nazev = nazev
        self.palivo = palivo
    
    def predstav_se(self):
        return f"Zde lod {self.nazev}"
    
    def let_na(self, cil:str):
        self.cil = cil
        if self.palivo >= 10:
            self.palivo -= 10
            return f"Zahajuji podsvětelný let na {self.cil}. Zbývá paliva: {self.palivo}%"
        else:
            return f"Needostatek paliva pro let!"

class PozemskyKriznik(VesmirnaLod):
    def __init__(self, nazev, velitel:str, palivo:int):
        super().__init__(nazev, velitel, palivo)
        self.velitel = velitel

    def predstav_se(self):
        return super().predstav_se(f"Zde pozemský křižník {self.nazev}, velí {self.velitel}")
    
    def let_na(self, cil):
        return super().let_na(cil)
     


class PuddleJumper(VesmirnaLod):
    def __init__(self, nazev, maskovani:bool, palivo:int):
        super().__init__(nazev, maskovani, palivo)
        self.maskovani = maskovani
    
    def predstav_se(self):
        return super().predstav_se(f"Zde antický Jumper {self.nazev}")
    
    def let_na(self, cil):
        return super().let_na(cil)
    
    def zamaskuj_se(self):
        if self.maskovani == True:
            if not self.maskovani:
                return f"Jumper 1 : Maskování AKTIVOVÁNO"
            



class Teltak(VesmirnaLod):
    def __init__(self, nazev, palivo:int, naklad = []):
        super().__init__(nazev, naklad, palivo)
        self.naklad = naklad

    def naloz_naklad(self, polozka:str):
        self.polozka = polozka
        self.naklad.append(polozka)
        return f"Na lod {self.nazev} bylo naloženo: {self.polozka}"     
    


Daedalus = PozemskyKriznik("Daedalus", "Aragon", 20)
print(Daedalus.predstav_se())
print(Daedalus.let_na())

Atlantis = PuddleJumper("Atlantis", "Leon")
print(Atlantis.predstav_se())
print(Atlantis.maskovani())  


flotila = [Daedalus, Atlantis]
spolecny_cil = "Planeta Lantea"

for lode in flotila:
    print(VesmirnaLod.predstav_se)
    print(VesmirnaLod.let_na(spolecny_cil))