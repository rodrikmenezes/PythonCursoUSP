''' Este algorítimo coverte um numero inteiro (seg) em um valor de horas, min e seg '''

segundos_str = input('Entre com um valor em segundos = ')
segundos = int(segundos_str)

dias = segundos // 86400 # 1 dia = 86400 seg
horas = (segundos % 86400)//3600 # 1h = 3600 seg
minutos = (segundos % 3600) // 60
segundos_restantes = (segundos % 3600) % 60

print(dias, ' dias,', +
      horas, ' horas,', +
      minutos, ' minuntos e', +
      segundos_restantes, ' segundos')