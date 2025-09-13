# p018-area-volumen-cilindro.py
# calcula el area y volumen de un cilindro.

import math


radio = float(input("Ingresa el radio del cilindro: "))
altura = float(input("Ingresa la altura del cilindro: "))


area = math.pi * radio * (radio + altura)
volumen = math.pi * (radio ** 2) * altura


print(f"El area del cilindro es    : {area:.2f} unidades cuadradas")
print(f"El volumen del cilindro es : {volumen:.2f} unidades cubicas")

