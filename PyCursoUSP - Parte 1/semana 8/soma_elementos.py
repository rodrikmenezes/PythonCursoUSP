'''
Escreva a função soma_elementos que recebe como parâmetro uma lista
com números inteiros e devolve um número inteiro correspondente
à soma dos elementos da lista recebida.
'''

def soma_elementos(lista):
    soma = 0
    for elemento in lista:
        soma = soma + elemento
    return soma

# teste
# lista = [2,4,6,20]
# soma_elementos(lista)) -> 32
# print(soma_elementos(lista))