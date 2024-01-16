menesis = input('izvēlaties mēnesi(jan/feb/mar/apr/mai/jun/jul/aug/sep/okt/nov/dec) ') #cilvēks ievada mēnesi
def dienas():
    print('mēnesī ir 30 dienas')
if menesis == 'feb':
    print('mēnesī ir 28 dienas') #ja mēnesis ir februāris pasaka ka 28 dienas
elif menesis == 'apr' or menesis == 'jun' or menesis == 'sep' or menesis == 'nov':
    dienas()
else:
    print('mēnesī ir 31 diena') #pārējos mēnešos ir 31 diena

