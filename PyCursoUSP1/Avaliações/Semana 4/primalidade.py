
"""
Escreva um programa que receba um número inteiro positivo na entrada
e verifique se é primo.
Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".
"""
x = int(input('Digite um número inteiro: '))

divisores = []
n = 1

while n <= x:
    if x % n == 0:
        # esta lista recebe todos os números divisores de x
        divisores.append(n)
n += 1
if len(divisores) > 2 or x == 1:
    print('não primo')
    print('seus divisores são: ', divisores)
else:
    print('primo')
