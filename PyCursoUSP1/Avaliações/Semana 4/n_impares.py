"""
Receba um número inteiro positivo na entrada e imprima os n
primeiros números ímpares naturais. 
"""

n = int(input('Digite o valor de n: '))

ext = 2 * n

for i in range(ext):
  if i % 2 != 0:
    print(i)
  i += 1