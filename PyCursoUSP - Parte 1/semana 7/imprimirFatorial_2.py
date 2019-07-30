''' Esta é uma solução mais inteligente para o probelam de imprimier fatorial '''

print('Digite um número inteiro positivo e o programa retorna o fatorial')
print('Digite um número negativo para terminar')
print()

n = int(input('Número: '))
while n >= 0:
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n -= 1
    print(fatorial)
    print()
    n = int(input('Número: '))
