import random
from datetime import datetime

class Server:
    def __init__(self, hostname:str, os:str, deployYear:int, warrantaYear:int = 0, storageFree:int = 100):
        self.hostname = hostname
        self.os = os
        self.deployYear = deployYear
        self.warrantyYear = warrantaYear
        self.storageFree = storageFree
        pass

    def __str__(self):
        return f"{self.hostname} ({self.os} {self.deployYear}) - volné místo: {self.storageFree}%"

    def saveData(self):
        usage = random.randint(5, 20)
        if self.storageFree >= usage:
            self.storageFree = self.storageFree - usage
            self.storageFree -= usage
            return f"Na server {self.hostname} se uložila data (zabrano {usage}%). Zbývá {self.storageFree}% volného místa."
        else:
            return f"Chyba:Na serveru {self.hostname} není místo! Potřeba {usage}%, ale k dispozici je jen {self.storageFree}%."

    def cleanDist(self):
        cleaned = 100 - self.storageFree
        self.storageFree = 100
        return f"Disky na serveru {self.hostname} byly pročištěny. Uvolnilo se {cleaned} místa"
    
    def warrantyCheck(self):
        if self.warrantyYear < datetime.now().year:
            return f"Konec záruky u serveru {self.hostname} = {self.warrantyYear}"
        else:
            return f"U serveru {self.hostname} zbýva do konce záruky = {self.warrantyYear - datetime.now().year} roky"


web = Server ("Web-Main","Ubuntu Linux", 2018, 2029, 80)
web1 = Server ("Host","Windows", 2014, 2029, 50)
web2 = Server ("Gimpl","MacOs", 2019, 2025, 20)
print(web) 
print(web.saveData())
print(web.cleanDist())
print(web.warrantyCheck())
print("*"*50)
print(web1) 
print(web1.saveData())
print(web1.cleanDist())
print(web1.warrantyCheck())
print("*"*50)
print(web2) 
print(web2.saveData())
print(web2.cleanDist())
print(web2.warrantyCheck())
print("*"*50)

class ServerRoom:
    def __init__(self, name):
        self.name = name
        self.webs = []
        pass 

    def addServer(self, server:Server):
        self.webs.append(server)
        return f"Byl přidán nový server: {server.hostname}"
    
    def showServers(self):
        if len (self.webs) == 0:
            print (f"Serverovna je prádzná!")
        else:
            print(f"Server v {self.name}:")
            for server in self.webs:
                print("---->", server)
                
    def oldestServers(self):
        if len(self.webs) == 0:
            return None
        theOldest = min(self.webs, key = lambda a: a.deployYear)            
        return theOldest
    
    def avgStorage(self):
        if len(self.webs) == 0:
            return 0
        return sum(web.storageFree for web in self.webs)/ len(self.webs)

serverroom = ServerRoom("SOUEPL Datacentrum")

serverroom.showServers()
print(serverroom.addServer(web))
print(serverroom.addServer(web1))
print(serverroom.addServer(web2))
serverroom.showServers()
print(f"{serverroom.avgStorage():.1f} %")

oldest = serverroom.oldestServers()
if oldest:
    print(f"Nejstarsi server v serverovne je {oldest.hostname} {oldest.deployYear} {oldest.warrantyYear}")
print(serverroom.webs[2].deployYear())


print("*"*50)
for serv in serverroom.webs:
    print(serv.warrantyCheck())