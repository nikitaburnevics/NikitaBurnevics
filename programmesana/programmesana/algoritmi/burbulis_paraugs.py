'''Programma ļauj lietotājam ievadīt skaitļus,
pēc tam tos sakarto ar bubbleSort
tajā pašā programma uztaisīt f-ju quickSort un selectionSort
papildināt, noformēt pēc saviem ieskatiem'''
def burbulis(saraksts):
    saraksta_garums = len(saraksts) #kopejais saraksta garums
    for i in range(saraksta_garums):
        for j in range(0, saraksta_garums-i-1): #elements peld uz augsšu nonākot pareizajā vietā
            #izlaiž pēdējo(sakārtoto) elementu
            if saraksts[j]>saraksts[j+1]: #ja patiess, tad notiek apmaiņa
                saraksts[j],saraksts[j+1]=saraksts[j+1],saraksts[j]

def sakartot():
    saraksta_garums = int(input('Ievadiet skaitļu skaitu sarakstā: '))
    if saraksta_garums <0:
        print('Saraksta garums nerīkst būt negatīvs')
        exit()

    saraksts = []

    for i in range(saraksta_garums):
        skaitlis = int(input(f'Ievadiet {i+1}. skaitli: '))
        saraksts.append(skaitlis)

    burbulis(saraksts) #tiek sakārtots saraksts
    print('Sakārtots saraksts:')
    for skaitlis in saraksts:
        print(skaitlis,'', end='')

sakartot()


