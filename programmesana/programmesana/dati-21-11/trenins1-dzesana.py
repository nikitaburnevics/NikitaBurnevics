file_name = 'dzest.txt'
delete_me = 'Drīz būs Ziemassvētku brīvdienas!'

try:
    with open(file_name,'r',encoding='UTF-8') as data:
        #r atver failu lasīšanai un saglabā mainīgajā
    #readlines ielasa visas rindas no faila un saglabā tās sarakstā
        rows = data.readlines()

    with open(file_name, 'w',encoding='UTF-8') as data:
        #atver rakstīšanai

        for row in rows: #iet cauri visām saraksta rindām
            if delete_me not in row:
                data.write(row)
        #ja neatrod vārdu tad šī rinda ieraksta šo rindu atpakaļ failā
        #ignorējot vai izdzēšot rindas kuras atbilst
    print(f'Rindas ar vārdu "{delete_me}" ir veiksmīgi dzēstas no faila "{file_name}".')

except FileNotFoundError:
    print(f'Kļūda: data "{file_name}" nav atrasts.')
except Exception as e:
    print(f'Kļūda: Neparadzēta kļūda "{e}".')