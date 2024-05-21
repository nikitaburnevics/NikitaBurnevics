from abc import ABC, abstractmethod
import csv
print('Programma palīdz grāmatvežiem sarakstīt un saglabāt datus par darbiniekiem un viņu algām')

class Dati(ABC): #abstrakta klase "Dati", kurā ir izveidoti lauki: "darbinieku_skaits", "vards_uzvards", "personas_kods", "alga", "papildus_funkcionalitate".
    def __init__(self,darbinieku_skaits, vards_uzvards, personas_kods, alga, papildus_funkcionalitate): 
        self.darbinieku_skaits=darbinieku_skaits 
        self.vards_uzvards=vards_uzvards 
        self.personas_kods=personas_kods 
        self.alga=alga 
        self.papildus_funkcionalitate=papildus_funkcionalitate 

class Ievada_datus(Dati): #klase "Ievada_datus", kura manto abstraktu klasi "Dati"
    def ievada_darbinieku_skaits(self): #funkcija ievada_darbinieku_skaits, kura ļauj lietotājam ievadīt darbinieku skaitu
        while True: #Ielikts while ciklā
            self.darbinieku_skaits = int(input("Ievadiet darbinieku skaitu: ")) #lietotājs ievada darbinieku skaitu
            if self.darbinieku_skaits <=0: #Ja darbinieku skaits ir mazāks vai vienāds ar "0", programma liek ievadīt pareizus datus
                print("Ievadiet pozitīvu skaitli!")
                continue
            else:
                break

    def ievada_vards_uzvards(self): #funkcija "ievada_vards_uzvards", kura ļauj lietotājam ievadīt vārdu un uzvārdu
        while True:
            self.vards_uzvards = input("Ievadiet darbinieka vārdu un uzvārdu: ") #lietotājs ievada darbinieka vārdu un uzvārdu
            if self.vards_uzvards.isdigit(): #Ja lietotājs ievada skaitli, tad programma prasa lietotājam ievadīt pareizus datus
                print("Ievadiet pareizus datus!")
                continue
            else:
                break

    def ievada_personas_kods(self): #funkcija "ievada_personas_kods", kura lietotājam ļauj ievadīt darbinieka personas kodu.
        while True:
            personas_kods = input("Ievadiet darbinieka personas kodu (formātā 000000-00000): ") #lietotājs ievada darbinieka personas kodu
            if len(personas_kods) == 12 and personas_kods[6] == '-': #Ja personas kods simbolu virkne ir vienāda ar 12 un personas kodu simbolu virknē 7 elements ir "-"
                try:
                    int(personas_kods[:6]) 
                    int(personas_kods[7:]) 
                    self.personas_kods = personas_kods
                    break
                except ValueError: #ja personas kods nav cipari, programma liek ievadīt pareizi
                    print("Personas kods nav pareizā formātā. Lūdzu, ievadiet to atkārtoti.")
            else: #ja personas kods nav 12 simboli vai 7 elemets nav "-", tad programma liek lietotājam ievadīt pareizi
                print("Personas kods nav pareizā formātā. Lūdzu, ievadiet to atkārtoti.")
                continue

    def ievada_alga(self): #funkija "ievada_alga", kura ļauj ievadīt darbinieka algu
        while True:
            self.alga = input("Ievadiet darbinieka saņemto algu: ") #lietotājs ievada darbinieka algu
            try: #Tiek pārbaudīts vai self.alga ir float, ja nav tad programma liek lietotājam ievadit pareizus datus
                self.alga = float(self.alga)
                break
            except ValueError:
                print("Ievadiet pareizus datus!")

    def ievada_papildus_funkcionalitate(self): #funkcija "ievada_papildus_funkcionalitate", kura ļauj lietotājam izveidot un ievadīt jaunus datus par darbinieku
        self.papildus_funkcionalitate = [] #Lists, kurā tiek saglabāti dati par papildus funkcionalitāti
        papildus_funkcionalitate = input("Vai Jūs vēlaties papildus funkcionalitāti? (j/n): ") #Tiek jautāts lietotājam vai viņš/viņa vēlas izveidot un ievadīt jaunus datus par lietotāju
        while True:
            if papildus_funkcionalitate == 'j': #ja lietotājs vēlas lietotājam ievadīt papildus datus par darbinieku jeb papildus funkcionalitāti
                papildus_funkcionalitate1 = input("Ievadiet papildus funkcionalitāti: ") #Tiek prasīts no lietotāja ievadīt papildus funkcionalitates vārdu
                papildus_funkcionalitate2 = input("Ievadiet papildus funkcionalitātes aprakstu: ") #Tiek prasīts no lietotāja ievavīd papildus funkcionalitates aprakstu
                self.papildus_funkcionalitate.append((papildus_funkcionalitate1, papildus_funkcionalitate2)) #Lists tiek papildināts ar ievadītajiem datiem
                break
            elif papildus_funkcionalitate == 'n': #Ja lietotājs šim darbiniekam nevēlas ievadīt papildus datus, tad no cikla tiek iziets ārā
                break 
            else: #Ja tiek ievadīti nepareizi dati, tad programma liek ievadīt pareizus
                print('Ievadiet pareizus datus!')
                continue

class Rezultats(Ievada_datus): #klase "Rezultāts", kura manto klasi "Ievada_datus"
    darbinieku_dati = [] #Lists, kur tiks saglabāti dati par darbiniekiem
    def darbinieku_dati_rezultats(self): #funkcija darbinieku_dati_rezultats, kura sagalabā visus datus par visiem darbiniekiem
        for i in range(self.darbinieku_skaits): #For cikls, kas iziet cauri tik daudz reizes, cik ir ievadīti darbinieki
            print(f"Ievadiet {i+1}. darbinieka datus:")
            self.ievada_vards_uzvards() 
            self.ievada_personas_kods()
            self.ievada_alga()
            self.ievada_papildus_funkcionalitate()
            self.darbinieku_dati.append((self.vards_uzvards, self.personas_kods, self.alga, self.papildus_funkcionalitate)) #Listā "darbinieku_dati" tiek pievienoti visi darbienieku dati

    def izprinte_datus(self):
            print("\n"f"Darbinieku skaits: {self.darbinieku_skaits}")
            for i, darbinieks in enumerate(self.darbinieku_dati, 1):
                print(f"\n{i}. Darbinieka dati; Vārds un uzvārds: {darbinieks[0]}, Personas kods: {darbinieks[1]}, Alga: {darbinieks[2]} €", end='')
                for i in darbinieks[3]: #Tik reizes cik tika ievadīta papildus funkcionalitātes, tās tiek izvadīta pie tiem darbinieka datiem, kur lietotājs tos ievadīja.
                    print(f", {i[0]}: {i[1]}", end='')

    def saglabat_datus(self):
            fails = input("\n" + 'Ievadiet faila nosaukumu(csv): ') # izveidotajā funkcijā lietotājam pajautā csv faila nosaukumu, kurā tiks glabāts rezultāts.
            with open(fails + '.csv','a',encoding = 'utf8') as csvfails: # izveido failu, ko lietotājs ievadīja.
                rakstitajs = csv.writer(csvfails) # izveido mainīgo, kas ievada datus failā.
                rakstitajs.writerow(['Vards uzvards', 'Personas kods', 'Alga', 'Papildus funkcionalitāte'])# failā pievieno virsrakstu katrai šūnai: vards, personas kods, alga, papildus funkcionalitāte.
                print(f'Dati tika saglabāti {fails}.csv failā.')
                for darbinieks in self.darbinieku_dati:
                    darbinieku_dati = [darbinieks[0], darbinieks[1], darbinieks[2]] # izveido mainīgo, kas satur rezultātu no lietotāja, ko lietotājs bija ievadījis katram darbiniekam, bez papildus funkcionalitātes.
                    if darbinieks[3]: 
                        for dati in darbinieks[3]:
                            rakstitajs.writerow(darbinieku_dati + [f"{dati[0]}: {dati[1]}"]) # ja tika ievadīta funkcionalitāte darbiniekam, tad tā tiek izvadīta kopā ar pārējiem darbinieka datiem.
                    else:
                        rakstitajs.writerow(darbinieku_dati) #ja nav papildus funkcionalitāte, tad tiek saglabāti dati bez papildus funkcionalitates

while True:
    ievade = Rezultats("", "", "", "", "")
    ievade.ievada_darbinieku_skaits()
    ievade.darbinieku_dati_rezultats()
    ievade.izprinte_datus()
    ievade.saglabat_datus()
    while True:   
        turpinat = input('\nVai vēlaties turpināt?(j/n): ') 
        if turpinat == 'j':
            break
        elif turpinat == 'n':
            print("Uzredzēšanos!")
            exit()
        else:
            print('Ievadiet pareizus datus!')
            continue
    