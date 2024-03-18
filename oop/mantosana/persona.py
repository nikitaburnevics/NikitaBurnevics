class person: #bāzes klase
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def output(self):
        print(self.name,self.age)

#klase student mantos no person klases
class student(person):
    
    def __init_(self,name,study_year):
        #pirmo divu lauku uzstādīšana un izdrukāšana notiek caur bāzes klases funkcionalitāti
        super().__init__(name,age) #bāzes klases konstruktors
        self.study_year=study_year

    def output(self): #metodes pārdefinēšana (overriding)
        super().output #bāzes klases output
        print(self.study_year) #izdrukā specifisko lauku



p = person('peter',20)
p.output() # personas izdruka


s=student('Jānis',19,2) 
s.output()

#studentu kā persoas izduka(bez gada)
super(student,s).output()