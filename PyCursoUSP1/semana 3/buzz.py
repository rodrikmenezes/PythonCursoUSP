# =============================================================================
# Receba um número inteiro na entrada e imprima: Buzz
# se o número for divisí­vel por 5. Caso contrário,
# imprima o mesmo número que foi dado na entrada
# =============================================================================

numero = int(input('Entre com um número inteiro: '))

if numero % 5 == 0:
    print('Buzz')
else:
    print(numero)
