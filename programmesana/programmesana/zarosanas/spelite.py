import random
gajieni = ['akmens','skeres','papirs']

cilveka_gajiens = input('ievadi gājienu: ')
dators_gajiens = random.choice(gajieni)

print(f'Cilvēks: {cilveka_gajiens} vs. Dators: {dators_gajiens}')

if cilveka_gajiens == dators_gajiens:
    print('Neizšķirts!!!!!!')
elif cilveka_gajiens == 'akmens' and dators_gajiens == 'skeres':
    print('Tu uzvarēji!')
elif cilveka_gajiens == 'papirs' and dators_gajiens == 'akmens':
    print('Tu uzvarēji')
elif cilveka_gajiens == 'skeres' and dators_gajiens == 'papirs':
    print('Tu uzvarēji!')

else:
    print('Dators uzvar!')