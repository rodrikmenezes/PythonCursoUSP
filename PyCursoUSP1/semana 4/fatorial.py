# =============================================================================
# Escreva um programa que receba um número natural n na entrada
# e imprima n! (fatorial) na sáida
# =============================================================================

n = int(input('Digite o valor de n: '))
valor_inicial = n
resultado = n
while n != 1:
    if n == 0 or n == 1:
        resultado = 1
        n = 2
    else:
        resultado = resultado * (n - 1)
    n -= 1

print('O resultado de %d fatorial é %d' % (valor_inicial, resultado))

# =============================================================================
# # Testes
# fatorial(0) == 1:
# fatorial(1) == 1:
# fatorial(2) == 2:
# fatorial(3) == 6:
# fatorial(4) == 24:
# fatorial(5) == 120:
# =============================================================================
