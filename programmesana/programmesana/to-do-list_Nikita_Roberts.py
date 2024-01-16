todo = {   #Vārdnīca "todo" kur glabājās dati
    'darba_nosaukums': [],
    'darba_status': [],
    'nodosanas_termiņš': []
}

while True:   #
    izvelne = input("""Ko vēlaties darīt? 
                    1 - izprintēt visus darāmos darbus
                    2 - pievienot darāmo darbu
                    3 - izdzēst darāmo darbu
                    4 - iziet no programmas 
                    5 - eksportēt datus teksta failā \n """)
    izvelnes_atbilde = int(izvelne) # Lietotājam ir izvēle uzpiest (1, 2, 3, 4, 5) atkarība kādu darbību tas vēlēsies

    if izvelnes_atbilde == 1:  #Ja lietotājs izvēlas "1"
        if not todo['darba_nosaukums']:  #Pārbauda vai vārnīcā ir kāds pievienots darbs
            print("Jums nav pievienotu nevienu darbu.")
        else:
            for i in range(len(todo['darba_nosaukums'])): #
                nosaukums = todo['darba_nosaukums'][i] #
                statuss = todo['darba_status'][i] #
                termiņš = todo['nodosanas_termiņš'][i] #Tiek parādīts viss saraksts
                print(f"Darba nosaukums: {nosaukums}; Darba statuss: {statuss}; Nodosanas termins: {termiņš}")

    if izvelnes_atbilde == 2: #Ja lietotājs izvēlas "2"
        kuru_darbibu_pirmo = int(input("Kādā darba uzdevumu jūs vēlaties prioritizēt? (1 - darba nosaukumu, 2 - darba statusu, 3 - nodošanas termiņu): "))
        #Tiek pajautāts kuru darbību lietotājs prioritizēs
        if kuru_darbibu_pirmo == 1: #Ja lietotājs izvēlas "1"
            darba_nosaukums = input('Ievadiet jaunā darba nosaukumu: ')
            darba_status = input('Ievadiet darba statusu: (aktīvs/neaktīvs): ')
            if darba_status not in["aktīvs", "neaktīvs"]:  #Ja nav ievadīts "aktīvs" vai "nepareizs" tad programma parādīs nepareizus datus
                print("Nepareizi dati")
                continue
            nodošanas_termiņš = input('Ievadiet nodošanas termiņu: ')
        if kuru_darbibu_pirmo == 2: #Ja lietotājs izvēlas "2"
            darba_status = input('Ievadiet darba statusu: (aktīvs/neaktīvs): ')
            if darba_status not in["aktīvs", "neaktīvs"]:
                print("Nepareizi dati")
                continue
            darba_nosaukums = input('Ievadiet jaunā darba nosaukumu: ')
            nodošanas_termiņš = input('Ievadiet nodošanas termiņu: ')
        if kuru_darbibu_pirmo == 3:
            nodošanas_termiņš = input('Ievadiet nodošanas termiņu: ')
            darba_nosaukums = input('Ievadiet jaunā darba nosaukumu: ')
            darba_status = input('Ievadiet darba statusu: (aktīvs/neaktīvs): ')
            if darba_status not in["aktīvs", "neaktīvs"]: #Ja lietotājs izvēlas "3"
                print("Nepareizi dati")
                continue
        
        if kuru_darbibu_pirmo == 4: #Ja lietotājs uzpiež "4" programma beidzas
            break


        todo['darba_nosaukums'].append(darba_nosaukums)
        todo['darba_status'].append(darba_status)
        todo['nodosanas_termiņš'].append(nodošanas_termiņš)

    if izvelnes_atbilde == 3:
        darba_nonemsana = input("Ievadiet darāmā darba nosaukumu, kuru jūs vēlaties dzēst: ")

        if darba_nonemsana == "4": #Ja lietotājs uzpiež "4" programma beidzas
            break

        elif darba_nonemsana in todo['darba_nosaukums']:
            index = todo['darba_nosaukums'].index(darba_nonemsana)
            todo['darba_nosaukums'].pop(index)
            todo['darba_status'].pop(index)
            todo['nodosanas_termiņš'].pop(index)
            print(f"Darāmais darbs ar nosaukumu '{darba_nonemsana}' ir noņemts.")
        else:
            print("Nepareizi dati")

    if izvelnes_atbilde == 4: #Ja lietotājs uzpiež "4" programma beidzas
        break

    if izvelnes_atbilde == 5: #Ja lietotājs izvēlas "5" tiek eksportēti dati teksta failā
        file = open('dati3.txt','a',encoding='utf-8')
        for i in range(len(todo['darba_nosaukums'])):
            nosaukums = todo['darba_nosaukums'][i]
            statuss = todo['darba_status'][i]
            termiņš = todo['nodosanas_termiņš'][i]
            file.write(f"Darba nosaukums: {nosaukums}, Darba statuss: {statuss}, Nodošanas termiņš: {termiņš}\n")
        file.close()
