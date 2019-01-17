''' 
Escreva a função remove_repetidos que recebe como parâmetro uma lista com números
inteiros, verifica se tal lista possui elementos repetidos e os remove.
A função deve devolver uma lista correspondente à primeira lista,
sem elementos repetidos. A lista devolvida deve estar ordenada.
'''

def remove_repetidos(lista):
    ''' remove números duplicados de uma lista de inteiros '''    
    a = 0
    n = 0
    while n < len(lista):
        a = lista.count(lista[n])
        if a > 1:
            lista.remove(lista[n])
            n -= 1
        else:
            n += 1
    return sorted(lista)

# teste 1
# lista = [2, 4, 2, 2, 3, 3, 1]
# remove_repetidos(lista) -> [1, 2, 3, 4]
# print(remove_repetidos(lista)) 

# teste 2
# lista = [7,3,33,12,3,3,3,7,12,100]
# remove_repetidos(lista) -> [3,7,12,33,100]
# print(remove_repetidos(lista))
