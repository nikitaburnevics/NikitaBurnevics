#izveidot txt failu ar nosaukumu dati2.txt
fails = open('dati2.txt','w',encoding='utf-8')

#ierakstīt failā sarakstu ar 3 pilsētām
saraksts = ['Rīga\n','Sigulda\n','Kuldīga\n']
fails.writelines(saraksts)#writelines lai var ierakstīt virkni, kur vairāk kā 1 vārds
fails.write('Hello world!')#ieraksta vienu virkni

#pārrakstīt faila saturu iz 3 valstīm
valstis = ['Latvija\n','Igaunija\n','Lietuva\n']
fails = open('dati2.txt','w',encoding='utf-8')
fails.writelines(valstis)

#vai

#pārrakstīt faila saturu uz 3 valstīm
f=open('dati2.txt','w',encoding='utf-8')
valstis={
    'Daugavpils':'Latvija',
    'Čitagonga':'Bangladeša',
    'Vladivostoka':'Krievija'
}
for object in valstis:
    f.write(valstis[object]+'\n')



