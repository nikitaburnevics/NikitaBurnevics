import math
import random
r = float(input('Ievadiet riņķa līnijas rādiusu: '))
print(r)
garums = 2*math.pi*r    
print('Riņķa līnijas garums:', "%.2f"%garums)
laukums = math.pi*math.pow(r,2)
print('Riņķa līnijas laukums:', "%.2f"%laukums)

k1 = float(input('Ievadiet taisleņķa trijstūra pirmās katetes garumu: '))
k2 = float(input('Ievadiet taisleņķa trijstūra otrās katetes garumu: '))
hipotenuza = math. sqrt(math.pow(k1,2)+math.pow(k2,2))
print('Taisleņķa trijstūra hipotenūzas garums:', "%.2f"%hipotenuza)
print('Gadījuma skaitlis no 0 - 1: ', random.random())