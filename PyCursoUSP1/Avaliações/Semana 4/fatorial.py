"""
Escreva um programa que receba um número natural n na entrada 
e imprima n! (fatorial) na saída.
"""
n = int(input('Digite o valor de n: '))
resultado = n
while n != 1:
  if n == 0 or n == 1:
    resultado = 1
    n = 2
  else:
    resultado = resultado * (n - 1)
  n -= 1
print(resultado)
