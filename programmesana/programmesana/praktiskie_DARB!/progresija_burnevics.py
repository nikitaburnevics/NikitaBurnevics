print('Aritmētiskās progresijas elementu aprēķins')
print('Ievadiet pirmo locekli! ')
sk1 = float(input())
print('Ievadiet differenci! ')
diff = float(input())
print('Ievadiet elementu skaitu! ')
n = int(input())
a=1

for i in range(1, n+1):
    print(a,". loceklis: ", sk1)
    sk1 = sk1+diff
    a= a+1 
    