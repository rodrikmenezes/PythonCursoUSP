""" Este script recebe um númerodo usuário e escreve este número em fatores """

n = int(input('Digite um número inteiro maior que 1: '))

fator = 2
multipicidade = 0
while n > 1:
    while n % fator == 0:
        multipicidade += 1
        n = n / fator
    if multipicidade != 0:
        print('fator', fator, 'multiplicidade', multipicidade)
    fator += 1
    multipicidade = 0