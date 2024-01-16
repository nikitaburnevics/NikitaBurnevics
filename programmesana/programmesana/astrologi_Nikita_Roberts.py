import random
while True: #Programma ielikta ciklā
    turpinasana = input('Nospiediet jebkuru taustiņu, lai parādītu prognozes. Uzrakstiet stop, lai iziet.\n \n')
    if turpinasana == 'stop': #Ja lietotājs uzsaksta "stop" programma beidzās.
        exit('\nPaldies par programmas izmantošanu!\n')
    else: #Kamēr vien nav uzrakstīts "stop" programma turpināsies
        horoskopa_zimes = ['Auns','Vērsis','Dvīņi','Vēzis','Lauva','Jaunava','Svari','Skorpions','Strēlnieks','Mežāzis','Ūdensvīrs','Zivis']
        file = open('prognozes.txt', 'r', encoding='UTF-8')  #Tiek atvērts teksta fails "prognozes.txt"
        content = file.readlines() #Tiek izlasītas teksta faila līnijas
        print('\nPrognozes visiem horoskopiem:\n\n')
        for i in horoskopa_zimes: #cikls, lai var izdrukāt prognozi katram horoskopam no saraksta 'horoskopa_zimes'
            pirmais_teikums = content[random.randint(0,38)] #Nejauši tiek izvēlēta viena rinda
            otrais_teikums = content[random.randint(0,38)]
            tresais_teikums = content[random.randint(0,38)]
            while pirmais_teikums == otrais_teikums or pirmais_teikums == tresais_teikums: #Ja pirmais teikums ir vienāds ar otro vai trešo, pirmais teikums tiek izvēlēts no jauna līdz tas nesakrīt ar otro un trešo
                pirmais_teikums = content[random.randint(0,38)]
            while otrais_teikums == tresais_teikums: #Ja otrais teikums ir vienāds ar trešo, tad izvēlas otro no jauna līdz tas nesakrīt ar trešo
                otrais_teikums = content[random.randint(0,38)]
            if pirmais_teikums != otrais_teikums and pirmais_teikums != tresais_teikums and otrais_teikums != tresais_teikums: #Ja neviens teikums nesakrīt ar citu, tad tiek izprintētas prognozes
                print(i+': -Prognoze šodienai-','\n','\n'+pirmais_teikums+otrais_teikums+tresais_teikums,'\n')
            else: #Ja kāds teikums sakrīt ar citu, tad jāmēģina vēlreiz
                print('Neparedzēta kļūda, mēģiniet vēlreiz!')    