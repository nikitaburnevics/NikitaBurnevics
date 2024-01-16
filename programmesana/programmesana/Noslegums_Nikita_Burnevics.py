import datetime

def iegut_datus(eksperimenta_nosaukums,laiks,vards,vieta):
    global dati #globalizē mainīgo
    dati = [eksperimenta_nosaukums,laiks,vards,vieta] #saliek datus sarakstā

def saglabat_datus():
    file_name = 'eksperimenta_dati.txt'
    text = str(dati) #pārveido sarakstu par 'string', lai var ielikt failā

    try:   #liek failā. try, lai lietotājs var saprast kas par erroru
        with open(file_name,'a',encoding='UTF-8') as fails:
            fails.write('\n'+text)
        print(f'\nRindas ar vārdiem "{text}" ir veiksmīgi pievienotas "{file_name}".')

    except FileNotFoundError: 
        print(f'Kļūda: fails "{file_name}" nav atrasts.')
    except Exception as e: 
        print(f'Kļūda: Neparadzēta kļūda "{e}".')



def iziet(): #beidz programmu
    exit('Programma beidzas, Paldies par izmantošanu :)')

def galvena():
    print('-----------------------------------------------------------')
    print('Labdien! \nProgrammā var pierakstīt savus eksperimentus :)\n')

    eksperimenta_nosaukums = input('Ievadiet eksperimenta nosaukumu: ')
    #ja lietotājs jebkurā brīdī ievada iziet, stop vai exit, programma beidzas
    if eksperimenta_nosaukums == 'exit' or eksperimenta_nosaukums == 'iziet' or eksperimenta_nosaukums == 'stop':
        iziet()
    else:
        laiks = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        vards = input('Ievadiet jūsu vārdu: ')

        if vards == 'exit' or vards == 'iziet' or vards == 'stop':
            iziet()
        else:    
            vieta = input('Ievadiet eksperimenta veikšanas vietu: ')
            if vieta == 'exit' or vieta == 'iziet' or vieta == 'stop':
                iziet()
            else:
                
                iegut_datus(eksperimenta_nosaukums,laiks,vards,vieta)
                saglabat_datus()

#cikls, lai viss atkārtojas
while True:
    galvena()