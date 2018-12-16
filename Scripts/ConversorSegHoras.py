''' Este algorítimo coverte um numero inteiro (seg) em um valor de horas, min e seg '''

segundos_str = input('Entre com um valor em segundos = ')
segundos = int(segundos_str)

horas = segundos//3600 # 1h = 3600 seg
segundos_restantes = segundos % 3600
minutos = segundos_restantes // 60
segundos_restantes_final = segundos_restantes % 60

print(horas, ' hrs, ', minutos, ' min e ', segundos_restantes_final, ' seg')