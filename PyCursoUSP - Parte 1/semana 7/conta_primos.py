def n_primos(n):
    """
    n_primos que recebe como argumento um número inteiro
    maior ou igual a 2 como parâmetro e devolve
    a quantidade de números primos que existem entre 2 e n
    """
    cont_primos = 0
    for i in range(2, n + 1):
        q = 1
        cont_div = 0
        while q <= i:
            if i % q == 0:
                cont_div += 1
            q += 1
        if cont_div == 2:
            cont_primos += 1
    return cont_primos
