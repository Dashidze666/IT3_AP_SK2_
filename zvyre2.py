import random
class Zvire:
    def __init__(self, jmeno:str, vek:int, misto:str = "bouda"):
        self.jmeno = jmeno
        self.vek = vek
        self.misto = misto
        pass
    def zvuk(self):
        return "???"
    
    def predstav_se(self):
        return f"Jsem {self.jmeno} a je mi {self.vek}"
    
    def kde_jsi(self):
        return f"Jsem v místě zvaném {self.misto}"
    
    def jdi_na(self, nMisto:str):
        self.misto = nMisto
        return f"Šel jsem na {nMisto}"


class Pes(Zvire):
    def __init__(self, jmeno, vek, plemeno, misto = "bouda"):
        super().__init__(jmeno, vek, misto)
        self.plemeno = plemeno

    def zvuk(self):
        return ("HAF HAF!!!!")    
    
    def aport(self):
        return f"{self.jmeno} přinesl míč..."
    
    def vycesat(self):
        if(random.randint(0,1) >0):
            return f"{self.jmeno} utekl před tvým kartáčem"
        else:
            return f"{self.jmeno} se nechal vyčesat!"
        
    def predstav_se(self):
        return f"{super().predstav_se()} jsem {self.plemeno}"
    


class Kocka(Zvire):
     def __init__(self, jmeno, vek, barva, misto = "Dům"):
        super().__init__(jmeno, vek, misto)
        self.barva = barva

     def zvuk(self):
        return ("Miau Miau!!!!")    
    
     def utok(self):
        return f"{self.jmeno} tě naštvaně poškrábala!"
    
     def pohladit(self):
        if(random.randint(0,1) > 0):
            return self.utok()
        else:
            return f"{self.jmeno} se nechala pohladit!"

class Had(Zvire):
    def __init__(self, jmeno, vek, delkaCm: int, jedovaty:bool, misto = "Les"):
        super().__init__(jmeno, vek, misto)    
        self.delkaCm = delkaCm
        self.jedovaty = jedovaty    

    def zvuk(self):
        return "sssssss"
    def predstav_se(self):
        if self.jedovaty:
            typ = "jedovatý"
        else:
            typ = "škrtič"
        return f"ssssss....já jsem {self.jmeno}, měřim {self.delkaCm} cm a jsem {typ} "         

betka = Had("Bětka", 8, 250, False)
print(betka.predstav_se())      

luiza = Kocka("Luiza", 6, "Zelenaa", "Dům")
print(luiza.jmeno)
print(luiza.zvuk())
print(luiza.utok())
print(luiza.pohladit())
print("-" * 20)

walter = Pes("Walter", 13, "ChiChuaChua", "Obchod")
print(walter.jmeno)
print(walter.plemeno)
print(walter.kde_jsi())
print(walter.zvuk())
print(walter.aport())
print(walter.vycesat())
print(walter.predstav_se())
print("-" * 20)


zvire = Zvire("Šoral", 50)
print(zvire.jmeno)
print(zvire.vek)
print(zvire.misto)

print(zvire.zvuk())
print(zvire.predstav_se())
print(zvire.kde_jsi())
print(zvire.jdi_na("Kadeřnictvi"))
print(zvire.kde_jsi())






zvire2 = Zvire("Wolfram", 32, "PentHouse")
print(zvire2.jmeno)
print(zvire2.predstav_se())    
print(zvire2.kde_jsi())
print(zvire2.jdi_na("Klokánek"))


zoo = [walter, luiza, betka]

for obyvatel in zoo:
    print(obyvatel.predstav_se())
    print(obyvatel.zvuk())
    print("-" * 20)