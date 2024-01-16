rindas = 7
for i in range(1, rindas + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print('')
r = 6
for i in range(r + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")