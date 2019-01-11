# =============================================================================
# Escreva um programa que receba um número inteiro na entrada,
# calcule e imprima a soma dos dígitos deste número
# =============================================================================

num = input('Digite um número inteiro: ')
ext = len(num)
num = int(num)
valor_inicial = num
x = []
n = 0

while n < ext:
    x.append(num % 10)
    num = num // 10
    n += 1
print('A soma dos dígitos de %d é %d' % (valor_inicial, sum(x)))

# =============================================================================
# # Teste
# para número = 123
# saída = 6
# =============================================================================
