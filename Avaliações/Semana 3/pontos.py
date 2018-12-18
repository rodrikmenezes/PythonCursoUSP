'''
O programa deve receber as coordenadas cartesianas de dois pontos e 
retornar com a distância entre os pontos
'''

print('Informe as coordenadas de dos pontos A e B')

x1 = float(input('Ponto A, coordenada x: '))
y1 = float(input('Ponto A, coordenada y: '))
x2 = float(input('Ponto B, coordenada x: '))
y2 = float(input('Ponto B, coordenada y: '))

import math
distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)

if distancia >= 10:
    print('longe')
else:
    print('perto')









