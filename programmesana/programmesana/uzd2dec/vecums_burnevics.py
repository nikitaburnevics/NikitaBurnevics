vecums = int(input('ievadiet suņa vecumu ')) #ar input ievada vecumu
if vecums <= 0:
    print('vecums nedrīkst būt mazāks par 0') #ja vecums <= 0 pasaka ka tānevar būt
elif vecums <= 2:
    print('suns ir',vecums*10.5,'gadus vecs') #ja vecums <=2 reizina ar 10.5
else:
    print('suns ir ',(vecums-2)*4+21,'gadus vecs') #no vecuma atņem 2, sareizina ar 4 un pieskaita 21, un izdrukā
