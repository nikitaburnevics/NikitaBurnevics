import time
import csv

class Rekins:
    def __init__(self, vards, teksts, izmeri, cena_m3):
        self.laiks = time.localtime()
        self.vards = vards
        self.teksts = teksts
        #izveidos izmēru sarakstu no ievades
        self.izmeri = [int(x)for x in izmeri.split((','))]
        self.cena_m3 = round(float(cena_m3), 2) #noapaļo cenu ar 2 sk aiz komata
    
    def summa(self):
        darba_samaksa=15
        pvn = 21
        self.produkta_cena = round(len(self.teksts) * 1.2 + (self.izmeri[1]/100 * self.izmeri[0]/100 * self.izmeri[2]/100) / 3 * self.cena_m3, 2)
        self.pvn_summa=round(self.produkta_cena+darba_samaksa*pvn/100, 2)
        self.rekina_summa = round((self.produkta_cena+darba_samaksa)+self.pvn_summa, 2)

rekins1 = Rekins(
    input('Vards: '),
    input('Veltījums: '),
    input('Lādītes izmēri(mm)(vesels skaitlis, formāts = garums,platums,augstums): '),
    input('Cena(0.00): ')
)

rekins1.summa() #rezukātu izdruka(ļoti gara, var katru savā rindā)
print(
    f'\t-- Rēķins --\nDatums: {time.strftime("%D %H:%M",rekins1.laiks)}\nPasūtītājs: {rekins1.vards}\nVeltījuma teksts: «{rekins1.teksts}»\nIzmēri: {rekins1.izmeri[0]}x{rekins1.izmeri[1]}x{rekins1.izmeri[2]} mm\nKokmateriāla cena: {rekins1.cena_m3}€/m3\n\
    \t>>>\nProdukta cena: {rekins1.produkta_cena}€\nPVN 21%: {rekins1.pvn_summa}€\nRēķina summa: {rekins1.rekina_summa}€' # Izdrukā formatētu tekstu
)

with open('rekins.csv','a',encoding='utf8') as csvfails:
    rakstitajs = csv.writer(csvfails) #saglabā datus ailēs
    rakstitajs.writerow([time.strftime("%D%H%M",rekins1.laiks),
    rekins1.vards,
    rekins1.teksts,
    rekins1.izmeri])