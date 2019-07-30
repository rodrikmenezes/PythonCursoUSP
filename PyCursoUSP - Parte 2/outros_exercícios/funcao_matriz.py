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

#%% Função ler matriz
  
def ler_matriz(num_lin, num_col):
  """
  Função para criar uma matriz de forma rápida,
  com dados inseridos pelo usuário
  """
  
  matriz = []
  for i in range(1, num_lin + 1):
    linha = []
    for j in range(1, num_col + 1):
        linha.append(float(input('Elemento(' + str(i) + ',' + str(j) + ') = ')))
    matriz.append(linha)
  return matriz
  
