# p013-funciones-matematicas-precios.py
# Demostrar el uso de funciones de redondeo

import math as mt

precio = 15.65
arriba = mt.ceil(precio)
abajo = mt.floor(precio)
truncar = mt.trunc(precio)
redondeo = round(precio)
undecimal = round(precio,1)

print(f"El precio original    : {precio}")
print(f"Redondeo arriba       : {arriba}")
print(f"Redondeo abajo        : {abajo}")
print(f"Truncar               : {truncar}")
print(f"Redondeo              : {redondeo}")
print(f"Redondeo 1 decimal.    : {undecimal}")