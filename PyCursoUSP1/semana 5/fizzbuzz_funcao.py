# =============================================================================
# Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve
# 'Fizz' se o número for divisível por 3 e não for divisível por 5;
# 'Buzz' se o número for divisível por 5 e não for divisível por 3;
# 'FizzBuzz' se o número for divisível por 3 e por 5;
# Caso a função não seja divisível 3 e também não seja divisível por 5,
# ela deve devolver o número recebido como parâmetro.
# =============================================================================


def fizzbuzz(numero):
    ''' (int) -> (int)
    Se for divisível por 3 -> fiz
    Se for divisível por 5 -> buzz
    '''
    if numero % 3 == 0 and numero % 5 == 0:
        resultado = 'FizzBuzz'
    elif numero % 3 == 0:
        resultado = 'Fizz'
    elif numero % 5 == 0:
        resultado = 'Buzz'
    else:
        resultado = numero

    return resultado

# =============================================================================
# # Testes fizzbuzz #
# print(fizzbuzz(3)) # Fizz
# print(fizzbuzz(5)) # Buzz
# print(fizzbuzz(15)) # FizzBuzz
# print(fizzbuzz(4)) # 4
# =============================================================================
