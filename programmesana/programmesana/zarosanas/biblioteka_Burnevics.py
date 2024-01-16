laiks = input('Vai ir kāds laikā nenodots izdevums?(ja/ne) ')
if laiks == 'ja':
    print('nedrīkst ņemt neko')
    exit()
elif laiks == 'ne':
    pieprasijums = input('Vai tas ir pieprasīts izdevums?(ja/ne)')
if pieprasijums == 'ja':
    print('Saņemat uz 3 dienām')
    exit()
elif pieprasijums == 'ne':
    gramata = input('Vai tā ir grāmata?(ja/ne) ')
if gramata == 'ja':
    personals = input('Vai jūs esat personāls?(ja/ne)')
elif gramata == 'ne':
    print('Saņemat uz 7 dienām')
    exit()
if personals == 'ja':
    print('Sņemat uz 28 dienām')
    exit()
elif personals == 'ne':
    print('Saņemat uz 14 dienām')
    exit()

