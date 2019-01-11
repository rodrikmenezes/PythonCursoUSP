# =============================================================================
# O programa deve receber os parâmetros a, b, e c da equação ax^2 + bx + c,
# respectivamente, e imprimir o resultado das raízes (se houver)
# =============================================================================

print('Entre com os parâmetros de uma equação do segundo grau')
print('ax² + bx + c = 0')

a = float(input('a = '))
b = float(input('b = '))
c = float(input('C = '))

delta = b**2 - 4 * a * c

if delta < 0:
    print('esta equação não possui raízes reais')
elif delta == 0:
    raiz = -b / (2 * a)
    print('a única raiz desta equação é', raiz)
else:
    import math
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    if raiz1 < raiz2:
        print('as raízes da equação são', raiz1, 'e', raiz2)
    else:
        print('as raízes da equação são', raiz2, 'e', raiz1)

# =============================================================================
# # Teste #
# a = 12; b = 4; c = 20 -> não há raízes reais
# a = 2; b = 10; c = -20 -> raiz1 = -6,5311 e raiz2 = 1,5311
# a = 2; b = 0; c = 0 -> raiz única = 0
# =============================================================================
