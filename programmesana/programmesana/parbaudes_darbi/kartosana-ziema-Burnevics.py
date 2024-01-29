def galvenais():

    faila_nosaukums = 'ievades_dati.txt'
    #mēģināt atvērt failu un lasīt datus
    try:
        with open(faila_nosaukums,'r',encoding='UTF-8') as fails: #atver failiņu

            main_saraksts = {} #tukša vārdnīca

            for rindina in fails:
                dati = rindina.split() #katru rindiņu sadala pa vārdiem
    
                vards = dati[0]
                vecums = dati[1]
                main_saraksts[str(vards)] = int(vecums) #saraksta visus datus vārdnīcā
        main_saraksts = sorted(main_saraksts.items(), key=lambda x:x[1]) #sakārto (laikam neizskatās pēc bubblesort)
        print('Sakārtots saraksts augošā secībā:', main_saraksts,'\n\n')
        
        saraksta_garums = len(main_saraksts) #nosaka saraksta garumu
        mazakais = main_saraksts[0] #izvēlas pirmo saraksta elementu kā mazāko, jo ir sortots
        lielakais = main_saraksts[saraksta_garums-1] #izvēlas pēdējo saraksta elementu kā lielāko
        print('Mazākais elements:',mazakais,'\n--------------------------------\nLielākais elements:',lielakais)

        sakartots = open('sakartots.txt','w',encoding='UTF-8') #uztaisa failu sakartots.txt
        saraksts = str(main_saraksts)
        sakartots.writelines(saraksts) #ieraksta failā    

    except FileNotFoundError:
        print(f'Kļūda: Fails"{faila_nosaukums}" nav atrasts.')
    except Exception as e:
        print(f'Kļūda: neparedzēta kļūda - {e}')


galvenais()




