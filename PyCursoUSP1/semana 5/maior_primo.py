def maior_primo(x):
    '''
    A função maior_primo que recebe um número inteiro maior ou igual a
    2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função
    '''
    divisores_primos = []
    # este laço percorre todos os valores de 1 a x
    for i in range(1, x + 1):
        # este laço verifica se o valor i é primo
        n = 1
        divisores_i = []
        while n <= i:
            if i % n == 0:
                divisores_i.append(n)
            n += 1
        # verifica se i é primo ou não
        if len(divisores_i) == 2:
            divisores_primos.append(i)
    # retorna o último elemento da lista de divisores primos
    return divisores_primos[len(divisores_primos) - 1]
