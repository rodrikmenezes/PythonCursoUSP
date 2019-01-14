# este script imprime toda a tabuada

linha = 1
coluna = 0

while linha <= 10:
    while coluna <= 10:
        print(linha * coluna, end= '\t')
        coluna += 1
    linha += 1
    print()
    coluna = 0