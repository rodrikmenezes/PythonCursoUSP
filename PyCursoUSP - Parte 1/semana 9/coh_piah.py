import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.
    Esta deve ser a última a ser implementada'''
    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas_texto = separa_sentencas(texto) # lista com as sentenças do texto
    palavras_texto = [] # inicialização da lista com as palavras do texto
    soma_caracteres_texto = 0 # inicialização variável que soma a quantidade de caracteres de todas as palavras do texto
    soma_caracteres_sentenca = 0 # soma de todos os caracteres das sentenças (incluso espaços brancos e caracteres especiais)
    soma_numero_frases = 0
    soma_caracteres_frase = 0

    for sentenca in range(len(sentencas_texto)):
        
        aux_sentenca = separa_frases(sentencas_texto[sentenca]) # separa cada sentença em frases (variável de apoio)
        soma_caracteres_sentenca += len(sentencas_texto[sentenca])
        soma_numero_frases += len(separa_frases(sentencas_texto[sentenca]))

        for frase in range(len(aux_sentenca)):
            palavras = separa_palavras(aux_sentenca[frase]) # separa cada frase em palavras
            soma_caracteres_frase += len(aux_sentenca[frase])

            for palavra in range(len(palavras)):
                palavras_texto.append(palavras[palavra])
                soma_caracteres_texto += len(palavras[palavra])

    # tamanho médio de palavra
    wal = soma_caracteres_texto / len(palavras_texto)
    # número de palavras diferentes dividido pelo número total de palavras
    ttr = n_palavras_diferentes(palavras_texto) / len(palavras_texto)
    # número de palavras utilizadas uma vez dividido pelo número total de palavras    
    hlr = n_palavras_unicas(palavras_texto) / len(palavras_texto)
    # tamanho médio de sentença
    sal = soma_caracteres_sentenca / len(sentencas_texto)
    # complexidade de sentença
    sac = soma_numero_frases / len(sentencas_texto)
    # tamanho médio de frase
    # pal = soma_caracteres_texto / len(separa_frases(texto))
    # pal = soma_caracteres_frase / len(separa_frases(texto))
    pal = soma_caracteres_frase / soma_numero_frases

    return [wal, ttr, hlr, sal, sac, pal]

# calcula_assinatura("Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia.")


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass