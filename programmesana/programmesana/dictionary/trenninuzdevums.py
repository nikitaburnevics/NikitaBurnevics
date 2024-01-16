#1. Atjaunināt vārdnīcā norādīto gadu ar update() metodi.
telefoni = {
    'zimols': 'Apple',
    'modelis': '14',
    'gads': '2021'
}
telefoni.update([('gads',2022)])

#2. Izdzēst visus elementu no vārdnīcas.

skolas = {
    'nosaukums': 'Gimnazija',
    'novads': 'Sigulda',
    'skolenu_skaits': 569,
    'gads': 2019
}
dict.clear(skolas)

#3. Izdzēst divus elementus no vārdnīcas(pēc izvēles) izmantojot dict.pop(key, default) metodi.

augli = {
    1: 'banani',
    2: 'aboli',
    3: 'bumbieri',
    4: 'mango'
}
augli.pop(1)
augli.pop(4) #pop strādā tikai uz 1 key

#4. Pārbaudīt vai vērtība 200 ir vārdnīcā. Ar values() metodi un if nosacījumu

skaitli = {
    'a': 100,
    'b': 200,
    'c': 300,
    'd': 400
}
if 200 in skaitli.values():
    print("Skaitlis 200 ir vārdnīcā!")