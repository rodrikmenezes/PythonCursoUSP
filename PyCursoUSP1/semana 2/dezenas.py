x = input('Digite um número inteiro: ')

if len(x) == 1:
    dezenas = 0
else:
    dezenas = x[len(x)-2]

print('O dígito das dezenas é', dezenas)