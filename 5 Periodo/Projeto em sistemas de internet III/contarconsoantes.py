from typing import List

letras = []
i = 1
while i <= 0:
    letras.append(input("Letra: "))
    i += 1

i = 0
cont = 0

while i <= 9:
    if letras[i] not in 'aeiou':
         cont += 1
    i += 1
print ("Foram contatos %d consoantes" %cont)