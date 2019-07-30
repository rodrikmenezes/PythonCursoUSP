""" Escreva um programa que recebe como entradas dois números inteiros correspondentes à largura e à altura
de um retângulo, respectivamente. O programa deve imprimir uma cadeia de caracteres que represente o retângulo informado com 
caracteres '#' na saída, de forma a desenhar um retêngulo vazado"""

l = int(input('digite a largura: '))
h = int(input('digite a altura: '))
l_incremento = h_incremento = 0


while h_incremento < h:
    while l_incremento < l:
        l_incremento += 1
    if h_incremento == 0 or h_incremento == h - 1:
        print(l_incremento * '#')
    else:
        print('#' + ' ' * (l - 2) + '#')
    h_incremento += 1
    l_incremento = 0