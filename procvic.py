class ChytreZarizeni:
     def __init__(self, nazev:str, mistnost:str, zapnuto:bool = False):
          self.nazev = nazev
          self.mistnost = mistnost
          self.zapnuto = zapnuto
          pass
     def prepni_stav(self):
        return f"Zařizení je {self.zapnuto}"
     
     def proved_akci(self):
          return f"Zařizení čeká na přikaz"
 

class ChytraZarovka(ChytreZarizeni):
     def __init__(self, nazev: str, mistnost: str, zapnuto: bool = False, barva:str = "bílá"):
          super().__init__(nazev, mistnost, zapnuto)
          self.barva = barva

     def proved_akci(self):
          if ({self.zapnuto} == False):
               return f"{self.nazev} svítí barvou {self.barva}"
          else:
               return f"Je zhasnuto"
          
     def zmen_barvu(self, nova_barva:str):
          self.barva = nova_barva
          return f"Aktuální barva {nova_barva}"
          
                     
class ChytraZasuvka(ChytreZarizeni):
     def __init__(self, nazev: str, mistnost: str, aktualni_odber_W:int, zapnuto: bool = False):
          super().__init__(nazev, mistnost, zapnuto)   
          self.aktualni_odber_W = aktualni_odber_W 

     def proved_akci(self, aktualni_stav:str):
          self.zapnuto = aktualni_stav
          if (self.zapnuto == True):
               return f"{self.aktualni_odber_W} ma zasuvka"


zarovka = ChytraZarovka("Samsung", "Pokoj", 300, True)
print(zarovka.proved_akci())
print(zarovka.zmen_barvu("Modra"))

zasuvka = ChytraZasuvka("Xiaomi", "kuchin", 255, True)   
print(zasuvka.proved_akci())  

domacnosti = [zarovka, zasuvka]

for zarizeni in domacnosti:
     print(zarizeni.zapnuto())
     print(zarizeni.proved_akci())




