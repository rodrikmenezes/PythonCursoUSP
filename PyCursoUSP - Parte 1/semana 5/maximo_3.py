def maximo(x, y, z):
    ''' (int, int, int) -> int
    A função maximo que recebe 3 números inteiros como parâmetro e
    devolve o maior deles
    '''
    # x é o maior
    if x > y and x > z:
        resultado = x
    elif y > x and y > z:
        resultado = y
    else:
        resultado = z
    return resultado


# =============================================================================
# # Testes #
# print(maximo(30, 14, 10))  # deve devolver 30
# print(maximo(0, -1, 1))  # deve devolver 1
# =============================================================================
