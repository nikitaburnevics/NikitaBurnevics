lietotajvards = 'Nikita'
parole = 'nikita123'

a = input('ievadiet lietotājvārdu: ')
b = input('ievadiet paroli: ')
if a == lietotajvards and b == parole:                              #ja lietotājvārds un parole sakrīt veiksmīga pieslēgšanās
    print('Pieslēgšanās veiksmīga')
    x = int(input('Ievadiet pirmo skaitli: '))
    y = int(input('Ievadiet otro skaitli: '))                      #ievada skaitļus
    if x <0 or y < 0:                                                #pārbauda vai na negatīvi
        print('skaitļi nevar būt negatīvi')

else:
    meginajumi = 4
    while a != lietotajvards or b != parole:
        if lietotajvards == 'stop' or parole == 'stop':                     #nav ne jausmas kā likt šim strādāt
            print('Programmas beigas!')
            break
        elif meginajumi >=1:
            print('nepareizi ievadīti dati, atlikuši',meginajumi,' mēģinājumi')
            meginajumi = meginajumi-1                                       #19-23 ļauj ievadīt paroli nepareizi 5 reizes(ja ievada pareizi beidzas kods)
            a = input('ievadiet lietotājvārdu: ')
            b = input('ievadiet paroli: ')
        else:
            print('Atļauts mēģināt pieslēgties 5 reizes')  #24-26 uzraksta vairs nevar pieslēgties un beidz programmu
            break

        #nekad nekas nesanāk ar tiem cikliem