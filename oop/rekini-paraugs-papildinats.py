from datetime import datetime  
import csv #lai varētu strādāt ar csv
class Rekins:  
    def __init__(self,vards,teksts,izmers,materials):
        self.laiks=datetime.now()
        self.vards=vards
        self.teksts=teksts
        #izveidos izmēru sarakstu no ievades
        self.izmers=izmers
        #self.izmeri=[int(x)for x in izmeri.split((","))]
        self.materials=materials

    def izdrukat(self,apmaksa=None):
        print("Rēķins: ")
        print("Klients: ",self.vards)
        print("Veltījums: ",self.teksts)
        print("Izmērs: ",self.izmers)
        print("Materiāls: ",self.materials)
        print("Laiks: ",self.laiks)
        if apmaksa is not None:
            print("Apmaksas summa:", apmaksa)

    def aprekins(self):
        apmaksa=sum(self.izmers)*self.materials       
        return apmaksa
    
    def saglabat(self):
        datums=self.laiks.strftime("%Y-%m-%d_%H-%M-%S") 
        faila_nosaukums=f"{self.vards}_{datums}.csv" #faila nosaukums no vārda un datuma
        with open(faila_nosaukums,'w',encoding='utf8') as csvfails:
            rakstitajs=csv.writer(csvfails) #saglabā datus ailēs
            #raksta galvene
            rakstitajs.writerow(['Klients','Veltījums','Izmērs1','Izmērs2','Izmērs3','Materiāls','Apmaksas summa'])
            #raksta datms
            rakstitajs.writerow([self.vards,self.teksts]+self.izmers+[self.materials,self.aprekins()])

vards= input("Vārds: ")
teksts=input("Veltījums: ")
izmers=[int(x)for x in input("Ievadiet izmērus,atdalot ar atstarpi").split()]
materials=float(input("Ievadiet materiāla cenu: "))

r=Rekins(vards, teksts, izmers, materials)#jauns objekts no Rekins klases
apmaksa=r.aprekins()
#ieliek apamaksas summu objektā
r.apmaksa=apmaksa
r.saglabat()
r.izdrukat(apmaksa)