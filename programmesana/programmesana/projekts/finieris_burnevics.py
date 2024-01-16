listes_cena = 6.18
sturu_cena = 8.99
biezums = 18
def nepareizi():
    print('ievadiet pareizus datus')
    exit()

def materiala_izvele(materials): 
    global cena                  #globalizēta cena, lai darbojas visā kodā
    if materials == 'bērzs':
        cena = 23.92
    elif materials == 'egle':
        cena = 27.68
    elif materials == 'priede':
        cena = 31.74
    else:
        nepareizi()

standartpasutijums = input('Vai vēlaties pasūtīt podestu standarta izmērā?2x1m(jā/nē)')
if standartpasutijums == 'jā':
    garums = 1
    platums = 2
    materiala_izvele(input('izvelaties materiālu(bērzs/egle/priede)'))
    skaits = int(input('ievadiet podestu skaitu): '))
    if skaits <=0:
        nepareizi()
    else:
        materiala_daudzums = 6*(garums*platums)*skaits
        izmaksas = materiala_daudzums*cena+listes_cena+sturu_cena
        print()
        print('Pasūtīto podestu daudzums:',skaits)
        print('Cena par m^2 materiāla', cena)
        print('Pasūtījuma cena:',izmaksas)
        print('Cena ar PVN', izmaksas+0.21*izmaksas)
        exit()                                                                      #exit lai beidzas programma

else:
    garums = float(input('ievadiet podesta malas garumu(m): '))
    platums = float(input('ievadiet podesta malas platumu(m): '))
    skaits = int(input('ievadiet podestu skaitu): '))

if garums <=0 or platums <=0 or skaits <=0:
    nepareizi()
else:
    materiala_daudzums = 6*(garums*platums)*skaits #cik materiāla būs nepieciešams visam pasūtījumam

materiala_izvele(input('izvelaties materiālu(bērzs/egle/priede)'))

izmaksas = materiala_daudzums*cena+listes_cena+sturu_cena            #kopējā cena bez pvn
print()
print('podesta izmērs(m):',garums,'m x',platums,'m x',biezums,'mm')
print('podestu skaits:',skaits)
print('Nepieciešamais materiāla daudzums(m^2):', materiala_daudzums)
print('Aptuvenās izmaksas:',izmaksas,'EUR')
print('Cena ar PVN',izmaksas+izmaksas*0.21,'EUR')



