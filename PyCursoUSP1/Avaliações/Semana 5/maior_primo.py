def maior_primo(x):
    '''
    A função maior_primo que recebe um número inteiro maior ou igual a 
    2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função
    '''
    divisores = []
    n = 1

    while n <= x:
        if x % n == 0:
            # esta lista recebe todos os números divisores de x
            divisores.append(n)
        n += 1
    resultado = divisores[len(divisores)]

    return resultado

print(maior_primo(100))