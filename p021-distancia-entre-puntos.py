# p021-distancia-entre-puntos.py
# calcule la distancia entre dos puntos en un plano cartesiano

import math as mt


x1 = float(input("Ingresa la coordenada x del punto A: "))
y1 = float(input("Ingresa la coordenada y del punto A: "))


x2 = float(input("Ingresa la coordenada x del punto B: "))
y2 = float(input("Ingresa la coordenada y del punto B: "))

distancia = mt.sqrt((x1 - x2)**2 + (y1 - y2)**2)
print('La distancia entre los dos puntos es: {:.2f}' .format(distancia))
