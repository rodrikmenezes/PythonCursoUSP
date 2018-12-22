"""
O programa deve receber os parâmetros a, b, e c da equação ax^2 + bx + c,
respectivamente, e imprimir o resultado na saída da seguinte maneira:
Quando não houver raízes reais imprima:

esta equação não possui raízes reais

Quando houver apenas uma raiz real imprima:

a raiz desta equação é X

onde X é o valor da raiz

Quando houver duas raízes reais imprima:

as raízes da equação são X e Y

onde X e Y são os valor das raízes.

Além disso, no caso de existirem 2 raízes reais, 
elas devem ser impressas em ordem crescente, ou seja, X deve ser menor que Y
"""

print('Entre com as informações para cálculo das raízes de uma equalçao do segundo grau')
print('ax² + bx + c = 0')

a = float(input('a = '))
b = float(input('b = '))
c = float(input('C = '))

delta = b**2 - 4 * a * c

if delta < 0:
    print('esta equação não possui raízes reais')
elif delta == 0:
    raiz = -b / (2 * a)
    print('a raiz desta equação é', raiz)
else:
    import math
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    if raiz1 < raiz2:
        print('as raízes da equação são', raiz1,'e',raiz2)
    else:
        print('as raízes da equação são', raiz2,'e',raiz1)


