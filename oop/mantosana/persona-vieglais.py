class Persona:
    def __init__(self,vards):
        self.vards=vards

    def druka_vardu(self):
        print('So personu sauc',self.vards)



class Skolens(Persona): #mantošana
    def __init__(self,vards):
        Persona.__init__(self,vards)

persona1 = Persona('Jānis')
persona1.druka_vardu()

skolens1 = Skolens('Anna')
skolens1.druka_vardu()