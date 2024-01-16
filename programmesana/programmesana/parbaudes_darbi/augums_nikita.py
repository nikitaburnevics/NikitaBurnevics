augumi = {'vards': [], 'augums':[]} 
augumi['vards'] = ['Jāzeps','Zane','Jānis','Gustavs','Anna','Kate','Rūta','Kārlis','Artjoms','Reinis','Paula','Uģis']  
augumi['augums'] = ['172','185','164','184','162','164','165','167','177','184','165','180']

print(augumi)
darbiba = 1
while darbiba != '4': #kamēr darbība nebūs 4, tikmēr kods turpināsies un prasīs ievadīt pareizu vērtību
    darbiba= input('1 - parādīt visus datus\n2 - pievienot datus\n3 - dzēst datus\n4 - iziet\nKo vēlaties darīt? ')

    if darbiba == '1': #ja ievada 1 tad uz izdrukā visus vārdus un augumus
      
        print('Jūs uzspiedāt taustiņu 1 - visi dati: ')
        print(augumi)
        print('-------------------------')

    elif darbiba == '2': #ja ievada 2 tad var pievienot jaunus datus

        print('Jūs uzspiedāt taustiņu 2 - pievienot datus:')
        vards = input('Ievadi vārdu: ') #lietotājs ievada vārdu un augumu
        augums = input('Ievadi augumu(cm): ')
        augumi['vards'].append(vards)
        augumi['augums'].append(augums)
        print('Jūs pievienojāt vārdu:',vards,'un augumu:',augums,'cm')
        print('-------------------------')

    elif darbiba == '3': #ja ievada 3 tad var dzēst

        print('Jūs uzspiedāt taustiņu 3 - dzēst datus: ')
        vards = input('Ievadiet vārdu: ')
        vertiba = augumi['vards'].index(vards)  #vērtība, ko pēc tam izņems no datiem
        augumi['vards'].pop(vertiba) #iznem no datiem konkrētas vertibas
        augumi['augums'].pop(vertiba)
        print('Jūs izdzēsāt vārdu',vards)
        print('atjaunotās vērtības:',augumi)
        print('----------------------------')
    elif darbiba == '4': #ja ievada 4 programma beidzas
        print('Jūs uzspiedāt taustiņu 4 - programma aizvērta')
        exit()
    else:
        print()
        print('ievadiet eksistējošu darbību')            
        print('---------------------------------')