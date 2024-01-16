#programmā lietotājs var aprēķināt viena kreklu pasūtījuma izmaksas
print('Jūs sveicina labākā t-kreklu kompānija pasaulē')

def pasuti_tkreklus(skaits:int,apdruka,piegade:bool): #definēta funkcija ar 3 parametriem un to datu tipiem
    if apdruka == 'TEKSTS':
        cena = 5
    elif apdruka == 'ZIME':
        cena = 7
    elif apdruka == 'FOTO':
        cena = 20
    else:    #ja ievada nepareizus datus programma beidzas
        print('ievadiet pareizus datus')
        exit()

    rezultats = skaits*cena
    if rezultats >= 100:                     #16-26 | Atkarībā no pasūtījuma cenas iedod atlaidi un piegādi
        piegade = True
        rezultats = rezultats-rezultats*0.05  #aprēķina cenu ar 5% atlaidi
        atlaide = '5%'  
    elif rezultats >= 50:
        piegade = True
        atlaide = 'Nav'
    else:
        piegade = False
        rezultats = rezultats+15
        atlaide = 'Nav'
    
    if piegade == True: #samaina piegādi no true/false uz skaitlisko vērtību, lai pēc tam var pieskaitīt pie pasūtījuma
        piegade = 0
    else:
        piegade = 15

    print('--------------------\nČeks:\n\nJūsu Kreklu skaits:',skaits,'\nKreklu prints:',apdruka,'\nPiegāde:',piegade,'EUR','\nAtlaides:',atlaide,'\n\nKopējās izmaksas:',rezultats,'EUR\n--------------------')

try: #ieliku try, jo nekad nebiju lietojis un gribēju izmēģināt to except valueError, sanāca labi :)
    skaits = int(input("Ievadiet kreklu skaitu: "))
    if skaits <= 0:
        print('ievadiet pareizus datus') #ja ievada skaitu <=0 programma beidzas
        exit()
    apdruka = input('Kādu printu vēlaties uz krekliem? Izvēlaties no 3 variantiem:\nTEKSTS - 5 EUR\nZIME - 7 EUR\nFOTO - 20 EUR\n')

    piegade = False
    pasuti_tkreklus(skaits,apdruka,piegade)
        
except ValueError: #ja ievada nepareizu datu tipu programma beidzas
    print('Ievadiet pareizus datus') 