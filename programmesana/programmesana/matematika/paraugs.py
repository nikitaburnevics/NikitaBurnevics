import math #raksta programmas sākumā tikai 1 reizi
skaitlis = 27.32
print('noapaļots uz leju:',math.floor(skaitlis)) #noapaļo uz leju
print('noapaļots uz augšu:',math.ceil(skaitlis)) #noapaļo uz augšu

print('PI vērtība:',math.pi) #PI vērtība
print(math.pow(skaitlis,3)) #kāpināšana, pirmais skaitlis ir ko kāpina, otrais pakāpe. var izmantot arī mainīgos

#skaitļu formatēšana
x = 26192/123         #/ dala ar atlikumu, // dala bez atlikuma
print('Bez formatēšanas:',x)

print('Ar formatēšanu:' "%.5f"%x)
#vai
print('Ar formatēšanu:' "{:.7f}".format(x))
