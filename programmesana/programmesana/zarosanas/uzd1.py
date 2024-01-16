result = int(input('Ievadiet rezultātu '))
if result >= 100:
    print('rezultāts nevar būt lielāks par 100')
elif result < 0:
    print('rezultāts nevar būt mazāks par 0')
elif result >= 90:
    print('Atzīme ir 10')
elif result >= 70:
    print('Atzīme ir 7')
elif result >= 40:
    print('Atzīme ir 4')
else:
    print('tests nav nokārtots')