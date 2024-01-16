fails = open('dati.txt','a',encoding='utf-8') #izveidos failu
fails.write('Ingvera sula garšo pēc suši!\n')#izveidotajā failākaut ko ieraksta (\n lai katrs jaunais teksts jaunā rindā)

fails = open('dati.txt','r',encoding='utf-8')
print(fails.read())

#w pārraksta datus
fails = open('dati.txt','w',encoding='utf-8')
fails.write('Mācos rakstīt failā\n')

fails = open('dati.txt','a',encoding='utf-8')
fails.write('Ērces ir the best!!!')


fails.close()