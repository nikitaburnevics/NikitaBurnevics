from abc import ABC, abstractmethod



class Ediens(ABC):
    def __init__(self,nosaukums,cena):
        self.nosaukums = nosaukums
        self.cena = cena
    def apraksts(self):
        pass
    
class Deserts(Ediens):
    def __init__(self,nosaukums,cena,piedevas):
        super().__init__(nosaukums, cena)
        self.piedevas = piedevas
    def apraksts(self):
        pass

class pamatEdiens(Ediens):
     def __init__(self,nosaukums,cena):
        super().__init__(nosaukums,cena)

while True: 
    #ievades dati
    nosaukums = input('\nIevadiet ēdiena nosaukumu: ')
    cena = float(input('Ievadiet ēdiena cenu: '))
    tips = input('Ievadiet ēdiena tipu (deserts vai pamatēdiens): ')

    #ja ēdiena tips ir deserts, programma piedāvā uzrakstīt piedevas un ierakstīt informāciju failā
    if tips == 'deserts':
        piedevas = input('Ievadiet piedevas, atdalot tās ar komatu: ')
        ieraksts = input('Vai vēlaties ierakstīt informāciju failā? (jā/nē): ')

        if ieraksts == 'jā':
            fails = open('gurmans_Nikita.txt','a',encoding='UTF-8')
            saraksts = str([nosaukums, cena, tips, piedevas])+'\n' #saraksts pārtaisīts par str, lai var ierakstīt failā + \n, lai viss būtu jaunā rindā
            fails.writelines(saraksts) #ieraksta failā
            print('Dati ir ierakstīti failā!\n******************************\n')

            turpinat = input('Vai vēlaties turpināt programmu? ("Stop", lai pārtrauktu | "jā", lai turpinātu): ')
            if turpinat == 'jā':
                continue
            else:
                exit('******************************\n')
        else:
            turpinat = input('Vai vēlaties turpināt programmu? ("Stop", lai pārtrauktu | "jā", lai turpinātu): ')
            if turpinat == 'jā':
                continue
            else:
                exit('******************************\n')


    elif tips == 'pamatēdiens': #ja kā tipu izvēlas pamatēdienu, uzreiz piedājā ierakstīt visu failā
        ieraksts = input('Vai vēlaties ierakstīt informāciju failā? (jā/nē): ')
        if ieraksts == 'jā':
            fails = open('gurmans_Nikita.txt','a',encoding='UTF-8')
            
            saraksts = str([nosaukums, cena, tips])+'\n'
            fails.writelines(saraksts) #ieraksta failā
            print('Dati ir ierakstīti failā!\n******************************\n')
            turpinat = input('Vai vēlaties turpināt programmu? ("Stop", lai pārtrauktu | "jā", lai turpinātu): ')
            
            if turpinat == 'jā':
                continue
            else:
                exit('******************************\n')
        else:
            turpinat = input('Vai vēlaties turpināt programmu? ("Stop", lai pārtrauktu | "jā", lai turpinātu): ')
            if turpinat == 'jā':
                continue
            else:
                exit('******************************\n')
    else:
        exit('Nepareizi ievadīts ēdiena tips')