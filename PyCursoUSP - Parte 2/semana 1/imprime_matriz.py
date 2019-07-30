"""
escreva uma função imprime_matriz(matriz),
que recebe uma matriz como parâmetro e imprime a matriz, linha por linha
"""


def imprime_matriz(A):
    n_lin = len(A)
    n_col = len(A[0])

    for i in range(n_lin):
        for j in range(n_col):

            if j == n_lin - 1:
                print(A[i][j], end=' ')
                print('\n')
            else:
                print(A[i][j], end=' ')
    return A

