
def burbulis(saraksts):
    saraksta_garums = len(saraksts) #kopejais saraksta garums
    for i in range(saraksta_garums):
        for j in range(0, saraksta_garums-i-1): #elements peld uz augsšu nonākot pareizajā vietā
            #izlaiž pēdējo(sakārtoto) elementu
            if saraksts[j]>saraksts[j+1]: #ja patiess, tad notiek apmaiņa
                saraksts[j],saraksts[j+1]=saraksts[j+1],saraksts[j]

def sakartot():
    dati = {'rezultats': [], 'vards':[]} 
    dati['vards'] = []  
    dati['rezultats'] = []
    
    saraksta_garums = int(input('Ievadiet studenta saraksta izmēru(<=10): '))
    if saraksta_garums <=0:
        print('Saraksta izmēram ir jābūt lielākam par 0')
        exit()
    elif saraksta_garums > 10:
        print('Saraksta izmēram ir jābūt mazākam par 10')
        exit()
    saraksts = list(dati.keys())

    for i in range(saraksta_garums):
        vards = input(f'\nIevadiet {i+1} studenta vārdu: ')
        rezultats = input(f'\nIevadiet {i+1} studenta rezultātu rezultātu: ')
        dati['vards'].append(vards)
        dati['rezultats'].append(rezultats)

    burbulis(saraksts) #tiek sakārtots saraksts

    print('Sakārtots saraksts:')
    for a in range(0,saraksta_garums):
        print('Studenta vārds:',dati[saraksts[a]])
        print('Studenta rezultāts:',saraksts[a],'\n')


sakartot()