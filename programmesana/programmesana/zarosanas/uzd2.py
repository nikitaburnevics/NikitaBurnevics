forma = input('Vai ir iesniegta forma?(ja/ne): ')
if forma == 'ja':
    aps = input('Vai forma ir apstiprinta?(ja/ne): ')
else:
    print('Jāiesniedz forma') 
if aps == 'ja':
    kred = input('Vai vajag kredītu?(ja/ne): ')
elif aps == 'ne':
    print('Jāgaida formas apstiprināšana')
if kred == 'ja':
    print('Paņem kredītu un samaksā!')
elif kred == 'ne':
    print('Samaksā!')
x = int(input('Cik tālu dzīvo? '))
if x >=60:
    vajag = input('Vai vajag kopmītni?(ja/ne) ')
elif x <= 60:
    print('Nebūs kopmītnes')
if vajag == 'ja':
    print('Paraksti līgumu, izvēlies kursu un gatavs.')
if vajag == 'ne':
    print('Paraksti līgumu, izvēlies kursu un gatavs.')