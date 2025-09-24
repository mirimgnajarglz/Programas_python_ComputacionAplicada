# p030-verifica-suma.py
# Verificar si la suma de dos números es igual a un tercero.

print("\033[2J\033[H")
print('--- Verificar si la suma de dos números es igual a un tercero ')

# Entrada
print('Dame 3 números enteros separados por un espacio:')
n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

# Proceso
if n1 + n2 == n3:
    print(f' n1 + n2 es igual a n3 ({n1} + {n2} = {n3})')
elif n1 + n3 == n2:
    print(f' n1 + n3 es igual a n2 ({n1} + {n3} = {n2})')
elif n2 + n3 == n1:
    print(f' n2 + n3 es igual a n1 ({n2} + {n3} = {n1})')
else:
    print(' Ninguna combinación de suma es igual al tercer número.')

print("\nProceso terminado")