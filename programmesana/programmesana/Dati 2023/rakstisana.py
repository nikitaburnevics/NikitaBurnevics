fails = open('dati.txt','w',encoding='UTF-8')
#w arī izveido neeksistējošu failu no jauna

#ieraksta failā datus
saraksts = ['Alūksne\n','Valmiera\n','Balvi\n']
fails.writelines(saraksts) #ieraksta failā
fails.write('Puķes lol')

fails.close() #aizver

#pārraksta faila(kopijas) saturu
fails = open('dati_copy.txt','w+',encoding='UTF-8')
fails.write('Es gribu ēst!!!!')
fails = open('dati_copy.txt','w+',encoding='UTF-8')
print(fails.read()) #parāda faila saturu uz ekrāna
fails.close()

fails = open('dati_copy.txt','a+',encoding='UTF-8')
fails.write('\naizmirsu paņemt klaviatūru')
fails.close