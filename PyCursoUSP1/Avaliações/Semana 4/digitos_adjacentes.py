"""
Escreva um programa que receba um número inteiro na entrada e verifique 
se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. 
Caso exista, imprima "sim"; se não existir, imprima "não".
"""
x = input('Digite um número inteiro: ')
ext = len(x)
x = int(x)
numeros = []; n = 0

while n < ext:
  numeros.append(x % 10)
  x = x // 10
  n += 1
numeros.reverse()

cont = 0
for i in range(ext - 1):
  if numeros[i] == numeros[i+1]:
    cont += 1

if cont > 0:
  print('sim')
else:
  print('não')
