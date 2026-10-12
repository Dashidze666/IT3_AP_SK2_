class Hero:
    def __init__(self, jmeno:str, lvl:int, lokace:str = "Obchod"):
        self.jmeno = jmeno
        self.lvl = lvl
        self.lokace = lokace
        pass
    def pokrik(self):
        return "AAAAAAAAAAAAA!!!!!!!"
    
    def predstav_se(self):
        return f"Jsem {self.jmeno} mam {self.lvl} lvl"
    
    def kde_jsi(self):
        return f"Ted jsem ve miste, {self.lokace}"
    
    def presun_se(self, nMisto:str):
        self.misto = nMisto
        return f"Přesunul se na nové místo, {nMisto}"
    
hero = Hero("Batman", 80)    
print(hero.pokrik())
print(hero.predstav_se())
print(hero.kde_jsi())
print(hero.presun_se("Okno"))