def nepareizi():
    print('ievadiet pareizus datus')
    exit()
pasazieri = int(input('Cik cilvēki brauks? ')) #cilvēks ievada cik cilvēki brauks
if pasazieri >4:
    print('Pasažieru skaits nedrīkst būt lielāks par 4')  
    exit()
elif pasazieri <=0:                                   #line 2-7 ja vairāk par 4 vai mazāk par 0 pasažieriem programma beidzas
    nepareizi()
laiks = int(input('cik pulkstens? '))
if laiks <0 or laiks >24:
    nepareizi()
elif laiks >= 6 and laiks <= 24:                              #line 9-15 izskaita kāds būs tarifs dienas vai nakts, un ja ievada neeksistējošo laiku programma beidzas
    tarifs = 0.57
else:
    tarifs = 0.67
taksometrs = input('vai stacijā ir taksometrs?ja/ne ') #cilvēks ievada vai ir taksometrs
if taksometrs == 'ja':
    izsaukums = 1.25
elif taksometrs == 'ne':             #line 16-20 atkarībā no atbildes nosaka cenu
    izsaukums = 2.20
else:
    nepareizi()  #21,22,23 - ja ievada kaut ko izņemot ja/ne programma beidzas
pacietigstaksists = input('taksists ir gatavs gaidīt?ja/ne ') #cilveks ievada vai taksists ir gatavs gaidīt
if pacietigstaksists == 'ja':
    gaidisana = int(input('cik laiks nogaidīts?(min) ')) #cilvēks ievada cik laiku taksists gaidīja
    if gaidisana <0:
        nepareizi() #28,29,30 - ja ievada skaitli mazāku par 0, programma beidzas
else:
    print('taksists jūs negaidīs')
    exit()
cels = int(input('cik tālu tālu jānobrauc?(km) '))  #cilvēks ievada cik tālu jābrauc
if cels <=0:
    print('ievadiet pareizus datus')  #34,35,36 - ja ievada skaitli mazāku vai vienādu par 0, programma beidzas
    exit()
elif cels >20:
    taksists = input('vai taksists brauks tik tālu?ja/ne ')
    if taksists == 'ne':                                          #37-41 papildus funkcionalitāte (kāds taksists nebrauks tālāk par 20 km)
        print('taksists nebrauks tik tālu')
        exit()
else:
    izsaukums = round(izsaukums, 2)
    maksa = tarifs*cels
    maksa = round(maksa, 2)
    gaidisana = gaidisana*0.13                                   #43-48 noapaļo līdz 2 cipariem aiz komata
    gaidisana = round(gaidisana, 2)
    kopcena = izsaukums+maksa+gaidisana
    print()
    print('cena par nolīgšanu/izsaukumu', izsaukums,"EUR")
    print('cena par nobraukto ceļu pēc tarifa', maksa,"EUR")     # veic aprēķinus un izprintē čeku
    print('cena par gaidīšanu', gaidisana,"EUR")
    print('kopējā cena -', kopcena,"EUR")
