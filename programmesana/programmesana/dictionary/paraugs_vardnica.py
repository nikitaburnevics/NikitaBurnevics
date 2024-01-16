#izveidot vārdnīcu ar skaitļa tipa atslēgām
dict1 = {
    6: 'tev',
    1: 'garšo',
    3: 'āboli'
}
print('Vārdnīva ar skaitļa tipa atslēgām:')
print(dict1[6])
print(dict1[1])
print(dict1[3])

##izveidot vārdnīcu ar non-numeric keys
dict2 = {
    'Auglis': 'Ābols',
    'Augļu_karalis': 'Mango',
    'Sezonas_auglis': 'Apelsīns',
}
print(dict2['Auglis'])
print(dict2['Augļu_karalis'])
print(dict2['Sezonas_auglis'])
print(' '.join(dict2.values()))