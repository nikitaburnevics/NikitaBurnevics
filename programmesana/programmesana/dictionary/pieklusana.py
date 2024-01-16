#izveidot vārdnīcu, kas satur sarakstu
valstis = {
    'Somija':['Helsinki','Rovaniemi','Tampere','Kemijarvi','Jyvaskyle'],
    'Norvēģija':['Oslo','Bergena','Arendāla','Trumse','Molde'],
    'Dānija':['Kopenhāgena','Odense','Esbjerga','Aarhus','Ronne']
}
#1. variants ar for cilku
for atslega, vertiba in valstis.items():
    for i in vertiba:
        print(atslega,':',i)
    print('----------------------')

#2. variants ar for ciklu vienai atslēgu grupai
for i in valstis['Dānija']:
    print(i)

#iegūt pirmās 3 pilsētas no somijas
print(valstis['Somija'][:3])

#tas pats tikai pēdējās divas no norvēģijas + noņemtas iekavas un atdalīts ar komatu
print(', '.join(valstis['Norvēģija'][-2:]))


#iegūst 2. līdz 5. pilsētu no Dānijas
print(valstis['Dānija'][1:5])
#tas pats bez iekavām print(', '.join(valstis['Dānija'][1:5]))