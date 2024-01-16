faila_nosaukums = 'mana_klase.txt'

#mēģināt atvērt failu un lasīt datus
try:
    with open(faila_nosaukums,'r',encoding='UTF-8') as fails:
        for rindina in fails:
            dati = rindina.split() #katru rindiņu sadala pa vārdiem
            #pārbaudīt vai pietiek datu
            if len(dati) >=3:
                vards = dati[0]
                uzvards = dati[1]
                vecums = dati[2]

                print(f'Vārds:{vards} Uzvārds:{uzvards} Vecums:{vecums}')
            else:
                print('Kļūda: Nepietiekami daudz datu failā.')
except FileNotFoundError:
    print(f'Kļūda: Fails"{faila_nosaukums}" nav atrasts.')
except Exception as e:
    print(f'Kļūda: neparedzēta kļūda - {e}')

        

