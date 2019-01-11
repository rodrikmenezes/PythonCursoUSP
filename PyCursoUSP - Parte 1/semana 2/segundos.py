# =============================================================================
# Este Script coverte um numero inteiro dado em segundos em um valor
# composto em horas, minutos e segundos
# =============================================================================

valorInformado = int(input('Entre com um valor em segundos = '))

# este comando captura a parte inteira do valor dado em dias
dias = valorInformado // 86400  # 1 dia = 86400 seg
# este comando captura o valor em horas
horas = (valorInformado % 86400) // 3600  # 1h = 3600 seg
# este comando captura o valor em minutos
minutos = (valorInformado % 3600) // 60
# este comando captura o valor em segundos
segundos = (valorInformado % 3600) % 60

print(dias, ' dias,',
      horas, ' horas,',
      minutos, ' minuntos e',
      segundos, ' segundos')

# =============================================================================
# # Teste #
#
# Entrada de Dados:
# Por favor, entre com o número de segundos que deseja converter: 178615
#
# Saída de Dados:
# 2 dias, 1 horas, 36 minutos e 55 segundos.
# =============================================================================
