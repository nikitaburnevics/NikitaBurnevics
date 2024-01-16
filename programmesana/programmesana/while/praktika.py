reiz = 7
for i in range(1, 13):
    print('Cik ir ',i,'x',reiz,'?')
    minejums = input()

    if minejums == 'stop':
        break #ar break programma beidzas

    if minejums == 'izlaist':
        print('tieks izlaists')
        continue
    atb = i*reiz #glabā pareizās atbildes
    if int(minejums) == atb:
        print('Pareizi')
    else:
        print('Nepareizi, atbilde ir',atb)


