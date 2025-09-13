# p014-funciones-trigonometricas.py
# Demostrar el uso de funciones trigonometricas 

import math as mt


angulo = 45
radianes = mt.radians(angulo)

# Calcular las funciones trigonometricas 

seno = mt.sin(radianes)
coseno = mt.cos(radianes)
tangente = mt.tan(radianes)

grados = mt.degrees(radianes)

# Formatear la salida con f-string previo a la impresion

salida = ('Resumen de funciones\n'
f'El seno es     :{seno:.4f}\n'
f'El coseno es   :{coseno:.4f}\n'
f'La tangente es :{tangente:.4f}\n'
f'El angulo {angulo} grados, equivale a {radianes:.4f}radianes\n'
f'Los {radianes:.4f} radianes equivalen a {grados:.1f}grados\n')

# Mostrar la salida formateada
print(salida)