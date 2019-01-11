'''
Escrever um programa que lê dez números e conta a quantidade de números pares e 
ímpares digitados pelo usuário. No final, imprime o resultado.
'''

terminou = False
p = i = 0
while (not terminou):
    n = int(input("Digite um número, ou zero para terminar: "))
    if n == 0:
        terminou = True
    else:
        if n % 2 == 0:
            p = p + 1
        else:
            i = i + 1

print ("Pares = ", p)
print ("Ímpares = ", i)