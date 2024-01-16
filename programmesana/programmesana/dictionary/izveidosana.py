#ar inicializācijas virkni
#key:value
dd = {'četri':(4,'four'), 'divi':(2,'two'), 'trīs':(3,'three')}
print(dd) #izdrukā vārdnīcu
print(len(dd)) #vārdnīcas garums
print(dd.keys()) #atgriež atslēgas (četri, divi, trīs)
print(dd.values()) #atgriež vērtības
print(' '.join(dd.keys())) #noņem iekavas. priekšā pēdiņās tas, ar ko atdala

#fromkeys metode vārdnīcas izveidošanai
dati = ('viens','divi','trīs')
vertiba = input('Vērtība: ')
vardnica = dict.fromkeys(dati,vertiba)
print(vardnica)
