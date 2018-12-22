"""
Receba 3 números inteiros na entrada e imprima

crescente

se eles forem dados em ordem crescente. Caso contrário, imprima

não está em ordem crescente
"""
print('Entre com três números inteiros')
num1 = int(input('Primeiro: '))
num2 = int(input('Segundo: '))
num3 = int(input('Terceiro: '))

if num3 > num2 and num2 > num1:
    print('crescente')
else:
    print('não está em ordem crescente')