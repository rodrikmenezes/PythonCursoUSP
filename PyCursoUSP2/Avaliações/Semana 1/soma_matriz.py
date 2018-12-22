"""
Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e devolve 
uma matriz que represente sua soma caso as matrizes tenham dimensões iguais. 
Caso contrário, a função deve devolver False.
"""

# Esta função será utilizada na definição da próxima função
def criar_matriz(num_lin, num_col, valor):
  """
  Função para criar uma matriz de forma rápida
  """
  
  matriz = []
  for i in range(1,num_lin + 1):
    linha = []
    for j in range(1, num_col + 1):
        linha.append(valor)
    matriz.append(linha)
  return matriz


def soma_matrizes(m1, m2):
  
  n_lin = len(m1)
  n_col = len(m1[0])
  m_soma = criar_matriz(n_lin, n_col, 0)
    
  if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
    
    for i in range(n_lin):
      for j in range(n_col):
        m_soma[i][j] =  (m1[i][j] + m2[i][j])

  else:
    m_soma = False
  
  print(m_soma)
  return m_soma
  
