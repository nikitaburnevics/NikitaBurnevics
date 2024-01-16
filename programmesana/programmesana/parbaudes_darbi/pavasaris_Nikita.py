import math

def faktorials(n): #definēta funkcija 'faktoriāls' ar parametru n
        
        return 1 if (n==1 or n==0) else n * faktorials(n - 1) #ja n ir 0 vai 1 - atgriež 1. Ja cits - izrēķina faktoriālu

def zvaigznites():

    print('*******************************************************')

def tuksums():
    print()
    print()


def virsraksts(): 
    global skaitlis

    print('Faktoriāla aprēķināšana')

    zvaigznites()

    skaitlis = int(input('Ievadiet veselu, pozitīvu skaitli(mazāku par 13)\n')) 

    if skaitlis>13: #ja ievadītais skaitlis ir lielāks par 13, tad pasaka, ka skaitlis ir pārāk liels

        print('Ievadītais skaitlis ir pārāk liels!')

    elif skaitlis<0: #nedrīkst būt arī mazāks par 0

        print('Ievadītais skaitlis nedrīkst būt mazāks par 0!')

    else: #ja viss atbilst nosacījumiem, tad izrēķina un izprintē faktoriālu

        faktorials(skaitlis)

        print('Faktoriāls:',faktorials(skaitlis))


turpinat = 'j'

while turpinat == 'j':
    
     virsraksts()

     turpinat = input('Vai vēlaties turpināt darbu?(j-jā, citi taustiņi-nē)\n') #pēc funkcijas 'virsraksts' izpildes prasa vai vēlaties turpināt

     if turpinat != 'j': #ja lietotājs uzspiež jabko, kas nav 'j' - beigas

        tuksums()

        print('Paldies!')

        exit()

     else:  #ja uzspiež 'j' izprintē 2 tukšumus un cikls sākas no jauna
          tuksums()
    