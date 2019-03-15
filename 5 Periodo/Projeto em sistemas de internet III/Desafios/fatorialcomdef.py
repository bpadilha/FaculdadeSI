def fatorial (x):
    f=1
    while x >= 1:
        f = f * x
        x = x - 1
    return f

numero = int(input('Digite um número: '))

print (f'O fatorial de {numero} é {fatorial(numero)}.')