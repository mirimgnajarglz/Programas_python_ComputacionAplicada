# p076-tablas-todas.py
# Imprimir las tablas de multiplicar de 1 a n hasta m

print('\033[H\033[J')
print('Imprimmiendo las tablas de Multiplicar del 1 a n hasta m')

n = int(input('¿Hasta que tabla de multiplicar deseas generar? '))
m = int(input('¿Hasta que numero deseas multiplicar cada tabla? '))

for i in range(1, n + 1):
    print(f'\n--- Tabla del {i} ')
    for j in range(1, m + 1):
        resultado = i * j

print(f"{i} x {j} = {resultado}")
print('\n')