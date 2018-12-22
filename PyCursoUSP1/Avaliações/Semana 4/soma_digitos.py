"""
Escreva um programa que receba um número inteiro na entrada,
calcule e imprima a soma dos dígitos deste número na saída
"""
num = input('Digite um número inteiro: ')
ext = len(num)
num = int(num)
x = []
n = 0

while n < ext:
    x.append(num % 10)
    num = num // 10
    n += 1
print(sum(x))
