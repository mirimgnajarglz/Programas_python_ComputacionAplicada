# p088-modificar-lista.py
# Modifica los elementos de una lista

print('\033[H\033[J')

print('Modifica los elementos de una lista')

califs = [10, 9, 8.5, 6.5, 9.8, 7, 5, 6.2, 9.5]

print(f'\nTodas las calificaciones: {califs} - {len(califs)}')

print(f'\nModificar [0] y [1] con 7 y 7:')
califs[0]=7
califs[1]=7
print(f'Resultado: {califs} - {len(califs)}')

print(f'\nModificar calificaciones en el rango [2:5] (5 no incluida) con 9,9,9:')
califs[2:5] = [9,9,9]
print(f'Resultado: {califs} - {len(califs)}')

print("\nPrograma terminado")