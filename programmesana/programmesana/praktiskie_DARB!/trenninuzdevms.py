#programmā var izvēlēties vienu no veikaliem un aprēķināt vienas preces cenu. Katrā veikalā ir savas atlaides
import math
def ceks():
    print('Čeks: \nar ',atlaide,'% atlaidi:','\n',nosaukums,':', round(daudzums-daudzums*x,2),'EUR')
atbilde = 'nē'
if atbilde == 'jā':
    print()
    exit()
else:
    while atbilde == 'nē': #kamēr lietotājs uz jautājumu vai viss ir nopirkts atbildēs ar 'nē', programma sāksies no jauna
        veikals = input('Uz kuru veikalu iesim? maxima/rimi/elvi/vesko? ')   #pārbauda uz kuru veikalu iet (katram ir savas atlaides)
        if veikals == 'maxima':
            daudzums = int(input('ievadiet preču daudzumu: '))
            if daudzums <=0:
                print('preču daudzums nedrīkst būt mazāks vai vienāds ar 0')
                break
            cena = float(input('ievadiet preces cenu: '))
            nosaukums = input('ievadiet preces nosaukumu: ')
            karte = input('vai jums ir karte? jā/nē ')
            if karte == 'jā':
                x = 0.4
                atlaide = 40
                ceks()   #ja ir karte parāda cenu ar 40% atlaidi
            else:
                x = 0.3
                atlade = 30
                ceks()    #ja nav tad 30% atlaide
            atbilde = (input('Vai ir nopirkts viss, kas sarakstā? jā/nē '))


        elif veikals == 'rimi':
            daudzums = int(input('ievadiet preču daudzumu: '))
            if daudzums <=0:
                print('preču daudzums nedrīkst būt mazāks vai vienāds ar 0')
                break
            cena = float(input('ievadiet preces cenu: '))
            nosaukums = input('ievadiet preces nosaukumu: ')
            karte = input('vai jums ir karte? jā/nē ')
            if karte == 'jā':
                x = 0.5
                atlaide = 50
                ceks()
            else:
                x = 0.2
                atlaide = 20
                ceks()
            atbilde = (input('Vai ir nopirkts viss, kas sarakstā? jā/nē '))


        elif veikals == 'elvi':
            daudzums = int(input('ievadiet preču daudzumu: '))
            if daudzums <=0:
                print('preču daudzums nedrīkst būt mazāks vai vienāds ar 0')
                break
            cena = float(input('ievadiet preces cenu: '))
            nosaukums = input('ievadiet preces nosaukumu: ')
            
            if daudzums >=3:
                x = 0.3
                atlaide = 30
                ceks()
            else:
                print('Čeks: \n',nosaukums,':',cena)
            atbilde = (input('Vai ir nopirkts viss, kas sarakstā? jā/nē '))


        elif veikals == 'vesko':
            daudzums = int(input('ievadiet preču daudzumu: '))
            if daudzums <=0:
                print('preču daudzums nedrīkst būt mazāks vai vienāds ar 0')
                break
            cena = float(input('ievadiet preces cenu: '))
            nosaukums = input('ievadiet preces nosaukumu: ')
            if daudzums >=2:
                daudzums1 = math.floor(daudzums-daudzums*0.5) #daudzums1 mainīgas kur glabājas cik ir pāra preces(lai par katru otro nav jāmaksā)
                daudzums = daudzums-daudzums1
            print('Čeks: \nar katru otro preci par brīvu:','\n',nosaukums,':', round(daudzums-daudzums*0.3,2),'EUR')
            atbilde = (input('Vai ir nopirkts viss, kas sarakstā? jā/nē '))