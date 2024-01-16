import math

def nepareizi():
    print('ievadiet pareizus datus')
    exit()

linoleja_cena = float(input('ievadiet linoleja cenu: '))
if linoleja_cena <0:
    nepareizi()

rulla_platums = float(input('ievadiet ruļļa platumu: '))
if rulla_platums <0:
    nepareizi()

telpas_platums = float(input('ievadiet telpas platumu: '))
if telpas_platums <0:
    nepareizi()

telpas_garums = float(input('ievadiet telpas garumu: '))
if telpas_garums <0:
    nepareizi()

materiala_daudzums = math.ceil(telpas_platums/rulla_platums)
materiala_daudzums = materiala_daudzums*telpas_garums

atlikums = telpas_platums//rulla_platums
atlikums = telpas_platums-rulla_platums*atlikums
atlikums = atlikums*telpas_garums

izmaksas = round(materiala_daudzums*linoleja_cena,2)
print('izmaksas:',izmaksas,'EUR')
print('Atlikums:',atlikums,'m^2')
