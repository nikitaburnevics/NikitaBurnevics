file_name = 'dzest.txt'
text = 'Drīz būs Ziemassvētku brīvdienas!'

try:
    with open(file_name,'a',encoding='UTF-8') as fails:
        fails.write('\n'+text)
    print(f'Rindas ar vārdiem "{text}" ir veiksmīgi pievienotas "{file_name}".')

except FileNotFoundError:
    print(f'Kļūda: data "{file_name}" nav atrasts.')
except Exception as e:
    print(f'Kļūda: Neparadzēta kļūda "{e}".')