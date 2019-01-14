
print('Informe números inteiros positivos e o programa efeuará o cálculo do fatorial')
print("Digite 'X' para terminar")
print()

while 1:
    numero = int(input('Número = '))

    # condição de finalização
    condicao = str(numero)
    if condicao == 'x':
        break
    
    # cálculo do fatorial
    if numero == 0 or numero == 1:
        fatorial = 1
        print('Fatorial de', numero, 'é', fatorial)
        print()
    else:
        i = 2
        fatorial = numero
        while i < numero:
            fatorial = fatorial * i
            i += 1
        print('Fatorial de', numero, 'é', fatorial)
        print()
    
    