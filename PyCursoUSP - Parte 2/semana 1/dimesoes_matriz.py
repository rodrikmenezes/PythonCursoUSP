"""
Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e
imprime as dimensões da matriz recebida, no formato iXj
"""


def dimensoes(matriz):

    i = len(matriz)
    j = len(matriz[0])
    return print(str(i) + 'X' + str(j))
