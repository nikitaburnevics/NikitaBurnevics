#uzraksti programmu kurā ir 2 saraksti + abus apvieno
mans_saraksts = ['svece', 2, 'sāls']  #pirmais elements ir ar indeksu 0
otrs_saraksts = ['karstmaizes', 'brauniji', 'kafija']
liels_saraksts = mans_saraksts+otrs_saraksts
print(liels_saraksts)

#nokopēt saraksta vērtības un ielikt tās jaunā sarakstā
milzis = ['zupa', 'dzērvene', 'tastatūra']
jauns = list(milzis)
print(milzis)
print(jauns)

#izveidot sarakstu ar 4 krāsu nosaukumiem, atrast katra elementa garumu
krasas = ['zils', 'zaļš', 'dzeltens', 'sarkans']
jauns_saraksts = [] #tukšs saraksts
for krasa in krasas:
    burti = 0 #katru reizi palaižot sarakstu atgriežas uz 0
    for burts in krasa:
        burti +=1 #katru reizi pieskaita 1
pagaidu_saraksts = [krasa, burti]
jauns_saraksts.append(pagaidu_saraksts)
print(jauns_saraksts)

#pagājušais tikai īsāk
krasas = ['zils', 'zaļš', 'dzeltens', 'sarkans']
for krasa in krasas:
    print(len(krasa)) #len parāda garumu



