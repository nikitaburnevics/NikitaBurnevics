#tiek realizēta decimālskaitļu ievade, aprēķināts izteksmes (x+y)*(x-y)/(x-y)

#vards = input('ievadiet')
#print('vards:',vards)

x = float(input('ievadiet decimalskaitli')) #javeic konvertesana jo "input()" atgriež datus teksta veidā
print('ievadītais skaitlis:',x)
print('___________________')
y = float(input('ievadiet otru decimalskaitli'))
print('ievadītais skaitlis:',y)
print('_________________')
print('rezultats:',(x+y)*(x-y)/(x-y))


