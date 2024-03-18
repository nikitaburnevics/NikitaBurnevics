class Persona:
    def __init__(self,vards,uzvards,epasts):
        self.vards=vards
        self.uzvards=uzvards
        self.epasts=epasts

class Skolens(Persona): #manto klase persona
    def __init__(self,vards,uzvards,epasts):
        super().__init__(vards,uzvards,epasts)
        self.vid_atzime=0
    def macities(self):
        self.vid_atzime+= 0.1

class Skolotajs(Persona):
    def __init__(self,vards,uzvards,epasts,mac_prieksmets):
        super().__init__(vards,uzvards,epasts)
        self.mac_prieksmets=mac_prieksmets
    
    def macit():
        print('Mācu', self.mac_prieksmets)

skolens1=Skolens('Jānis','Bērziņš','janis.berzins@svg.lv')
print(skolens1.vards)
skolens1.macities()
print(skolens1.vid_atzime)

skolotajs1=Skolotajs('Anna','Kokle','anna.kokle@svg.lv','Zīmēšana')
