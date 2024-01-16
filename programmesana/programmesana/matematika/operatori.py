print('ievadiet 3 skaitļus')
x = int(input())
y = int(input())
z = int(input())

#loģiskais and
if x>0 and y>0 and z>0:
    print('visi skalitļi lielāki par 0')
else:
    print('vismaz viens skaitlis nav lielāks vai vienāds par 0')

#loģiskais or
if x>0 or y>0 or z>0:
    print('viens skalitlis lielāks par 0')
else:
    print('neviens nav lielāks par 0')
