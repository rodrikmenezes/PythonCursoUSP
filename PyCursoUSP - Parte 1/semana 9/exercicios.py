#%%-------------------------------------------------
def pertence(item,lista):
    
    '''(objeto, list) -> bool

    Recebe uma lista de itens e um item e
    retorna True se o item eh um elemento da lista e
    False em caso contrario.
    '''
    
    i = 0
    resultado = False
    while i < len(lista):
        if item == lista[i]:
            resultado = True
        i += 1
    return resultado
#---------------------------------------------------
# testes da função pertente
lista  = [1, "oi", 3.14, 7, True]

# teste 1
if pertence("oi",lista):
    print("Passou no primeiro teste! :-)")
else:
    print("Nao passou no primeiro teste! :-(")

# teste 2
if pertence(True,lista):
    print("Passou no segundo teste! :-)")
else:
    print("Nao passou no segundo teste! :-(")

# teste 3
if not pertence(False,lista):
    print("Passou no terceiro teste! :-)")
else:
    print("Nao passou no terceiro teste! :-(")

# teste 4
if not pertence(1000,lista):
    print("Passou no quarto teste! :-)")
else:
    print("Nao passou no quarto teste! :-(")
#%%-----------------------------------------------
def indice(item, lista):
    '''(objeto,list) -> int ou None

    Recebe um objeto 'item' e uma lista 'lista' e retorna o
    indice da posicao em que item ocorre na lista.
    Caso item nao ocorra na lista a funcao retorna None
    '''
    i = 0
    resultado = None
    while i < len(lista):
        if lista[i] == item:
            resultado = i
        i += 1
    return resultado
#-----------------------------------------------
# testes da função indica
lista  = [1, "oi", 3.14, 7, True]

# teste 1
if indice("oi",lista) == 1:
    print("Passou no primeiro teste! :-)")
else:
    print("Nao passou no primeiro teste! :-(")

# teste 2
if indice(True,lista) == 4:
    print("Passou no segundo teste! :-)")
else:
    print("Nao passou no segundo teste! :-(")

# teste 3
if indice(False,lista) == None:
    print("Passou no terceiro teste! :-)")
else:
    print("Nao passou no terceiro teste! :-(")

# teste 4
if indice('caceta',lista) == None:
    print("Passou no terceiro teste! :-)")
else:
    print("Nao passou no terceiro teste! :-(")

#%%---------------------------------------------------------------
def soma_elementos(ini, fim, lista):
    """ (int, int, lista) --> int

    Recebe uma lista `lista` de numero e dois indices ini e fim,
    retorna a soma da sublista (= fatia) formada pelos elementos de
    indices ini, ini+1,...,fim-1.

    Pre-condicao: a funcao supoe que:

           0 <= ini <= fim <= len(lista)
    """
    soma = 0
    for i in range(ini, fim):
        soma = soma + lista[i]
    return soma
    
#-----------------------------------------------
# testes
lista  = [1, 2, 3, 4, 5]

# teste 1
if soma_elementos(0,len(lista),lista) == 15:
    print("Passou no primeiro teste! :-)")
else:
    print("Nao passou no primeiro teste! :-(")

# teste 2
if soma_elementos(1,4,lista) == 9:
    print("Passou no segundo teste! :-)")
else:
    print("Nao passou no segundo teste! :-(")

# teste 3
if soma_elementos(2,2,lista) == 0:
    print("Passou no terceiro teste! :-)")
else:
    print("Nao passou no terceiro teste! :-(")

#%%
