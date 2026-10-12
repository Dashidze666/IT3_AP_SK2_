class Vozidlo:
    def __init__(self, znacka:str, rok_vyroby:int, stav_nadrze:int = 100):
        self.znacka = znacka
        self.rok_vyroby = rok_vyroby
        self.stav_nadrze = stav_nadrze

    def zvuk_motoru(self,zvuk:str = "???"):
        return zvuk
    
    def info(self):
        return f"{self.znacka}, {self.rok_vyroby}, {self.stav_nadrze}"
    
    def startuj(self, ):
        if self.stav_nadrze > 0:
            return f"Startuje {self.zvuk_motoru()}"
        else:
            return f"Došla štáva"
        
class Auto(Vozidlo):
    def __init__(self, znacka:str, rok_vyroby:int,typ_prevodovky:str, stav_nadrze:int = 100):
        super().__init__(znacka, rok_vyroby, stav_nadrze,)
        self.typ_prevodovky = typ_prevodovky 

    def zvuk_motoru(self, zvuk:str = "Wrooom"):
        return super().zvuk_motoru((zvuk))        

    def zatrub(self):
        return f"BEEEEP BEEEEEP"    

class Moped(Vozidlo):
    def __init__(self, znacka:str, rok_vyroby:int, ma_slapadla:bool = True, stav_nadrze:int = 100):
        super().__init__(znacka, rok_vyroby, stav_nadrze)
        self.ma_slapadla = ma_slapadla

    def zvuk_motoru(self, zvuk:str = "Trrrrrrr"):
        return super().zvuk_motoru((zvuk))        

    def slapej(self):
        return f"Brbrbrbbrbrbbrbbrbrbr" 
    
Auto = Auto("Shevrolet", 2016, "automat")
Moped = Moped("Honda", 2008, True)



garaz = [Auto, Moped]

for vozidlo in garaz:
    print(vozidlo.info())
    print(vozidlo.startuj())


