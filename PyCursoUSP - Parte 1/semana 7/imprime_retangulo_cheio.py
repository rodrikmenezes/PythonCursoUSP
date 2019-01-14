""" Escreva um programa que recebe como entradas dois números inteiros correspondentes à largura e à altura
de um retângulo, respectivamente. O programa deve imprimir uma cadeia de caracteres que represente o retângulo informado com 
caracteres '#' na saída. """

l = int(input('digite a largura: '))
h = int(input('digite a altura: '))
l_incremento = h_incremento = 0

while h_incremento < h:
    while l_incremento < l:
        l_incremento += 1
    print(l_incremento * '#')
    h_incremento += 1
    l_incremento = 0