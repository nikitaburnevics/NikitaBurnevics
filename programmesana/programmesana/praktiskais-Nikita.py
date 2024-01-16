dati = {'Lietotājvārds': [], 'Vārds':[]} 

dati['Vārds'] = ''
dati['Lieotājvārds'] = ''


#virkne =input('Ievadet vārdu virkni: ')
#virkne = virkne.split()
#virkne = list(virkne)

vards = input('Ievadi vārdu: ') 
lietotajvards = input('Ievadi lietotājvārdu: ')

dati['Vārds'].append(vards)
dati['Lietotājvārds'].append(lietotajvards)

print(dati)



#print(virkne[0])
faila_nosaukums = input('Ievadiet faila nosaukumu, kurā eksportēt datus')

#nestrādā
