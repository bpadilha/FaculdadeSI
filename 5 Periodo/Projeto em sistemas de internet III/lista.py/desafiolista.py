#n1 = float(input('Primeira nota: '))
#n2 = float(input('Segunda nota: '))
#n3 = float(input('Terceira nota: '))
#n4 = float(input('Quarta nota: '))
#n5 = float(input('Quinta nota: '))
#lista = [n1,n2,n3,n4,n5]
#print('O vetor de notas é:',lista)

vetor=[]
i=1
while i<5:
    n=int(input('Digite um número: '))
    vetor.append(n)
    i=i+1
print ('Vetor lido:',vetor)