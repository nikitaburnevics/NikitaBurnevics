#3 un 4 izvēles strādā tad ja kādu no tām izvēlas pirmo, bet ja izvēlas pēc kādas citas - uzmet erroru. Nezinu kāpēc tā notiek

valstis = {
    'Latvija':1884000,
    'Igaunija':1331000,
    'Lietuva':2801000,
    'Cehija':10510000,
    'Ukraina':43790000,
    'ASV':331900000,
    'Kanāda':38250000,
    'Vācija':83200000,
    'Zviedrija':10420000,
    'Somija':5541000
}

while True: #kamēr lietotājs neuzrakstīs stop programa turpināsies
    izvele = input('Ko vēlaties darīt? \n1 - Sakārtot valstis pēc to nosaukumiem augošā secībā \n2 - Sakārtot valstis pēc to nosaukumiem dilstošā secībā \n3 - Sakārtot valstis pēc to iedzīvotāju skaita augošā secībā\n4 - Sakārtot valstis pēc to iedzīvotāju skaita dilstošā secībā\n5 - Pievienot jaunu valsti un iedzīvotāju skaitu \n6 - Apskatīt visas valstis \nstop - iziet no programmas\n')

    if izvele == 'stop': #kad uzraksta stop, lietotājam paziņo, ka programma beidzas
        print('--------------------')
        print('Programma beidzas')
        exit('--------------------')

    elif izvele == '1':
        valstis = sorted(valstis) #valstis tiek sakārtotas augošā secībā
        print('Valstis sakārtotas pēc nosaukumiem augošā secībā')
        print('--------------------')

    elif izvele == '2':
        valstis = sorted(valstis,reverse=True) #valstis tiek sakārtotas dilstošā secībā
        print('Vlastis sakārtotas pēc nosaukumiem dilstošā secībā')
        print('--------------------')

    elif izvele == '3':
        valstis = sorted(valstis.items(), key=lambda x:x[1]) #valstis tiek sakārtotas pēc iedz. skaita augošā secībā
        print('Vlastis sakārtotas pēc iedzīvotāju skaita augošā secībā')
        print('--------------------')

    elif izvele == '4':
        valstis = sorted(valstis.items(), key=lambda x:x[1],reverse=True) #valstis tiek sakārtotas pēc iedz. skaita dilstošā secībā
        print('Vlastis sakārtotas pēc iedzīvotāju skaita dilstošā secībā')
        print('--------------------')

    elif izvele == '5':   #nemācēju uztaisīt
        print('Jūs uzspiedāt taustiņu 5 - pievienot jaunu valsti:')
        print('Neizdevās pievienot jaunu valsti')

    elif izvele == '6':
        print('Jūs uzspiedāt taustiņu 6 - apskatīt visas valstis:')
        print(valstis)
        print('--------------------')

    else: #ja ievada kaut ko, kas nav piedāvāts izvēlē, cikls sākas no jauna
        print('Izvēlaties eksistējošu darbību!')
        print('--------------------')