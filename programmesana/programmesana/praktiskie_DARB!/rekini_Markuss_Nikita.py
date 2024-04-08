from datetime import datetime

class rekins:
    def __init__(self):
        self.laiks = datetime.now()
        self.vards = input('Ievadiet savu vārdu: ')
        self.teksts = input('Ievadiet veltījuma tekstu: ')
        self.platums, self.garums, self.augstums = int(input('Ievadiet izmēru milimetros\nPlatums: ')), int(input('Garums: ')), int(input('Augstums: '))
        self.materiala_cena = float(input('Ievadiet kokmateriāla cenu (EUR/m^2)'))
        
    def display(self):
        current_time = self.laiks.strftime("%H:%M:%S")
        print(f"Rēķina izveidošanas laiks: {current_time}")
        print(f"Vards:, {self.vards}, Teksts:, {self.teksts}")
        teksta_garums = len(self.teksts)
        produkta_cena = (teksta_garums) * 1.2 + (self.platums/100 * self.garums/100 *self.augstums/100) /3 * self.materiala_cena
        pvn_summa = (produkta_cena + 15)*21/100
        print('Cena bez pvn:',produkta_cena)
        print('Cena ar pvn:',pvn_summa+produkta_cena)

rekins1 = rekins()
rekins1.display()