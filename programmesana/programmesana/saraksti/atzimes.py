#izveidot sarakstu 'atzimes' ar punktiem(test iegūtos punktus) 
#ar for ciklu iziet cauri visam sarakstam
#ar elif uz ekrāna parādīt punktus un atzīmi
#ja >=90 - A, >=80 - B, starp 70 un 80 - C, no 61 līdz 70 - D,<= 60 - F

atzimes = [int(input('punkti: '))]
rezultats = []
for punkti in atzimes:
    if punkti >=90:
        atzime = 'A'
    elif punkti >= 80:
        atzime = 'B'
    elif punkti >=70:
        atzime = 'C'
    elif punkti >=61:
        atzime = 'D'
    else:
        atzime = 'F'
    rezultats.append([punkti, atzime])
print(rezultats)
