# =============================================================================
# Receba 4 números na entrada, um de cada vez.
# Os dois primeiros devem corresponder, respectivamente,
# às coordenadas x e y de um ponto em um plano cartesiano.
# Os dois últimos devem corresponder, respectivamente,
# às coordenadas x e y de um outro ponto no mesmo plano.
# Calcule a distância entre os dois pontos. Se a distância
# for maior ou igual a 10, imprima: longe. Caso contrário
# imprima: perto
# =============================================================================
import math

print('Informe as coordenadas de dos pontos A e B')

x1 = float(input('Ponto A, coordenada x: '))
y1 = float(input('Ponto A, coordenada y: '))
x2 = float(input('Ponto B, coordenada x: '))
y2 = float(input('Ponto B, coordenada y: '))

distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)

if distancia >= 10:
    print('\nlonge')
else:
    print('\nperto')
