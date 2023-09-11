
cukura_cena = 2

abolu_daudzums = float(input('Ievadiet cik jums ir āboli (Kg) ja nav pilnds skaitlis atdalītājs ir ".":\n')) #lietotājs ievada cik viņam ir āboli

cukura_daudzums_vajadz = float(input("Ievadiet cik jums ir nepieciešams cukurs (g/kg):\n")) #lietotājs ievada cik viņam ir nepieciešams cukurs uz 1 kg ābolu

kopsumma = abolu_daudzums*cukura_daudzums_vajadz*cukura_cena #specifikācijā dotā funkcija cenas aprēķināšanai
kopsumma = round(kopsumma, 2) #rezultāts noapaļots līdz simtdaļām 

print('-------------------------------\nGala izmaksas ir ', kopsumma, "€", "\n-------------------------------") #"skaists" atbildes noformējums