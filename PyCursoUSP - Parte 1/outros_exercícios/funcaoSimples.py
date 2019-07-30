def soma(x, y, z):

    '''
    Função soma de dois números
    '''
    return x + y + z


def multiplica(x, y, z):
    '''
    Função que multiplica de dois números
    '''
    return x * y * z


def total_Caracteres(x, y, z):
    '''
    soma dos caracteres de 3 palavras
    '''
    return len(x)+len(y)+len(z)


def funcao_fixa_nome():
    '''
    Função que retorna sempre a mesma coisa
    Não existe parâmetros
    '''
    return 'rodrik'


def fatorial(n):
    '''
    Calcula n fatorial
    '''
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado


def coeficiente_binomial(n, k):
    ''' (int, int) -> int
    Calcula a combinação de n em k
    '''
    resultado = fatorial(n) / (fatorial(k) * fatorial(n - k))
    return resultado


def leitura():
    x = -1
    while x <= 0:
        x = int(input("Digite um valor: "))
    return x


def troca(x, y):
    aux = x
    x = y
    y = aux


# Teste função fatorial
def teste_fatorial():
    if fatorial(0) == 1:
        print('certo')
    else:
        print('errado')

    if fatorial(1) == 1:
        print('certo')
    else:
        print('errado')

    if fatorial(2) == 2:
        print('certo')
    else:
        print('errado')

    if fatorial(3) == 6:
        print('certo')
    else:
        print('errado')

    if fatorial(4) == 24:
        print('certo')
    else:
        print('errado')

    if fatorial(5) == 120:
        print('certo')
    else:
        print('errado')
